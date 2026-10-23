# R038HCA

## Descrição

Histórico Cargos

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 3
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data da Alteração do Cargo |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Novo Cargo |
| CodMot | Number(003,0) | Sim | Motivo da Alteração do Cargo |
| StaHis | Number(001,0) | Sim | Status do Histórico |
| CarVag | String(024) | Sim | Código do novo cargo para ocupação da vaga |
| CodCrr | Number(003,0) | Sim | Código da Carreira |
| FunEso | String(001) | Sim | Função eSocial |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

### R038HCAIndice2

**Tipo:** Não unico

Campos:
- StaHis
- DatAlt

### R038HCAIndice3

**Tipo:** Não unico

Campos:
- EstCar
- CodCar

### R038HCAIndice4

**Tipo:** Não unico

Campos:
- CodMot

---

## Relacionamentos

### IR_R038HCA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R038HCA_004

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R038HCA_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R038HCA_006

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

