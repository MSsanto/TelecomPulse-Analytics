# TelecomPulse Analytics

Plataforma de analytics para operações de telecom e NOC, focada em transformar eventos operacionais de conectividade em indicadores de disponibilidade, SLA, incidentes, reincidência e desempenho por operadora/unidade.

> Status: **Sprint 0 implementada em branch e aguardando homologação humana.** Nenhum deploy foi executado.

## Objetivo

Criar um case de engenharia de dados + analytics + produto web que demonstre, de ponta a ponta:

- ingestão e tratamento de dados operacionais;
- qualidade e rastreabilidade dos dados;
- modelagem de métricas de NOC/telecom;
- geração de indicadores acionáveis;
- visualização em dashboard web;
- publicação controlada no Cloudflare;
- validação técnica e evidências de cada entrega.

## MVP

O MVP deve responder, no mínimo:

1. Qual a disponibilidade por período, unidade e operadora?
2. Quantos incidentes ocorreram e quanto tempo duraram?
3. Qual o MTTR?
4. Quais unidades, links e operadoras mais reincidem?
5. Quais causas concentram maior indisponibilidade?
6. Qual a evolução temporal dos principais indicadores?
7. Quais registros apresentam problema de qualidade de dados?

## Arquitetura-alvo inicial

`Dados brutos → Python/Pandas → validação/normalização → camada analítica → JSON/CSV processado → React/Vite → Cloudflare`

Banco/API não fazem parte do MVP inicial sem necessidade comprovada.

## Desenvolvimento local

### Pipeline Python

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
python -m telecom_pulse.cli
```

O pipeline usa por padrão `data/raw/incidents_synthetic.csv` e gera `data/processed/incidents.csv`.

### Frontend

```bash
cd web
npm install
npm run build
npm run dev
```

O frontend da Sprint 0 é apenas uma tela de fundação. O dashboard funcional começa depois da homologação desta sprint.

## CI

O workflow `.github/workflows/ci.yml` executa:

- Ruff;
- pytest;
- pipeline de referência;
- instalação do frontend;
- build React/TypeScript/Vite.

## Governança

Antes de qualquer implementação funcional, ler:

- [Governança](docs/GOVERNANCE.md)
- [Pré-projeto](docs/PROJECT_CHARTER.md)
- [Arquitetura](docs/ARCHITECTURE.md)
- [Plano de Sprints](docs/SPRINT_PLAN.md)
- [Baseline de validação](docs/VALIDATION_BASELINE.md)
- [Evidências Sprint 0](docs/SPRINT_0_EVIDENCE.md)
- [Gate humano Sprint 0](docs/SPRINT_0_HUMAN_GATE.md)
- [Template de mudança](docs/CHANGE_TEMPLATE.md)

## Estado do projeto

- Repositório: criado.
- Cloudflare: ambiente criado pelo proprietário do projeto.
- Integração/deploy Cloudflare: ainda não homologado.
- Sprint 0: implementada na branch `sprint-0-foundation`.
- PR de homologação: #1.
- Merge: pendente de CI verde + decisão humana.
- Dados reais de produção: não autorizados no repositório público.
