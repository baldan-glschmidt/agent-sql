# E075CAT

## Descrição

Cadastros - Categoria

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCat | String(010) | Não | Código da Categoria vinculada a um produto |
| DesCat | String(040) | Não | Descrição usual da categoria |
| NivCat | Number(010,0) | Não | Número de Nível da Categoria na Estrutura |
| CatPai | String(010) | Sim | Categoria pai da categoria |
| ClaCat | String(250) | Não | Classificação da categoria |
| PosCat | Number(010,0) | Não | Quantidade de posições do nível da categoria |

---

## Chave Primária

- IdeUni

---

## Índices

### E075CATIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodCat

---

## Relacionamentos

Nenhum relacionamento cadastrado.
