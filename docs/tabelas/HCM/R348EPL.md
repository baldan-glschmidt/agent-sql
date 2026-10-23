# R348EPL

## Descrição

eSocial - Conferência PIS - Código de Receita por Estabelecimento - Liminares

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
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
| FilEst | Number(006,0) | Não | Código da Filial do Estabelecimento |
| CodRec | Number(006,0) | Não | Código de Receita |
| FilLim | Number(006,0) | Não | Código da Filial |
| CodLim | Number(002,0) | Não | Código da Liminar |
| DesLim | String(040) | Sim | Descrição da Liminar |
| BasCod | Number(014,2) | Sim | Base Suspensa do Código de Receita |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- FilEst
- CodRec
- FilLim
- CodLim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
