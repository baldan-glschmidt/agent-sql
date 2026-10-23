# R020ELF

## Descrição

Exceções Rateio Mão de Obra por Local e Cargo - Contas Financeiras

---

## Resumo

- Campos: 11
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 7

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
| ConFin | Number(007,0) | Não | Conta Financeira |
| PerFin | Number(005,2) | Sim | % Conta Financeira |

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
- ConFin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R020ELF_001

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

### IR_R020ELF_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R020ELF_003

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R020ELF_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R020ELF_006

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

### IR_R020ELF_007

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

### IR_R020ELF_008

**Tabela:** R020ELC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| EstCar | EstCar |
| CodCar | CodCar |
| CmpRef | CmpRef |
| TabEve | TabEve |
| CodEve | CodEve |
| CodRat | CodRat |

