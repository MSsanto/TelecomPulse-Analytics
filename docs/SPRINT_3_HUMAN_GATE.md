# Sprint 3 — Gate de homologação humana

## Escopo

Esta sprint entrega o dashboard MVP local/buildável. Não executa deploy.

## Evidências técnicas concluídas

- [x] Ruff verde.
- [x] pytest verde.
- [x] pipeline analítico verde.
- [x] TypeScript verde.
- [x] Vite build verde.
- [x] contrato dashboard v1 presente no `dist`.
- [x] cards usam apenas `summary`.
- [x] rankings usam agregados homologados.
- [x] filtros afetam somente detalhe.
- [x] estados loading/error/empty implementados.
- [x] dataset sintético sinalizado.
- [x] layout responsivo implementado.
- [x] labels/semântica básica de acessibilidade presentes.
- [x] nenhum deploy executado.

## Itens para decisão humana

- [ ] Aprovar direção visual do dashboard.
- [ ] Aprovar cards executivos.
- [ ] Aprovar visualização temporal.
- [ ] Aprovar rankings.
- [ ] Aprovar regra de filtros somente no detalhe.
- [ ] Aprovar tabela operacional.
- [ ] Aprovar merge e avanço para Sprint 4.

## O que observar na homologação

1. A hierarquia visual deixa disponibilidade, downtime, MTTR e volume fáceis de identificar?
2. A distinção “dataset sintético” está visível o suficiente?
3. Timeline e rankings ajudam a responder onde e quando ocorreu impacto?
4. Os filtros de detalhe são compreensíveis sem sugerir que os cards foram recalculados?
5. A tabela é adequada para investigação operacional?
6. Em mobile, o dashboard continua navegável sem esconder informação crítica?

## Fora do escopo

- auditoria UX aprofundada;
- testes frontend extensivos;
- WCAG completa;
- otimização avançada;
- segurança/dependency review final;
- Cloudflare deploy.

Esses itens pertencem principalmente à Sprint 4.

## Estado

**AGUARDANDO HOMOLOGAÇÃO HUMANA.**
