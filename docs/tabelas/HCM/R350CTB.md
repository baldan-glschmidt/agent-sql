# R350CTB

## Descrição

S-1300 - eSocial - Detalhamento Contribuição Sindical Patronal

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
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
| SeqSin | Number(009,0) | Não | Sequência |
| SeqCon | Number(009,0) | Não | Sequência |
| NumSin | Number(015,0) | Sim | Número de inscrição do Sindicato |
| CfjSin | String(014) | Sim | Número de inscrição do Sindicato |
| TipCon | Number(001,0) | Sim | Tipo Contribuição Sindical |
| ValCon | Number(014,2) | Sim | Valor Contribuição Sindical |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqSin
- SeqCon

---

## Índices

### R350CTBIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
