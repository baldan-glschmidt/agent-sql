# R349CCO

## Descrição

Conferência S-5001 - Informações das contribuições sociais por colaborador

---

## Resumo

- Campos: 20
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| PerApu | Date | Não | Período Apuração |
| CodFil | Number(006,0) | Não | Código da Filial |
| IdeLot | String(030) | Não | Código atribuído pela empresa para a lotação |
| CodCat | Number(004,0) | Não | Código da categoria do trabalhador |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| BasVea | Number(011,2) | Sim | Base de INSS Verde e Amarelo |
| BasIns | Number(011,2) | Sim | Base de INSS |
| BasSus | Number(011,2) | Sim | Base de INSS Suspenso |
| ValRet | Number(011,2) | Sim | Valor de INSS Retido |
| SalFam | Number(011,2) | Sim | Valor Salário Família |
| Matern | Number(011,2) | Sim | Valor Maternidade |
| VaSest | Number(011,2) | Sim | Valor SEST |
| VSenat | Number(011,2) | Sim | Valor SENAT |
| GraExp | Number(001,0) | Sim | Grau de exposição a agentes nocivos |
| CodCal | String(030) | Sim | Código de Cálculo que formaram as bases |
| IndInc | Number(001,0) | Sim | Indicativo de Incidência |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CodFil
- IdeLot
- CodCat
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
