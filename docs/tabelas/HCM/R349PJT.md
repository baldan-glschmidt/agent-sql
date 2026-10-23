# R349PJT

## Descrição

S-5001 - eSocial - Processos judiciais do trabalhador

---

## Resumo

- Campos: 10
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
| SeqPjt | Number(009,0) | Não | Sequência |
| NumPro | String(021) | Sim | Número do processo judicial |
| CodSus | Number(014,0) | Sim | Código Suspensão |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqPjt

---

## Índices

### R349PJTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
