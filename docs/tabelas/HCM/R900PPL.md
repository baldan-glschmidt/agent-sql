# R900PPL

## Descrição

Usuários - People

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PERID | Number(010,0) | Não | Identificador do usuário |
| PERNAM | String(255) | Sim | Nome do usuário |
| PERFNM | String(255) | Sim | Campo usado na pesquisa de usuário por nome completo |
| PERDES | String(255) | Sim | Campo usado na pesquisa de usuário/grupo por apelido |
| UTLLGN | Date | Sim | Campo usado como filtro na pesquisa de usuário por nome ou apelido |
| PERDIS | String(001) | Sim | Indica se o usuário foi desabilitado ou não |
| PERDEL | String(001) | Sim | Indica se o usuário foi excluído ou não |

---

## Chave Primária

- PERID

---

## Índices

### R900PPLPERNAM

**Tipo:** Unico

Campos:
- PERNAM

---

## Relacionamentos

Nenhum relacionamento cadastrado.
