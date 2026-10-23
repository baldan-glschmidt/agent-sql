# R350RAF

## Descrição

S-1210 - eSocial - Detalhamento das rubricas do recibo antecipado de férias

---

## Resumo

- Campos: 15
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqIpe | Number(009,0) | Não | Sequência |
| SeqDpf | Number(009,0) | Não | Sequência |
| SeqRaf | Number(009,0) | Não | Sequência |
| CodRub | String(030) | Sim | Código que identifica a rubrica na folha de pagamento |
| TabRub | String(008) | Sim | Tabela de Rubrica |
| QtdRef | Number(014,2) | Sim | Quantidade de referência para apuração |
| FatRub | Number(005,2) | Sim | Fator, percentual, etc, da rubrica |
| ValUni | Number(014,2) | Sim | Valor unitário da rubrica |
| ValRub | Number(014,2) | Sim | Valor da rubrica |
| PidExc | String(050) | Sim | Identificador da execução da pendência |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqIpe
- SeqDpf
- SeqRaf

---

## Índices

### R350RAFIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
