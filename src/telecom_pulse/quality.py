from __future__ import annotations

import pandas as pd


def build_quality_report(frame: pd.DataFrame) -> dict[str, int]:
    """Return deterministic data-quality counters for the processed dataset."""
    resolved = frame["status"].eq("resolved")
    return {
        "rows": int(len(frame)),
        "duplicate_incident_ids": int(frame["incident_id"].duplicated().sum()),
        "missing_site_id": int(frame["site_id"].isna().sum()),
        "missing_carrier": int(frame["carrier"].isna().sum()),
        "invalid_opened_at": int(frame["opened_at"].isna().sum()),
        "resolved_without_restored_at": int(
            (resolved & frame["restored_at"].isna()).sum()
        ),
        "negative_downtime": int(
            (resolved & frame["downtime_minutes"].lt(0)).sum()
        ),
    }


def quality_ok(report: dict[str, int]) -> bool:
    """Return True when all critical counters are zero."""
    critical = (
        "duplicate_incident_ids",
        "missing_site_id",
        "missing_carrier",
        "invalid_opened_at",
        "resolved_without_restored_at",
        "negative_downtime",
    )
    return all(report[name] == 0 for name in critical)
