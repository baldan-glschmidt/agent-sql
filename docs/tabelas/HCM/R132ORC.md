# R132ORC

## Descrição

Reserva de Curso - Por Participante - Orçamento TR

---

## Resumo

- Campos: 11
- Chave Primária: 11 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do curso de aperfeiçoamento |
| NumEmp | Number(004,0) | Não | Código da empresa do participante da reserva |
| TipCol | Number(001,0) | Não | Tipo do colaborador participante da reserva |
| NumCad | Number(009,0) | Não | Cadastro do colaborador participante da reserva |
| DatRes | Date | Não | Data de cadastro da reserva |
| EmpOrc | Number(004,0) | Não | Código da empresa do orçamento |
| TabOrg | Number(004,0) | Não | Código da tabela de organograma do local do orçamento |
| NumLoc | Number(009,0) | Não | Local do organograma do orçamento |
| AnoBas | Number(004,0) | Não | Ano base do orçamento |
| MesBas | Number(002,0) | Não | Mês base do orçamento |
| SeqCus | Number(002,0) | Não | Sequência de custos do orçamento |

---

## Chave Primária

- CodCua
- NumEmp
- TipCol
- NumCad
- DatRes
- EmpOrc
- TabOrg
- NumLoc
- AnoBas
- MesBas
- SeqCus

---

## Índices

### R132ORCIndice2

**Tipo:** Não unico

Campos:
- EmpOrc
- TabOrg
- NumLoc
- AnoBas
- MesBas
- SeqCus
- CodCua

---

## Relacionamentos

### IR_R132ORC_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R132ORC_004

**Tabela:** R132RPA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatRes | DatRes |

### IR_R132ORC_010

**Tabela:** R130OCU

| Origem | Destino |
|--------|---------|
| EmpOrc | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| AnoBas | AnoBas |
| MesBas | MesBas |
| CodCua | CodCua |
| SeqCus | SeqCus |

