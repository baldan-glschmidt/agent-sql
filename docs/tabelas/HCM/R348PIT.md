# R348PIT

## Descrição

eSocial - Conferência INSS - Base Liminares Terceiro Colaborador

---

## Resumo

- Campos: 15
- Chave Primária: 9 campo(s)
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
| FilEst | Number(006,0) | Sim | Código da filial do estabelecimento |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TerFpa | Number(004,0) | Não | Código do Terceiro da Liminar |
| CodPro | Number(009,0) | Não | Número do Processo/Benefício |
| NumPro | String(021) | Sim | Número do Processo/Benefício |
| CodSus | Number(014,0) | Sim | Código Suspensão |
| TipDec | Number(002,0) | Sim | Suspensão da Exigibilidade |
| BaInSu | Number(014,2) | Sim | Base INSS Suspenso |

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
- TerFpa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
