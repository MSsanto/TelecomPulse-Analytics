# Sprint 0 — Gate de homologação humana

## Escopo implementado

A Sprint 0 entrega somente fundação técnica. Não entrega dashboard funcional nem deploy.

## Evidências esperadas antes da homologação

- [ ] `ruff check src tests` verde.
- [ ] `pytest -q` verde.
- [ ] pipeline de referência executa e gera `data/processed/incidents.csv`.
- [ ] resumo de referência: 4 incidentes, 3 resolvidos, 180 min de downtime e MTTR de 60 min.
- [ ] instalação de dependências do frontend verde em `web/`.
- [ ] `npm run build` verde em `web/`.
- [ ] GitHub Actions verde no PR.
- [ ] nenhum `.env`, token ou secret versionado.
- [ ] dataset está identificado como sintético.

## Itens para decisão humana

1. Aprovar Python 3.13 + Pandas + pytest + Ruff como baseline do pipeline.
2. Aprovar React + TypeScript + Vite como baseline do frontend.
3. Aprovar dataset sintético como fonte oficial do MVP público.
4. Aprovar arquitetura sem Worker/D1 no MVP inicial.
5. Aprovar merge da Sprint 0 na `main`.

## Fora da homologação

- Cloudflare deploy;
- domínio público;
- KPIs finais da Sprint 1;
- UX final;
- dados corporativos reais.
