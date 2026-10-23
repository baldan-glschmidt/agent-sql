# R348CFT

## Descrição

eSocial - Conferência FGTS - Base Colaborador por Tipo Valor

---

## Resumo

- Campos: 13
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| FgtOri | Number(001,0) | Não | Tipo de origem da base de cálculo do FGTS |
| TipVal | Number(002,0) | Não | Tipo de valor do FGTS |
| IndInc | Number(001,0) | Sim | Indicativo de incidência do FGTS |
| ValBas | Number(014,2) | Sim | Base de cálculo do FGTS para o tipo de valor |
| AliFgt | Number(005,2) | Sim | Alíquota aplicada ao FGTS para o tipo de valor |
| ValFgt | Number(014,2) | Sim | Valor de FGTS a ser depositado para o tipo de valor |

---

## Chave Primária

- NumEmp
- CodFil
- CodRat
- PerApu
- IndApu
- TipCol
- NumCad
- FgtOri
- TipVal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
