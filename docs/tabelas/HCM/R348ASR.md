# R348ASR

## Descrição

eSocial - GRFGTS - Visão Remuneração - Trabalhadores Sem Remuneração - obsoleta

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdePen | String(040) | Não | Identificador da solicitação |
| SeqASR | Number(009,0) | Não | Sequência |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| FilEmp | Number(006,0) | Sim | Código da Filial Empregadora |
| NomTra | String(200) | Sim | Nome do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| MatTra | String(050) | Sim | Matrícula |

---

## Chave Primária

- IdePen
- SeqASR

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
