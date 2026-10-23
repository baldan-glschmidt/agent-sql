# R349BPA

## Descrição

S-5003 - eSocial - Bases de cálculo e valores do FGTS

---

## Resumo

- Campos: 15
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
| SeqBpa | Number(009,0) | Não | Sequência das Bases no Período de Apuração |
| TipVal | Number(002,0) | Sim | Tipo de valor que influi na apuração do FGTS |
| IndInc | Number(001,0) | Sim | Indicativo de incidência de FGTS |
| ValBas | Number(014,2) | Sim | Remuneração (valor da base de cálculo) do FGTS |
| ValHis | Number(014,2) | Sim | Valor histórico do FGTS a ser depositado na conta vinculada do trabalhador |
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
- SeqBpa

---

## Índices

### R349BPAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
