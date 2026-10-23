# R350IHC

## Descrição

S-2200 - eSocial - Informações diárias do horário contratual

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
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
| SeqAdm | Number(009,0) | Não | Sequência |
| SeqIhc | Number(009,0) | Não | Sequência |
| CodDia | Number(001,0) | Sim | Código relativo ao dia |
| CodHor | String(030) | Sim | Código do Horário Contratual |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqAdm
- SeqIhc

---

## Índices

### R350IHCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
