# TelecomPulse Analytics — Backlog

## P0 — Publicação Cloudflare

**Status:** backlog / não iniciado externamente  
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

1. conectar o projeto Cloudflare Pages ao repositório `MSsanto/TelecomPulse-Analytics`;
2. usar branch de produção `main`;
3. build command: `bash scripts/build-cloudflare.sh`;
4. output directory: `web/dist`;
5. confirmar Python 3.13 e Node 22;
6. executar deploy;
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
