# R350PRS

## Descrição

S-1070 - eSocial - Suspensão de Exigibilidade de Tributos e FGTS

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| CodPro | Number(009,0) | Não | Número do Processo/Benefício |
| DatIni | Date | Não | Data Início |
| SeqPro | Number(009,0) | Não | Sequência |
| SeqSus | Number(009,0) | Não | Sequência |
| CodSus | Number(014,0) | Sim | Código Suspensão |
| TipDec | Number(002,0) | Sim | Indicativo de Suspensão de exigibilidade |
| DatDec | Date | Sim | Data de Decisão, Sentença ou Despacho Administrativo |
| DepInt | String(001) | Sim | Indicativo de Depósito do Monante Integral |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute. |
| LayOut | String(006) | Sim | Leiaute |

---

## Chave Primária

- NumEmp
- FilEmp
- CodPro
- DatIni
- SeqPro
- SeqSus

---

## Índices

### R350PRSIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
