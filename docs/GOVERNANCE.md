# TelecomPulse Analytics — Governança de Implementação

## Regra de ouro

Nenhuma alteração funcional começa antes de:
1. ler a documentação normativa vigente;
2. identificar escopo e critérios de aceite;
3. executar os validadores aplicáveis no baseline;
4. registrar evidências;
5. atualizar a documentação obrigatória;
6. implementar em mudança rastreável;
7. executar novamente os validadores;
8. registrar evidências pós-implementação.

## Implementador governado

Toda mudança deve declarar:
- objetivo;
- arquivos afetados;
- risco de regressão;
- critérios de aceite;
- validadores aplicáveis;
- evidências antes/depois;
- impacto em segurança, dados e compatibilidade;
- documentação atualizada.

## Ordem obrigatória

`Normas → Baseline → Validação → Evidências → Documentação → Implementação → Revalidação → Review`

## Bloqueios

Interromper implementação quando:
- a documentação normativa estiver ausente ou contraditória;
- o escopo exigir decisão de produto não documentada;
- um validador crítico falhar sem diagnóstico;
- houver risco de exposição de segredo/dado sensível;
- a mudança exigir deploy/publicação não explicitamente autorizados.

## Definição de pronto

Uma mudança só está pronta quando:
- critérios de aceite foram demonstrados;
- validadores relevantes passaram;
- evidências foram registradas;
- nenhuma regressão conhecida foi introduzida;
- documentação necessária foi atualizada;
- nenhuma ação de deploy/publicação ocorreu sem autorização.


## Camada de orquestração

Para tarefas complexas, o projeto usa o modelo de coordenação inspirado no Ruflo como camada acima do roteamento de skills.

Ordem:

`Ruflo-style Coordinator → SKILLS_ORCHESTRATOR → Implementador governado → Validadores → Gate`

O orquestrador pode decompor, paralelizar e coordenar trabalho, mas não pode:
- reduzir critérios de aceite;
- ignorar falhas críticas;
- substituir evidência por consenso entre agentes;
- autorizar deploy/publicação;
- promover dado não validado para produção.

Leia: `docs/RUFLO_ORCHESTRATION.md`.
