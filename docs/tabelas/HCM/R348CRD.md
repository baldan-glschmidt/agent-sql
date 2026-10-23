# R348CRD

## Descrição

eSocial - Conferência IRRF - Código de Receita por Empresa - Diário

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
| PerApu | Date | Não | Período Apuração |
| PerDia | Date | Não | Período apuração diário |
| CodRec | Number(006,0) | Não | Código de receita relativo ao IRRF sobre rendimentos do trabalho |
| DiaApu | Number(002,0) | Sim | Dia de Apuração - Período de apuração diário do Código de Receita |
| ValCod | Number(014,2) | Sim | Valor correspondente ao Código de Receita |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- PerDia
- CodRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
