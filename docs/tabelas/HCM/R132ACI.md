# R132ACI

## Descrição

Reserva Curso - Por Participante - Aval. Conhecimento - Item

---

## Resumo

- Campos: 10
- Chave Primária: 9 campo(s)
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
| FamCnc | String(004) | Não | Família do conhecimento |
| CodCnc | String(005) | Não | Código do conhecimento |
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
- FamCnc
- CodCnc

---

## Índices

### R132ACIIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CmpAva
- SeqAva
- FamCnc
- CodCnc

---

## Relacionamentos

### IR_R132ACI_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R132ACI_004

**Tabela:** R132RPA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatRes | DatRes |

### IR_R132ACI_006

**Tabela:** R077ACT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpAva | CmpAva |
| SeqAva | TipAva |

### IR_R132ACI_008

**Tabela:** R077ACN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpAva | CmpAva |
| SeqAva | TipAva |
| FamCnc | FamCnc |
| CodCnc | CodCnc |

