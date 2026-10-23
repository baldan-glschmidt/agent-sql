# R350RCR

## Descrição

S-1210 - eSocial - Informações de Imposto de Renda, por Código de Receita - CR

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqInf | Number(009,0) | Não | Sequência |
| SeqRcr | Number(009,0) | Não | Sequência |
| CodRec | Number(006,0) | Sim | Código de receita relativo ao Imposto de Renda Retido na Fonte sobre rendimentos do trabalho |
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

---

## Índices

### R350RCRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
