# Sprint 3 — Dashboard MVP

## Objetivo

Transformar o contrato analítico homologado na Sprint 2 em uma interface navegável, responsiva e compreensível, sem recalcular KPIs críticos no navegador.

## Escopo autorizado

- layout base;
- visão executiva;
- cards de KPI;
- série temporal;
- ranking por operadora;
- ranking por unidade;
- ranking por causa;
- filtros de detalhe;
- tabela de incidentes;
- estados loading, empty e error;
- indicação explícita de dataset sintético;
- responsividade desktop/mobile;
- acessibilidade básica;
- consumo exclusivo do contrato dashboard v1.

## Regra de dados

O frontend pode:
- formatar números/datas;
- ordenar visualmente coleções já calculadas;
- filtrar registros de detalhe;
- calcular proporções exclusivamente visuais, como largura de barra relativa.

O frontend não pode:
- recalcular MTTR;
- recalcular disponibilidade;
- recalcular downtime;
- produzir agregações substitutas às da Sprint 2.

## Filtros do MVP

Os filtros afetam a tabela de detalhe:
- operadora;
- unidade;
- causa;
- status.

Os cards executivos e rankings continuam exibindo métricas pré-calculadas do contrato. Isso evita semântica falsa para combinações não materializadas no backend.

## Estados

- Loading: enquanto o contrato é carregado.
- Error: contrato indisponível ou inválido no fetch.
- Empty: contrato válido sem incidentes.
- Ready: dashboard navegável.

## Critérios de aceite

- dados são carregados de `/data/dashboard-v1.json`;
- cards usam `summary` do contrato;
- rankings usam agregados pré-calculados;
- timeline usa `timeline` do contrato;
- filtros afetam somente detalhe;
- dataset sintético está claramente sinalizado;
- interface funciona em viewport móvel e desktop;
- controles possuem labels;
- tabela permanece legível/rolável em telas estreitas;
- build verde;
- pipeline/analytics continuam verdes;
- nenhum deploy é executado.
