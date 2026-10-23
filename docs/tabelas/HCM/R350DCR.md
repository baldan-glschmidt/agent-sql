# R350DCR

## Descrição

S-1210 - eSocial - Dedução do rendimento tributável relativa a dependentes

---

## Resumo

- Campos: 12
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
| SeqRcr | Number(009,0) | Não | Sequência |
| SeqDcr | Number(009,0) | Não | Sequência |
| TipRen | Number(002,0) | Sim | Tipo de Rendimento |
| CpfDep | Number(011,0) | Sim | Número de inscrição no CPF |
| VlrDed | Number(014,2) | Sim | Valor da dedução da base de cálculo |
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
- SeqDcr

---

## Índices

### R350DCRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
