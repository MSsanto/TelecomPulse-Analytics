# Sprint 4 — Qualidade de produto e engenharia

## Objetivo

Reduzir a distância entre um dashboard funcional e um produto de portfólio tecnicamente defensável, com testes de UI, revisão de acessibilidade, segurança de dependências, performance, documentação e riscos residuais explícitos.

## Escopo autorizado

- testes frontend prioritários;
- revisão UX;
- acessibilidade;
- tratamento de erros;
- performance de bundle;
- auditoria de dependências;
- README completo;
- arquitetura atualizada;
- evidências técnicas;
- riscos residuais;
- code review governado.

## Critérios de aceite

- Ruff e pytest verdes;
- testes frontend verdes;
- build TypeScript/Vite verde;
- nenhum alerta high/critical no npm audit;
- bundle JavaScript principal dentro do orçamento do MVP;
- fluxo principal coberto por testes;
- loading/error/empty testados;
- filtros testados;
- navegação por teclado sem bloqueios óbvios;
- skip link e foco visível presentes;
- README reproduzível por terceiro;
- arquitetura reflete o estado real;
- riscos residuais documentados;
- nenhum deploy executado.

## Orçamento de performance

Para o MVP estático:
- JavaScript principal pós-build: alvo <= 250 KiB não comprimido;
- ausência de biblioteca de gráficos pesada enquanto a visualização puder ser construída com CSS/HTML;
- contrato JSON separado do bundle.

O orçamento não substitui medição de performance real no navegador, que poderá ser aprofundada antes da publicação.

## Segurança

- executar `npm audit --audit-level=high`;
- revisar que nenhum secret/env foi adicionado;
- manter dados sintéticos;
- nenhuma credencial Cloudflare no código;
- dependências adicionais apenas para testes/desenvolvimento quando possível.

## Fora do escopo

- deploy Cloudflare;
- autenticação;
- pentest;
- auditoria WCAG formal completa;
- observabilidade de runtime;
- backend runtime.

## Gate

A Sprint 4 só chega à homologação humana após todos os validadores automatizados aplicáveis estarem verdes e os riscos residuais estarem documentados.
