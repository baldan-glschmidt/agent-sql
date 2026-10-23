# R195HCA

## Descrição

Cenário - Histórico Cargos

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data da Alteração do Cargo |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Novo Cargo |
| CodMot | Number(003,0) | Sim | Motivo da Alteração do Cargo |
| CarVag | String(024) | Sim | Código do novo cargo para ocupação da vaga |
| OriHca | Number(001,0) | Sim | Origem do Histórico |

---

## Chave Primária

- NumEmp
- CodCen
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195HCA_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195HCA_005

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R195HCA_006

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R195HCA_007

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

