# R996REL

## Descrição

Relacionamentos do usuário

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| RELNAM | String(032) | Não | Nome do relacionamento |
| FORTBL | String(032) | Não | Tabela que foi relacionada |
| REFTBL | String(032) | Não | Tabela usada como referência |
| RELTYP | Number(005,0) | Não | Tipo de relacionamento |
| ORINAM | String(032) | Sim | Nome original, caso o relacionamento seja renomeado |
| CODUSU | Number(010,0) | Sim | Código do último usuário que efetuou alguma alteração |
| LASUPD | Date | Sim | Data da última alteração |
| ObjSis | String(001) | Sim | Identifica se o relacionamento é de sistema ou usuário |

---

## Chave Primária

- RELNAM

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
