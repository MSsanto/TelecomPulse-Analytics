from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

COMPETITION_REQUIRED = {
    "service",
    "period",
    "geography",
    "provider",
    "metric",
    "value",
    "unit",
    "source_id",
}

SATISFACTION_REQUIRED = {
    "year",
    "service",
    "provider",
    "isg",
    "source_id",
}


def _require_columns(frame: pd.DataFrame, required: set[str], name: str) -> None:
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"{name}: missing required columns: {sorted(missing)}")


def load_competition_snapshot(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    _require_columns(frame, COMPETITION_REQUIRED, "competition")
    if frame["value"].isna().any() or frame["value"].lt(0).any():
        raise ValueError("competition: invalid numeric value")
    if frame.duplicated(["service", "period", "geography", "provider", "metric"]).any():
        raise ValueError("competition: duplicate observation")
    return frame


def load_satisfaction_snapshot(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    _require_columns(frame, SATISFACTION_REQUIRED, "satisfaction")
    if frame["isg"].isna().any() or ~frame["isg"].between(0, 10).all():
        raise ValueError("satisfaction: ISG must be between 0 and 10")
    if frame.duplicated(["year", "service", "provider"]).any():
        raise ValueError("satisfaction: duplicate observation")
    return frame


def top_providers_by_metric(
    frame: pd.DataFrame,
    service: str,
    metric: str,
    n: int = 5,
) -> list[dict[str, object]]:
    if n <= 0:
        raise ValueError("n must be positive")
    selected = frame[
        frame["service"].eq(service)
        & frame["metric"].eq(metric)
        & frame["provider"].ne("TOTAL")
    ].sort_values(["value", "provider"], ascending=[False, True])
    return [
        {
            "provider": str(row.provider),
            "value": float(row.value),
            "unit": str(row.unit),
        }
        for row in selected.head(n).itertuples()
    ]


def _single_metric(frame: pd.DataFrame, service: str, metric: str) -> float | None:
    selected = frame[
        frame["service"].eq(service)
        & frame["metric"].eq(metric)
        & frame["provider"].eq("TOTAL")
    ]
    if selected.empty:
        return None
    if len(selected) != 1:
        raise ValueError(f"expected one total observation for {service}/{metric}")
    return float(selected.iloc[0]["value"])


def _period_for(frame: pd.DataFrame, service: str) -> str:
    periods = sorted(frame.loc[frame["service"].eq(service), "period"].unique())
    if len(periods) != 1:
        raise ValueError(f"expected one period for reference snapshot {service}: {periods}")
    return str(periods[0])


def build_public_dashboard(
    competition: pd.DataFrame,
    satisfaction: pd.DataFrame,
    source_registry: dict[str, object],
) -> dict[str, object]:
    source_ids = sorted(
        set(competition["source_id"].astype(str))
        | set(satisfaction["source_id"].astype(str))
    )

    return {
        "contract_version": "2.0",
        "data_mode": "official_public",
        "authority": "Agência Nacional de Telecomunicações - Anatel",
        "market": {
            "SMP": {
                "service_name": "Telefonia móvel",
                "period": _period_for(competition, "SMP"),
                "geography": "BR",
                "total_accesses": _single_metric(competition, "SMP", "accesses"),
                "accesses_5g": _single_metric(competition, "SMP", "accesses_5g"),
                "share_5g_pct": _single_metric(competition, "SMP", "share_5g"),
                "provider_market_share": top_providers_by_metric(
                    competition, "SMP", "market_share", 10
                ),
                "ranking_complete": False,
            },
            "SCM": {
                "service_name": "Banda larga fixa",
                "period": _period_for(competition, "SCM"),
                "geography": "BR",
                "total_accesses": _single_metric(competition, "SCM", "accesses"),
                "fiber_accesses": _single_metric(competition, "SCM", "fiber_accesses"),
                "provider_market_share": top_providers_by_metric(
                    competition, "SCM", "market_share", 10
                ),
                "ranking_complete": False,
            },
        },
        "satisfaction": {
            "year": int(satisfaction["year"].max()),
            "rows": [
                {
                    "service": str(row.service),
                    "provider": str(row.provider),
                    "isg": float(row.isg),
                }
                for row in satisfaction.sort_values(
                    ["service", "isg", "provider"],
                    ascending=[True, False, True],
                ).itertuples()
            ],
        },
        "sources": [
            source
            for source in source_registry["sources"]
            if source["source_id"] in source_ids
        ],
        "methodology_notes": [
            "Valores são provenientes de publicações oficiais da Anatel.",
            "Rankings do snapshot são parciais até a ingestão mensal SMP/SCM.",
            "Ausência de prestadora no snapshot não significa participação zero.",
            "SMP e SCM são mercados distintos e não são somados em um ranking único.",
        ],
    }


def write_public_dashboard(contract: dict[str, object], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "dashboard-v2.json").write_text(
        json.dumps(contract, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
