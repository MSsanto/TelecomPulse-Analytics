# TelecomPulse Analytics v2 — Project Charter

## 1. Visão

TelecomPulse Analytics é uma plataforma pública de analytics para o setor brasileiro de telecomunicações.

Seu foco é transformar bases oficiais abertas em análises reproduzíveis de:
- mercado;
- competição;
- qualidade;
- experiência do consumidor;
- cobertura;
- evolução tecnológica.

## 2. Mudança de fase

As versões iniciais do projeto usaram dados sintéticos para validar arquitetura e experiência.

Esse trabalho é considerado **protótipo/ensaio técnico**.

A v2 inicia a fase de dados reais:
- nenhuma métrica pública pode ser inventada;
- nenhuma ocorrência sintética pode ser apresentada como evento real;
- toda conclusão deve ser rastreável a uma fonte oficial.

## 3. Fonte primária

Agência Nacional de Telecomunicações — Anatel.

Fontes complementares só entram quando:
1. forem públicas;
2. possuírem proveniência clara;
3. adicionarem uma dimensão não coberta pela Anatel;
4. sua metodologia for documentada.

## 4. Serviços analisados

### SMP — Serviço Móvel Pessoal
Telefonia e banda larga móvel.

### SCM — Serviço de Comunicação Multimídia
Banda larga fixa.

Os dois serviços não devem ser misturados em um único ranking de prestadoras sem explicitar a diferença de mercado.

## 5. Dimensões canônicas

- período;
- serviço;
- prestadora/grupo econômico;
- município;
- UF;
- região;
- tecnologia;
- modalidade quando aplicável.

## 6. Métricas v2

### Mercado
- acessos;
- market share;
- crescimento absoluto;
- crescimento percentual;
- Top N;
- concentração quando metodologicamente suportada.

### Qualidade
- IQS;
- indicadores RQUAL aplicáveis ao serviço;
- selo de qualidade.

### Consumidor
- reclamações;
- reclamações por mil acessos / IR;
- IQP/ISG;
- satisfação por serviço.

### Rede/cobertura
- cobertura por tecnologia;
- indicadores de conexão/queda;
- velocidade quando disponível.

## 7. Métricas removidas do produto real

Os seguintes conceitos pertencem ao protótipo sintético e **não fazem parte da v2 real por padrão**:
- incident_count;
- downtime_minutes;
- MTTR;
- recurrence_count de incidentes;
- disponibilidade calculada a partir de incidentes.

Podem existir no futuro somente se uma fonte pública adequada suportar a semântica.

## 8. Top 5 / Top 10

O Top N é derivado dos acessos oficiais por:
- serviço;
- período;
- geografia selecionada.

Nunca será uma lista fixa de marcas.

O usuário poderá comparar:
- Top 5;
- Top 10;
- todas as prestadoras elegíveis.

## 9. Regras de comparação

- móvel e banda larga fixa têm rankings separados;
- ausência de dado não equivale a zero;
- mudança de marca/grupo precisa de tabela de correspondência temporal;
- indicadores com metodologias diferentes não devem ser agregados em um score proprietário sem justificativa;
- mudanças metodológicas da Anatel devem ser versionadas.

## 10. Público-alvo

- profissionais de telecom/NOC;
- analistas de dados/BI;
- gestão de operações;
- pesquisadores;
- consumidores interessados em dados públicos;
- recrutadores e avaliadores técnicos.

## 11. Critério de sucesso

O produto é defensável quando:
- cada KPI possui fonte e metodologia;
- ingestão é reproduzível;
- snapshots são identificáveis;
- prestadoras são normalizadas sem perder razão social/origem;
- totais reconciliam;
- dashboard não recalcula regra crítica;
- dados oficiais e derivados são distinguíveis;
- atualização pode ser repetida sem edição manual arbitrária.

## 12. Restrições

- não usar dados corporativos privados;
- não inferir falhas/indisponibilidade onde a fonte não permite;
- não apresentar correlação como causalidade;
- não preencher dado ausente com estimativa silenciosa;
- não misturar períodos incompatíveis;
- não esconder revisão ou limitação da fonte.
