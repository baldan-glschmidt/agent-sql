# R082PQA

## Descrição

Perigo/Fator de Risco - Produtos Químicos

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| CodPro | Number(006,0) | Não | Código do Produto Químico |

---

## Chave Primária

- CodAgt
- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R082PQA_000

**Tabela:** R082AGT

| Origem | Destino |
|--------|---------|
| CodAgt | CodAgt |

### IR_R082PQA_001

**Tabela:** R082PRO

| Origem | Destino |
|--------|---------|
| CodPro | CodPro |

