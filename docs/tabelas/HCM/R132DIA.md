# R132DIA

## Descrição

Reserva de Curso - Por Participante - Diagnóstico

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
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
| CodDia | Number(009,0) | Não | Código do diagnóstico |

---

## Chave Primária

- CodCua
- NumEmp
- TipCol
- NumCad
- DatRes
- CodDia

---

## Índices

### R132DIAIndice2

**Tipo:** Não unico

Campos:
- CodDia

---

## Relacionamentos

### IR_R132DIA_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R132DIA_004

**Tabela:** R132RPA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatRes | DatRes |

