# R349FPD

## Descrição

S-5003 - eSocial - Depósitos de FGTS em Períodos de Apuração

---

## Resumo

- Campos: 11
- Chave Primária: 8 campo(s)
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
| SeqFdt | Number(009,0) | Não | Sequência Matrícula e Categoria do Trabalhador |
| SeqFpd | Number(009,0) | Não | Sequência Depósitos no Período de Apuração |
| TipDps | Number(002,0) | Sim | Tipo Depósito FGTS |
| ValDps | Number(014,2) | Sim | Valor do Depósito de FGTS |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqFdt
- SeqFpd

---

## Índices

### R349FPDIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
