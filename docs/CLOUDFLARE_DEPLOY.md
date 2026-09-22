# Cloudflare Pages — Deploy do TelecomPulse Analytics

## Modelo de publicação

O MVP é um site estático. O destino recomendado é **Cloudflare Pages** com integração ao GitHub.

## Repositório

`MSsanto/TelecomPulse-Analytics`

## Branch de produção

`main`

## Configuração de build

### Build command

`bash scripts/build-cloudflare.sh`

### Build output directory

`web/dist`

### Root directory

Raiz do repositório.

### Versões recomendadas

- Python 3.13
- Node.js 22

Se o projeto Cloudflare permitir variáveis de versão, configurar:
- `PYTHON_VERSION=3.13`
- `NODE_VERSION=22`

## O que o build faz

1. instala o pacote Python;
2. instala dependências web;
3. gera `web/public/data/dashboard-v1.json`;
4. executa TypeScript/Vite build;
5. valida `web/dist/index.html`;
6. valida `web/dist/data/dashboard-v1.json`.

## Headers

`web/public/_headers` aplica headers defensivos ao artefato publicado.

## Smoke test pós-deploy

Validar no domínio público:
- `/` retorna 200;
- `/data/dashboard-v1.json` retorna 200;
- título contém TelecomPulse;
- contrato possui `contract_version = 1.0`;
- dashboard não exibe erro de carregamento;
- headers de segurança estão presentes.

## Rollback

Se o deploy publicado apresentar regressão:
1. identificar o commit/release anterior homologado;
2. usar rollback de deployment no Cloudflare Pages ou restaurar a branch `main` ao commit anterior via PR/revert;
3. repetir smoke test;
4. registrar o deployment restaurado.

Não reescrever histórico de `main` para rollback normal.
