# R349SUD

## Descrição

S-5002 - eSocial - Deduções suspensas - Dependentes e beneficiários da pensão

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
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCpl | Number(009,0) | Não | Sequência |
| SeqCri | Number(009,0) | Não | Sequência |
| SeqPro | Number(009,0) | Não | Sequência |
| SeqRtr | Number(009,0) | Não | Sequência |
| SeqDsu | Number(009,0) | Não | Sequência |
| SeqSud | Number(009,0) | Não | Sequência |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| VlrSud | Number(014,2) | Sim | Valor da dedução relativa a dependentes ou a pensão alimentícia com exigibilidade suspensa |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqCpl
- SeqCri
- SeqPro
- SeqRtr
- SeqDsu
- SeqSud

---

## Índices

### R349SUDIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
