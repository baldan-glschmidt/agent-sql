# R349FAB

## Descrição

S-5003 - eSocial - Bases de FGTS em Períodos Anteriores

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
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqFel | Number(009,0) | Não | Sequência Identificação do Estabelecimento |
| SeqFit | Number(009,0) | Não | Sequência Matrícula e Categoria do Trabalhador |
| PerRef | Date | Não | Período ao qual se refere a remuneração |
| TipIns | String(001) | Não | Tipo do instrumento ou situação ensejadora da remuneração |
| SeqFab | Number(009,0) | Não | Sequência das Bases em Períodos Anteriores |
| TipBas | Number(002,0) | Sim | Tipo Base FGTS |
| ValBas | Number(014,2) | Sim | Valor da base de cálculo do FGTS |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqFel
- SeqFit
- PerRef
- TipIns
- SeqFab

---

## Índices

### R349FABIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
