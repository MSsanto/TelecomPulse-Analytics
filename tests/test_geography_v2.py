import pytest

from telecom_pulse.geography import REGIONS, STATES, reconcile_additive, states_for_region


def test_geography_has_five_regions_and_27_ufs():
    assert set(REGIONS) == {"N", "NE", "CO", "SE", "S"}
    assert len(STATES) == 27
    assert len({state.ibge_code for state in STATES.values()}) == 27


def test_sao_paulo_identity_is_canonical():
    sp = STATES["SP"]
    assert sp.name == "São Paulo"
    assert sp.ibge_code == "35"
    assert sp.region_code == "SE"
    assert sp.region_name == "Sudeste"
    assert sp.ibge_region_code == "3"


def test_sudeste_contains_exactly_four_ufs():
    assert {state.code for state in states_for_region("SE")} == {"ES", "MG", "RJ", "SP"}


def test_reconcile_sudeste_reference_snapshot():
    # Reference snapshot documented in docs/REAL_DATA_SPRINT_0_EVIDENCE.md.
    values = {
        "SP": 86_765_457,
        "MG": 27_665_157,
        "RJ": 22_093_588,
        "ES": 5_014_235,
    }
    assert reconcile_additive(values, "SE") == 141_538_437


def test_reconciliation_rejects_incomplete_region():
    with pytest.raises(ValueError, match="missing"):
        reconcile_additive({"SP": 1}, "SE")


def test_reconciliation_rejects_cross_region_state():
    with pytest.raises(ValueError, match="extras"):
        reconcile_additive({"SP": 1, "MG": 1, "RJ": 1, "ES": 1, "PR": 1}, "SE")
