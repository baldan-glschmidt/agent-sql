# R046ATF

## Descrição

Conversão Acidente Trabalho com rateio - Contas Financeiras

---

## Resumo

- Campos: 10
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatCnv | Date | Não | Data Conversão |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| CodRat | Number(009,0) | Não | Código do Rateio |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| ConFin | Number(007,0) | Não | Conta Financeira |
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
- ConFin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R046ATF_007

**Tabela:** R046ATV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatCnv | DatCnv |
| CodCal | CodCal |
| TabEve | TabEve |
| CodEve | CodEve |

