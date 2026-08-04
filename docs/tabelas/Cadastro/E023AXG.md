# E023AXG

## Descrição

Cadastros - Finanças - Contas a Pagar/Receber - Grupos de Contas desconsiderados para Ajustes Financeiros

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCrp | String(003) | Não | Código do grupo de contas a receber ou pagar |
| DesAvp | String(001) | Sim | Indicativo se desconsidera o grupo de contas no AVP |
| DesAvm | String(001) | Sim | Indicativo se desconsidera o grupo de contas no AVM |
| DesVcb | String(001) | Sim | Indicativo se desconsidera o grupo de contas na variação cambial |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodCrp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
