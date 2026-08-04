# E440HAR

## Descrição

Compras - Notas Fiscais de Entrada - Histórico de arredondamento

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| DatAlt | Date | Não | Data da última alteração do arrendontamento |
| SeqAlt | Number(004,0) | Não | Sequência da alteração na data |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| VlrOld | Number(015,2) | Sim | Valor máximo do arredondamento antigo da nota de entrada |
| VlrMar | Number(015,2) | Sim | Valor máximo do arredondamento da nota de entrada |

---

## Chave Primária

- CodEmp
- CodFil
- DatAlt
- SeqAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
