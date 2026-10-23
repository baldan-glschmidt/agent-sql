# R185VCC

## Descrição

Orçamento Individual - Val. Alteração Quadro - C.Custo

---

## Resumo

- Campos: 15
- Chave Primária: 11 campo(s)
- Índices: 1
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpOrc | Date | Não | Competência Orçamento |
| CodCcu | String(018) | Não | Código do Centro de Custo |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| TipVag | Number(002,0) | Não | Código do tipo de vaga |
| AnoBas | Number(004,0) | Não | Ano base de cálculo do orçamento |
| VerOrc | Number(004,0) | Não | Versão do orçamento |
| RevOrc | Number(004,0) | Não | Revisão  da versão do orçamento |
| IteOrc | Number(003,0) | Não | Item de orçamento |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| IndCal | Number(001,0) | Sim | Tipo de cálculo(1-Base/2-Valor Mensal) |
| ValOrc | Number(011,2) | Sim | Valor do Orçamento |
| CodCon | String(030) | Sim | Código da conta contábil |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |

---

## Chave Primária

- NumEmp
- CmpOrc
- CodCcu
- EstCar
- CodCar
- TipVag
- AnoBas
- VerOrc
- RevOrc
- IteOrc
- NatDes

---

## Índices

### R185VCCIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- AnoBas
- VerOrc
- RevOrc

---

## Relacionamentos

### IR_R185VCC_002

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R185VCC_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R185VCC_008

**Tabela:** R185REV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| AnoBas | AnoBas |
| VerOrc | VerOrc |
| RevOrc | RevOrc |

### IR_R185VCC_009

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

### IR_R185VCC_010

**Tabela:** R048NAT

| Origem | Destino |
|--------|---------|
| NatDes | NatDes |

