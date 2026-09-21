# Sprint 2 — Evidências técnicas

Data: 2026-09-21  
Branch: `sprint-2-analytics-contracts`  
PR: #3

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
- JSON de dashboard;
- CSVs auxiliares;
- disponibilidade por site-time sem dupla contagem;
- reconciliação de incidentes e downtime bruto;
- documentação explícita das métricas;
- geração determinística de artefatos;
- CI validando todos os artefatos esperados.

## Contrato de apresentação

Artefatos gerados:
- `data/presentation/dashboard-v1.json`;
- `data/presentation/by_carrier.csv`;
- `data/presentation/by_site.csv`;
- `data/presentation/by_cause.csv`;
- `data/presentation/timeline.csv`;
- `data/presentation/incidents.csv`.

Os arquivos são gerados pelo pipeline e permanecem fora do controle de versão. O contrato e a lógica geradora são versionados.

## Semântica validada

### Downtime bruto

É soma de duração por incidente resolvido e reconcilia entre:
- detalhe;
- operadora;
- site;
- causa;
- timeline por data de abertura.

### Disponibilidade

Usa site-time:
- janela explícita;
- recorte dos intervalos à janela;
- merge de intervalos sobrepostos/tangentes por site;
- denominador = quantidade de sites × minutos da janela.

Logo, disponibilidade não deriva cegamente do downtime bruto quando existe sobreposição.

### Timeline

A Sprint 2 agrupa por data UTC de abertura do incidente. Downtime de um incidente é atribuído à sua data de abertura.

## GitHub Actions — evidência autoritativa da implementação

Run validado: `35657147142`  
Commit da implementação validada: `58675f00b76c725b1824b11a010f0011f6013e99`

### Python — PASS

- instalação: PASS;
- Ruff: **All checks passed**;
- pytest: **15 passed in 0.84s**;
- pipeline base: PASS;
- presentation CLI: PASS;
- seis artefatos esperados: PASS.

### Web — PASS

- npm install: PASS;
- npm run build: PASS.

## Incidente encontrado e corrigido

O primeiro pytest da Sprint 2 revelou uma regressão no teste legado de disponibilidade: a semântica nova passou a ser site-time e, corretamente, exige `site_id`.

O fixture legado possuía apenas status e timestamps. Como `site_id` já é obrigatório pelo contrato de incidente homologado na Sprint 1, a correção foi alinhar o fixture ao contrato, sem adicionar fallback que escondesse dados incompletos.

Após a correção:
- 15 testes passaram;
- geração de artefatos passou;
- build web permaneceu verde.

## Revisão de escopo

- nenhum dashboard funcional foi implementado;
- nenhuma biblioteca de gráficos foi adicionada;
- nenhum cálculo crítico foi movido para o browser;
- nenhum dado corporativo real foi adicionado;
- nenhum deploy Cloudflare foi executado;
- Worker/D1 continuam fora do escopo.

## Resultado técnico

**SPRINT 2: TECHNICALLY READY FOR HUMAN HOMOLOGATION**

Merge e avanço para Sprint 3 permanecem bloqueados até decisão humana.
