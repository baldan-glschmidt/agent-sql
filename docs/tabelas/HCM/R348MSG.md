# R348MSG

## Descrição

eSocial - GRFGTS - Status das solicitações - Mensagens - obsoleta

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdePen | String(040) | Não | Identificador da solicitação |
| SeqMsg | Number(004,0) | Não | Sequência |
| CodMsg | String(010) | Sim | Código |
| LocMsg | String(250) | Sim | Local |
| TexMsg | String(5000) | Sim | Mensagem |
| TipMsg | Number(001,0) | Sim | Tipo da Mensagem |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| FilEmp | Number(006,0) | Sim | Código da Filial Empregadora |

---

## Chave Primária

- IdePen
- SeqMsg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
