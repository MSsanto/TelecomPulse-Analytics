# Frontend — uso do contrato dashboard v1

## Fonte única

A interface deve carregar:

`/data/dashboard-v1.json`

Esse arquivo é gerado por:

`python -m telecom_pulse.presentation_cli --output-dir web/public/data`

## Seções consumidas

- `summary`: cards executivos;
- `by_carrier`: ranking de operadoras;
- `by_site`: ranking de unidades;
- `by_cause`: ranking de causas;
- `timeline`: evolução temporal;
- `incidents`: tabela e filtros;
- `window`: período exibido;
- `generated_from`: rastreabilidade;
- `contract_version`: compatibilidade.

## Restrições

A UI não recalcula KPIs críticos.

Filtros combinados são aplicados apenas ao detalhe porque a Sprint 2 não materializa cubos multidimensionais para combinações arbitrárias.

Quando houver necessidade de KPIs recalculados por filtros combinados, o contrato analítico deve evoluir antes da UI.
