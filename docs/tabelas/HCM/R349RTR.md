# R349RTR

## Descrição

S-5002 - eSocial - Valores - Não retenção de tributos ou depósitos judiciais

---

## Resumo

- Campos: 16
- Chave Primária: 9 campo(s)
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
| IndApu | Number(001,0) | Sim | Indicativo de período de apuração |
| VlrRet | Number(014,2) | Sim | Valor da retenção que deixou de ser efetuada em função de processo administrativo ou judicial |
| VlrJud | Number(014,2) | Sim | Valor do depósito judicial em função de processo administrativo ou judicial |
| VlrAno | Number(014,2) | Sim | Valor da compensação relativa ao ano calendário em função de processo judicial |
| VlrAnt | Number(014,2) | Sim | Valor da compensação relativa a anos anteriores, em função de processo judicial |
| VlrSus | Number(014,2) | Sim | Valor do rendimento com exigibilidade suspensa |
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

---

## Índices

### R349RTRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
