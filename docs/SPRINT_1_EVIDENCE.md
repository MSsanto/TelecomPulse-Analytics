# Sprint 1 — Evidências técnicas

Data: 2026-09-21  
Branch: `sprint-1-data-quality`

## Governança prévia

Antes da implementação foram relidos:
- `docs/GOVERNANCE.md`;
- `docs/SPRINT_PLAN.md`;
- `docs/ARCHITECTURE.md`.

## Escopo implementado

- contrato versionado de incidente;
- gerador de dataset sintético;
- normalização determinística;
- validação de campos e regras temporais;
- detecção de duplicidades;
- relatório de qualidade;
- KPI de recorrência;
- downtime sem dupla contagem de sobreposição;
- disponibilidade com recorte da janela de análise;
- testes automatizados das regras críticas.

## Regras validadas por teste

- coluna obrigatória ausente bloqueia ingestão;
- incidente duplicado é rejeitado;
- incidente resolvido sem `restored_at` é rejeitado;
- downtime negativo é rejeitado;
- normalização de carrier/status/cause/link_type é determinística;
- intervalos sobrepostos não duplicam downtime;
- disponibilidade respeita os limites da janela;
- pipeline gera dataset processado e relatório de qualidade.

## Resultado esperado de referência

Dataset base:
- 4 incidentes;
- 3 resolvidos;
- 180 minutos de downtime bruto;
- MTTR = 60 minutos;
- recurrence_count = 1.

## Validação autoritativa

O GitHub Actions da branch/PR é o validador autoritativo para:
- Ruff;
- pytest;
- execução do pipeline;
- regressão de build frontend.

## Estado

**AGUARDANDO CI DA SPRINT 1.**

Este documento deve ser atualizado com run/commit verde antes da homologação humana.
