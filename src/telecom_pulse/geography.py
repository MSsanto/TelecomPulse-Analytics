from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class State:
    code: str
    name: str
    ibge_code: str
    region_code: str
    region_name: str
    ibge_region_code: str


REGIONS = {
    "N": ("Norte", "1"),
    "NE": ("Nordeste", "2"),
    "SE": ("Sudeste", "3"),
    "S": ("Sul", "4"),
    "CO": ("Centro-Oeste", "5"),
}

_STATES = [
    ("AC", "Acre", "12", "N"),
    ("AP", "Amapá", "16", "N"),
    ("AM", "Amazonas", "13", "N"),
    ("PA", "Pará", "15", "N"),
    ("RO", "Rondônia", "11", "N"),
    ("RR", "Roraima", "14", "N"),
    ("TO", "Tocantins", "17", "N"),
    ("AL", "Alagoas", "27", "NE"),
    ("BA", "Bahia", "29", "NE"),
    ("CE", "Ceará", "23", "NE"),
    ("MA", "Maranhão", "21", "NE"),
    ("PB", "Paraíba", "25", "NE"),
    ("PE", "Pernambuco", "26", "NE"),
    ("PI", "Piauí", "22", "NE"),
    ("RN", "Rio Grande do Norte", "24", "NE"),
    ("SE", "Sergipe", "28", "NE"),
    ("DF", "Distrito Federal", "53", "CO"),
    ("GO", "Goiás", "52", "CO"),
    ("MS", "Mato Grosso do Sul", "50", "CO"),
    ("MT", "Mato Grosso", "51", "CO"),
    ("ES", "Espírito Santo", "32", "SE"),
    ("MG", "Minas Gerais", "31", "SE"),
    ("RJ", "Rio de Janeiro", "33", "SE"),
    ("SP", "São Paulo", "35", "SE"),
    ("PR", "Paraná", "41", "S"),
    ("RS", "Rio Grande do Sul", "43", "S"),
    ("SC", "Santa Catarina", "42", "S"),
]

STATES = {
    code: State(
        code=code,
        name=name,
        ibge_code=ibge_code,
        region_code=region_code,
        region_name=REGIONS[region_code][0],
        ibge_region_code=REGIONS[region_code][1],
    )
    for code, name, ibge_code, region_code in _STATES
}


def states_for_region(region_code: str) -> tuple[State, ...]:
    if region_code not in REGIONS:
        raise ValueError(f"unknown region: {region_code}")
    return tuple(state for state in STATES.values() if state.region_code == region_code)


def reconcile_additive(values_by_state: dict[str, int], region_code: str) -> int:
    expected_states = {state.code for state in states_for_region(region_code)}
    provided = set(values_by_state)

    unknown = provided - set(STATES)
    if unknown:
        raise ValueError(f"unknown state codes: {sorted(unknown)}")

    missing = expected_states - provided
    extras = provided - expected_states
    if missing or extras:
        raise ValueError(
            f"invalid state coverage for {region_code}: "
            f"missing={sorted(missing)} extras={sorted(extras)}"
        )

    if any(value < 0 for value in values_by_state.values()):
        raise ValueError("additive values cannot be negative")

    return sum(values_by_state.values())
