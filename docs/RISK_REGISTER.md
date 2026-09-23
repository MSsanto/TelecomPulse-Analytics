# TelecomPulse Analytics — Riscos residuais

## Estado após Sprint 3

| Risco | Impacto | Estado/Mitigação |
|---|---|---|
| Dataset sintético não representar toda a variabilidade real | Médio | Declarado explicitamente; ampliar fixtures nas próximas evoluções |
| Filtros não recalcularem KPIs executivos | Médio | Comportamento intencional e sinalizado na UI; contrato multidimensional exigiria evolução analítica |
| Acessibilidade ainda não auditada por especialista/ferramenta completa | Médio | Semântica, labels, foco e testes básicos na Sprint 4; auditoria formal permanece residual |
| Performance medida apenas por build/bundle | Baixo no MVP | Orçamento de bundle + arquitetura estática; medir Web Vitals após publicação |
| npm ecosystem sofrer nova vulnerabilidade após homologação | Médio | CI executa audit high/critical; revisar antes de release |
| 2 vulnerabilidades npm moderadas presentes na Sprint 4 | Médio | Gate high/critical passa; revisar atualização/remediação antes do release e não tratá-las como risco zero |
| Publicação Cloudflare ainda não executada | Baixo | Build, smoke test local e rollback já reproduzidos no repositório; publicação externa foi adiada e registrada no backlog |
| Dados reais poderiam introduzir PII/segredos no futuro | Alto | Dataset público sintético por padrão e governança bloqueia publicação não autorizada |
| Ausência de testes E2E em navegador real | Médio | Testes de componente cobrem fluxos prioritários; E2E pode ser adicionado se risco justificar |

## Real Data Reboot — Sprint R0

| Risco | Impacto | Estado/Mitigação |
|---|---|---|
| Host oficial de CSV da ANATEL bloquear automação de download | Alto | **Materializado na R0.** Não substituir por scraping/espelho como fonte primária; registrar bloqueio e exigir captura raw oficial reproduzível antes de GO |
| Dados históricos da ANATEL sofrerem correções retroativas | Médio | Registrar URL, data de coleta, tamanho e SHA-256 de cada raw; manter raw imutável e versionar metadados |
| Nomes jurídicos/comerciais de operadoras variarem entre fontes/períodos | Alto | Criar dimensão/aliases de operadoras somente após inspecionar o raw oficial; preservar valor original |
| Agregar índices não aditivos por soma/média simples | Alto | Bloqueio metodológico: qualidade, satisfação e reclamações só entram com regra oficial documentada |
| Snapshot secundário de validação ser confundido com raw oficial | Alto | Arquivo classificado como VALIDATION_SECONDARY, documentação explícita e proibição de uso como produção |
| Divergência Brasil → Região → UF | Alto | Função de reconciliação exige cobertura exata para métricas aditivas; ampliar para as 27 UFs após raw oficial |
