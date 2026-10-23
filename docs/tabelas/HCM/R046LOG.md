# R046LOG

## Descrição

Log de alterações do controle de pagamentos

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CmpPag | Date | Não | Competência |
| SeqPag | Number(002,0) | Não | Sequência |
| SeqLog | Number(002,0) | Não | Sequência |
| DatLog | Number(014,6) | Sim | Data e hora da alteração |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| MotAlt | String(255) | Sim | Motivo da alteração |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpPag
- SeqPag
- SeqLog

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
