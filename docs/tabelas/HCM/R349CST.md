# R349CST

## Descrição

S-5001 - eSocial - Cálculo das contribuições sociais devidas a Outras Entidades e Fundos

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
| SeqElt | Number(009,0) | Não | Sequência |
| SeqMct | Number(009,0) | Não | Sequência |
| SeqCst | Number(009,0) | Não | Sequência |
| CodRec | Number(006,0) | Sim | Código de Receita (CR) da contribuição descontada do trabalhador |
| ValCon | Number(014,2) | Sim | Valor da contribuição social devida a Outras Entidades ou Fundos |
| ValDes | Number(014,2) | Sim | Valor efetivamente descontado do segurado |
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
- SeqCst

---

## Índices

### R349CSTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
