# TelecomPulse Analytics

TelecomPulse Analytics é um case de engenharia de dados + analytics + frontend para operações de telecom/NOC. O projeto transforma eventos sintéticos de indisponibilidade em métricas operacionais rastreáveis e em um dashboard web estático.

> Status: **Sprint 4 em validação técnica.** Nenhum deploy Cloudflare foi executado.

## O que o MVP responde

- disponibilidade por janela;
- downtime bruto;
- MTTR;
- quantidade de incidentes;
- recorrência;
- concentração por operadora;
- concentração por unidade/site;
- causas de indisponibilidade;
- evolução temporal;
- detalhe operacional filtrável;
- qualidade dos dados.

## Arquitetura

`CSV sintético → Python/Pandas → validação/normalização → analytics → dashboard-v1.json/CSVs → React/TypeScript/Vite → build estático → Cloudflare (Sprint 5)`

O frontend não recalcula KPIs críticos. Cards, rankings e timeline consomem os agregados homologados produzidos pelo pipeline.

## Stack

### Dados
- Python 3.13
- Pandas
- pytest
- Ruff

### Frontend
- React 19
- TypeScript
- Vite
- Vitest
- Testing Library
- jsdom

## Desenvolvimento local

### 1. Preparar Python

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -e ".[dev]"
ruff check src tests
pytest -q
```

### 2. Executar pipeline

```bash
python -m telecom_pulse.cli
python -m telecom_pulse.presentation_cli
```

### 3. Dashboard

```bash
cd web
npm install
npm test
npm run audit:high
npm run build
npm run dev
```

`npm run dev` e `npm run build` geram automaticamente `web/public/data/dashboard-v1.json` antes de iniciar/buildar.

## Contratos

- `contracts/incident.schema.json`
- `contracts/dashboard-v1.schema.json`

Documentação:
- `docs/METRICS.md`
- `docs/FRONTEND_DATA_CONTRACT.md`
- `docs/ARCHITECTURE.md`

## Governança

A ordem obrigatória de mudança é:

`Normas → Baseline → Validação → Evidências → Documentação → Implementação → Revalidação → Review`

Leia:
- `docs/GOVERNANCE.md`
- `docs/SPRINT_PLAN.md`
- `docs/RISK_REGISTER.md`
- evidências/gates de cada sprint.

## Segurança e dados

- dataset público sintético;
- sem CNPJ, telefone, nome de contato ou identificadores operacionais reais;
- sem secrets ou tokens no frontend;
- `npm audit --audit-level=high` no CI;
- deploy somente após autorização explícita.

## Performance

O CI da Sprint 4 limita o maior bundle JavaScript principal a **250 KiB não comprimido**. O contrato JSON permanece separado do bundle.

## Estado das sprints

- Sprint 0 — fundação: homologada e mergeada.
- Sprint 1 — dados/qualidade: homologada e mergeada.
- Sprint 2 — analytics/contratos: homologada e mergeada.
- Sprint 3 — dashboard MVP: homologada e mergeada.
- Sprint 4 — qualidade de produto/engenharia: em validação.
- Sprint 5 — Cloudflare/release: não iniciada.

## Dados

O dataset público de referência é sintético e existe apenas para tornar o case reproduzível e seguro.
