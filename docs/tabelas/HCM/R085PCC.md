# R085PCC

## Descrição

Param Orçamento - Percentuais - por C.Custo e Cargo

---

## Resumo

- Campos: 14
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CodCcu | String(018) | Não | Código do Centro de Custo |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| CmpPer | Date | Não | Competência |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| IteOrc | Number(003,0) | Não | Código do Item de Orçamento |
| PerIte | Number(008,5) | Sim | Percentual do Item no Local |
| QtdHor | Number(010,0) | Sim | Quantidade de  Horas Extras |
| PerInc | Number(007,4) | Sim | % Incremento |
| ValCal | Number(013,4) | Sim | Valor Cálculo |
| QtdHra | Number(010,0) | Sim | Quantidade de  Horas Extras - rateadas entre as vagas |
| ValRat | Number(013,4) | Sim | Valor Rateado entre as vagas |

---

## Chave Primária

- NumEmp
- CodCen
- CodCcu
- EstCar
- CodCar
- CmpPer
- NatDes
- IteOrc

---

## Índices

### R085PCCIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodCen
- IteOrc

---

## Relacionamentos

### IR_R085PCC_002

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R085PCC_003

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R085PCC_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R085PCC_007

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

