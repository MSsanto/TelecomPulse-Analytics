# Sprint 2 — Camada analítica e contrato do dashboard

## Objetivo

Produzir artefatos analíticos estáveis e documentados para o frontend consumir na Sprint 3, sem recalcular regras críticas no browser.

## Escopo autorizado

- visão geral;
- agregações por operadora;
- agregações por unidade;
- agregações por causa;
- série temporal por data de abertura;
- dataset de detalhe;
- contrato JSON v1;
- CSVs auxiliares;
- documentação das métricas;
- testes de reconciliação entre detalhe e agregados.

## Decisões de métrica

### Downtime bruto

`downtime_minutes` é a soma das durações dos incidentes resolvidos.

Ele deve reconciliar entre detalhe e agregações quando cada incidente pertence a uma única dimensão.

### Disponibilidade

`availability_pct` não reutiliza simplesmente o downtime bruto.

Para evitar dupla contagem:
1. incidentes são agrupados por site;
2. intervalos resolvidos são recortados à janela;
3. intervalos sobrepostos/tangentes do mesmo site são unidos;
4. o downtime efetivo é dividido pelo total de minutos disponíveis de todos os sites do grupo.

Portanto, `downtime_minutes` e o downtime usado internamente para disponibilidade podem divergir quando existem incidentes sobrepostos no mesmo site. Isso é intencional.

### Série temporal

A série temporal é uma visão de **coorte por data de abertura do incidente**. O downtime fica associado à data de abertura; não é distribuído entre dias atravessados pelo incidente no MVP.

## Janela analítica

O contrato exige `window_start` e `window_end` explícitos para métricas de disponibilidade.

No dataset de referência da Sprint 2 será utilizada uma janela fixa e reproduzível.

## Critérios de aceite

- totais de incidentes reconciliam entre detalhe e agregações;
- downtime bruto reconcilia entre detalhe e dimensões;
- contratos possuem versão;
- JSON não depende de DataFrame/Pandas no frontend;
- timestamps são serializados em ISO-8601 UTC;
- disponibilidade é testada com sobreposição;
- outputs são determinísticos;
- CI completo fica verde;
- nenhum dashboard funcional é antecipado.
