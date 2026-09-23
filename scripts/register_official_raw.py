from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from telecom_pulse.raw_capture import RawCaptureError, register_official_raw


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Register a manually downloaded official ANATEL raw file."
    )
    parser.add_argument("--service", required=True, choices=["SMP", "SCM"])
    parser.add_argument("--file", required=True, type=Path)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--retrieved-at",
        help="Optional ISO-8601 timestamp of browser download; defaults to registration time.",
    )
    args = parser.parse_args()

    try:
        metadata = register_official_raw(
            service=args.service,
            source_url=args.source_url,
            source_file=args.file,
            output_path=args.output,
            retrieved_at=args.retrieved_at,
        )
    except RawCaptureError as exc:
        parser.exit(2, f"registration failed: {exc}\n")

    print(json.dumps(asdict(metadata), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
