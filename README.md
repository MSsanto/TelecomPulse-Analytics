# TelecomPulse Analytics

**Brazilian Telecom Market & Quality Intelligence**

TelecomPulse Analytics transforma dados públicos oficiais de telecomunicações em indicadores comparáveis de mercado, qualidade, experiência do consumidor e cobertura.

> **v2 — Real Data Reboot.** As Sprints 0–5 provaram arquitetura, governança, métricas, frontend e deploy com um dataset sintético. Essa fase passa a ser tratada como protótipo/ensaio. A partir da v2, o produto principal utiliza somente dados públicos rastreáveis a fontes oficiais.

## Perguntas que o produto pretende responder

- quais são as maiores prestadoras por serviço e período;
- como o market share evolui;
- onde o mercado é mais concentrado;
- como qualidade técnica varia por prestadora e geografia;
- como reclamações se comportam por mil acessos;
- como a qualidade percebida/satisfação se compara;
- como cobertura e tecnologia evoluem;
- onde mercado, qualidade e percepção divergem.

## Fontes oficiais

A fonte primária é a **Agência Nacional de Telecomunicações — Anatel**.

Famílias de dados previstas:
- acessos SMP — telefonia móvel;
- acessos SCM — banda larga fixa;
- RQUAL — IQS e indicadores técnicos;
- Selos de Qualidade;
- reclamações / Índice de Reclamações;
- Pesquisa de Satisfação e Qualidade Percebida;
- cobertura e tecnologia móvel;
- relatórios trimestrais de competição.

Consulte `docs/DATA_SOURCES.md` para proveniência e granularidade.

## Regra de verdade

Nenhum indicador será chamado de:
- incidente;
- downtime;
- MTTR;
- disponibilidade operacional;

a menos que exista fonte pública que realmente suporte essa semântica.

Os KPIs do protótipo sintético permanecem apenas como material histórico/teste e não representam desempenho real de prestadoras.

## Arquitetura v2

`Anatel/dados.gov.br → ingestão raw → staging imutável → normalização de prestadoras/serviços/geografia → marts analíticos → contrato JSON/CSV → React/TypeScript → Cloudflare Workers Static Assets`

## Stack

### Dados
- Python 3.13
- Pandas
- requests
- pytest
- Ruff

### Frontend
- React 19
- TypeScript
- Vite
- Vitest / Testing Library

### Entrega
- GitHub Actions
- Cloudflare Workers + Static Assets

## Fase atual

**Real Data Foundation**

O objetivo imediato é:
1. catalogar fontes oficiais;
2. consolidar contratos;
3. construir ingestão reproduzível;
4. definir dimensão canônica de prestadoras;
5. calcular Top N por serviço e período;
6. validar market share e qualidade;
7. só então reconstruir o dashboard público.

## Histórico sintético

O protótipo anterior demonstrou:
- pipeline;
- validação;
- métricas;
- contrato frontend;
- dashboard;
- testes;
- CI/CD;
- publicação Cloudflare.

Ele não será apagado da história Git. A v2 assume explicitamente que essa etapa foi um ensaio técnico.

## Governança

Mudanças continuam seguindo:

`Normas → Baseline → Fontes → Contratos → Validação → Evidências → Implementação → Revalidação → Review → Deploy autorizado`

Leia:
- `docs/GOVERNANCE.md`
- `docs/PROJECT_CHARTER.md`
- `docs/DATA_SOURCES.md`
- `docs/ARCHITECTURE.md`
- `docs/SPRINT_PLAN.md`

## Licença e atribuição de dados

O projeto deve preservar a atribuição das fontes públicas. Dados da Anatel podem sofrer revisões posteriores pela própria Agência; por isso cada snapshot precisa registrar período, data de aquisição e origem.
