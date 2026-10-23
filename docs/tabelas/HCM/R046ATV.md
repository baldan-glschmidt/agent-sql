# R046ATV

## Descrição

Conversão Acidente Trabalho - Valores

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 3
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatCnv | Date | Não | Data Conversão |
| CodCal | Number(005,0) | Não | Código do Cálculo |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |
| CodRub | Number(009,0) | Sim | Código da rubrica |
| FatRub | Number(005,2) | Sim | Fator, Percentual Entre Outros da Rubrica. |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatCnv
- CodCal
- TabEve
- CodEve

---

## Índices

### R046ATVIndice2

**Tipo:** Não unico

Campos:
- CodCal
- CodEve

### R046ATVIndice3

**Tipo:** Não unico

Campos:
- CodCal
- TipCol
- NumCad
- NumEmp
- CodEve
- ValEve

### R046ATVIndice4

**Tipo:** Não unico

Campos:
- CodRub
- NumEmp

---

## Relacionamentos

### IR_R046ATV_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R046ATV_003

**Tabela:** R046ATC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatCnv | DatCnv |

### IR_R046ATV_004

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

### IR_R046ATV_006

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

