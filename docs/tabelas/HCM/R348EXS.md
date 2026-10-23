# R348EXS

## Descrição

eSocial - Conferência IRRF - Detalhamento deduções com exigibilidade suspensa

---

## Resumo

- Campos: 15
- Chave Primária: 11 campo(s)
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
| CnpjEn | Number(014,0) | Sim | Número de inscrição da entidade de previdência complementar |
| CfjIns | String(014) | Sim | Número de inscrição da entidade de previdência complementar |
| VlrDed | Number(014,2) | Sim | Valor da dedução da base de cálculo do IR com exigibilidade suspensa |
| VlrPat | Number(014,2) | Sim | Valor da contribuição do ente público patrocinador Funpresp |

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

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
