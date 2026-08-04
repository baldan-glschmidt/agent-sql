# E000INP

## Descrição

Insight Control - Ligação Insights X Papéis

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| HasHid | String(050) | Não | Hash da mensagem conforme Insight Control |
| IdePap | Number(009,0) | Não | Identificador de registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E000INPIndice1

**Tipo:** Unico

Campos:
- CodEmp
- HasHid
- IdePap

---

## Relacionamentos

Nenhum relacionamento cadastrado.
