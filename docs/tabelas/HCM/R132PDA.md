# R132PDA

## Descrição

Reserva de Curso - Por Participante - Acompanhamento PDI

---

## Resumo

- Campos: 9
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do curso de aperfeiçoamento |
| NumEmp | Number(004,0) | Não | Código da empresa do participante da reserva |
| TipCol | Number(001,0) | Não | Tipo do colaborador participante da reserva |
| NumCad | Number(009,0) | Não | Cadastro do colaborador participante da reserva |
| DatRes | Date | Não | Data de cadastro da reserva |
| CodPln | Number(004,0) | Não | Código do plano de desenvolvimento |
| CodObj | Number(002,0) | Não | Código do Objetivo |
| CodAco | Number(002,0) | Não | Sequência da Ação |
| SeqAco | Number(002,0) | Não | Sequência da Ação |

---

## Chave Primária

- CodCua
- NumEmp
- TipCol
- NumCad
- DatRes
- CodPln
- CodObj
- CodAco
- SeqAco

---

## Índices

### R132PDAIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodPln
- CodObj
- CodAco
- SeqAco

---

## Relacionamentos

### IR_R132PDA_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R132PDA_004

**Tabela:** R132RPA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatRes | DatRes |

