# R020ELC

## Descrição

Exceções Rateio Mão de Obra por Local e Cargo

---

## Resumo

- Campos: 10
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 8

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Tabela de Organograma |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| EstCar | Number(004,0) | Não | Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| CmpRef | Date | Não | Competência do Rateio |
| TabEve | Number(003,0) | Não | Código Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodRat | Number(009,0) | Não | Código do Rateio |
| PerRat | Number(005,2) | Sim | % Rateio |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- EstCar
- CodCar
- CmpRef
- TabEve
- CodEve
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R020ELC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R020ELC_001

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

### IR_R020ELC_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R020ELC_003

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R020ELC_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R020ELC_006

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

### IR_R020ELC_007

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

### IR_R020ELC_008

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

