# Cloudflare Workers — Deploy do TelecomPulse Analytics

## Modelo de publicação

O MVP é publicado como **Cloudflare Worker com Static Assets**, integrado ao GitHub por Workers Builds.

URL de produção atual:

`https://telecompulse-analytics.matheus-sergio.workers.dev`

## Repositório

`MSsanto/TelecomPulse-Analytics`

## Branch de produção

`main`

## Configuração versionada

O arquivo `wrangler.jsonc` é a fonte de verdade para o Worker:

- Worker: `telecompulse-analytics`
- assets: `./web/dist`
- observability: habilitada

Isso impede a autodetecção incorreta que anteriormente publicou `web/` em vez do build Vite.

## Workers Builds

No painel Cloudflare, em **Worker → Settings → Build**, usar:

### Build command

`bash scripts/build-cloudflare.sh`

### Deploy command

`npx wrangler deploy`

### Production branch

`main`

### Root directory

Raiz do repositório.

### Versões

- Python 3.13
- Node.js 22

O Workers Builds executa build e deploy como etapas separadas. O build deve existir no painel; o `build.command` do Wrangler não é usado por Workers Builds.

## O que o build faz

1. instala o pacote Python;
2. instala dependências web;
3. gera `web/public/data/dashboard-v1.json`;
4. executa TypeScript/Vite build;
5. valida `web/dist/index.html`;
6. valida `web/dist/data/dashboard-v1.json`.

## Validação de deploy no CI

O job `cloudflare-build`:
1. executa o build de produção;
2. roda `wrangler deploy --dry-run`;
3. realiza smoke test local em `web/dist`.

O dry-run deve ler `wrangler.jsonc` e preparar os assets de `web/dist`.

## Headers

`web/public/_headers` é copiado pelo Vite para o `dist` e aplica headers defensivos aos assets publicados.

## Smoke test pós-deploy

Validar:
- `/` retorna 200;
- `/data/dashboard-v1.json` retorna 200;
- a página contém TelecomPulse Analytics;
- o contrato possui `contract_version = 1.0`;
- não aparece `DATA_ERROR`;
- assets compilados são carregados;
- headers de segurança estão presentes.

## Rollback

Se houver regressão:
1. identificar versão anterior no Cloudflare Workers;
2. usar rollback para a versão anterior ou reverter o commit via PR;
3. repetir smoke test público;
4. registrar a versão restaurada.

Não reescrever histórico de `main` para rollback normal.
