# R044MOF

## Descrição

Movimento p/ Folha - Contas Financeiras

---

## Resumo

- Campos: 11
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 2

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
| ConFin | Number(007,0) | Não | Conta Financeira |
| RefFin | Number(011,2) | Sim | Referência do Evento |
| ValFin | Number(011,2) | Sim | Valor do Evento |

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
- ConFin

---

## Índices

### R044MOFIndice2

**Tipo:** Não unico

Campos:
- TabEve
- CodEve

---

## Relacionamentos

### IR_R044MOF_003

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

### IR_R044MOF_005

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

