# R350MSG

## Descrição

eSocial - Status de pendências - Mensagens

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PidExc | String(050) | Não | Identificador da pendência para execução |
| SeqMsg | Number(004,0) | Não | Sequência |
| CodMsg | String(010) | Sim | Código |
| LocMsg | String(250) | Sim | Local |
| TexMsg | String(5000) | Sim | Mensagem |
| NumEmp | Number(004,0) | Sim | Abrangência Empresa |
| TipMsg | Number(001,0) | Sim | Tipo da Mensagem |

---

## Chave Primária

- PidExc
- SeqMsg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
