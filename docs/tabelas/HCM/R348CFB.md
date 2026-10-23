# R348CFB

## Descrição

eSocial - Conferência FGTS - Base Colaborador

---

## Resumo

- Campos: 15
- Chave Primária: 8 campo(s)
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
| CodCal | String(200) | Sim | Códigos de cálculo associados à base |
| BasCal | Number(014,2) | Sim | Base de cálculo do FGTS |
| ValNor | Number(014,2) | Sim | Valor normal do FGTS |
| BasDec | Number(014,2) | Sim | Base de cálculo do 13° salário |
| ValDec | Number(014,2) | Sim | Valor calculado do 13° salário |
| BasInd | Number(014,2) | Sim | Base de cálculo indenizado |
| ValInd | Number(014,2) | Sim | Valor calculado indenizado |

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

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
