# R999ASD

## Descrição

Configuração assinatura digital

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
| CodUsu | Number(010,0) | Não | Codigo de usuário |
| CodMod | String(011) | Não | Nome do modelo |
| AssTip | String(005) | Não | Tipo do arquivo que será assinado (PDF, XML, DOCX) |
| DatSeq | Number(002,0) | Não | Sequência de registros |
| Dat1 | String(254) | Sim | Dados 1 |
| Dat2 | String(254) | Sim | Dados 2 |

---

## Chave Primária

- CodUsu
- CodMod
- AssTip
- DatSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
