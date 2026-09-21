# Sprint 0 — Evidências técnicas

Data: 2026-09-21  
Branch: `sprint-0-foundation`

## Governança prévia

Antes da implementação foram relidos:
- `docs/GOVERNANCE.md`;
- `docs/VALIDATION_BASELINE.md`;
- `docs/PROJECT_CHARTER.md`;
- `docs/ARCHITECTURE.md`;
- `docs/SPRINT_PLAN.md`.

## Validação fora do GitHub

Resultados observados no ambiente de implementação:

- `python -m compileall -q src tests`: **PASS**;
- sanidade do CSV sintético: **PASS** — 4 linhas, 4 IDs únicos, origem `synthetic`;
- varredura básica por nomes de arquivo sensíveis no conteúdo criado: **PASS**.

## Limitação observada

A instalação local de dependências não pôde ser concluída porque o ambiente de execução não conseguiu resolver o host do índice de pacotes. O erro ocorreu antes dos testes dependentes de Pandas/pytest e não foi convertido artificialmente em sucesso.

Por isso, a evidência autoritativa de:
- `ruff check src tests`;
- `pytest -q`;
- execução do pipeline;
- instalação do frontend;
- `npm run build`;

é o workflow `.github/workflows/ci.yml` executado pelo GitHub Actions na branch/PR.

## Resultado esperado do dataset de referência

- incidentes: 4;
- resolvidos: 3;
- downtime resolvido: 180 minutos;
- MTTR de referência: 60 minutos.

## Regra de gate

A Sprint 0 **não pode ser homologada** se o CI do PR não estiver verde. Merge e deploy não fazem parte da execução automática desta rodada.
