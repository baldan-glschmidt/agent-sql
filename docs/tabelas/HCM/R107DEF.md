# R107DEF

## Descrição

PDI - Definições gerais

---

## Resumo

- Campos: 12
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ConObj | String(001) | Sim | Define quem deve registrar que tomou conhecimento dos objetivos |
| UsaIns | String(001) | Sim | Usa instituição no plano de desenvolvimento individual |
| CstPrv | String(001) | Sim | Usa custos previstos no PDI |
| CstRea | String(001) | Sim | Usa custos realizados no PDI |
| RspPln | Number(001,0) | Sim | Define quem será o responsável pelos planos de ação do PDI |
| CodThp | Number(003,0) | Sim | Indica a hierarquia que deve ser considerada na sugestão do responsável do PDI |
| NomBtn | String(020) | Sim | Nome do 1º Botão que será disponibilizado nas telas do PDI WEB |
| ModBtn | String(011) | Sim | Modelo de Relatório do 1º Botão |
| RegBtn | Number(003,0) | Sim | Código da regra do 1º botão |
| CicObr | String(001) | Sim | Especifica se o código do ciclo será obrigatório ao gerar/inserir/alterar o PDI |
| ResPdi | Number(001,0) | Sim | Define quem deve ter acesso ao PDI de um colaborador |
| AvaCon | String(001) | Sim | Indica se Colaborador do PDI pode lançar acompanhamentos do plano de ação |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
