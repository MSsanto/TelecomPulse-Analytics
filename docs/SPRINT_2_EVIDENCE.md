# Sprint 2 — Evidências técnicas

Data: 2026-09-21  
Branch: `sprint-2-analytics-contracts`

## Governança prévia

Antes da implementação foram relidos:
- `docs/GOVERNANCE.md`;
- `docs/SPRINT_PLAN.md`;
- `docs/ARCHITECTURE.md`;
- `docs/SPRINT_1_EVIDENCE.md`.

## Escopo implementado

- contrato dashboard v1 versionado;
- visão geral;
- agregações por operadora;
- agregações por unidade;
- agregações por causa;
- série temporal por data de abertura;
- detalhe serializável;
- CSVs auxiliares;
- disponibilidade por site-time sem dupla contagem;
- reconciliação de incidentes e downtime bruto;
- documentação de métricas;
- geração determinística de artefatos.

## Artefatos esperados

- `dashboard-v1.json`;
- `by_carrier.csv`;
- `by_site.csv`;
- `by_cause.csv`;
- `timeline.csv`;
- `incidents.csv`.

## Validação autoritativa

O GitHub Actions da branch/PR valida:
- Ruff;
- pytest;
- pipeline;
- geração dos artefatos;
- existência dos arquivos do contrato;
- regressão do build web.

## Estado

**AGUARDANDO CI DA SPRINT 2.**
