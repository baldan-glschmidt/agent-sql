# E070RIG

## Descrição

Parâmetros do Recebimento Eletrônico - Relacionamento entre Itens e Grupos

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeIre | Number(009,0) | Não | Identificador do item de recebimento eletrônico |
| IdeGre | Number(009,0) | Não | Identificador do grupo de campos de recebimento eletrônico |
| SitReg | String(001) | Não | Situação do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E070RIGIndice1

**Tipo:** Unico

Campos:
- IdeIre
- IdeGre

### E070RIGIndice2

**Tipo:** Não unico

Campos:
- IdeGre

---

## Relacionamentos

### IR_E070RIG_001

**Tabela:** E070IRE

| Origem | Destino |
|--------|---------|
| IdeIre | IdeUni |

### IR_E070RIG_002

**Tabela:** E070GRE

| Origem | Destino |
|--------|---------|
| IdeGre | IdeUni |

