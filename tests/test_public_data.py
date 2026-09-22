import json
from pathlib import Path

import pytest

from telecom_pulse.public_data import (
    build_public_dashboard,
    load_competition_snapshot,
    load_satisfaction_snapshot,
    top_providers_by_metric,
    write_public_dashboard,
)

COMPETITION = Path("data/public/reference/anatel_competition_2026q2.csv")
SATISFACTION = Path("data/public/reference/anatel_satisfaction_2025.csv")
SOURCES = Path("config/sources.json")


def _contract() -> dict[str, object]:
    competition = load_competition_snapshot(COMPETITION)
    satisfaction = load_satisfaction_snapshot(SATISFACTION)
    sources = json.loads(SOURCES.read_text(encoding="utf-8"))
    return build_public_dashboard(competition, satisfaction, sources)


def test_reference_snapshot_uses_official_sources() -> None:
    competition = load_competition_snapshot(COMPETITION)
    assert set(competition["source_id"]) == {"ANATEL_COMPETITION_2026Q2"}

    satisfaction = load_satisfaction_snapshot(SATISFACTION)
    assert set(satisfaction["source_id"]) == {"ANATEL_SATISFACTION_2025"}


def test_known_official_competition_values_are_preserved() -> None:
    contract = _contract()
    smp = contract["market"]["SMP"]
    scm = contract["market"]["SCM"]

    assert smp["total_accesses"] == 276_400_000
    assert smp["accesses_5g"] == 66_100_000
    assert smp["share_5g_pct"] == 23.9

    assert scm["total_accesses"] == 55_400_000
    assert scm["fiber_accesses"] == 44_700_000


def test_reference_provider_shares_are_sorted_without_fabricating_missing_rows() -> None:
    competition = load_competition_snapshot(COMPETITION)
    mobile = top_providers_by_metric(competition, "SMP", "market_share", 10)
    fixed = top_providers_by_metric(competition, "SCM", "market_share", 10)

    assert [row["provider"] for row in mobile] == ["Vivo", "TIM"]
    assert [row["provider"] for row in fixed] == ["Claro", "Vivo", "NIO"]


def test_public_contract_rejects_synthetic_noc_metrics() -> None:
    contract = _contract()
    serialized = json.dumps(contract)
    for forbidden in ("incident_count", "downtime_minutes", "mttr_minutes", "availability_pct"):
        assert forbidden not in serialized


def test_satisfaction_values_are_real_reference_rows() -> None:
    contract = _contract()
    rows = contract["satisfaction"]["rows"]
    vivo_post = next(
        row
        for row in rows
        if row["provider"] == "Vivo" and row["service"] == "celular_pos_pago"
    )
    assert vivo_post["isg"] == 7.87


def test_top_n_requires_positive_n() -> None:
    competition = load_competition_snapshot(COMPETITION)
    with pytest.raises(ValueError, match="positive"):
        top_providers_by_metric(competition, "SMP", "market_share", 0)


def test_dashboard_v2_is_written(tmp_path: Path) -> None:
    contract = _contract()
    write_public_dashboard(contract, tmp_path)
    output = tmp_path / "dashboard-v2.json"
    assert output.exists()
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["contract_version"] == "2.0"
    assert payload["data_mode"] == "official_public"
