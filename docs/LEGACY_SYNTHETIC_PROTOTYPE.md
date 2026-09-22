# Fase sintética — legado de prototipação

As Sprints 0–5 do TelecomPulse Analytics usaram dados sintéticos de incidentes para provar:

- governança;
- pipeline Python/Pandas;
- validação;
- analytics;
- contratos;
- React/TypeScript;
- testes;
- CI/CD;
- Cloudflare.

## Decisão v2

A partir do **Real Data Reboot**, esses dados deixam de ser o produto principal.

Conceitos como:
- incidentes;
- downtime;
- MTTR;
- recorrência;
- disponibilidade derivada de incidentes;

não devem aparecer no dashboard público v2, porque o projeto agora exige suporte direto em fontes públicas reais.

## Por que preservar

O legado continua útil para:
- histórico de evolução;
- demonstração de engenharia;
- testes de regressão do código antigo durante a transição;
- discussão arquitetural.

Ele não deve ser confundido com dados de desempenho real de operadoras.
