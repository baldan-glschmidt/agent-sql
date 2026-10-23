# R132OCC

## Descrição

Reserva de Curso - Por Participante - Orçamento por Centro de Custo

---

## Resumo

- Campos: 10
- Chave Primária: 10 campo(s)
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
| CodCcu | String(018) | Não | Código Centro Custo Contábil |
| AnoBas | Number(004,0) | Não | Ano base do orçamento |
| MesBas | Number(002,0) | Não | Mês base do orçamento |
| SeqCus | Number(003,0) | Não | Sequência de custos do orçamento |

---

## Chave Primária

- CodCua
- NumEmp
- TipCol
- NumCad
- DatRes
- EmpOrc
- CodCcu
- AnoBas
- MesBas
- SeqCus

---

## Índices

### R132OCCIndice2

**Tipo:** Não unico

Campos:
- EmpOrc
- CodCcu
- AnoBas
- MesBas
- SeqCus
- CodCua

---

## Relacionamentos

### IR_R132OCC_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R132OCC_004

**Tabela:** R132RPA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatRes | DatRes |

### IR_R132OCC_009

**Tabela:** R138OCC

| Origem | Destino |
|--------|---------|
| EmpOrc | NumEmp |
| CodCcu | CodCcu |
| AnoBas | AnoBas |
| MesBas | MesBas |
| CodCua | CodCua |
| SeqCus | SeqCus |

