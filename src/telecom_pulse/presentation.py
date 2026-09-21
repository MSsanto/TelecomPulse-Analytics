from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from telecom_pulse.analytics import availability_pct, recurrence_count


def _raw_downtime(frame: pd.DataFrame) -> float:
    resolved = frame[frame["status"].eq("resolved")]
    return round(float(resolved["downtime_minutes"].sum()), 2)


def _mttr(frame: pd.DataFrame) -> float:
    resolved = frame[frame["status"].eq("resolved")]
    count = int(len(resolved))
    if count == 0:
        return 0.0
    return round(float(resolved["downtime_minutes"].sum()) / count, 2)


def _metrics(
    frame: pd.DataFrame,
    window_start: pd.Timestamp,
    window_end: pd.Timestamp,
) -> dict[str, float | int]:
    return {
        "incident_count": int(len(frame)),
        "resolved_incident_count": int(frame["status"].eq("resolved").sum()),
        "open_incident_count": int(frame["status"].eq("open").sum()),
        "downtime_minutes": _raw_downtime(frame),
        "mttr_minutes": _mttr(frame),
        "recurrence_count": recurrence_count(frame),
        "availability_pct": availability_pct(frame, window_start, window_end),
        "site_count": int(frame["site_id"].nunique()),
    }


def _grouped_metrics(
    frame: pd.DataFrame,
    dimension: str,
    window_start: pd.Timestamp,
    window_end: pd.Timestamp,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for value, group in frame.groupby(dimension, dropna=False):
        row: dict[str, object] = {dimension: str(value)}
        row.update(_metrics(group, window_start, window_end))
        rows.append(row)
    return sorted(rows, key=lambda item: str(item[dimension]))


def _timeline(frame: pd.DataFrame) -> list[dict[str, object]]:
    working = frame.copy()
    working["opened_date"] = working["opened_at"].dt.strftime("%Y-%m-%d")
    rows: list[dict[str, object]] = []
    for opened_date, group in working.groupby("opened_date"):
        rows.append(
            {
                "opened_date": str(opened_date),
                "incident_count": int(len(group)),
                "resolved_incident_count": int(group["status"].eq("resolved").sum()),
                "open_incident_count": int(group["status"].eq("open").sum()),
                "downtime_minutes": _raw_downtime(group),
            }
        )
    return sorted(rows, key=lambda item: str(item["opened_date"]))


def _incident_records(frame: pd.DataFrame) -> list[dict[str, object]]:
    columns = [
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
        "downtime_minutes",
    ]
    result: list[dict[str, object]] = []
    for row in frame[columns].itertuples(index=False):
        record = dict(zip(columns, row, strict=True))
        for field in ("opened_at", "restored_at"):
            value = record[field]
            if pd.isna(value):
                record[field] = None
            else:
                record[field] = value.isoformat()
        if pd.isna(record["downtime_minutes"]):
            record["downtime_minutes"] = None
        else:
            record["downtime_minutes"] = round(float(record["downtime_minutes"]), 2)
        result.append(record)
    return result


def build_dashboard_contract(
    frame: pd.DataFrame,
    window_start: pd.Timestamp,
    window_end: pd.Timestamp,
    generated_from: str,
) -> dict[str, object]:
    """Build versioned frontend-ready analytics contract."""
    return {
        "contract_version": "1.0",
        "generated_from": generated_from,
        "window": {
            "start": window_start.isoformat(),
            "end": window_end.isoformat(),
        },
        "summary": _metrics(frame, window_start, window_end),
        "by_carrier": _grouped_metrics(frame, "carrier", window_start, window_end),
        "by_site": _grouped_metrics(frame, "site_id", window_start, window_end),
        "by_cause": _grouped_metrics(frame, "cause_category", window_start, window_end),
        "timeline": _timeline(frame),
        "incidents": _incident_records(frame),
    }


def write_presentation_artifacts(
    contract: dict[str, object],
    output_dir: Path,
) -> None:
    """Persist dashboard JSON plus CSV views with deterministic ordering."""
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "dashboard-v1.json").write_text(
        json.dumps(contract, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    table_map = {
        "by_carrier.csv": contract["by_carrier"],
        "by_site.csv": contract["by_site"],
        "by_cause.csv": contract["by_cause"],
        "timeline.csv": contract["timeline"],
        "incidents.csv": contract["incidents"],
    }
    for filename, rows in table_map.items():
        pd.DataFrame(rows).to_csv(output_dir / filename, index=False)
