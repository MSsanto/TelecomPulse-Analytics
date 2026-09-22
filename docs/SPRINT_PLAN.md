# TelecomPulse Analytics v2 — Plano de Reescrita

## Fase anterior — Protótipo sintético

Sprints 0–5 provaram:
- governança;
- pipeline;
- testes;
- contrato;
- frontend;
- CI/CD;
- Cloudflare.

**Status:** encerrada como ensaio técnico.

---

## Sprint R0 — Real Data Foundation

### Objetivo
Trocar o centro de gravidade do projeto de incidentes sintéticos para dados públicos oficiais.

### Entregas
- novo charter;
- catálogo de fontes;
- arquitetura v2;
- modelo canônico de prestadora/serviço/período/geografia;
- snapshots públicos de referência;
- funções de market share e Top N;
- testes de reconciliação;
- documentação de proveniência.

### Gate
Nenhum dashboard v2 antes de fontes e contratos estarem validados.

---

## Sprint R1 — Ingestão Anatel SMP/SCM

### Objetivo
Automatizar acessos móveis e banda larga fixa.

### Entregas
- download/versionamento lógico;
- parser SMP;
- parser SCM;
- normalização de prestadoras;
- normalização geográfica;
- marts de acessos;
- Top 5/10 dinâmico;
- market share;
- crescimento temporal.

### Gate
Totais nacionais e rankings reconciliam com a fonte oficial.

---

## Sprint R2 — Qualidade e Consumidor

### Objetivo
Adicionar RQUAL, reclamações e satisfação sem fabricar score próprio.

### Entregas
- IQS/Selos;
- indicadores técnicos;
- IR/reclamações;
- IQP/ISG;
- cruzamentos por serviço/prestadora/geografia/período;
- regras explícitas para dado ausente.

---

## Sprint R3 — Dashboard Real v2

### Objetivo
Substituir visualmente o dashboard sintético.

### Seções
- panorama do mercado;
- Top 5/10;
- evolução;
- qualidade;
- consumidor;
- cobertura/tecnologia;
- geografia;
- metodologia/fontes.

### Gate
Nenhum rótulo sintético na página principal.

---

## Sprint R4 — QA, metodologia e publicação

- E2E;
- acessibilidade;
- performance;
- SEO técnico;
- data freshness;
- smoke test público;
- changelog;
- release v2.

---

## Pós-v2

- comparação de períodos;
- HHI/concentração;
- mapa municipal;
- séries históricas longas;
- download de datasets tratados;
- API somente se houver necessidade comprovada.
