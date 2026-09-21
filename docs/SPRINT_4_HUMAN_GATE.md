# Sprint 4 — Gate de homologação humana

## Escopo

Esta sprint endurece produto e engenharia antes do release. Não executa deploy.

## Evidências técnicas concluídas

- [x] Ruff verde.
- [x] pytest verde.
- [x] frontend tests verdes — 5/5.
- [x] npm audit sem high/critical.
- [x] TypeScript/Vite build verde.
- [x] contrato presente no dist.
- [x] bundle dentro de 250 KiB — 233685 bytes.
- [x] loading/error/empty cobertos.
- [x] filtro de detalhe coberto.
- [x] skip link/foco/contexto de tabela implementados.
- [x] README reproduzível.
- [x] arquitetura atualizada.
- [x] riscos residuais documentados.
- [x] nenhum deploy executado.

## Ressalvas para homologação

- npm reporta 2 vulnerabilidades moderadas;
- auditoria WCAG formal ainda não foi realizada;
- não há teste E2E em navegador real;
- Web Vitals reais serão medidos somente com ambiente publicado;
- screenshots automáticos não fazem parte do CI atual.

## Itens para decisão humana

- [ ] Aprovar qualidade visual/UX após hardening.
- [ ] Aprovar comportamento de erro/retry.
- [ ] Aprovar nível de acessibilidade do MVP antes da publicação.
- [ ] Aceitar os riscos residuais documentados para avançar.
- [ ] Aprovar orçamento de bundle.
- [ ] Aprovar merge e avanço para Sprint 5.

## O que permanece para Sprint 5

- validar projeto Cloudflare;
- confirmar domínio/URL;
- definir build command/output;
- deploy do commit homologado;
- smoke test público;
- rollback;
- release/tag.

## Estado

**AGUARDANDO HOMOLOGAÇÃO HUMANA.**
