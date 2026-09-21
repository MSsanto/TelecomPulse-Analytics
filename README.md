# TelecomPulse Analytics

Plataforma de analytics para operações de telecom e NOC, focada em transformar eventos operacionais de conectividade em indicadores de disponibilidade, SLA, incidentes, reincidência e desempenho por operadora/unidade.

> Status: **pré-projeto / Sprint 0**. Ainda não existe implementação funcional homologada.

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

## Governança

Antes de qualquer implementação funcional, ler:

- [Governança](docs/GOVERNANCE.md)
- [Pré-projeto](docs/PROJECT_CHARTER.md)
- [Arquitetura](docs/ARCHITECTURE.md)
- [Plano de Sprints](docs/SPRINT_PLAN.md)
- [Baseline de validação](docs/VALIDATION_BASELINE.md)
- [Template de mudança](docs/CHANGE_TEMPLATE.md)

## Estado do projeto

- Repositório: criado.
- Cloudflare: ambiente criado pelo proprietário do projeto.
- Integração/deploy reproduzível: ainda não validado.
- Código funcional: ainda não iniciado.
- Dados reais de produção: não autorizados no repositório público.
