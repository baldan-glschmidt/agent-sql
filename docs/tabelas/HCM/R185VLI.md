# R185VLI

## Descrição

Orçamento Individual - Val. Colaborador - Local

---

## Resumo

- Campos: 20
- Chave Primária: 14 campo(s)
- Índices: 2
- Relacionamentos: 5

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
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| IteOrc | Number(003,0) | Não | Item Orçamento |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| IndCal | Number(001,0) | Sim | Tipo de cálculo(1-Base/2-Valor Mensal) |
| ValOrc | Number(011,2) | Sim | Valor do Orçamento |
| CarNiv | String(024) | Sim | Código do cargo no nível de controle do QL |
| CarVag | String(024) | Sim | Código do cargo da vaga |
| CodCon | String(030) | Sim | Código da conta contábil |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |

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
- TipCol
- NumCad
- IteOrc
- NatDes

---

## Índices

### R185VLIIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- AnoBas
- VerOrc
- RevOrc

### R185VLIIndice3

**Tipo:** Não unico

Campos:
- NumEmp
- CmpOrc
- TabOrg
- NumLoc
- EstCar
- CarNiv
- TipVag
- AnoBas
- VerOrc
- RevOrc
- TipCol
- NumCad
- IteOrc

---

## Relacionamentos

### IR_R185VLI_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R185VLI_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R185VLI_009

**Tabela:** R185REV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| AnoBas | AnoBas |
| VerOrc | VerOrc |
| RevOrc | RevOrc |

### IR_R185VLI_012

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

### IR_R185VLI_013

**Tabela:** R048NAT

| Origem | Destino |
|--------|---------|
| NatDes | NatDes |

