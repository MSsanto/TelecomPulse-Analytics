from pathlib import Path

import pandas as pd

from telecom_pulse.pipeline import load_incidents
from telecom_pulse.presentation import build_dashboard_contract, write_presentation_artifacts

FIXTURE = Path("data/raw/incidents_synthetic.csv")
WINDOW_START = pd.Timestamp("2026-09-01T00:00:00Z")
WINDOW_END = pd.Timestamp("2026-09-05T00:00:00Z")


def _contract() -> dict[str, object]:
    frame = load_incidents(FIXTURE)
    return build_dashboard_contract(
        frame,
        WINDOW_START,
        WINDOW_END,
        generated_from=FIXTURE.as_posix(),
    )


def test_contract_has_version_and_expected_sections() -> None:
    contract = _contract()
    assert contract["contract_version"] == "1.0"
    assert set(contract) == {
        "contract_version",
        "generated_from",
        "window",
        "summary",
        "by_carrier",
        "by_site",
        "by_cause",
        "timeline",
        "incidents",
    }


def test_incident_totals_reconcile_across_dimensions() -> None:
    contract = _contract()
    summary = contract["summary"]
    assert sum(row["incident_count"] for row in contract["by_carrier"]) == summary["incident_count"]
    assert sum(row["incident_count"] for row in contract["by_site"]) == summary["incident_count"]
    assert sum(row["incident_count"] for row in contract["by_cause"]) == summary["incident_count"]


def test_raw_downtime_reconciles_across_dimensions() -> None:
    contract = _contract()
    summary = contract["summary"]
    assert sum(row["downtime_minutes"] for row in contract["by_carrier"]) == summary[
        "downtime_minutes"
    ]
    assert sum(row["downtime_minutes"] for row in contract["by_site"]) == summary[
        "downtime_minutes"
    ]
    assert sum(row["downtime_minutes"] for row in contract["by_cause"]) == summary[
        "downtime_minutes"
    ]


def test_timeline_reconciles_incidents_and_downtime() -> None:
    contract = _contract()
    summary = contract["summary"]
    assert sum(row["incident_count"] for row in contract["timeline"]) == summary["incident_count"]
    assert sum(row["downtime_minutes"] for row in contract["timeline"]) == summary[
        "downtime_minutes"
    ]


def test_summary_site_time_availability_is_deterministic() -> None:
    contract = _contract()
    summary = contract["summary"]
    assert summary["site_count"] == 3
    assert summary["availability_pct"] == 98.9583


def test_presentation_artifacts_are_written(tmp_path: Path) -> None:
    contract = _contract()
    write_presentation_artifacts(contract, tmp_path)
    assert (tmp_path / "dashboard-v1.json").exists()
    assert (tmp_path / "by_carrier.csv").exists()
    assert (tmp_path / "by_site.csv").exists()
    assert (tmp_path / "by_cause.csv").exists()
    assert (tmp_path / "timeline.csv").exists()
    assert (tmp_path / "incidents.csv").exists()
