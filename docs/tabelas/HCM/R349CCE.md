# R349CCE

## Descrição

S-5011 - eSocial - Códigos de Receita por Estabelecimento

---

## Resumo

- Campos: 11
- Chave Primária: 7 campo(s)
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
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCeo | Number(009,0) | Não | Sequência |
| SeqCce | Number(009,0) | Não | Sequência |
| CodRec | Number(006,0) | Sim | Código de Receita (CR) de contribs devidas à Prev Social e Outras Entidades |
| ValRec | Number(014,2) | Sim | Valor correspondente ao Código de Receita apurado |
| ValSus | Number(014,2) | Sim | Valor do tributo com exigibilidade suspensa |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- SeqTab
- SeqCeo
- SeqCce

---

## Índices

### R349CCEIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
