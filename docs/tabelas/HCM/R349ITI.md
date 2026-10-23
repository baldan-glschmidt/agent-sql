# R349ITI

## Descrição

S-5001 - eSocial - Informações relativas ao trabalho intermitente

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
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
| SeqIti | Number(009,0) | Não | Sequência |
| DiaMes | Number(002,0) | Sim | Dia do mês efetivamente trabalhado pelo empregado |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| HorTra | String(004) | Sim | Horas Trabalhadas |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqIti

---

## Índices

### R349ITIIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
