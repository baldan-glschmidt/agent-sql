# R348VPJ

## Descrição

eSocial - Conferência IRRF - Valores de não retenção e depósitos judiciais

---

## Resumo

- Campos: 14
- Chave Primária: 9 campo(s)
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
| VlrRet | Number(014,2) | Sim | Valor da retenção que deixou de ser efetuada - processo admin. ou judicial. |
| VlrJud | Number(014,2) | Sim | Valor do depósito judicial em função de processo administrativo ou judicial |
| VlrAno | Number(014,2) | Sim | Valor da compensação relativa ao ano calendário em função de processo judicial |
| VlrAnt | Number(014,2) | Sim | Valor da compensação relativa a anos anteriores em função de processo judicial |
| VlrRen | Number(014,2) | Sim | Valor do rendimento com exigibilidade suspensa |

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

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
