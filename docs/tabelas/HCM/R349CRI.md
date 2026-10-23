# R349CRI

## Descrição

S-5002 - eSocial - Informações de IR por Código de Receita

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
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCpl | Number(009,0) | Não | Sequência |
| SeqCri | Number(009,0) | Não | Sequência |
| CriRrt | Number(006,0) | Sim | Código de Receita - CR relativo ao Imposto de Renda Retido na Fonte sobre rendimentos do trabalho |
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

---

## Índices

### R349CRIIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
