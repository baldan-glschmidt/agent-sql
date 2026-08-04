# E099TTM

## Descrição

Cadastros - Usuários - Dados de login com TTM da TAN

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodUsu | Number(010,0) | Não | Código do Usuário |
| CodAec | Number(004,0) | Não | Código do autenticador externo de crédito de clientes |
| UsrTtm | String(050) | Sim | Usuário TTM no autenticador externo de crédito TAN |
| SenTtm | String(050) | Sim | Senha do usuário TTM no autenticador externo de crédito TAN |

---

## Chave Primária

- CodEmp
- CodUsu
- CodAec
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
