# R348DEX

## Descrição

eSocial - Conferência IRRF - Deduções suspensas de dependentes e pensão

---

## Resumo

- Campos: 13
- Chave Primária: 12 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| CodRec | Number(006,0) | Não | Código de receita relativo ao IRRF sobre rendimentos do trabalho |
| TipPro | Number(001,0) | Não | Código correspondente ao tipo de processo |
| NumPro | String(021) | Não | Número do processo administrativo/judicial |
| CodSus | Number(014,0) | Não | Código do indicativo da suspensão, atribuído pelo empregador em S-1070 |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| TipDed | Number(001,0) | Não | Indicativo do tipo de dedução |
| SeqExs | Number(009,0) | Não | Sequência |
| CpfDep | Number(011,0) | Não | Número de inscrição no CPF |
| VlrSus | Number(014,2) | Sim | Valor da dedução relativa a dependentes/pensão com exigibilidade suspensa |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- CodRec
- TipPro
- NumPro
- CodSus
- IndApu
- TipDed
- SeqExs
- CpfDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
