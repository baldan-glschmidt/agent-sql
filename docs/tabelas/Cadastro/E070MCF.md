# E070MCF

## Descrição

Cadastros - Filiais - Movimento de Compra por Competência

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| VcfCpr | Date | Não | Mês e ano da competência para controle de verba de compra da filial |
| CodNtg | Number(004,0) | Não | Natureza de gasto para controle de verba de compra da filial |
| SeqMcf | Number(004,0) | Não | Sequência do movimento de compra na filial |
| VlrMcf | Number(014,2) | Sim | Valor do movimento de compra na filial |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- VcfCpr
- CodNtg
- SeqMcf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
