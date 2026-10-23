# R349FBT

## Descrição

S-5003 - eSocial - Bases de FGTS no Período de Apuração

---

## Resumo

- Campos: 12
- Chave Primária: 9 campo(s)
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
| SeqFbt | Number(009,0) | Não | Sequência das Bases no Período de Apuração |
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
- SeqFbt

---

## Índices

### R349FBTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
