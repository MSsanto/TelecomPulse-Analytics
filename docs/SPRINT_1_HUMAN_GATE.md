# Sprint 1 — Gate de homologação humana

## Escopo

Esta sprint entrega o núcleo confiável de dados. Não entrega dashboard funcional nem deploy.

## Evidências técnicas concluídas

- [x] Ruff verde.
- [x] pytest verde — 9 testes.
- [x] pipeline executa.
- [x] quality report é gerado.
- [x] build frontend regressivo verde.
- [x] contrato de incidente versionado.
- [x] sobreposição temporal coberta por teste.
- [x] disponibilidade coberta por teste.
- [x] nenhum dado real/confidencial foi adicionado.
- [x] CI agora valida qualquer branch e pull request.

## Itens para decisão humana

- [ ] Aprovar o contrato inicial de incidente.
- [ ] Aprovar a estratégia de normalização.
- [ ] Aprovar rejeição de erros críticos em vez de correção silenciosa.
- [ ] Aprovar disponibilidade calculada sem dupla contagem de intervalos sobrepostos.
- [ ] Aprovar merge da Sprint 1 e avanço para Sprint 2.

## O que está sendo homologado

1. Dados inválidos críticos não são corrigidos silenciosamente.
2. Carrier/status/cause/link_type recebem normalização previsível.
3. Duplicidades por `incident_id` são bloqueadas.
4. Incidente resolvido sem data de restauração é inválido.
5. Intervalos sobrepostos não somam downtime duas vezes.
6. Dataset público continua sintético.

## Fora do escopo

- dashboard;
- charts;
- Cloudflare deploy;
- Worker/D1;
- autenticação;
- dados corporativos reais.

## Estado

**AGUARDANDO HOMOLOGAÇÃO HUMANA.**
