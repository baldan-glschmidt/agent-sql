# R349FDT

## Descrição

S-5003 - eSocial - Matrícula e Categoria do Trabalhador por Depósitos de FGTS

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
| SeqFdt | Number(009,0) | Não | Sequência Matrícula e Categoria do Trabalhador |
| MatTra | String(030) | Sim | Matrícula do colaborador |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
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

---

## Índices

### R349FDTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
