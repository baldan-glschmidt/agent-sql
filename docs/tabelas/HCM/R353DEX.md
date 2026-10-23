# R353DEX

## Descrição

eSocial - perAnt - Deduções suspensas - dep. e beneficiários pensão alimentícia

---

## Resumo

- Campos: 11
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
| CodRec | Number(006,0) | Não | Código de receita do IRRF sobre rendimentos do trabalho |
| SeqJcr | Number(009,0) | Não | Sequência |
| SeqVpj | Number(009,0) | Não | Sequência |
| SeqExs | Number(009,0) | Não | Sequência |
| SeqDex | Number(009,0) | Não | Sequência |
| CpfDep | Number(011,0) | Sim | Número de inscrição no CPF |
| VlrDed | Number(014,2) | Sim | Dedução de dependentes/pensão alimentícia com exigibilidade suspensa |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- CodRec
- SeqJcr
- SeqVpj
- SeqExs
- SeqDex

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
