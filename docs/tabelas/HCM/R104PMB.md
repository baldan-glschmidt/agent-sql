# R104PMB

## Descrição

JR - Pedidos - Motivos - Base

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMtj | Number(003,0) | Não | Código do motivo do pedido |
| PedBas | Number(003,0) | Não | Código do motivo do pedido |
| OpeBas | String(001) | Sim | Operação |

---

## Chave Primária

- CodMtj
- PedBas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104PMB_000

**Tabela:** R104MTJ

| Origem | Destino |
|--------|---------|
| CodMtj | CodMtj |

### IR_R104PMB_001

**Tabela:** R104MTJ

| Origem | Destino |
|--------|---------|
| PedBas | CodMtj |

