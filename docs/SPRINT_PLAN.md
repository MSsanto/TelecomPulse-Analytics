# TelecomPulse Analytics — Plano de Sprints

## Convenção

Sprints orientadas a entrega demonstrável. A duração recomendada é de **1 semana por sprint** para o MVP, mas o gate é qualidade/evidência, não calendário.

Nenhuma sprint avança com bloqueio crítico não diagnosticado.

---

## Sprint 0 — Fundação governada

### Objetivo
Transformar o repositório vazio em uma base de engenharia pronta para receber features.

### Entregas
- validar stack;
- criar estrutura mínima;
- definir dataset sintético;
- especificar schema;
- configurar Python/pytest/lint;
- configurar frontend React/TypeScript/Vite;
- configurar CI;
- documentar comandos locais;
- definir estratégia Cloudflare sem publicar;
- capturar baseline técnico após bootstrap.

### Critérios de aceite
- pipeline mínimo executa;
- teste mínimo passa;
- lint passa;
- frontend instala e builda;
- CI reproduz essas verificações;
- nenhum secret está versionado;
- documentação de setup existe.

### Gate
**GO:** baseline verde e evidências registradas.  
**NO-GO:** qualquer validador crítico vermelho sem causa compreendida.

---

## Sprint 1 — Dados e qualidade

### Objetivo
Construir o núcleo confiável de dados antes de qualquer dashboard real.

### Entregas
- gerador/dataset sintético;
- contrato de incidente versionado;
- ingestão;
- validação;
- normalização;
- tratamento de duplicidades;
- regras temporais;
- relatório de qualidade;
- testes de transformação.

### KPIs ainda não visuais
- incident_count;
- downtime_minutes;
- mttr_minutes;
- recurrence_count;
- disponibilidade inicial com tratamento de sobreposição definido.

### Critérios de aceite
- entradas inválidas são rejeitadas ou classificadas;
- pipeline é determinístico;
- fórmulas têm testes;
- dataset processado é reproduzível;
- relatório de qualidade é gerado.

### Demonstração
Executar raw → processed e comparar KPIs esperados do dataset de referência.

---

## Sprint 2 — Camada analítica e contrato do dashboard

### Objetivo
Produzir datasets prontos para consumo do frontend sem duplicar lógica analítica na UI.

### Entregas
- agregações por período;
- agregações por operadora;
- agregações por unidade;
- agregações por causa;
- séries temporais;
- contrato JSON/CSV do frontend;
- documentação das métricas;
- testes de consistência entre granularidades.

### Critérios de aceite
- totais reconciliam entre detalhe e agregados;
- métricas possuem definição explícita;
- contratos não dependem de conhecimento implícito do pipeline;
- dados de apresentação têm tamanho adequado ao MVP.

### Demonstração
Gerar todos os artefatos que o frontend consumirá sem iniciar servidor backend.

---

## Sprint 3 — Dashboard MVP

### Objetivo
Tornar os dados analíticos navegáveis e compreensíveis.

### Entregas
- layout base;
- visão executiva;
- cards de KPI;
- evolução temporal;
- operadoras;
- unidades;
- causas;
- filtros;
- tabela detalhada;
- estados loading/empty/error;
- indicação de dataset sintético;
- responsividade.

### Critérios de aceite
- frontend usa somente contratos da Sprint 2;
- nenhum KPI crítico é recalculado silenciosamente no browser;
- filtros produzem resultados coerentes;
- build passa;
- fluxo principal funciona em desktop e mobile;
- acessibilidade básica verificada.

### Demonstração
Navegação completa local com dataset de referência.

---

## Sprint 4 — Qualidade de produto e engenharia

### Objetivo
Reduzir a diferença entre “demo que funciona” e produto de portfólio tecnicamente defensável.

### Entregas
- testes frontend prioritários;
- revisão UX;
- acessibilidade;
- tratamento de erros;
- performance;
- segurança;
- revisão de dependências;
- README completo;
- arquitetura atualizada;
- screenshots/evidências;
- code review governado.

### Critérios de aceite
- validadores verdes;
- sem erros críticos de console;
- sem segredo/dado sensível;
- navegação por teclado nos fluxos principais;
- documentação permite reprodução por terceiro;
- riscos residuais documentados.

### Demonstração
Rodada de homologação local completa.

---

## Sprint 5 — Preparação de release e publicação Cloudflare

### Estado
**Preparação técnica concluída no GitHub. Publicação Cloudflare adiada para o backlog por decisão do proprietário.**

### Objetivo
Publicar somente o que já está tecnicamente homologado.

### Pré-condição
Deploy/publicação explicitamente autorizado.

