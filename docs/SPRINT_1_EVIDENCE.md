# Sprint 1 — Evidências técnicas

Data: 2026-09-21  
Branch: `sprint-1-data-quality`  
PR: #2

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
- testes automatizados das regras críticas;
- CI corrigido para validar qualquer branch e pull request.

## Regras validadas por teste

- coluna obrigatória ausente bloqueia ingestão;
- incidente duplicado é rejeitado;
- incidente resolvido sem `restored_at` é rejeitado;
- downtime negativo é rejeitado;
- normalização de carrier/status/cause/link_type é determinística;
- intervalos sobrepostos não duplicam downtime;
- disponibilidade respeita os limites da janela;
- pipeline gera dataset processado e relatório de qualidade.

## GitHub Actions — evidência autoritativa

Run validado: `35654481390`  
Commit validado: `59838355d6ce538a3480505f82c0304e5355f1c0`

### Python — PASS

- instalação: PASS;
- Ruff: **All checks passed**;
- pytest: **9 passed in 0.23s**;
- pipeline CLI: PASS.

Resultado do pipeline:
- incident_count = 4;
- resolved_incident_count = 3;
- downtime_minutes = 180.0;
- mttr_minutes = 60.0;
- recurrence_count = 1.

### Web — PASS

- npm install: PASS;
- npm run build: PASS.

## Falhas encontradas e tratadas

O lint identificou formatação inadequada do bloco de imports do gerador sintético. A implementação foi simplificada para eliminar dependências desnecessárias no gerador e o CI foi reexecutado até passar integralmente.

Também foi identificado que o workflow da Sprint 0 limitava `push` à `main` e à antiga branch da Sprint 0. O CI foi corrigido para validar todas as branches e pull requests.

## Revisão de escopo

- nenhum dashboard funcional foi antecipado;
- nenhum dado corporativo real foi usado;
- nenhum segredo foi adicionado;
- nenhum deploy Cloudflare foi executado;
- Worker/D1 continuam fora do escopo;
- dados processados gerados são ignorados pelo Git.

## Resultado técnico

**SPRINT 1: TECHNICALLY READY FOR HUMAN HOMOLOGATION**

Merge e avanço para Sprint 2 permanecem bloqueados até decisão humana.
