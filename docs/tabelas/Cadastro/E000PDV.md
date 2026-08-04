# E000PDV

## Descrição

Tabelas - Integrações - Parâmetros PDV

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
| IdeUni | Number(009,0) | Não | Identificador Único do Parâmetro |
| IdeInt | Number(009,0) | Não | Código Identificador do tipo de informação |
| IdeReg | Number(009,0) | Não | Identificador de registro |
| ChaPdv | String(250) | Não | Chave do parâmetro para o PDV |
| VlrPdv | String(250) | Sim | Valor do parâmetro para o PDV |
| DesPdv | String(1000) | Sim | Descrição do parâmetro para o PDV |

---

## Chave Primária

- IdeUni

---

## Índices

### E000PDVIndice1

**Tipo:** Unico

Campos:
- ChaPdv
- IdeReg
- IdeInt

### E000PDVIndice2

**Tipo:** Não unico

Campos:
- IdeInt
- IdeReg

---

## Relacionamentos

Nenhum relacionamento cadastrado.
