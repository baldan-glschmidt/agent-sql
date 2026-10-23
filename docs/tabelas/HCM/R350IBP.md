# R350IBP

## Descrição

S-1210 - eSocial - Informações sobre benefíciarios de pensão alimentícia

---

## Resumo

- Campos: 14
- Chave Primária: 9 campo(s)
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
| SeqDpf | Number(009,0) | Não | Sequência |
| SeqRaf | Number(009,0) | Não | Sequência |
| SeqIbp | Number(009,0) | Não | Sequência |
| CpfBen | Number(011,0) | Sim | CPF do Beneficiário |
| DatNas | Date | Sim | Data Nascimento do Beneficiário |
| NomDep | String(070) | Sim | Nome do Beneficiário |
| ValPen | Number(014,2) | Sim | Valor Pensão Alimentícia |
| PidExc | String(050) | Sim | Identificador da execução da pendência |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqIpe
- SeqDpf
- SeqRaf
- SeqIbp

---

## Índices

### R350IBPIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
