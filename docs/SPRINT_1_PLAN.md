# Sprint 1 — Dados e qualidade

## Objetivo

Construir o núcleo confiável de dados antes do dashboard.

## Escopo autorizado

- contrato versionado de incidente;
- geração sintética reproduzível;
- ingestão;
- normalização;
- validação;
- duplicidades;
- regras temporais;
- qualidade;
- MTTR, downtime, recorrência e disponibilidade;
- tratamento de sobreposição de incidentes.

## Critérios de aceite

- dados inválidos críticos bloqueiam processamento;
- normalização é determinística;
- dataset de referência é reproduzível;
- relatório de qualidade é gerado;
- disponibilidade não duplica downtime sobreposto;
- fórmulas relevantes possuem testes;
- CI continua verde;
- nenhum dashboard funcional ou deploy entra nesta sprint.

## Riscos

- dupla contagem de downtime;
- normalização alterar significado do dado;
- aceitar incidente resolvido sem restauração;
- misturar dado sintético e real;
- KPI correto em casos simples, mas incorreto em bordas temporais.

## Validadores

- Ruff;
- pytest;
- execução do pipeline;
- build frontend regressivo;
- revisão de diff;
- conferência do relatório de qualidade.
