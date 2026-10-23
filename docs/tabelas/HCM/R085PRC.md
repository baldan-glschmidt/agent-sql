# R085PRC

## Descrição

Param Orçamento - Proporcionalização Dias - por Local e Cargo

---

## Resumo

- Campos: 11
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
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
- EstCar
- CodCar
- CmpPrm
- NatDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085PRC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R085PRC_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R085PRC_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

