# R348PPC

## Descrição

eSocial - Conferência PIS - Base Processo Colaborador

---

## Resumo

- Campos: 17
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| PerApu | Date | Não | Período Apuração |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| FilEst | Number(006,0) | Sim | Código da Filial do Estabelecimento |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| FilLim | Number(006,0) | Não | Código da Filial |
| CodLim | Number(002,0) | Não | Código da Liminar |
| DesLim | String(040) | Sim | Descrição da Liminar |
| CodPro | Number(009,0) | Não | Número do Processo/Benefício |
| NumPro | String(021) | Sim | Número do Processo/Benefício |
| CodSus | Number(014,0) | Sim | Código Suspensão |
| TipDec | Number(002,0) | Sim | Suspensão da Exigibilidade |
| BasPis | Number(014,2) | Sim | Base PIS Suspenso |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CodFil
- CodRat
- TipCol
- NumCad
- FilLim
- CodLim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
