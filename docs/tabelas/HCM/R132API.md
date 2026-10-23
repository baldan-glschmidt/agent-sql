# R132API

## Descrição

Reserva Curso - Por Participante - Aval. Performance - Item

---

## Resumo

- Campos: 9
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do curso de aperfeiçoamento |
| NumEmp | Number(004,0) | Não | Código da empresa do participante da reserva |
| TipCol | Number(001,0) | Não | Tipo do colaborador participante da reserva |
| NumCad | Number(009,0) | Não | Cadastro do colaborador participante da reserva |
| DatRes | Date | Não | Data de cadastro da reserva |
| CmpAva | Date | Não | Competência de geração da avaliação |
| SeqAva | Number(004,0) | Não | Sequência da avaliação |
| CodHte | String(006) | Não | Código da habilidade técnica |
| ObsRes | String(250) | Sim | Observação |

---

## Chave Primária

- CodCua
- NumEmp
- TipCol
- NumCad
- DatRes
- CmpAva
- SeqAva
- CodHte

---

## Índices

### R132APIIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CmpAva
- SeqAva
- CodHte

---

## Relacionamentos

### IR_R132API_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R132API_004

**Tabela:** R132RPA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatRes | DatRes |

### IR_R132API_006

**Tabela:** R077APA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpAva | CmpAva |
| SeqAva | TipAva |

### IR_R132API_007

**Tabela:** R077AHN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpAva | CmpAva |
| SeqAva | TipAva |
| CodHte | CodHte |

