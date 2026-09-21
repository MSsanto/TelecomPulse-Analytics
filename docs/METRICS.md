# TelecomPulse Analytics — Dicionário de métricas v1

## incident_count

Quantidade de registros de incidente válidos no conjunto analisado.

## resolved_incident_count

Quantidade de incidentes cujo status normalizado é `resolved`.

## open_incident_count

Quantidade de incidentes cujo status normalizado é `open`.

## downtime_minutes

Soma da duração dos incidentes resolvidos:

`restored_at - opened_at`

É uma métrica de volume de incidentes e pode conter sobreposição temporal quando dois incidentes do mesmo site acontecem simultaneamente.

## mttr_minutes

`downtime_minutes / resolved_incident_count`

Se não houver incidentes resolvidos, retorna 0.

## recurrence_count

Quantidade de incidentes além da primeira ocorrência por site no conjunto analisado.

Exemplo: um site com 3 incidentes contribui com 2 recorrências.

## availability_pct

Percentual de minutos disponíveis na janela de análise.

Para cada site:
- recorta os incidentes resolvidos à janela;
- une intervalos sobrepostos/tangentes;
- soma somente downtime efetivo.

Depois:

`availability = 100 * (1 - effective_downtime / (site_count * window_minutes))`

A disponibilidade não usa diretamente `downtime_minutes` quando há sobreposição.

## Série temporal

A série `timeline` é agrupada por `opened_date` em UTC.

O downtime de cada incidente resolvido é atribuído integralmente ao dia de abertura. Uma futura versão pode implementar alocação temporal por fatias diárias se houver requisito analítico.
