# TelecomPulse Analytics — Arquitetura inicial

## Status

**Arquitetura implementada até a Sprint 4.** O frontend estático e a camada analítica estão funcionais e validados por CI. Publicação Cloudflare permanece para a Sprint 5.

## Princípios

1. Dados antes de dashboard.
2. Métrica sem fórmula documentada não entra.
3. Dataset público não pode conter segredo ou dado operacional sensível.
4. Complexidade deve ser adicionada somente quando resolver necessidade concreta.
5. Frontend não recalcula regras analíticas críticas que pertencem ao pipeline.
6. Saídas processadas devem ser determinísticas e rastreáveis.

## Fluxo

```text
data/raw
   ↓
ingestão
   ↓
validação de schema
   ↓
limpeza e normalização
   ↓
modelo analítico / KPIs
   ↓
data/processed
   ↓
artefatos JSON/CSV
   ↓
React + Vite
   ↓
build estático
   ↓
Cloudflare
```

## Camadas

### 1. Raw

Entrada imutável do pipeline.

Regras:
- nunca corrigir manualmente o arquivo bruto durante processamento;
- manter origem e versão identificáveis;
- dataset público do MVP deve ser sintético ou autorizado.

### 2. Validation

Responsável por:
- tipos;
- campos obrigatórios;
- datas;
- duração;
- enumerações;
- duplicidades;
- integridade referencial mínima.

### 3. Transform

Responsável por:
- padronização de operadora;
- unidade/site;
- categorias de causa;
- timestamps;
- duração;
- dimensões temporais;
- chaves técnicas.

### 4. Analytics

Responsável por derivar:
- incident_count;
- downtime_minutes;
- mttr_minutes;
- availability_pct;
- recurrence_count;
- indicadores por operadora, unidade, causa e período;
- métricas de qualidade.

### 5. Presentation datasets

Arquivos enxutos preparados especificamente para consumo pelo dashboard.

### 6. Frontend

Responsável por:
- visualização;
- filtros;
- navegação;
- explicação das métricas;
- estado vazio/erro;
- acessibilidade.

Não deve conter lógica escondida que altere a definição dos KPIs.

## Stack proposta

### Dados
- Python 3.13;
- Pandas;
- testes com pytest;
- formato raw: CSV;
- formato processado: CSV/JSON no MVP;
- Parquet pode ser usado internamente quando trouxer benefício mensurável.

### Frontend
- React;
- TypeScript;
- Vite;
- gráficos com biblioteca a escolher na Sprint 2 após prova de adequação;
- CSS simples e responsivo.

### Hospedagem
- Cloudflare para o frontend.
- Workers/D1: **não usar no MVP sem requisito que justifique backend em runtime**.

## Estrutura alvo

```text
TelecomPulse-Analytics/
├── .github/
├── data/
│   ├── raw/
│   ├── processed/
│   └── samples/
├── docs/
├── src/
│   └── telecom_pulse/
│       ├── ingest/
│       ├── validation/
│       ├── transform/
│       └── analytics/
├── tests/
├── web/
├── scripts/
├── README.md
├── pyproject.toml
└── ...
```

A estrutura é alvo; diretórios só devem ser criados quando utilizados.

## Contrato conceitual de incidente

Campos mínimos propostos:

| Campo | Tipo | Obrigatório | Observação |
|---|---|---:|---|
| incident_id | string | sim | identificador sintético/técnico |
| site_id | string | sim | unidade anonimizada |
| carrier | string | sim | operadora normalizada |
| opened_at | datetime | sim | início |
| restored_at | datetime/null | condicional | fim |
| status | enum | sim | open/resolved |
| cause_category | string | sim | categoria normalizada |
| region | string | não | agrupamento geográfico |
| link_type | string | não | fibra, rádio etc. |
| source | string | sim | rastreabilidade |

## Fórmulas iniciais

### Downtime
`restored_at - opened_at` para incidentes resolvidos.

### MTTR
`soma(duração dos incidentes resolvidos) / quantidade de incidentes resolvidos`.

### Disponibilidade

Para uma entidade e janela de análise:

`availability = 1 - (downtime / tempo_total_da_janela)`

A Sprint 1 deve tratar sobreposição de incidentes antes de homologar a fórmula para agregações.

## Segurança e privacidade

- sem secrets no Git;
- sem tokens Cloudflare no frontend;
- sem dados pessoais;
- sem dados corporativos não autorizados;
- qualquer variável sensível via secret manager/variável de ambiente;
- dataset sintético identificado visualmente como tal.

## Evolução pós-MVP

Backend em runtime poderá ser avaliado quando houver:
- volume incompatível com artefatos estáticos;
- atualização frequente;
- necessidade de autenticação;
- filtros/consultas server-side;
- ingestão contínua;
- persistência multiusuário.

Até lá, adicionar D1, Workers ou API seria complexidade sem requisito.


## Estado implementado até Sprint 4

- ingestão CSV sintético;
- normalização e validação em Python/Pandas;
- métricas analíticas testadas;
- contrato dashboard v1;
- artefatos JSON/CSV de apresentação;
- React/TypeScript/Vite;
- testes de componente com Vitest/Testing Library;
- CI com Ruff, pytest, frontend tests, npm audit e budget de bundle;
- build estático contendo o contrato em `dist/data/dashboard-v1.json`.

## Decisão de runtime

O MVP continua sem API, Worker ou D1. O dashboard é compilado como site estático e consome um contrato JSON gerado antes do build.

Essa decisão reduz:
- superfície de ataque;
- custo operacional;
- dependências de runtime;
- complexidade de deploy.

Uma camada de backend só deverá ser introduzida quando atualização frequente, autenticação, volume ou consultas server-side justificarem a mudança.
