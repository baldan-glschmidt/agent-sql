# R350DPF

## Descrição

S-1210 - eSocial - Detalhamento dos pagamentos efetuados relativos a férias

---

## Resumo

- Campos: 13
- Chave Primária: 7 campo(s)
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
| CodCat | Number(004,0) | Sim | Código da categoria atribuída ao trabalhador |
| IniGoz | Date | Sim | Data de início do gozo das férias |
| QtdDia | Number(002,0) | Sim | Quantidade de dias de férias |
| ValLiq | Number(014,2) | Sim | Valor Líquido |
| PidExc | String(050) | Sim | Identificador da execução da pendência |
| MatTra | String(030) | Sim | Matrícula do colaborador |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqIpe
- SeqDpf

---

## Índices

### R350DPFIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
