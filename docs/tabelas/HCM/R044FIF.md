# R044FIF

## Descrição

Eventos Fixos - Contas Financeiras

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código Evento Fixo |
| CodRat | Number(009,0) | Não | Código do Rateio |
| DatIni | Date | Não | Data de Início da Validade do Evento |
| ConFin | Number(007,0) | Não | Conta Financeira |
| ValFin | Number(011,2) | Sim | Valor do Evento |
| EmpFin | Number(011,2) | Sim | Valor do Empréstimo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TabEve
- CodEve
- CodRat
- DatIni
- ConFin

---

## Índices

### R044FIFIndice2

**Tipo:** Não unico

Campos:
- TabEve
- CodEve

---

## Relacionamentos

### IR_R044FIF_004

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

