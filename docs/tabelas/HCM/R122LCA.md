# R122LCA

## Descrição

Lote de Candidatos - Participantes

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
| CodLot | Number(004,0) | Não | Código do Lote |
| NumCan | Number(007,0) | Não | Cadastro Candidato |

---

## Chave Primária

- CodLot
- NumCan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122LCA_000

**Tabela:** R122LOT

| Origem | Destino |
|--------|---------|
| CodLot | CodLot |

### IR_R122LCA_001

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

