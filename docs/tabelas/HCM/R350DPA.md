# R350DPA

## Descrição

S-1210 - eSocial - Pagamento de competências anteriores ao início do eSocial

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqIpe | Number(009,0) | Não | Sequência |
| SeqDpa | Number(009,0) | Não | Sequência |
| CodCat | Number(004,0) | Sim | Código da categoria atribuída ao trabalhador |
| PidExc | String(050) | Sim | Identificador da execução da pendência |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqIpe
- SeqDpa

---

## Índices

### R350DPAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
