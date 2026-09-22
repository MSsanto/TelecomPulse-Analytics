from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from telecom_pulse.raw_capture import RawCaptureError, capture_official_raw


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Capture an official ANATEL raw file with immutable provenance metadata."
    )
    parser.add_argument("--service", required=True, choices=["SMP", "SCM"])
    parser.add_argument("--url", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    try:
        metadata = capture_official_raw(
            service=args.service,
            source_url=args.url,
            output_path=args.output,
        )
    except RawCaptureError as exc:
        parser.exit(2, f"capture failed: {exc}\n")

    print(json.dumps(asdict(metadata), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
