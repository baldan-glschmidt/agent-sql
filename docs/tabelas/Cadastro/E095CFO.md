# E095CFO

## Descrição

Cadastros - Fornecedores - Características

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| CodCcl | String(003) | Não | Código da característica de fornecedor |
| SeqOrd | Number(002,0) | Não | Ordem preferencial da característica |
| CodCcc | Number(003,0) | Não | Código do componente da característica de fornecedor |

---

## Chave Primária

- CodFor
- CodCcl
- SeqOrd

---

## Índices

### E095CFOIndice1

**Tipo:** Não unico

Campos:
- CodCcl
- CodCcc

---

## Relacionamentos

### IR_E095CFO_000

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E095CFO_003

**Tabela:** E014CCC

| Origem | Destino |
|--------|---------|
| CodCcl | CodCcl |
| CodCcc | CodCcc |

