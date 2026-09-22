from __future__ import annotations

import argparse
import json
from pathlib import Path

from telecom_pulse.public_data import (
    build_public_dashboard,
    load_competition_snapshot,
    load_satisfaction_snapshot,
    write_public_dashboard,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build TelecomPulse v2 dashboard from official public data snapshots"
    )
    parser.add_argument(
        "--competition",
        type=Path,
        default=Path("data/public/reference/anatel_competition_2026q2.csv"),
    )
    parser.add_argument(
        "--satisfaction",
        type=Path,
        default=Path("data/public/reference/anatel_satisfaction_2025.csv"),
    )
    parser.add_argument(
        "--sources",
        type=Path,
        default=Path("config/sources.json"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/presentation"),
    )
    args = parser.parse_args()

    competition = load_competition_snapshot(args.competition)
    satisfaction = load_satisfaction_snapshot(args.satisfaction)
    source_registry = json.loads(args.sources.read_text(encoding="utf-8"))
    contract = build_public_dashboard(competition, satisfaction, source_registry)
    write_public_dashboard(contract, args.output_dir)


if __name__ == "__main__":
    main()
