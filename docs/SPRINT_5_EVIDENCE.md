# Sprint 5 — Evidências de release

Data: 2026-09-22  
Branch: `sprint-5-cloudflare-release`

## Autorização

Deploy/publicação autorizado explicitamente pelo proprietário.

## Preparação implementada

- script reproduzível de build Cloudflare;
- headers estáticos de segurança;
- runbook de deploy/rollback;
- CI com job `cloudflare-build`;
- smoke test local do artefato de produção;
- documentação da configuração recomendada de Cloudflare Pages.

## Validação necessária antes do merge

- Python job verde;
- Web job verde;
- Cloudflare production build verde;
- smoke test local verde;
- nenhum secret versionado.

## Publicação externa

Este ambiente não possui conector Cloudflare. Após o merge na `main`:
- se o projeto Cloudflare já estiver conectado ao GitHub, o merge deve disparar o deploy;
- caso contrário, a conexão GitHub ↔ Cloudflare precisa ser feita externamente na conta.

## Estado

**AGUARDANDO CI DA SPRINT 5.**
