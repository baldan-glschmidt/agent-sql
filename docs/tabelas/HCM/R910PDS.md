# R910PDS

## Descrição

Políticas de duração de senhas (só para consultas)

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPol | Number(010,0) | Não | Código da política. |
| DesPol | String(127) | Não | Descrição da política. |
| PerAlt | Number(001,0) | Não | 0=O usuário não pode alterar sua senha. 1=O usuário pode alterar sua senha. |
| MxDias | Number(005,0) | Sim | Quantidade máxima de dias de duração de uma senha. 0=A senha nunca expira. |
| MnDias | Number(005,0) | Sim | Quantidade mínima de dias de duração de uma senha. |

---

## Chave Primária

- CodPol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
