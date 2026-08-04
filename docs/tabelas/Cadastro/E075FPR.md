# E075FPR

## Descrição

Cadastros - Ligação entre a empresa e o produto produzido por filial

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeOfc | Number(009,0) | Não | Identificador do registro de origem por empresa |
| IdeOpr | Number(009,0) | Não | Identificador do registro de origem dos produtos produzidos |
| CodFil | Number(005,0) | Não | Código da filial |

---

## Chave Primária

- IdeOfc
- IdeOpr
- CodFil

---

## Índices

### E075FPRIndice1

**Tipo:** Não unico

Campos:
- IdeOfc

### E075FPRIndice2

**Tipo:** Não unico

Campos:
- IdeOpr

---

## Relacionamentos

### IR_E075FPR_000

**Tabela:** E075OFC

| Origem | Destino |
|--------|---------|
| IdeOfc | IdeUni |

### IR_E075FPR_001

**Tabela:** E075OPR

| Origem | Destino |
|--------|---------|
| IdeOpr | IdeUni |

