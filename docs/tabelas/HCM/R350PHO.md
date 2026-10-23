# R350PHO

## Descrição

eSocial - Pendência da Geração de Horários

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PidPen | String(025) | Não | Identificador sequencial da pendência |
| NumEmp | Number(004,0) | Sim | Empresa |
| DatHor | Number(014,6) | Sim | Data e Hora de geração da pendência |
| TabPen | String(007) | Sim | Tabela do sistema que originou a pendência. |
| OpePen | String(001) | Sim | Operação que originou a pendência (I,A,E) |
| UsuPen | Number(010,0) | Sim | Usuário que originou a pendência |
| VlrPen | String(2000) | Sim | Dados da pendência |
| VlrPe2 | String(2000) | Sim | Dados da pendência |
| OriPen | String(060) | Sim | Origem da Pendência |

---

## Chave Primária

- PidPen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
