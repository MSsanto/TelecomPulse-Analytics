# Sprint 3 — Evidências técnicas

Data: 2026-09-21  
Branch: `sprint-3-dashboard-mvp`

## Governança prévia

Antes da implementação foram relidos:
- `docs/GOVERNANCE.md`;
- `docs/SPRINT_PLAN.md`;
- `docs/ARCHITECTURE.md`;
- `docs/SPRINT_2_EVIDENCE.md`.

## Escopo implementado

- dashboard React/TypeScript;
- cards executivos;
- evolução temporal;
- rankings por operadora, unidade e causa;
- filtros de detalhe;
- tabela de incidentes;
- estados loading, error e empty;
- indicação explícita de dataset sintético;
- responsividade;
- acessibilidade básica;
- geração automática do contrato analítico antes do build;
- validação de presença do contrato no `dist`.

## Regras preservadas

- KPIs críticos continuam vindo do contrato da Sprint 2;
- filtros não recalculam MTTR, disponibilidade ou downtime;
- proporções visuais são apenas apresentação;
- nenhum backend runtime foi introduzido;
- nenhum deploy Cloudflare foi executado.

## Validação autoritativa

O GitHub Actions da branch/PR deve validar:
- Ruff;
- pytest;
- pipelines Python;
- generation do dashboard-v1;
- TypeScript;
- Vite build;
- inclusão de `dist/data/dashboard-v1.json`.

## Estado

**AGUARDANDO CI DA SPRINT 3.**
