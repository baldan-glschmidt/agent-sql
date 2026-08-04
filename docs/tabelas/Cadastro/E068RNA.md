# E068RNA

## Descrição

Tabelas - Rotinas para Controle de Níveis de Aprovação

---

## Resumo

- Campos: 14
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa do nível de aprovação |
| RotNap | Number(002,0) | Não | Código da rotina para controle de níveis de aprovação |
| IndNef | String(001) | Não | Indicativo se o número do controle de aprovação é por empresa ou filial |
| AprSeq | String(001) | Sim | Obedecer a sequência de níveis nos níveis exigidos para aprovação |
| MulApr | String(001) | Sim | Utilizar múltiplos aprovadores no mesmo nível |
| ConVlr | String(001) | Sim | Indicativo se a rotina irá considerar o valor financeiro para as aprovações |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAtu | Date | Sim | Data da última alteração do registro |
| HorAtu | Number(005,0) | Sim | Hora da última alteração do registro |
| UtiEap | String(001) | Sim | Utiliza Encaminhamento Aprovação |
| IntWF2 | String(001) | Sim | Indicativo se a rotina integra aprovações com o Workflow 2.0 |

---

## Chave Primária

- CodEmp
- RotNap

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
