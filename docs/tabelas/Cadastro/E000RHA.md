# E000RHA

## Descrição

Tabelas - Integrações - Retorno da persistência por HASH para o sistema integrador

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
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodInt | Number(002,0) | Sim | Código da integração |
| IdeInt | Number(009,0) | Não | Código Identificador do tipo de informação |
| CodHas | String(050) | Sim | Código da hash da requisição |
| TipRet | Number(001,0) | Sim | Tipo de retorno |
| RetReq | Image | Sim | JSON de retorno da requisição |

---

## Chave Primária

- IdeUni

---

## Índices

### E000RHAIndice

**Tipo:** Unico

Campos:
- CodInt
- IdeInt
- CodHas

---

## Relacionamentos

Nenhum relacionamento cadastrado.
