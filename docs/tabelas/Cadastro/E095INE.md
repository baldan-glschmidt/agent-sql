# E095INE

## Descrição

Cadastros - Fornecedores - Inscrição Estadual

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| SigUfs | String(002) | Não | Estado do fornecedor |
| InsEst | String(025) | Não | Inscrição estadual do fornecedor |

---

## Chave Primária

- CodFor
- SigUfs

---

## Índices

### E095INEIndice1

**Tipo:** Não unico

Campos:
- SigUfs

---

## Relacionamentos

### IR_E095INE_000

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E095INE_001

**Tabela:** E007UFS

| Origem | Destino |
|--------|---------|
| SigUfs | SigUfs |

