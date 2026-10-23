# R197CND

## Descrição

Cenário - Contas Contábeis por Natureza Despesa

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código do C.Custo Contábil |
| NatDes | Number(003,0) | Não | Natureza de despesa |
| IteOrc | Number(003,0) | Não | Código do Item |
| CodCon | String(030) | Sim | Código da conta contábil |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| CodCen | Number(004,0) | Sim | Código do cenário |

---

## Chave Primária

- NumEmp
- CodCcu
- NatDes
- IteOrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
