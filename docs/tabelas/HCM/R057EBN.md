# R057EBN

## Descrição

Tabela de Eventos do Benefício

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBnf | Number(002,0) | Não | Código do Benefício Entregue no Relógio |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Sim | Código do Evento do Benefício |

---

## Chave Primária

- CodBnf
- TabEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R057EBN_000

**Tabela:** R057BNF

| Origem | Destino |
|--------|---------|
| CodBnf | CodBnf |

