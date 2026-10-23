# R085PRL

## Descrição

Param Orçamento - Proporcionalização Dias - por Local

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CmpPrm | Date | Não | Competência |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| QtdDia | Number(004,0) | Sim | Quantidade de dias no mês |
| DiaDsr | Number(004,0) | Sim | Quantidade de dias DSR |
| DiaUti | Number(004,0) | Sim | Quantidade de dias úteis |

---

## Chave Primária

- NumEmp
- CodCen
- TabOrg
- NumLoc
- CmpPrm
- NatDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085PRL_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R085PRL_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

