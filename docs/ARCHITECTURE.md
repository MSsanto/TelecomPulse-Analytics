# TelecomPulse Analytics v2 — Arquitetura

## Estado

**Real Data Reboot em construção.**

A arquitetura sintética anterior foi validada e permanece no histórico Git. A arquitetura principal agora é orientada a fontes públicas reais.

## Fluxo

```text
Anatel / dados.gov.br
        ↓
source registry + provenance
        ↓
raw snapshots imutáveis
        ↓
staging / schema validation
        ↓
normalização canônica
  prestadora | serviço | geografia | período
        ↓
marts analíticos
  market | quality | consumer | coverage
        ↓
contratos versionados JSON/CSV
        ↓
React / TypeScript
        ↓
Cloudflare Workers Static Assets
```

## Camadas

### 1. Source registry

Responsável por:
- nome da fonte;
- órgão mantenedor;
- URL de landing page;
- URL/download quando estável;
- periodicidade;
- granularidade;
- licença/atribuição;
- data de aquisição;
- status de disponibilidade.

### 2. Raw

Snapshots da fonte sem transformação de negócio.

Regras:
- não editar arquivos raw manualmente;
- registrar checksum quando possível;
- preservar nome/período da origem;
- fonte grande pode ser baixada no pipeline e não versionada no Git.

### 3. Staging

Converte cada fonte para tipos e colunas previsíveis:
- datas/períodos;
- códigos geográficos;
- nomes de prestadoras;
- serviço;
- medidas numéricas.

### 4. Canonical dimensions

#### provider
Mantém:
- `provider_id`;
- `display_name`;
- nome/grupo informado pela fonte;
- aliases;
- vigência temporal quando necessário.

#### service
Valores iniciais:
- `SMP`;
- `SCM`.

#### geography
- Brasil;
- região;
- UF;
- município;
- código IBGE quando disponível.

#### period
Preferir `YYYY-MM`, `YYYY-Qn` ou ano de referência, conforme a fonte.

### 5. Marts

#### market
- accesses;
- market_share_pct;
- growth;
- rank;
- top_n.

#### quality
- IQS;
- selo;
- indicadores técnicos do RQUAL.

#### consumer
- IR/reclamações por mil acessos;
- IQP/ISG;
- satisfação.

#### coverage
- cobertura;
- tecnologia;
- indicadores associados quando disponíveis.

## Regra de reconciliação

Métricas derivadas devem reconciliar com a granularidade da fonte.

Exemplo:
`market_share = accesses_provider / accesses_market`

Não calcular participação usando universos diferentes.

## Frontend

O browser:
- formata;
- filtra;
- ordena;
- apresenta.

O browser não deve recriar regras regulatórias ou metodologias da Anatel.

## Deploy

O build continua estático:
- Python produz contratos;
- Vite compila a UI;
- Wrangler publica `web/dist`.

## Legado sintético

O pipeline de incidentes existente é considerado legado de prototipação. Ele será removido do caminho principal depois que os novos contratos reais cobrirem o dashboard v2.
