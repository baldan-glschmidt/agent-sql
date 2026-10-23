# R349IRP

## Descrição

S-5001 - eSocial - Informações de remuneração por período de referência

---

## Resumo

- Campos: 11
- Chave Primária: 9 campo(s)
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
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqElt | Number(009,0) | Não | Sequência |
| SeqMct | Number(009,0) | Não | Sequência |
| SeqIrp | Number(009,0) | Não | Sequência |
| PerRef | Date | Sim | Período ao qual se refere a remuneração |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqElt
- SeqMct
- SeqIrp

---

## Índices

### R349IRPIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
