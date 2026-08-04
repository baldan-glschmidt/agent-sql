# E000ATX

## Descrição

Tabelas - Autotextos

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| AplAtx | String(004) | Não | Código da aplicação do autotexto |
| CodAtx | Number(010,0) | Não | Código do autotexto |
| DesAtx | String(250) | Não | Descrição do autotexto |
| SitAtx | String(001) | Não | Situação do autotexto |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora/minuto da última alteração do registro |

---

## Chave Primária

- CodEmp
- AplAtx
- CodAtx

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
