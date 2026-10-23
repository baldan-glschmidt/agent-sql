# R349REE

## Descrição

S-5002 - eSocial - Reembolsos de despesas médicas

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCpl | Number(009,0) | Não | Sequência |
| SeqRee | Number(009,0) | Não | Sequência |
| IndRee | Number(001,0) | Sim | Indicativo da Origem do Reembolso |
| NumIns | Number(014,0) | Sim | CNPJ da Operadora do Plano de Saúde |
| CfjIns | String(014) | Sim | CNPJ da Operadora do Plano de Saúde |
| RegAns | String(006) | Sim | Registro na Agência Nacional de Saúde - ANS |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqCpl
- SeqRee

---

## Índices

### R349REEIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
