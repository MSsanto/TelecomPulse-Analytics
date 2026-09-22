# TelecomPulse Analytics — Pré-projeto

## 1. Visão

TelecomPulse Analytics é um projeto de analytics para operações de telecom/NOC. Seu propósito é converter registros de indisponibilidade, incidentes, links, unidades e operadoras em métricas operacionais compreensíveis e rastreáveis.

O projeto deve funcionar como case público de portfólio sem depender de dados confidenciais de empregadores, clientes ou operadoras.

## 2. Problema

Dados de NOC costumam ficar dispersos entre planilhas, ITSM, monitoramento e controles manuais. Isso dificulta responder rapidamente:

- onde a indisponibilidade se concentra;
- quais links/unidades reincidem;
- qual operadora apresenta maior volume ou duração de incidentes;
- quanto tempo a operação leva para restaurar o serviço;
- quais causas geram maior impacto;
- onde há falhas de qualidade cadastral.

## 3. Objetivo do MVP

Entregar uma solução reproduzível que:

1. carregue um conjunto de dados de incidentes de telecom;
2. valide schema e qualidade;
3. normalize dimensões e eventos;
4. calcule KPIs operacionais;
5. gere datasets analíticos;
6. apresente os resultados em dashboard web responsivo;
7. possa ser publicada no Cloudflare de forma controlada;
8. possua testes, evidências e documentação suficientes para auditoria técnica.

## 4. Usuários-alvo

### Analista NOC
Precisa localizar rapidamente incidentes, reincidências e gargalos.

### Coordenação/Gestão
Precisa acompanhar disponibilidade, MTTR, SLA, tendência e concentração de impacto.

### Recrutador/avaliador técnico
Precisa entender claramente problema, arquitetura, decisões técnicas e evidências de qualidade sem depender de contexto interno.

## 5. Escopo do MVP

### Dados
- incidentes;
- unidade/site;
- link/designação anonimizada;
- operadora;
- início e fim da indisponibilidade;
- duração;
- causa/categoria;
- status;
- região/UF quando disponível;
- campos de qualidade e rastreabilidade.

### KPIs
- disponibilidade;
- downtime acumulado;
- número de incidentes;
- MTTR;
- recorrência;
- incidentes por operadora;
- incidentes por unidade;
- incidentes por causa;
- evolução temporal;
- qualidade dos registros.

### Produto
- visão executiva;
- análise por operadora;
- análise por unidade/link;
- análise temporal;
- filtros;
- tabela detalhada;
- indicação clara da origem/período dos dados;
- documentação metodológica.

## 6. Fora do escopo inicial

- integração direta com ambiente corporativo;
- credenciais de operadoras;
- automação de abertura de chamados;
- dados pessoais;
- dados reais confidenciais;
- alertas em tempo real;
- machine learning;
- previsão de falhas;
- autenticação;
- multi-tenant;
- alta disponibilidade de backend;
- banco distribuído.

Esses itens só entram mediante nova decisão registrada.

## 7. Fonte de dados

O repositório público deve usar uma destas opções:

1. dataset sintético realista;
2. dados públicos adequadamente citados;
3. dados operacionais anonimizados somente quando houver autorização explícita e risco de reidentificação tiver sido eliminado.

**Padrão do MVP: dataset sintético e reproduzível.**

Os nomes de operadoras podem usar marcas reais de mercado como dimensão demonstrativa. Isso não transforma os eventos em dados reais: incidentes, sites, horários, causas, downtime, disponibilidade e demais métricas permanecem sintéticos e não devem ser interpretados como desempenho real de qualquer operadora.

## 8. Restrições

- não versionar secrets;
- não publicar CNPJ, telefone, nome de contato ou identificadores sensíveis provenientes de operação real;
- não representar dados sintéticos como dados reais;
- não publicar deploy sem validação;
- manter compatibilidade com hospedagem Cloudflare do frontend;
- preferir componentes de baixo custo e baixa complexidade.

## 9. Critérios de sucesso do MVP

O MVP será considerado funcionalmente concluído quando:

- pipeline executar do início ao fim de forma reproduzível;
- schema inválido for rejeitado;
- KPIs tiverem fórmula documentada e testes;
- dashboard consumir apenas saída processada;
- filtros e visualizações principais funcionarem;
- build frontend passar;
- validações automatizadas passarem;
- nenhum segredo ou dado sensível estiver no repositório;
- README permitir reprodução local;
- deploy Cloudflare estiver documentado e validado apenas quando autorizado;
- evidências de homologação estiverem registradas.

## 10. Métricas do projeto

### Qualidade técnica
- testes automatizados relevantes passando;
- lint/build sem erro;
- ausência de secrets versionados;
- pipeline determinístico com dataset de referência.

### Qualidade de dados
- registros válidos/invalidos contabilizados;
- nulos críticos explicitados;
- duplicidades detectadas;
- duração negativa/impossível rejeitada;
- dimensões normalizadas.

### Produto
- KPIs compreensíveis;
- filtros funcionais;
- carregamento aceitável para dataset do MVP;
- responsividade desktop/mobile;
- acessibilidade básica verificada.

## 11. Riscos principais

| Risco | Impacto | Mitigação |
|---|---|---|
| Usar dados corporativos indevidamente | Alto | Dataset sintético por padrão |
| Construir infraestrutura demais | Médio | MVP estático/processado primeiro |
| KPI incorreto | Alto | Fórmula documentada + teste |
| Dashboard bonito mas sem rastreabilidade | Alto | Metodologia e data lineage visíveis |
| Cloudflare manual e irreproduzível | Médio | Documentar e validar integração antes de produção |
| Escopo crescer cedo demais | Médio | Backlog pós-MVP separado |

## 12. Definition of Ready

Uma história pode entrar em implementação quando possui:
- objetivo;
- critérios de aceite;
- dados/contratos afetados;
- riscos;
- dependências;
- validadores previstos;
- evidências esperadas.

## 13. Definition of Done

Além da governança global, a história precisa:
- implementação revisada;
- testes aplicáveis passando;
- documentação atualizada;
- evidência registrada;
- ausência de regressão conhecida;
- segurança e dados revisados;
- deploy apenas quando explicitamente autorizado.

## 14. Decisões pendentes

Não bloqueiam o pré-projeto, mas devem ser resolvidas na Sprint 0:
- versão final do stack frontend;
- formato canônico dos datasets processados;
- ferramenta de validação de schema;
- estratégia de CI;
- domínio/URL final do Cloudflare;
- método de integração GitHub ↔ Cloudflare.
