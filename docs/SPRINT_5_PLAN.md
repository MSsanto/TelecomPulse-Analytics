# Sprint 5 — Cloudflare e release público

## Objetivo

Publicar o MVP homologado no Cloudflare Pages com build reproduzível, smoke test e rollback documentado.

## Autorização

Deploy/publicação explicitamente autorizado pelo proprietário do projeto.

## Escopo

- build reproduzível para Cloudflare;
- security headers;
- CI equivalente ao build de produção;
- merge na main;
- disparo da integração Git/Cloudflare quando configurada;
- smoke test do domínio público;
- evidência da versão publicada;
- release/tag do MVP quando a publicação estiver confirmada.

## Critérios de aceite

- build Cloudflare reproduzido no CI;
- main contém somente código homologado;
- deployment público corresponde à main homologada;
- / responde 200;
- /data/dashboard-v1.json responde 200;
- contract_version = 1.0;
- headers de segurança presentes;
- rollback documentado;
- nenhum secret versionado.

## Bloqueio externo possível

Este ambiente ChatGPT não possui conector Cloudflare instalado. Se a integração Cloudflare ↔ GitHub não estiver previamente configurada, a etapa de criação/conexão do projeto na conta Cloudflare requer ação externa do proprietário.
