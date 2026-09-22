from pathlib import Path

import pandas as pd
import pytest

from telecom_pulse.analytics import availability_pct, downtime_minutes_without_overlap
from telecom_pulse.generator import generate_reference_dataset
from telecom_pulse.pipeline import build_summary, load_incidents, run_pipeline

FIXTURE = Path("data/raw/incidents_synthetic.csv")


def test_reference_dataset_summary() -> None:
    frame = load_incidents(FIXTURE)
    assert build_summary(frame) == {
        "incident_count": 4,
        "resolved_incident_count": 3,
        "downtime_minutes": 180.0,
        "mttr_minutes": 60.0,
        "recurrence_count": 1,
    }


def test_pipeline_writes_processed_output_and_quality_report(tmp_path: Path) -> None:
    output = tmp_path / "processed.csv"
    quality = tmp_path / "quality.json"
    summary = run_pipeline(FIXTURE, output, quality)
    assert output.exists()
    assert quality.exists()
    result = pd.read_csv(output)
    assert "downtime_minutes" in result.columns
    assert summary["incident_count"] == 4


def test_missing_required_column_is_rejected(tmp_path: Path) -> None:
    bad = tmp_path / "bad.csv"
    pd.DataFrame({"incident_id": ["x"]}).to_csv(bad, index=False)
    with pytest.raises(ValueError, match="Missing required columns"):
        load_incidents(bad)


def test_duplicate_incident_is_rejected(tmp_path: Path) -> None:
    frame = pd.read_csv(FIXTURE)
    frame = pd.concat([frame, frame.iloc[[0]]], ignore_index=True)
    bad = tmp_path / "duplicate.csv"
    frame.to_csv(bad, index=False)
    with pytest.raises(ValueError, match="Duplicate incident_id"):
        load_incidents(bad)


def test_normalization_is_deterministic(tmp_path: Path) -> None:
    generated = tmp_path / "generated.csv"
    generate_reference_dataset(generated)
    frame = load_incidents(generated)
    assert frame.loc[0, "carrier"] == "Claro"
    assert frame.loc[0, "status"] == "resolved"
    assert frame.loc[0, "cause_category"] == "fiber_break"
    assert frame.loc[0, "link_type"] == "fiber"


def test_carrier_normalization_preserves_real_brand_casing() -> None:
    frame = pd.DataFrame(
        {
            "incident_id": ["x", "y", "z"],
            "site_id": ["S1", "S2", "S3"],
            "carrier": ["claro empresas", "TELEFÔNICA", "tim brasil"],
            "opened_at": [
                "2026-09-01T10:00:00Z",
                "2026-09-01T10:00:00Z",
                "2026-09-01T10:00:00Z",
            ],
            "restored_at": [
                "2026-09-01T11:00:00Z",
                "2026-09-01T11:00:00Z",
                "2026-09-01T11:00:00Z",
            ],
            "status": ["resolved", "resolved", "resolved"],
            "cause_category": ["power", "power", "power"],
            "region": ["SE", "SE", "SE"],
            "link_type": ["fiber", "fiber", "fiber"],
            "source": ["synthetic", "synthetic", "synthetic"],
        }
    )
    from telecom_pulse.pipeline import normalize_incidents

    normalized = normalize_incidents(frame)
    assert normalized["carrier"].tolist() == ["Claro", "Vivo", "TIM"]


def test_resolved_incident_without_restore_is_rejected(tmp_path: Path) -> None:
    frame = pd.read_csv(FIXTURE)
    frame.loc[0, "restored_at"] = ""
    bad = tmp_path / "missing_restore.csv"
    frame.to_csv(bad, index=False)
    with pytest.raises(ValueError, match="Resolved incident without restored_at"):
        load_incidents(bad)


def test_negative_downtime_is_rejected(tmp_path: Path) -> None:
    frame = pd.read_csv(FIXTURE)
    frame.loc[0, "restored_at"] = "2026-09-01T09:00:00Z"
    bad = tmp_path / "negative.csv"
    frame.to_csv(bad, index=False)
    with pytest.raises(ValueError, match="Negative downtime"):
        load_incidents(bad)


def test_overlap_is_not_double_counted() -> None:
    frame = pd.DataFrame(
        {
            "status": ["resolved", "resolved"],
            "opened_at": pd.to_datetime(
                ["2026-09-01T10:00:00Z", "2026-09-01T10:30:00Z"], utc=True
            ),
            "restored_at": pd.to_datetime(
                ["2026-09-01T11:00:00Z", "2026-09-01T11:30:00Z"], utc=True
            ),
        }
    )
    assert downtime_minutes_without_overlap(frame) == 90.0


def test_availability_clips_intervals_to_window() -> None:
    frame = pd.DataFrame(
        {
            "site_id": ["SITE-TEST"],
            "status": ["resolved"],
            "opened_at": pd.to_datetime(["2026-09-01T09:30:00Z"], utc=True),
            "restored_at": pd.to_datetime(["2026-09-01T10:30:00Z"], utc=True),
        }
    )
    start = pd.Timestamp("2026-09-01T10:00:00Z")
    end = pd.Timestamp("2026-09-01T11:00:00Z")
    assert availability_pct(frame, start, end) == 50.0
