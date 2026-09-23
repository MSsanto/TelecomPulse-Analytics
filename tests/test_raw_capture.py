import hashlib
import json

import pytest

import telecom_pulse.raw_capture as raw_capture


OFFICIAL_URL = "https://www.anatel.gov.br/dadosabertos/example.csv"


def test_official_source_requires_anatel_https():
    raw_capture._validate_source_url(OFFICIAL_URL)

    with pytest.raises(raw_capture.RawCaptureError, match="HTTPS"):
        raw_capture._validate_source_url("http://www.anatel.gov.br/example.csv")

    with pytest.raises(raw_capture.RawCaptureError, match="unexpected source host"):
        raw_capture._validate_source_url("https://example.com/example.csv")


def test_waf_block_page_is_detected():
    payload = (
        "Por questões de segurança, esta operação no sistema foi bloqueada. "
        "Código de bloqueio: 123"
    ).encode()
    assert raw_capture._looks_like_block_page(payload, "text/html; charset=utf-8")
    assert raw_capture._looks_like_block_page(payload, None)


def test_csv_like_payload_is_not_a_block_page():
    payload = b"UF;Grupo;Acessos\nSP;EXEMPLO;10\n"
    assert not raw_capture._looks_like_block_page(payload, "text/csv")
    assert not raw_capture._looks_like_block_page(payload, None)


def test_html_without_block_marker_is_not_misclassified():
    payload = b"<html><body>dataset catalog</body></html>"
    assert not raw_capture._looks_like_block_page(payload, "text/html")


def test_manual_registration_is_byte_exact_and_generates_manifest(tmp_path):
    source = tmp_path / "browser-download.csv"
    payload = b"UF;Grupo;Acessos\nSP;EXEMPLO;10\n"
    source.write_bytes(payload)
    output = tmp_path / "raw" / "smp.csv"

    metadata = raw_capture.register_official_raw(
        service="SMP",
        source_url=OFFICIAL_URL,
        source_file=source,
        output_path=output,
        retrieved_at="2026-09-22T20:00:00-03:00",
    )

    assert output.read_bytes() == payload
    assert metadata.acquisition_method == "manual_governed"
    assert metadata.original_filename == "browser-download.csv"
    assert metadata.sha256 == hashlib.sha256(payload).hexdigest()

    manifest = json.loads(
        output.with_suffix(".csv.metadata.json").read_text(encoding="utf-8")
    )
    assert manifest["source_url"] == OFFICIAL_URL
    assert manifest["retrieved_at"] == "2026-09-22T20:00:00-03:00"
    assert manifest["byte_size"] == len(payload)


def test_manual_registration_refuses_overwrite(tmp_path):
    source = tmp_path / "source.csv"
    source.write_bytes(b"UF;Acessos\nSP;1\n")
    output = tmp_path / "raw.csv"
    output.write_bytes(b"existing")

    with pytest.raises(raw_capture.RawCaptureError, match="already exists"):
        raw_capture.register_official_raw(
            service="SMP",
            source_url=OFFICIAL_URL,
            source_file=source,
            output_path=output,
        )


def test_manual_registration_rejects_waf_html(tmp_path):
    source = tmp_path / "blocked.html"
    source.write_text(
        "<html>Por questões de segurança, esta operação foi bloqueada. "
        "Codigo de bloqueio: 123</html>",
        encoding="utf-8",
    )

    with pytest.raises(raw_capture.RawCaptureError, match="block page"):
        raw_capture.register_official_raw(
            service="SCM",
            source_url=OFFICIAL_URL,
            source_file=source,
            output_path=tmp_path / "raw.csv",
        )
