# Sprint 3 — Evidências técnicas

Data: 2026-09-21  
Branch: `sprint-3-dashboard-mvp`  
PR: #4

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

## GitHub Actions — evidência autoritativa

Run validado: `35660133355`  
Commit validado: `be2f02348807d45a5a660d9d1a6e81c7e827217d`

### Python — PASS

- instalação: PASS;
- Ruff: PASS;
- pytest: PASS;
- pipeline base: PASS;
- presentation CLI: PASS;
- seis artefatos analíticos: PASS.

### Web — PASS

- Python 3.13 preparado no job web: PASS;
- pacote analytics instalado: PASS;
- Node 22: PASS;
- npm install: PASS;
- prebuild gerando `web/public/data/dashboard-v1.json`: PASS;
- TypeScript: PASS;
- Vite build: PASS;
- `dist/data/dashboard-v1.json`: PASS.

## Incidente encontrado e corrigido

O primeiro build da Sprint 3 falhou com TypeScript TS7053 na renderização genérica dos rankings.

Causa:
- a UI tentava indexar uma união de tipos (`CarrierMetric | SiteMetric | CauseMetric`) com uma chave dinâmica.

Correção:
- rankings passaram a receber uma estrutura comum `MetricRow & { label: string }`;
- cada coleção transforma somente o rótulo de apresentação;
- nenhuma métrica foi recalculada;
- novo CI executado e aprovado.

## Comportamento do dashboard

### Cards
Usam exclusivamente `summary`.

### Timeline
Usa exclusivamente `timeline`. Altura das barras é uma proporção visual.

### Rankings
Usam exclusivamente `by_carrier`, `by_site` e `by_cause`. Ordenação e largura de barra são apresentação.

### Filtros
Atuam somente em `incidents`:
- operadora;
- unidade;
- causa;
- status.

KPIs e rankings permanecem nos agregados homologados para não criar métricas multidimensionais não materializadas.

### Estados
- loading;
- error;
- empty;
- ready.

## Responsividade e acessibilidade implementadas

- layout adaptativo;
- tabela com overflow horizontal;
- labels associados aos selects;
- headings/sections semânticos;
- foco visível;
- `aria-live` no loading;
- `role=alert` no erro;
- `prefers-reduced-motion` respeitado.

A auditoria aprofundada permanece para a Sprint 4.

## Revisão de escopo

- nenhum deploy Cloudflare;
- nenhum Worker/D1;
- nenhuma autenticação;
- nenhum dado corporativo real;
- nenhuma fórmula crítica duplicada no browser.

## Resultado técnico

**SPRINT 3: TECHNICALLY READY FOR HUMAN HOMOLOGATION**

Merge e avanço para Sprint 4 permanecem bloqueados até decisão humana.
