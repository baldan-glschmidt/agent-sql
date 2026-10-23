# R349IPB

## Descrição

S-5001 - eSocial - Informações sobre bases de cálculo do PIS/PASEP

---

## Resumo

- Campos: 13
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
| SeqIpp | Number(009,0) | Não | Sequência Bases do PIS/PASEP |
| SeqIcp | Number(009,0) | Não | Sequência Matrícula e Categoria do Trabalhador |
| SeqIpb | Number(009,0) | Não | Sequência |
| Ind13s | Number(001,0) | Sim | Indicativo Folha |
| TipVal | Number(002,0) | Sim | Tipo de valor |
| ValBas | Number(014,2) | Sim | Valor da base de cálculo, dedução ou desconto da contribuição social |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqIpp
- SeqIcp
- SeqIpb

---

## Índices

### R349IPBIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
