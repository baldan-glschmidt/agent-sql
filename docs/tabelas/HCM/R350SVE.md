# R350SVE

## Descrição

S-2399 - eSocial - Informações de desconto do empréstimo em folha

---

## Resumo

- Campos: 15
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqRsv | Number(009,0) | Não | Sequência |
| SeqPsv | Number(009,0) | Não | Sequência |
| SeqSvl | Number(009,0) | Não | Sequência |
| SeqSvr | Number(009,0) | Não | Sequência |
| SeqSve | Number(009,0) | Não | Sequência |
| TpDesc | Number(001,0) | Sim | Indicativo do tipo de desconto |
| InsFin | String(003) | Sim | Instituição Financeira |
| NroDoc | String(015) | Sim | Número Contrato |
| NumCtr | String(050) | Sim | Número do contrato alfanumérico |
| ObsErv | String(255) | Sim | Observação |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqRsv
- SeqPsv
- SeqSvl
- SeqSvr
- SeqSve

---

## Índices

### R350SVEIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
