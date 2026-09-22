# TelecomPulse v2 — Data Sources

## Status

Sprint 0 / Real Data Reboot.

Nenhum dataset entra na camada analítica sem:
- proprietário/fonte identificada;
- URL oficial;
- período de referência;
- data de coleta;
- formato conhecido;
- granularidade documentada;
- chave de junção conhecida;
- regra de transformação;
- classificação CORE / AUXILIARY / VALIDATION.

## Fontes aprovadas

### DS-001 — ANATEL — Acessos de telecomunicações

**Classe:** CORE  
**Serviços alvo:** SMP e SCM  
**Uso:** acessos, market share, crescimento, distribuição territorial, séries históricas.  
**Origem institucional:** Agência Nacional de Telecomunicações — Dados Abertos.  
**URL institucional:** https://www.gov.br/anatel/pt-br/dados/dados-abertos

A Anatel mantém bases abertas de quantitativo de acessos de SMP e SCM e declara os dados abertos como estruturados, processáveis por máquina e reutilizáveis.

**Campos mínimos esperados para homologação:** período, serviço, prestadora/grupo, UF e quantidade de acessos.  
**Chaves candidatas:** período + serviço + operadora normalizada + UF.  
**Gate:** validar o recurso de download efetivamente consumido pelo pipeline antes da implementação.

### DS-002 — ANATEL — RQUAL / IQS / Selos de Qualidade

**Classe:** CORE  
**Uso:** qualidade técnica e comparação por serviço, operadora e território.  
**URL institucional:** https://www.gov.br/anatel/pt-br/dados/qualidade/qualidade-dos-servicos/resultados  
**Referência metodológica:** https://www.gov.br/anatel/pt-br/dados/qualidade/qualidade-dos-servicos/regulamento

O MOP vigente em 2026 define métodos de coleta, cálculo, consolidação e publicação. A base de Selos de Qualidade e IQS foi publicada em dados abertos em abril de 2026.

**Regra:** índices não serão agregados por média simples sem método oficial compatível.

### DS-003 — ANATEL — Reclamações / Índice de Reclamações

**Classe:** CORE  
**Uso:** experiência pós-consumo e comparação de reclamações normalizadas.  
**Referência metodológica:** https://www.gov.br/anatel/pt-br/dados/qualidade/qualidade-dos-servicos/regulamento

O IR é definido como razão entre reclamações registradas no Anatel Consumidor e acessos da operadora, em grupos de mil acessos.

**Regra:** armazenar numerador, denominador e índice sempre que a fonte permitir.

### DS-004 — ANATEL — Pesquisa de Satisfação e Qualidade Percebida

**Classe:** CORE  
**Uso:** ISG/IQP e percepção do consumidor por serviço/prestadora.  
**URL:** https://www.gov.br/anatel/pt-br/consumidor/pesquisa-de-satisfacao-e-qualidade

A Pesquisa 2025 foi realizada entre julho de 2025 e fevereiro de 2026 e inclui resultados por serviço e prestadora.

**Regra:** não comparar serviços diferentes como se fossem uma única métrica.

### DS-005 — ANATEL — Cobertura móvel

**Classe:** AUXILIARY  
**Uso:** cobertura 4G/5G, cobertura territorial/populacional e expansão de rede.  
**URL institucional:** https://www.gov.br/anatel/pt-br/dados/qualidade/qualidade-dos-servicos/mapa-cobertura

**Entrada planejada:** após homologação do núcleo SMP/SCM.

### DS-006 — IBGE — Estimativas populacionais 2026

**Classe:** CORE-AUXILIARY  
**Uso:** população por UF/município, densidade e indicadores por 100 habitantes.  
**URL:** https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-population.html  
**Referência:** 1º de julho de 2026.  
**Formatos declarados:** XLSX, ODS e PDF.

**Chave preferencial:** código IBGE.  
**Regra:** população deve ser associada ao período de referência correto e nunca tratada como mensal.

## Fontes complementares

### RI das operadoras

**Classe:** AUXILIARY  
**Uso futuro:** receita, EBITDA, CAPEX, ARPU e indicadores corporativos.

Não usar no núcleo v2 até existir uma matriz de comparabilidade contábil entre operadoras.

### Fontes secundárias de mercado

**Classe:** VALIDATION  
Ex.: portais setoriais e consolidações de mercado.

Podem ser usadas para conferência, nunca como fonte primária quando existir dado oficial equivalente.

## Hierarquia de confiança

1. ANATEL / IBGE — fonte primária.
2. Relações com investidores / documentos corporativos oficiais — complementar.
3. Fontes setoriais secundárias — validação.
4. Conteúdo editorial/social — fora do pipeline analítico.

## Próximos gates

- [ ] identificar o recurso/arquivo exato de acessos SMP;
- [ ] identificar o recurso/arquivo exato de acessos SCM;
- [ ] baixar amostra real;
- [ ] registrar hash, data de coleta e metadados;
- [ ] mapear nomes reais das operadoras;
- [ ] validar join territorial com IBGE;
- [ ] validar SP → Sudeste → Brasil;
- [ ] congelar schema v2 de apresentação.
