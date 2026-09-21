# Sprint 0 — Evidências técnicas

Data: 2026-09-21  
Branch: `sprint-0-foundation`  
PR: #1

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

A instalação local de dependências não pôde ser concluída porque o ambiente executor não resolveu o host do índice de pacotes. O erro ocorreu antes dos testes dependentes de Pandas/pytest e não foi convertido artificialmente em sucesso.

## GitHub Actions — evidência autoritativa

Run validado: `35653626384`  
Commit validado: `91a40edeef793ee7baaeacbc39b1a1fbb801aaed`

### Job Python — PASS

- checkout: PASS;
- Python 3.13: PASS;
- instalação do pacote e dependências: PASS;
- `ruff check src tests`: PASS;
- `pytest -q`: PASS;
- `python -m telecom_pulse.cli`: PASS.

### Job Web — PASS

- checkout: PASS;
- Node 22: PASS;
- `npm install`: PASS;
- `npm run build`: PASS.

## Incidente encontrado e corrigido

O primeiro build web falhou com TypeScript TS5096 porque `allowImportingTsExtensions` estava habilitado em `tsconfig.node.json` sem `noEmit` ou `emitDeclarationOnly`.

Correção aplicada:
- remoção da opção incompatível;
- novo CI executado;
- build web passou.

Isso confirma que a correção foi orientada por causa raiz observada no log, não por tentativa aleatória.

## Resultado do dataset de referência

- incidentes: 4;
- resolvidos: 3;
- downtime resolvido: 180 minutos;
- MTTR de referência: 60 minutos.

## Revisão de escopo

- nenhuma feature de dashboard foi antecipada;
- nenhum dado corporativo real foi usado;
- nenhum segredo foi adicionado;
- nenhum deploy Cloudflare foi executado;
- Worker/D1 continuam fora da Sprint 0;
- código, testes, CI, README e evidências estão na mesma branch governada.

## Resultado técnico

**SPRINT 0: TECHNICALLY READY FOR HUMAN HOMOLOGATION**

Merge e deploy permanecem bloqueados até decisão humana.
