# TelecomPulse v2 — Real Data Reboot

## Objetivo

Substituir o case sintético como núcleo do produto por uma plataforma analítica baseada em dados públicos reais, rastreáveis e reproduzíveis.

O histórico sintético permanece preservado como v1. O Real Data Reboot passa a usar contratos v2 e não altera silenciosamente o significado dos contratos anteriores.

## Golden Rule

Nenhum número chega ao dashboard sem:
1. fonte identificável;
2. período de referência;
3. transformação documentada;
4. validação;
5. contrato de apresentação versionado.

## Escopo inicial

### CORE
- ANATEL SMP — acessos móveis;
- ANATEL SCM — banda larga fixa;
- market share derivado pelo pipeline;
- dimensão de operadoras;
- dimensão territorial;
- IBGE — população;
- Brasil, 5 regiões e 27 UFs.

### Fase seguinte
- RQUAL / IQS;
- reclamações;
- satisfação;
- cobertura 4G/5G.

### Fora do núcleo inicial
- indicadores financeiros de RI;
- API em runtime;
- autenticação;
- D1;
- ingestão contínua.

## Arquitetura

```text
fontes oficiais
    ↓
data/raw (imutável)
    ↓
ingestão
    ↓
validação
    ↓
normalização
    ├── operadora
    ├── serviço
    ├── período
    └── território
    ↓
data/processed
    ↓
analytics
    ├── Brasil
    ├── regiões
    └── estados
    ↓
presentation contracts v2
    ↓
React / TypeScript / Vite
    ↓
Cloudflare Static Assets
```

## Modelo territorial

Hierarquia canônica:

```text
Brasil
 └── Região
      └── UF
           └── Município (quando a fonte justificar)
```

Campos:
- country_code;
- region_code / region_name;
- state_code / state_name;
- ibge_state_code;
- municipality_code quando aplicável.

## Regras de reconciliação

Para métricas aditivas:

```text
Brasil = soma das regiões
Região = soma das UFs
UF = soma das operadoras no recorte
```

Índices, satisfação, qualidade e métricas normalizadas não podem ser somados ou ter média simples sem regra metodológica explícita.

## Contratos de apresentação

Estrutura alvo:

```text
web/public/data/v2/
├── catalog.json
├── brazil.json
├── regions/
│   ├── norte.json
│   ├── nordeste.json
│   ├── centro-oeste.json
│   ├── sudeste.json
│   └── sul.json
└── states/
    ├── ac.json
    ├── ...
    └── sp.json
```

O frontend não acessa raw/processed e não recalcula KPIs críticos.

## Navegação planejada

- `/` — overview;
- `/brasil`;
- `/regiao/:slug`;
- `/estado/:uf`;
- `/metodologia`;
- `/dados`.

O mapa será SVG vetorial e não será o único meio de navegação. Regiões e UFs também devem estar acessíveis por controles textuais/teclado.

## Epic GEO-01 — Geographic Intelligence

### GEO-01 Dimensão territorial
27 UFs, 5 regiões, códigos IBGE, unicidade e testes.

### GEO-02 Normalização territorial
Mapear fontes oficiais para as chaves canônicas.

### GEO-03 Agregação Brasil
Gerar acessos, operadoras, market share, série temporal, serviço e metadados.

### GEO-04 Agregação regional
Gerar os cinco recortes e reconciliar métricas aditivas.

### GEO-05 Agregação estadual
Gerar as 27 UFs e reconciliar métricas aditivas.

### GEO-06 Contratos v2
Schemas para catalog, country, region e state.

### GEO-07 Presentation layer
Gerar arquivos JSON estáticos para consumo da UI.

### GEO-08 Router
URLs compartilháveis e deep links.

### GEO-09 Shell de páginas
BrazilPage, RegionPage e StatePage antes do mapa.

### GEO-10 Mapa SVG Brasil
27 UFs, hover, clique, teclado, foco, tooltip e responsividade.

### GEO-11 Navegação acessível alternativa
Lista/dropdown por região e UF.

### GEO-12 Choropleth
Começar por acessos; demais métricas apenas após homologação.

### GEO-13 Comparativo territorial
Estado vs região vs Brasil.

### GEO-14 Data lineage na UI
Fonte, período, atualização, serviço e metodologia.

### GEO-15 QA territorial
27 estados, 5 regiões, rotas inválidas, teclado, mobile, dados ausentes e contrato incompatível.

## Gates

- G0 Fonte oficial válida;
- G1 Identidade de operadora e território;
- G2 Integridade Brasil ↔ região ↔ UF;
- G3 Contrato versionado;
- G4 Analytics reproduzível;
- G5 Frontend apenas apresenta;
- G6 Navegação e acessibilidade;
- G7 Deep links Cloudflare;
- G8 Evidências e documentação.

## Gate atual

**Sprint 0 / arquitetura: GREEN.**

Pendências antes da implementação completa:
- recurso exato de download SMP/SCM;
- schema real das bases;
- aliases reais de operadoras;
- joins ANATEL ↔ IBGE;
- período comum;
- regra de agregação de índices não aditivos;
- fallback SPA/deep link no Cloudflare.
