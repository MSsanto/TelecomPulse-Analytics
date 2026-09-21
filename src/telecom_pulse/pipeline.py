from __future__ import annotations

from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {
    "incident_id",
    "site_id",
    "carrier",
    "opened_at",
    "restored_at",
    "status",
    "cause_category",
    "region",
    "link_type",
    "source",
}


def load_incidents(path: Path) -> pd.DataFrame:
    """Load and minimally validate the Sprint 0 synthetic incident dataset."""
    frame = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    if frame["incident_id"].duplicated().any():
        raise ValueError("Duplicate incident_id detected")

    for column in ("opened_at", "restored_at"):
        frame[column] = pd.to_datetime(frame[column], utc=True, errors="coerce")

    if frame["opened_at"].isna().any():
        raise ValueError("Invalid opened_at detected")

    resolved = frame["status"].eq("resolved")
    if frame.loc[resolved, "restored_at"].isna().any():
        raise ValueError("Resolved incident without restored_at")

    frame["downtime_minutes"] = (
        (frame["restored_at"] - frame["opened_at"]).dt.total_seconds() / 60
    )
    if frame.loc[resolved, "downtime_minutes"].lt(0).any():
        raise ValueError("Negative downtime detected")

    return frame


def build_summary(frame: pd.DataFrame) -> dict[str, float | int]:
    """Build the minimal reference summary used to validate the pipeline contract."""
    resolved = frame[frame["status"].eq("resolved")]
    downtime = float(resolved["downtime_minutes"].sum())
    count = int(len(frame))
    resolved_count = int(len(resolved))
    mttr = downtime / resolved_count if resolved_count else 0.0
    return {
        "incident_count": count,
        "resolved_incident_count": resolved_count,
        "downtime_minutes": round(downtime, 2),
        "mttr_minutes": round(mttr, 2),
    }


def run_pipeline(raw_path: Path, processed_path: Path) -> dict[str, float | int]:
    frame = load_incidents(raw_path)
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(processed_path, index=False)
    return build_summary(frame)
