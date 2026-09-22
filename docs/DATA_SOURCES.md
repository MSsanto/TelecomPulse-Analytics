# TelecomPulse Analytics v2 — Catálogo de Fontes

## Regra

A v2 usa somente dados públicos com proveniência explícita.

Cada fonte recebe:
- `source_id`;
- órgão;
- serviço;
- granularidade;
- periodicidade;
- landing page;
- download quando estável;
- observações metodológicas.

## ANATEL_OPEN_DATA

**Órgão:** Agência Nacional de Telecomunicações — Anatel  
**Tipo:** catálogo oficial de dados abertos  
**Landing page:** https://www.gov.br/anatel/pt-br/dados/dados-abertos

O catálogo oficial lista, entre outras bases:
- acessos SMP;
- acessos SCM;
- indicadores de qualidade;
- reclamações;
- satisfação;
- densidade/cobertura;
- Selos e IQS.

Os dados abertos são disponibilizados para uso e cruzamento com atribuição da fonte.

## ANATEL_SMP_ACCESS

**Serviço:** SMP — Serviço Móvel Pessoal  
**Periodicidade:** mensal  
**Formato:** CSV  
**Cobertura histórica:** 2005 até o presente, conforme glossário oficial  
**Dimensões documentadas:** empresa, grupo, tecnologia, tipo, DDD, UF, região e total.

Glossário:
https://www.anatel.gov.br/dadosabertos/PDA/Acessos/SMP/Glossario.pdf

Uso no TelecomPulse:
- acessos;
- market share;
- crescimento;
- Top N;
- tecnologia;
- geografia.

## ANATEL_SCM_ACCESS

**Serviço:** SCM — banda larga fixa  
**Periodicidade:** mensal  
**Formato:** CSV  
**Cobertura histórica:** 2007 até o presente, conforme glossário oficial  
**Dimensões documentadas:** empresa, grupo, faixa de velocidade, município, região, tecnologia, UF e total.

Glossário:
https://www.anatel.gov.br/dadosabertos/PDA/Acessos/SCM/Glossario.pdf

Uso no TelecomPulse:
- acessos;
- market share;
- crescimento;
- Top N;
- fibra/tecnologia;
- geografia.

## ANATEL_RQUAL

**Tipo:** indicadores de qualidade dos serviços  
**Landing page:** https://www.gov.br/anatel/pt-br/dados/qualidade/qualidade-dos-servicos/resultados/copy_of_qualidade-dos-servicos

O RQUAL publica resultados por prestadora e, dependendo do indicador, município, estado, Brasil e período.

Índices:
- IQS — Qualidade dos Serviços;
- IR — Reclamações;
- IQP — Qualidade Percebida.

Indicadores móveis incluem conexão de chamadas, queda de chamadas, conexão de dados, velocidade, experiência de aplicações e cobertura.

## ANATEL_QUALITY_SEALS

**Tipo:** Selos de Qualidade e IQS  
**Publicação em dados abertos:** 2026  
**Serviços:** telefonia móvel, telefonia fixa e banda larga fixa.

Landing page:
https://www.gov.br/anatel/pt-br/dados/qualidade/qualidade-dos-servicos/selos-qualidade

Uso:
- selo A–E;
- IQS;
- comparação geográfica e por serviço.

## ANATEL_SATISFACTION_2025

**Tipo:** Pesquisa de Satisfação e Qualidade Percebida  
**Ano de referência:** 2025  
**Amostra informada pela Anatel:** 58 mil consumidores  
**Landing page:** https://www.gov.br/anatel/pt-br/consumidor/pesquisa-de-satisfacao-e-qualidade/satisfacao-e-qualidade-percebida

Uso:
- ISG/IQP por prestadora e serviço.

## ANATEL_COMPETITION_2026Q2

**Tipo:** relatório oficial trimestral de competição  
**Período:** 2T2026  
**Landing page:** https://www.gov.br/anatel/pt-br/assuntos/noticias/anatel-divulga-relatorio-de-monitoramento-da-competicao-do-segundo-trimestre-de-2026

Valores publicados usados no snapshot de referência:
- SMP: 276,4 milhões de acessos;
- SMP: 66,1 milhões de acessos 5G, 23,9% da base;
- Vivo: 37,9% do mercado móvel;
- TIM: 22,4% do mercado móvel;
- SCM: 55,4 milhões de acessos;
- fibra: 44,7 milhões de acessos;
- Claro: 19,5% do SCM;
- Vivo: 15,1% do SCM;
- NIO: 6,2% do SCM.

### Limitação

O texto público desse relatório não fornece, na página de notícia, o ranking completo de todas as prestadoras móveis.

Por isso o snapshot de referência **não inventa** participações ausentes. O ranking completo virá da base mensal de acessos SMP/SCM na Sprint R1.

## Política de atualização

1. nunca sobrescrever silenciosamente um snapshot antigo;
2. registrar período de referência;
3. registrar fonte;
4. registrar data de aquisição;
5. manter transformação determinística;
6. aceitar que a Anatel pode corrigir dados históricos posteriormente;
7. documentar mudança metodológica antes de comparar séries incompatíveis.
