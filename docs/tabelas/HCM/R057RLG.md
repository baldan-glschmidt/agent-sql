# R057RLG

## Descrição

Relógios Benefícios

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| CodBnf | Number(002,0) | Sim | Código do Benefício Entregue no Coletor |

---

## Chave Primária

- CodPlt
- CodRlg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R057RLG_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R057RLG_001

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

### IR_R057RLG_002

**Tabela:** R057BNF

| Origem | Destino |
|--------|---------|
| CodBnf | CodBnf |

