# TelecomPulse Analytics — Backlog

## P0 — Real Data Reboot

**Status:** Sprint R0 pronta para fechamento por aquisição manual governada ou automática — **NO-GO enquanto os raws oficiais SMP/SCM não estiverem registrados**.

### Objetivo imediato
Validar e ingerir a primeira amostra real ANATEL + IBGE antes de implementar o mapa.

### Itens
- [x] arquitetura do reboot;
- [x] catálogo inicial de fontes;
- [x] contrato geográfico v2;
- [x] epic Geographic Intelligence definido;
- [x] validar família oficial de dados SMP/SCM e documentação de CSV;
- [x] validar códigos e hierarquia territorial IBGE;
- [x] implementar dimensão geográfica canônica;
- [x] provar SP + MG + RJ + ES → Sudeste em snapshot de validação;
- [x] endurecer contrato geográfico v2;
- [x] registrar evidências e homologação final;
- [x] implementar captura HTTPS governada com detecção de WAF;
- [x] implementar registro manual governado de arquivo baixado da URL oficial;
- [ ] **BLOQUEANTE R0:** registrar raw oficial SMP por caminho automático ou manual governado;
- [ ] **BLOQUEANTE R0:** registrar raw oficial SCM por caminho automático ou manual governado;
- [ ] registrar/validar SHA-256 e schema real dos dois arquivos;
- [ ] mapear aliases reais de operadoras diretamente no raw;
- [ ] executar reconciliação territorial com fonte primária;
- [ ] congelar contratos analíticos/apresentação v2 na Sprint R2/R3;
- [ ] validar estratégia SPA/deep-link antes do router na Sprint R4.

### Regra
Nenhum dashboard real será implementado antes do gate de dados da Sprint R0.

---

## P0 — Publicação Cloudflare

**Status:** em correção / publicação iniciada  
**Motivo:** decisão do proprietário de concluir primeiro o trabalho no GitHub e executar o deploy Cloudflare depois.

### Pré-condições já concluídas

- build de produção reproduzível;
- `scripts/build-cloudflare.sh`;
- `web/dist` validado;
- smoke test local de `/`;
- smoke test local de `/data/dashboard-v1.json`;
- security headers em `web/public/_headers`;
- runbook em `docs/CLOUDFLARE_DEPLOY.md`;
- rollback documentado;
- CI da `main` verde para Python, web e `cloudflare-build`.

### Quando retomar

1. confirmar no Workers Builds o Build command `bash scripts/build-cloudflare.sh`;
2. manter Deploy command `npx wrangler deploy`;
3. usar branch de produção `main`;
4. confirmar Python 3.13 e Node 22;
5. deixar `wrangler.jsonc` apontar para `./web/dist`;
6. executar novo deploy;
7. validar URL pública;
8. executar smoke test público;
9. validar headers;
10. registrar deployment e commit;
11. criar tag/release do MVP.

### Definition of Done

- URL pública responde 200;
- `/data/dashboard-v1.json` responde 200;
- contrato publicado é versão 1.0;
- dashboard carrega sem erro;
- headers defensivos estão presentes;
- versão publicada é rastreável ao commit homologado;
- rollback continua documentado.

---

## P1 — Remediação de dependências moderadas

- revisar as 2 vulnerabilidades npm moderadas registradas na Sprint 4;
- atualizar dependências sem quebrar build/testes;
- manter audit sem high/critical.

## P2 — Acessibilidade e qualidade pós-MVP

- auditoria WCAG mais completa;
- testes E2E em navegador real;
- Web Vitals após publicação;
- screenshots automatizados quando houver valor para homologação.

## P3 — Insights avançados

- comparação de períodos;
- heatmap temporal;
- Pareto de causas;
- tendência de MTTR;
- reincidência por link;
- indicadores de concentração de risco.

## P4 — Backend somente se necessário

Avaliar somente mediante requisito real:

- Cloudflare Workers;
- D1;
- API;
- atualização incremental;
- autenticação.

Não introduzir backend apenas por sofisticação arquitetural.
