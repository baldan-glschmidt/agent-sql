# R950CTM

## Descrição

Mobile - Configuração dos tokens

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTkn | String(120) | Não | Token identificador do processo mobile |
| IdApp | Number(004,0) | Não | Identificador do aplicativo |
| UsrTkn | String(255) | Sim | Usuário do token |
| PwdTkn | String(255) | Sim | Senha do usuário |
| DatTkn | Date | Sim | Data e hora da última consulta |
| TimTkn | Number(005,0) | Sim | Hora da última consulta |

---

## Chave Primária

- CodTkn

---

## Índices

### R950CTMINDIDAPP

**Tipo:** Não unico

Campos:
- IdApp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
