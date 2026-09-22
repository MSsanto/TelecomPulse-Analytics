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
| Cloudflare ainda não reproduzido pelo repositório | Médio | Sprint 5 dedicada a publicação/rollback |
| Dados reais poderiam introduzir PII/segredos no futuro | Alto | Dataset público sintético por padrão e governança bloqueia publicação não autorizada |
| Ausência de testes E2E em navegador real | Médio | Testes de componente cobrem fluxos prioritários; E2E pode ser adicionado se risco justificar |