### Entregas
- validar configuração Cloudflare;
- confirmar projeto e domínio;
- integração GitHub/Cloudflare ou fluxo reproduzível equivalente;
- build de produção;
- deploy;
- smoke test;
- validação de rotas/assets;
- evidência da versão publicada;
- documentação de rollback;
- tag/release do MVP.

### Critérios de aceite
- build publicado corresponde ao commit homologado;
- URL pública funciona;
- assets e rotas respondem corretamente;
- nenhum segredo foi exposto;
- smoke test registrado;
- rollback documentado.

### Demonstração
A preparação técnica já foi demonstrada por build de produção e smoke test local. A demonstração pública fica pendente até a retomada do item `P0 — Publicação Cloudflare` em `docs/BACKLOG.md`.

---

# Pós-MVP

## Sprint 6 — Insights avançados
Possíveis itens:
- comparação de períodos;
- heatmap temporal;
- Pareto de causas;
- tendência de MTTR;
- reincidência por link;
- indicadores de concentração de risco.

## Sprint 7 — Backend somente se necessário
Avaliar:
- Cloudflare Workers;
- D1;
- API;
- atualização incremental;
- autenticação.

**Não iniciar sem requisito comprovado.**

## Sprint 8 — Observabilidade e operação
Caso o produto deixe de ser somente estático:
- logging;
- métricas;
- health checks;
- tracing quando aplicável;
- alertas;
- runbook.

---

# Macro-roadmap

```text
Sprint 0  Fundação
   ↓
Sprint 1  Dados confiáveis
   ↓
Sprint 2  Analytics/contratos
   ↓
Sprint 3  Dashboard
   ↓
Sprint 4  Qualidade/homologação
   ↓
Sprint 5  Cloudflare/release
   ↓
Pós-MVP
```

# Regra de priorização

Prioridade:
1. corretude dos dados;
2. rastreabilidade;
3. valor analítico;
4. usabilidade;
5. estética;
6. sofisticação arquitetural.

Uma visualização bonita nunca compensa KPI incorreto.


---

# TelecomPulse v2 — Real Data Reboot

A v1 sintética permanece como baseline histórico. O roadmap abaixo governa a nova linha de produto baseada em dados públicos reais.

## Sprint R0 — Fontes, contrato e território

### Objetivo
Fechar as fontes oficiais, identidade de operadoras, dimensão territorial e regras de rastreabilidade antes de qualquer visualização real.

### Entregas
- `docs/DATA_SOURCES.md`;
- `docs/REAL_DATA_REBOOT.md`;
- contrato geográfico v2;
- matriz fonte × métrica × granularidade × período;
- prova de acesso a SMP/SCM;
- amostra ANATEL + IBGE;
- primeira reconciliação SP → Sudeste → Brasil.

### Gate
**GO:** fontes primárias acessíveis, joins demonstrados e reconciliação das métricas aditivas.  
**NO-GO:** fonte sem download reproduzível, operadora não normalizável ou divergência territorial sem diagnóstico.

### Homologação final R0 — 2026-09-22

**NO-GO por bloqueio externo único:** a documentação e o catálogo oficiais da ANATEL foram validados, porém o host de CSV bloqueou o download automatizado neste ambiente. O projeto não reduz o critério de aceite retroativamente.

A dimensão territorial, contrato, reconciliação de referência e testes estão concluídos. O único gate bloqueante é capturar bytes raw oficiais SMP/SCM, seus hashes e schema real.

## Sprint R1 — Ingestão real

- aquisição reproduzível ANATEL SMP/SCM;
- armazenamento raw imutável;
- metadados de coleta;
- hashes;
- schema checks;
- aliases de operadoras;
- normalização territorial;
- testes.

## Sprint R2 — Analytics territoriais

- Brasil;
- 5 regiões;
- 27 UFs;
- market share;
- crescimento;
- séries;
- densidade com IBGE;
- reconciliação entre granularidades;
- contratos v2.

## Sprint R3 — Presentation layer

- `catalog.json`;
- `brazil.json`;
- arquivos regionais;
- arquivos estaduais;
- lineage;
- testes de schema e tamanho.

## Sprint R4 — Navegação geográfica

- router;
- `BrazilPage`;
- `RegionPage`;
- `StatePage`;
- mapa SVG;
- navegação alternativa acessível;
- deep links;
- estados loading/empty/error.

## Sprint R5 — Qualidade, reclamações, satisfação e cobertura

Somente após validar granularidade e metodologia oficial de cada indicador.

## Sprint R6 — Homologação e release

- testes Python/frontend;
- reconciliação completa;
- acessibilidade;
- segurança;
- performance;
- documentação;
- smoke test;
- publicação somente mediante autorização explícita.

## Prioridade v2

1. fonte oficial;
2. rastreabilidade;
3. corretude;
4. reconciliação;
5. valor analítico;
6. usabilidade;
7. estética.
