# R260USU

## Descrição

Controle de usuários

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodUsu | Number(010,0) | Não | Código do Usuário |
| NomCmp | String(020) | Não | Nome do computador |
| SessID | Number(014,0) | Não | Sessão de conexão banco de dados |
| DatLog | Date | Sim | Data do logon do usuário no sistema |
| HorLog | Number(005,0) | Sim | Hora do logon do usuário no sistema |
| NomFrm | String(020) | Sim | Nome da Form ou tabela |
| CodMod | Number(002,0) | Não | Código do módulo acessado |
| QtdUsu | Number(004,0) | Sim | Quantidade de Usuários |

---

## Chave Primária

- CodUsu
- NomCmp
- SessID
- CodMod

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
