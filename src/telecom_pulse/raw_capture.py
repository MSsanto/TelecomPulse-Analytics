from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen


class RawCaptureError(RuntimeError):
    pass


@dataclass(frozen=True)
class RawCaptureMetadata:
    service: str
    source_url: str
    retrieved_at: str
    byte_size: int
    sha256: str
    content_type: str | None
    output_path: str


_ALLOWED_HOSTS = {"www.anatel.gov.br", "anatel.gov.br"}


def _validate_source_url(source_url: str) -> None:
    parsed = urlparse(source_url)
    if parsed.scheme != "https":
        raise RawCaptureError("official raw source must use HTTPS")
    if parsed.hostname not in _ALLOWED_HOSTS:
        raise RawCaptureError(f"unexpected source host: {parsed.hostname}")


def _looks_like_block_page(payload: bytes, content_type: str | None) -> bool:
    prefix = payload[:8192].lower()
    html = content_type is not None and "text/html" in content_type.lower()
    markers = (
        b"por quest",
        b"opera",
        b"bloquead",
        b"código de bloqueio",
        b"codigo de bloqueio",
    )
    return html and any(marker in prefix for marker in markers)


def capture_official_raw(
    *,
    service: str,
    source_url: str,
    output_path: Path,
    timeout_seconds: int = 60,
) -> RawCaptureMetadata:
    _validate_source_url(source_url)

    request = Request(
        source_url,
        headers={
            "User-Agent": "TelecomPulse-Analytics/2.0 (+public-data-validation)",
            "Accept": "text/csv,text/plain,application/octet-stream,*/*;q=0.5",
        },
    )

    try:
        with urlopen(request, timeout=timeout_seconds) as response:  # noqa: S310
            payload = response.read()
            content_type = response.headers.get("Content-Type")
    except Exception as exc:
        raise RawCaptureError(f"raw download failed: {exc}") from exc

    if not payload:
        raise RawCaptureError("raw download returned zero bytes")

    if _looks_like_block_page(payload, content_type):
        raise RawCaptureError("ANATEL security/WAF block page returned instead of raw data")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(payload)

    metadata = RawCaptureMetadata(
        service=service.upper(),
        source_url=source_url,
        retrieved_at=datetime.now(UTC).isoformat(),
        byte_size=len(payload),
        sha256=hashlib.sha256(payload).hexdigest(),
        content_type=content_type,
        output_path=str(output_path),
    )

    metadata_path = output_path.with_suffix(output_path.suffix + ".metadata.json")
    metadata_path.write_text(
        json.dumps(asdict(metadata), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return metadata
