# R348CRE

## Descrição

eSocial - Conferência INSS - Código de Receita por Empresa

---

## Resumo

- Campos: 14
- Chave Primária: 6 campo(s)
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
| PerCen | Number(006,4) | Não | Percentual |
| BasCod | Number(014,2) | Sim | Base de Código de Receita |
| BasCon | Number(014,2) | Sim | Base do INSS - Empresa concomitante |
| BasOne | Number(016,4) | Sim | Base do INSS - Onerada |
| BasDes | Number(016,4) | Sim | Base do INSS - Desonerada |
| BasN13 | Number(014,2) | Sim | Base do INSS - 13º salário - Lei 14.973/2024 |
| ValCod | Number(014,2) | Sim | Valor de Código de Receita |
| ValSup | Number(014,2) | Sim | Valor de Código de Receita Suspenso |
| VaSuCa | Number(014,2) | Sim | Valor de Código de Receita Suspenso Calculado |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CodRec
- PerCen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
