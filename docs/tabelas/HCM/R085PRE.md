# R085PRE

## Descrição

Param Orçamento - Proporcionalização Dias - por Empresa

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CmpPrm | Date | Não | Competência |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| QtdDia | Number(004,0) | Sim | Quantidade de dias no mês |
| DiaDsr | Number(004,0) | Sim | Quantidade de dias DSR |
| DiaUti | Number(004,0) | Sim | Quantidade de dias úteis |

---

## Chave Primária

- NumEmp
- CodCen
- CmpPrm
- NatDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085PRE_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

