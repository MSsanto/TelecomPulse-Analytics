# Sprint 4 — Evidências técnicas

Data: 2026-09-21  
Branch: `sprint-4-product-quality`  
PR: #5

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

## GitHub Actions — evidência autoritativa

Run de PR validado: `35665115775`  
Commit de implementação validado: `30dfeea7e0e5568f09103944024f1e7fd8acecba`

### Python — PASS

- Ruff: PASS;
- pytest: PASS;
- pipeline base: PASS;
- presentation CLI: PASS;
- artefatos analíticos: PASS.

### Web — PASS

- npm install: PASS;
- `npm audit --audit-level=high`: PASS;
- Vitest: **5 testes PASS**;
- TypeScript/Vite build: PASS;
- contrato no `dist`: PASS;
- bundle budget: PASS.

## Segurança de dependências

O audit não encontrou vulnerabilidades high/critical, portanto o gate configurado passou.

O npm reportou **2 vulnerabilidades moderadas**. Elas não foram ocultadas nem convertidas em “zero vulnerabilidades”; permanecem registradas como risco residual a revisar antes da publicação e em atualizações de dependências.

## Performance

Maior bundle JavaScript medido no CI:

`233685 bytes`

Orçamento definido:

`<= 256000 bytes`

Resultado: **PASS**, com margem aproximada de 22 KiB.

O build Vite concluiu em aproximadamente 828 ms no runner observado. Esse tempo não representa Web Vitals do usuário final.

## Testes frontend

Cinco cenários prioritários:
1. loading → dashboard pronto;
2. filtro de operadora altera apenas detalhe e preserva KPI;
3. dataset vazio;
4. falha HTTP;
5. contrato incompatível.

## Incidente encontrado e corrigido

A primeira rodada dos testes frontend teve 2 falhas por isolamento incompleto entre renders:
- múltiplos elementos “Operadora”;
- múltiplos elementos com role `alert`.

Causa:
- o ambiente Vitest não estava executando cleanup automático entre os testes nessa configuração.

Correção:
- `cleanup()` explícito no `afterEach`;
- globals de fetch restaurados;
- nova rodada: **5/5 testes passando**.

A correção não reduziu cobertura nem relaxou assertions.

## Acessibilidade/UX implementadas

- skip link para indicadores;
- foco visível;
- selects com labels;
- contexto de comportamento dos filtros;
- região rolável da tabela focável;
- caption descritiva invisível visualmente;
- retry em estado de erro;
- reduced motion;
- estados loading/error/empty explícitos.

## Limitações explícitas

- não há auditoria WCAG formal completa;
- não há E2E em navegador real;
- screenshots automáticos não são gerados pelo CI atual;
- Web Vitals reais dependem do ambiente publicado;
- 2 vulnerabilidades npm moderadas permanecem para revisão.

## Resultado técnico

**SPRINT 4: TECHNICALLY READY FOR HUMAN HOMOLOGATION**

Merge e avanço para Sprint 5 permanecem bloqueados até decisão humana.
