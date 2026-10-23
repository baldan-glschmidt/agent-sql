# R185QTL

## Descrição

Orçamento Individual - Qtde de Colaboradores - Local

---

## Resumo

- Campos: 13
- Chave Primária: 11 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpOrc | Date | Não | Competência Orçamento |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| TipVag | Number(002,0) | Não | Código do tipo de vaga |
| AnoBas | Number(004,0) | Não | Ano base de cálculo do orçamento |
| VerOrc | Number(004,0) | Não | Versão do orçamento |
| RevOrc | Number(004,0) | Não | Revisão  da versão do orçamento |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| QtdCol | Number(004,0) | Sim | Quantidade Colaboradores |
| IndCal | Number(001,0) | Sim | Tipo de cálculo(1-Base/2-Valor Mensal) |

---

## Chave Primária

- NumEmp
- CmpOrc
- TabOrg
- NumLoc
- EstCar
- CodCar
- TipVag
- AnoBas
- VerOrc
- RevOrc
- NatDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R185QTL_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R185QTL_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R185QTL_009

**Tabela:** R185REV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| AnoBas | AnoBas |
| VerOrc | VerOrc |
| RevOrc | RevOrc |

### IR_R185QTL_010

**Tabela:** R048NAT

| Origem | Destino |
|--------|---------|
| NatDes | NatDes |

