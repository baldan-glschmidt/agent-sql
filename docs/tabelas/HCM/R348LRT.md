# R348LRT

## Descrição

eSocial - Conferência INSS - Código de Receita por Estabelecimento - Liminares Terceiros

---

## Resumo

- Campos: 17
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
| FilEst | Number(006,0) | Não | Código da filial do estabelecimento |
| CodRec | Number(006,0) | Não | Código de Receita |
| PerCen | Number(006,4) | Não | Percentual |
| BasCod | Number(014,2) | Sim | Base do Código de Receita |
| BasCon | Number(014,2) | Sim | Base do INSS - Empresa concomitante |
| BasOne | Number(016,4) | Sim | Base do INSS - Onerada |
| BasDes | Number(016,4) | Sim | Base do INSS - Desonerada |
| BasN13 | Number(014,2) | Sim | Base do INSS - 13º salário - Lei 14.973/2024 |
| ValCod | Number(014,2) | Sim | Valor do Código de Receita |
| ValSup | Number(014,2) | Sim | Valor do Código de Receita suspenso |
| TerFpa | Number(004,0) | Não | Código do terceiro da liminar |
| DesLim | String(040) | Sim | Descrição da liminar |
| BaInSu | Number(014,2) | Sim | Base do Código de Receita suspenso |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- FilEst
- CodRec
- PerCen
- TerFpa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
