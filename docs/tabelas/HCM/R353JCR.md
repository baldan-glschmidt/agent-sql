# R353JCR

## Descrição

eSocial - perAnt - Processos - não retenção de tributos ou a depósitos judiciais

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
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
| CodRec | Number(006,0) | Não | Código de receita do IRRF sobre rendimentos do trabalho |
| SeqJcr | Number(009,0) | Não | Sequência |
| TipPro | Number(001,0) | Sim | Código correspondente ao tipo de processo |
| NumPro | String(021) | Sim | Número do processo administrativo/judicial |
| CodSus | Number(014,0) | Sim | Código do indicativo da suspensão, atribuído pelo empregador em S-1070 |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- CodRec
- SeqJcr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
