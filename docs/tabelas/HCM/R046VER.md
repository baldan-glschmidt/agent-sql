# R046VER

## Descrição

Ficha Financeira

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 3
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodCal | Number(005,0) | Não | Código do Cálculo |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| RefEve | Number(011,2) | Sim | Referência Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |
| OriEve | String(001) | Sim | Origem do Evento |
| CodRub | Number(009,0) | Sim | Código da rubrica |
| FatRub | Number(005,2) | Sim | Fator, Percentual Entre Outros da Rubrica. |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal
- TabEve
- CodEve

---

## Índices

### R046VERIndice2

**Tipo:** Não unico

Campos:
- CodCal
- CodEve

### R046VERIndice3

**Tipo:** Não unico

Campos:
- CodCal
- TipCol
- NumCad
- NumEmp
- CodEve
- RefEve
- ValEve

### R046VERIndice4

**Tipo:** Não unico

Campos:
- CodRub
- NumEmp

---

## Relacionamentos

### IR_R046VER_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R046VER_003

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

### IR_R046VER_005

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

