# E075GFE

## Descrição

Tabelas - Integrações - Grupo Fiscal Produto x UF - Compra

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeGfe | Number(009,0) | Não | Identificador do grupo fiscal |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto |
| CodFor | Number(009,0) | Não | Código do Fornecedor |

---

## Chave Primária

- IdeUni

---

## Índices

### E075UGFEIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodPro
- CodFor

### E075GFEIndice2

**Tipo:** Não unico

Campos:
- IdeGfe

---

## Relacionamentos

Nenhum relacionamento cadastrado.
