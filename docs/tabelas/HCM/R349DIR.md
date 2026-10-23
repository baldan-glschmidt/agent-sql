# R349DIR

## Descrição

S-5001 - eSocial - Detalhamento das informações de remuneração por período de referência

---

## Resumo

- Campos: 14
- Chave Primária: 10 campo(s)
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
| SeqIrp | Number(009,0) | Não | Sequência |
| SeqDir | Number(009,0) | Não | Sequência |
| Ind13s | Number(001,0) | Sim | Indicativo de 13° salário |
| TipVal | Number(002,0) | Sim | Tipo de valor que influi na apuração da contribuição devida |
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
- SeqElt
- SeqMct
- SeqIrp
- SeqDir

---

## Índices

### R349DIRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
