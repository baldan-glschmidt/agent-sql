# R348CRP

## Descrição

eSocial - Conferência PIS - Código de Receita por Empresa

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
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
| CodRec | Number(006,0) | Não | Código de Receita |
| BasCod | Number(014,2) | Sim | Base de Código de Receita |
| BasSus | Number(014,2) | Sim | Base Suspensa do Código de Receita |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CodRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
