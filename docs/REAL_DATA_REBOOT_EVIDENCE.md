# Real Data Reboot — Evidências da fundação v2

Data: 2026-09-22  
Branch: `v2-real-data-reboot`

## Decisão

O projeto deixa de apresentar dados sintéticos como produto principal.

A fase anterior é classificada como protótipo/ensaio técnico.

## Fontes oficiais verificadas

### Dados Abertos Anatel
Catálogo oficial com bases de acessos, qualidade, reclamações, satisfação e outras dimensões setoriais.

### Acessos SMP
A documentação oficial informa dados CSV de 2005 ao presente e consolidações por empresa/grupo, tecnologia, tipo, DDD, UF, região e total.

### Acessos SCM
A documentação oficial informa dados CSV de 2007 ao presente e consolidações por empresa/grupo, velocidade, município, região, tecnologia, UF e total.

### RQUAL
Qualidade publicada por prestadora e diferentes granularidades. Inclui IQS, IR, IQP e indicadores técnicos.

### Selos/IQS
Base de dados abertos publicada pela Anatel em 2026.

### Competição 2T2026
Snapshot oficial usado na fundação:
- SMP: 276,4 milhões de acessos;
- 5G: 66,1 milhões / 23,9%;
- Vivo móvel: 37,9%;
- TIM móvel: 22,4%;
- SCM: 55,4 milhões;
- fibra: 44,7 milhões;
- Claro SCM: 19,5%;
- Vivo SCM: 15,1%;
- NIO SCM: 6,2%.

### Satisfação 2025
Snapshot oficial de ISG por prestadora/serviço.

## Regras técnicas implementadas

- contrato v2 com `data_mode=official_public`;
- source registry;
- snapshots com `source_id`;
- Top N genérico;
- ausência não é transformada em zero;
- rankings parciais ficam marcados como incompletos;
- SMP e SCM permanecem separados;
- CI proíbe métricas sintéticas NOC no `dashboard-v2.json`;
- build Cloudflare exige o contrato v2 real.

## Próximo gate

A Sprint R1 deverá substituir o snapshot parcial por ingestão completa das bases mensais SMP/SCM antes de declarar Top 5/Top 10 completo.
