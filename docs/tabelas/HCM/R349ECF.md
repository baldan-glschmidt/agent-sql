# R349ECF

## Descrição

S-5003 - eSocial - Informações relativas ao desconto do eConsignado

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqEoc | Number(009,0) | Não | Sequência Identificação do Estabelecimento |
| SeqIlt | Number(009,0) | Não | Sequência Identificação da Lotação |
| SeqItf | Number(009,0) | Não | Sequência Matrícula e Categoria do Trabalhador |
| SeqEcf | Number(009,0) | Não | Sequência identificação eConsignado |
| InsFin | String(003) | Sim | Instituição financeira |
| NrCont | String(015) | Sim | Número do contrato |
| VreCon | Number(014,2) | Sim | Valor do desconto do empréstimo eConsignado |
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
- SeqEcf

---

## Índices

### R349ECFIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
