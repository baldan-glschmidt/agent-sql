# E001LTF

## Descrição

Cadastros - Transações - Ligação Transação X Filial

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodTns | String(005) | Não | Código da transação |
| DatIni | Date | Não | Data início de validade da ligação transação X filial |
| PrzRet | Number(004,0) | Sim | Prazo de retorno das mercadorias para fins de suspensão de ICMS (em dias) |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodTns
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
