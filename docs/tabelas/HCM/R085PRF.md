# R085PRF

## Descrição

Param Orçamento - Proporcionalização Dias -  por Filial

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPrm | Date | Não | Competência |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| QtdDia | Number(004,0) | Sim | Quantidade de dias no mês |
| DiaDsr | Number(004,0) | Sim | Quantidade de dias DSR |
| DiaUti | Number(004,0) | Sim | Quantidade de dias úteis |

---

## Chave Primária

- NumEmp
- CodCen
- CodFil
- CmpPrm
- NatDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085PRF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

