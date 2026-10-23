# R066MSG

## Descrição

Mensagens de acerto

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatApu | Date | Não | Data da Apuração |
| DatMsg | Date | Não | Data da Mensagem |
| HorMsg | Number(005,0) | Não | Hora da Mensagem |
| CodUsu | Number(010,0) | Não | Código do Usuário |
| ObsPen | String(255) | Sim | Observação sobre a pendência |
| SeqMsg | Number(005,0) | Não | Sequência Mensagem |
| MsgVis | String(001) | Sim | Mensagem visualizada |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatApu
- DatMsg
- HorMsg
- SeqMsg
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
