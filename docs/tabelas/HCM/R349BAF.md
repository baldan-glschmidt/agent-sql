# R349BAF

## Descrição

S-5003 - eSocial - Bases de cálculo e valores do FGTS em períodos anteriores

---

## Resumo

- Campos: 13
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
| SeqEoc | Number(009,0) | Não | Sequência Identificação do Estabelecimento |
| SeqIlt | Number(009,0) | Não | Sequência Identificação da Lotação |
| SeqItf | Number(009,0) | Não | Sequência Matrícula e Categoria do Trabalhador |
| SeqBaf | Number(009,0) | Não | Sequência da informação das bases e valores em períodos anteriores |
| PerRef | Date | Sim | Período ao qual se refere a remuneração |
| TipIns | String(001) | Sim | Tipo do instrumento ou situação ensejadora da remuneração |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqEoc
- SeqIlt
- SeqItf
- SeqBaf

---

## Índices

### R349BAFIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
