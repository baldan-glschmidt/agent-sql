# R348CFL

## Descrição

eSocial - Conferência FGTS - Total por Lotação

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodLot | String(030) | Não | Código da lotação no eSocial |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| TipVal | Number(002,0) | Não | Tipo de valor do FGTS |
| IndInc | Number(001,0) | Sim | Indicativo de incidência do FGTS |
| TipIns | Number(001,0) | Sim | Tipo de inscrição da filial |
| CfjIns | String(014) | Sim | Número de inscrição da filial |
| ValBas | Number(014,2) | Sim | Base de cálculo do FGTS por lotação |
| ValFgt | Number(014,2) | Sim | Valor de FGTS por lotação |

---

## Chave Primária

- NumEmp
- CodFil
- CodLot
- PerApu
- IndApu
- TipVal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
