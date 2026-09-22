from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from telecom_pulse.analytics import recurrence_count
from telecom_pulse.quality import build_quality_report, quality_ok

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

VALID_STATUS = {"open", "resolved"}

CARRIER_ALIASES = {
    "claro": "Claro",
    "claro empresas": "Claro",
    "vivo": "Vivo",
    "telefonica": "Vivo",
    "telefônica": "Vivo",
    "tim": "TIM",
    "tim brasil": "TIM",
}


def _clean_text(series: pd.Series) -> pd.Series:
    return series.astype("string").str.strip()


def normalize_incidents(frame: pd.DataFrame) -> pd.DataFrame:
    """Normalize text and temporal fields without changing business meaning."""
    result = frame.copy()

    for column in ("incident_id", "site_id", "carrier", "cause_category", "source"):
        result[column] = _clean_text(result[column])

    result["status"] = _clean_text(result["status"]).str.lower()
    normalized_carrier = result["carrier"].str.lower()
    result["carrier"] = normalized_carrier.map(CARRIER_ALIASES).fillna(
        result["carrier"].str.title()
    )
    result["cause_category"] = (
        result["cause_category"].str.lower().str.replace(r"\s+", "_", regex=True)
    )
    result["region"] = _clean_text(result["region"]).str.upper()
    result["link_type"] = _clean_text(result["link_type"]).str.lower()

    for column in ("opened_at", "restored_at"):
        result[column] = pd.to_datetime(result[column], utc=True, errors="coerce")

    result["downtime_minutes"] = (
        (result["restored_at"] - result["opened_at"]).dt.total_seconds() / 60
    )
    return result


def validate_incidents(frame: pd.DataFrame) -> None:
    """Raise ValueError when the normalized dataset violates critical rules."""
    missing = REQUIRED_COLUMNS.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    if frame["incident_id"].duplicated().any():
        raise ValueError("Duplicate incident_id detected")

    if frame["status"].isna().any() or not set(frame["status"].dropna()).issubset(VALID_STATUS):
        raise ValueError("Invalid status detected")

    if frame["incident_id"].isna().any() or frame["incident_id"].eq("").any():
        raise ValueError("Missing incident_id detected")

    if frame["site_id"].isna().any() or frame["site_id"].eq("").any():
        raise ValueError("Missing site_id detected")

    if frame["carrier"].isna().any() or frame["carrier"].eq("").any():
        raise ValueError("Missing carrier detected")

    if frame["opened_at"].isna().any():
        raise ValueError("Invalid opened_at detected")

    resolved = frame["status"].eq("resolved")
    if frame.loc[resolved, "restored_at"].isna().any():
        raise ValueError("Resolved incident without restored_at")

    if frame.loc[resolved, "downtime_minutes"].lt(0).any():
        raise ValueError("Negative downtime detected")


def load_incidents(path: Path) -> pd.DataFrame:
    """Load, normalize and validate incidents."""
    raw = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(raw.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    frame = normalize_incidents(raw)
    validate_incidents(frame)
    return frame


def build_summary(frame: pd.DataFrame) -> dict[str, float | int]:
    """Build Sprint 1 reference KPIs."""
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
        "recurrence_count": recurrence_count(frame),
    }


def run_pipeline(
    raw_path: Path,
    processed_path: Path,
    quality_path: Path | None = None,
) -> dict[str, float | int]:
    frame = load_incidents(raw_path)
    report = build_quality_report(frame)
    if not quality_ok(report):
        raise ValueError(f"Critical data-quality issue: {report}")

    processed_path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(processed_path, index=False)

    if quality_path is not None:
        quality_path.parent.mkdir(parents=True, exist_ok=True)
        quality_path.write_text(
            json.dumps(report, indent=2, sort_keys=True),
            encoding="utf-8",
        )

    return build_summary(frame)
