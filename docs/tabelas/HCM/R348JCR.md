# R348JCR

## Descrição

eSocial - Conferência IRRF - Processos de não retenção e depósitos judiciais

---

## Resumo

- Campos: 8
- Chave Primária: 8 campo(s)
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

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
