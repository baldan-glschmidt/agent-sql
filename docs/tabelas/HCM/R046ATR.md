# R046ATR

## Descrição

Conversão Acidente Trabalho com rateio

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatCnv | Date | Não | Data Conversão |
| CodCal | Number(005,0) | Não | Código do Cálculo |
| CodRat | Number(009,0) | Não | Código do Rateio |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatCnv
- CodCal
- CodRat
- TabEve
- CodEve

---

## Índices

### R046ATRIndice2

**Tipo:** Não unico

Campos:
- CodCal
- CodEve

---

## Relacionamentos

### IR_R046ATR_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R046ATR_004

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

### IR_R046ATR_005

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

### IR_R046ATR_007

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

