# R350DRE

## Descrição

S-2299 - eSocial - Informações de desconto do empréstimo em folha

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
| SeqDes | Number(009,0) | Não | Sequência |
| SeqRec | Number(009,0) | Não | Sequência |
| SeqDlt | Number(009,0) | Não | Sequência |
| SeqDru | Number(009,0) | Não | Sequência |
| SeqDre | Number(009,0) | Não | Sequência |
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
- SeqDes
- SeqRec
- SeqDlt
- SeqDru
- SeqDre

---

## Índices

### R350DREIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
