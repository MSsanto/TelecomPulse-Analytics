# Sprint 0 — Gate de homologação humana

## Escopo implementado

A Sprint 0 entrega somente fundação técnica. Não entrega dashboard funcional nem deploy.

## Evidências técnicas concluídas

- [x] `ruff check src tests` verde.
- [x] `pytest -q` verde.
- [x] pipeline de referência executa.
- [x] resumo de referência: 4 incidentes, 3 resolvidos, 180 min de downtime e MTTR de 60 min.
- [x] instalação de dependências do frontend verde em `web/`.
- [x] `npm run build` verde em `web/`.
- [x] GitHub Actions verde após correção do erro TS5096.
- [x] nenhum `.env`, token ou secret foi intencionalmente versionado.
- [x] dataset está identificado como sintético.
- [x] README contém comandos de setup e validação.
- [x] nenhum deploy Cloudflare foi executado.

## Itens para decisão humana

- [ ] Aprovar Python 3.13 + Pandas + pytest + Ruff como baseline do pipeline.
- [ ] Aprovar React + TypeScript + Vite como baseline do frontend.
- [ ] Aprovar dataset sintético como fonte oficial do MVP público.
- [ ] Aprovar arquitetura sem Worker/D1 no MVP inicial.
- [ ] Aprovar merge da Sprint 0 na `main`.

## O que validar visualmente/humanamente

1. O escopo da Sprint 0 corresponde ao que você esperava para a fundação.
2. O projeto não está sofisticado demais para o MVP.
3. O dataset sintético é aceitável como base pública inicial.
4. A separação Python analytics + frontend está coerente.
5. O PR #1 pode ser incorporado à `main`.

## Fora da homologação

- Cloudflare deploy;
- domínio público;
- KPIs finais da Sprint 1;
- UX final;
- dados corporativos reais.

## Estado

**AGUARDANDO HOMOLOGAÇÃO HUMANA.**

Não fazer merge nem iniciar Sprint 1 automaticamente antes da decisão humana.
