from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from telecom_pulse.raw_inspection import RawInspectionError, inspect_raw_zip, write_profile


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect a governed ANATEL raw ZIP.")
    parser.add_argument("--zip", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        profile = inspect_raw_zip(args.zip)
    except RawInspectionError as exc:
        parser.exit(2, f"inspection failed: {exc}\n")

    if args.output:
        write_profile(profile, args.output)

    print(json.dumps(asdict(profile), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
