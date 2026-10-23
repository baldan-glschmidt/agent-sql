# R350DEX

## Descrição

S-1210 - eSocial - Deduções suspensas - beneficiários da pensão alimentícia

---

## Resumo

- Campos: 14
- Chave Primária: 11 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqInf | Number(009,0) | Não | Sequência |
| SeqRcr | Number(009,0) | Não | Sequência |
| SeqJcr | Number(009,0) | Não | Sequência |
| SeqVpj | Number(009,0) | Não | Sequência |
| SeqExs | Number(009,0) | Não | Sequência |
| SeqDex | Number(009,0) | Não | Sequência |
| CpfDep | Number(011,0) | Sim | Número de inscrição no CPF |
| VlrDed | Number(014,2) | Sim | Valor da dedução relativa a dependentes ou a pensão alimentícia com exigibilidade suspensa |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqInf
- SeqRcr
- SeqJcr
- SeqVpj
- SeqExs
- SeqDex

---

## Índices

### R350DEXIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
