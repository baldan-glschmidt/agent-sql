# R044MOV

## Descrição

Movimento p/ Folha

---

## Resumo

- Campos: 14
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCal | Number(005,0) | Não | Código do Cálculo |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodRat | Number(009,0) | Não | Código do Rateio |
| SeqEve | Number(002,0) | Não | Sequência do Evento |
| OriMov | String(001) | Sim | Origem do Evento |
| RefEve | Number(011,2) | Sim | Referência do Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |
| BenCad | Number(009,0) | Sim | Código do Cálculo - Uso exclusivo ONIS |
| BenCod | Number(003,0) | Sim | Código do Benefício - Uso exclusivo ONIS |
| BenSeq | Number(009,0) | Sim | Sequência do Registro - Uso exclusivo ONIS |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal
- TabEve
- CodEve
- CodRat
- SeqEve

---

## Índices

### R044MOVIndice2

**Tipo:** Não unico

Campos:
- TabEve
- CodEve

---

## Relacionamentos

### IR_R044MOV_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R044MOV_003

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

### IR_R044MOV_005

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

