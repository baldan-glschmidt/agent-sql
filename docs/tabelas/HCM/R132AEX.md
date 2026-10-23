# R132AEX

## Descrição

Reserva Curso - Por Participante - Aval. Excelência

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
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
| CmpAva | Date | Não | Competência de geração da avaliação |
| SeqAva | Number(004,0) | Não | Sequência da avaliação |
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

---

## Índices

### R132AEXIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CmpAva
- SeqAva

---

## Relacionamentos

### IR_R132AEX_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R132AEX_004

**Tabela:** R132RPA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatRes | DatRes |

### IR_R132AEX_006

**Tabela:** R079AEA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpAva | CmpAva |
| SeqAva | TipAva |

