# Sprint 4 — Evidências técnicas

Data: 2026-09-21  
Branch: `sprint-4-product-quality`

## Governança prévia

Antes da implementação foram relidos:
- `docs/GOVERNANCE.md`;
- `docs/SPRINT_PLAN.md`;
- `docs/ARCHITECTURE.md`;
- `docs/SPRINT_3_EVIDENCE.md`.

## Escopo implementado

- testes frontend prioritários;
- fixture tipada do contrato dashboard v1;
- testes de loading, ready, empty e error;
- teste de filtro preservando KPIs executivos;
- skip link;
- foco visível;
- tabela com contexto acessível;
- recuperação de erro com retry;
- npm audit high/critical no CI;
- orçamento de bundle JavaScript;
- README atualizado;
- arquitetura atualizada;
- registro de riscos residuais.

## Validadores esperados

### Python
- Ruff;
- pytest;
- pipeline base;
- presentation CLI;
- artefatos analíticos.

### Web
- npm install;
- npm audit --audit-level=high;
- Vitest;
- TypeScript/Vite build;
- contrato no dist;
- bundle <= 250 KiB.

## Limitações explícitas

- não há auditoria WCAG formal completa;
- não há E2E em navegador real;
- screenshots automáticos não são gerados pelo CI atual;
- Web Vitals reais dependem do ambiente publicado e permanecem para validação posterior.

## Estado

**AGUARDANDO CI DA SPRINT 4.**
