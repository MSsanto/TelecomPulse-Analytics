from pathlib import Path

import pandas as pd
import pytest

from telecom_pulse.pipeline import build_summary, load_incidents, run_pipeline

FIXTURE = Path("data/raw/incidents_synthetic.csv")


def test_reference_dataset_summary() -> None:
    frame = load_incidents(FIXTURE)
    assert build_summary(frame) == {
        "incident_count": 4,
        "resolved_incident_count": 3,
        "downtime_minutes": 180.0,
        "mttr_minutes": 60.0,
    }


def test_pipeline_writes_processed_output(tmp_path: Path) -> None:
    output = tmp_path / "processed.csv"
    summary = run_pipeline(FIXTURE, output)
    assert output.exists()
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
