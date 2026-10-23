# R349MCT

## Descrição

S-5001 - eSocial - Matrícula, categoria do trabalhador e tipos de incidências

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
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqElt | Number(009,0) | Não | Sequência |
| SeqMct | Number(009,0) | Não | Sequência |
| MatTra | String(030) | Sim | Matrícula do colaborador |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| IndSim | Number(001,0) | Sim | Indicador de Contribuição Substituída |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqElt
- SeqMct

---

## Índices

### R349MCTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
