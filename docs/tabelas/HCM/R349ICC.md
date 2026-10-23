# R349ICC

## Descrição

S-5001 - eSocial - Informações complementares contratuais do trabalhador

---

## Resumo

- Campos: 11
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
| SeqIcc | Number(009,0) | Não | Sequência |
| CodCbo | String(006) | Sim | Classificação Brasileira de Ocupações - CBO |
| NatAti | Number(001,0) | Sim | Natureza da atividade |
| QtdDia | Number(002,0) | Sim | Quantidade de dias trabalhados |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqIcc

---

## Índices

### R349ICCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
