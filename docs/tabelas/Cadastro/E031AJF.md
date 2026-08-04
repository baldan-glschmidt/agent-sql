# E031AJF

## Descrição

Cadastros - Finanças - Contas a Pagar/Receber - Modeas desconsiderados para Ajustes Financeiros

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
| CodMoe | String(003) | Não | Código da moeda ou índice |
| DesAvp | String(001) | Sim | Indicativo se desconsidera a moeda no AVP |
| DesAvm | String(001) | Sim | Indicativo se desconsidera a moeda no AVM |
| DesVcb | String(001) | Sim | Indicativo se desconsidera a moeda na variação cambial |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodMoe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
