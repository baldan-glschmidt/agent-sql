# R350RDP

## Descrição

S-1210 - eSocial - Informação de reembolso do dependente do plano saúde coletivo

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqInf | Number(009,0) | Não | Sequência |
| SeqRps | Number(009,0) | Não | Sequência |
| SeqRdp | Number(009,0) | Não | Sequência |
| CpfBen | Number(011,0) | Sim | Número de inscrição no CPF do dependente |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqInf
- SeqRps
- SeqRdp

---

## Índices

### R350RDPIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
