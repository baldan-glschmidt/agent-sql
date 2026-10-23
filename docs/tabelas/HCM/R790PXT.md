# R790PXT

## Descrição

Parâmetros do HCM XT

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de Registro |
| CodUsu | Number(009,0) | Sim | Código do usuário |
| ChvExt | String(200) | Sim | chave HCM XT |
| VlrExt | String(4000) | Sim | Valor HCM XT |

---

## Chave Primária

- IdeUni

---

## Índices

### R790PXTIndice1

**Tipo:** Não unico

Campos:
- ChvExt

### R790PXTIndice2

**Tipo:** Não unico

Campos:
- CodUsu
- ChvExt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
