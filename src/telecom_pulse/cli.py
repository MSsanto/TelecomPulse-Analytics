from __future__ import annotations

import argparse
import json
from pathlib import Path

from telecom_pulse.pipeline import run_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Run TelecomPulse Sprint 0 pipeline")
    parser.add_argument("--input", type=Path, default=Path("data/raw/incidents_synthetic.csv"))
    parser.add_argument("--output", type=Path, default=Path("data/processed/incidents.csv"))
    args = parser.parse_args()
    summary = run_pipeline(args.input, args.output)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
