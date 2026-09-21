from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from telecom_pulse.pipeline import load_incidents
from telecom_pulse.presentation import build_dashboard_contract, write_presentation_artifacts


def main() -> None:
    parser = argparse.ArgumentParser(description="Build TelecomPulse dashboard data contract")
    parser.add_argument("--input", type=Path, default=Path("data/raw/incidents_synthetic.csv"))
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/presentation"),
    )
    parser.add_argument(
        "--window-start",
        default="2026-09-01T00:00:00Z",
    )
    parser.add_argument(
        "--window-end",
        default="2026-09-05T00:00:00Z",
    )
    args = parser.parse_args()

    frame = load_incidents(args.input)
    contract = build_dashboard_contract(
        frame=frame,
        window_start=pd.Timestamp(args.window_start),
        window_end=pd.Timestamp(args.window_end),
        generated_from=args.input.as_posix(),
    )
    write_presentation_artifacts(contract, args.output_dir)


if __name__ == "__main__":
    main()
