# R348RTR

## Descrição

eSocial - GRFGTS - Visão Remuneração - Trabalhadores c/ Remuneração - Remunerações - obsoleta

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdePen | String(040) | Não | Identificador da solicitação |
| SeqACR | Number(009,0) | Não | Sequência |
| SeqITR | Number(009,0) | Não | Sequência |
| SeqLTR | Number(009,0) | Não | Sequência |
| SeqRTR | Number(009,0) | Não | Sequência |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| FilEmp | Number(006,0) | Sim | Código da Filial Empregadora |
| TipRem | String(050) | Sim | Tipo da remuneração |
| IdeRem | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| RemFgt | Number(014,2) | Sim | Base do FGTS |
| FgtVal | Number(014,2) | Sim | Cálculo do FGTS |
| FgtRec | Number(014,2) | Sim | FGTS Recolhido |
| FgtDev | Number(014,2) | Sim | FGTS Devido |

---

## Chave Primária

- IdePen
- SeqACR
- SeqITR
- SeqLTR
- SeqRTR

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
