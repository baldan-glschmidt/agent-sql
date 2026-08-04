# E059TVE

## Descrição

Tabelas - Tipos de Volume (Embalagens)

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTvl | Number(004,0) | Não | Código do tipo de volume |
| SeqTvl | Number(004,0) | Não | Sequência da embalagem no tipo de volume |
| CodEmb | Number(004,0) | Não | Código da embalagem |
| EmbMes | String(001) | Sim | Indicativo se a embalagem é considerada uma embalagem mestre |
| EmbNiv | Number(004,0) | Sim | Nível hierárquico superior da embalagem dentro do volume |
| EmbPri | String(001) | Sim | Indicativo se a embalagem é primária (contato com os produtos) |

---

## Chave Primária

- CodEmp
- CodTvl
- SeqTvl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
