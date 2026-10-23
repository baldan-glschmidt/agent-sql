# R349SCT

## Descrição

S-5011 - eSocial - Informações de suspensão de contribuição a Terceiros

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| PerApu | Date | Não | Período Apuração |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCeo | Number(009,0) | Não | Sequência |
| SeqCle | Number(009,0) | Não | Sequência |
| SeqSct | Number(009,0) | Não | Sequência |
| CodTer | Number(004,0) | Sim | Código de terceiros |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- SeqTab
- SeqCeo
- SeqCle
- SeqSct

---

## Índices

### R349SCTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
