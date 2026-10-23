# R104LPR

## Descrição

JR - Ações do Lote

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodLot | Number(004,0) | Não | Código do Lote |
| CodPrc | Number(007,0) | Não | Código da Ação |

---

## Chave Primária

- NumEmp
- CodLot
- CodPrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104LPR_001

**Tabela:** R104LOT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodLot | CodLot |

### IR_R104LPR_002

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

