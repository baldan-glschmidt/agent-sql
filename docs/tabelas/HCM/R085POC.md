# R085POC

## Descrição

Param Orçamento - Percentuais - por Local e Cargo

---

## Resumo

- Campos: 15
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 4

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
| CmpPer | Date | Não | Competência |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| IteOrc | Number(003,0) | Não | Código do Item de Orçamento |
| PerIte | Number(008,5) | Sim | Percentual do Item no Local |
| QtdHor | Number(010,0) | Sim | Quantidade de  Horas Extras |
| PerInc | Number(007,4) | Sim | % Incremento |
| QtdHra | Number(010,0) | Sim | Quantidade de  Horas Extras - rateadas entre as vagas |
| ValRat | Number(013,4) | Sim | Valor Rateado entre as vagas |
| ValCal | Number(013,4) | Sim | Valor Cálculo |

---

## Chave Primária

- NumEmp
- CodCen
- TabOrg
- NumLoc
- EstCar
- CodCar
- CmpPer
- NatDes
- IteOrc

---

## Índices

### R085POCIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodCen
- IteOrc

---

## Relacionamentos

### IR_R085POC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R085POC_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R085POC_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R085POC_008

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

