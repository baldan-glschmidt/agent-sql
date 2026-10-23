# R348PIC

## Descrição

eSocial - Conferência INSS - Base Processo Colaborador

---

## Resumo

- Campos: 23
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
| FilEst | Number(006,0) | Sim | Código da filial do estabelecimento |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| FilLim | Number(006,0) | Não | Código da Filial |
| CodLim | Number(002,0) | Não | Código da Liminar |
| DesLim | String(040) | Sim | Descrição da Liminar |
| AplEmp | String(001) | Sim | Aplicação da Liminar no Cálculo da Parte Empresa |
| AplRAT | String(001) | Sim | Aplicação da Liminar no Cálculo do RAT |
| AplTer | String(001) | Sim | Aplicação da Liminar no Cálculo de Terceiros/Outras Entidades |
| CodPro | Number(009,0) | Não | Número do Processo/Benefício |
| NumPro | String(021) | Sim | Número do Processo/Benefício |
| CodSus | Number(014,0) | Sim | Código Suspensão |
| TipDec | Number(002,0) | Sim | Suspensão da Exigibilidade |
| BaInSu | Number(014,2) | Sim | Base INSS Suspenso |
| BasCon | Number(014,2) | Sim | Base do INSS - Empresa concomitante |
| BasOne | Number(016,4) | Sim | Base do INSS - Onerada |
| BasDes | Number(016,4) | Sim | Base do INSS - Desonerada |

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
