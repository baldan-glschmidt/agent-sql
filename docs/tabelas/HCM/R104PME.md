# R104PME

## Descrição

JR - Pedidos - Motivos - Eventos

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
| CodMtj | Number(003,0) | Não | Código do motivo do pedido |
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |

---

## Chave Primária

- CodMtj
- CodTab
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104PME_000

**Tabela:** R104MTJ

| Origem | Destino |
|--------|---------|
| CodMtj | CodMtj |

### IR_R104PME_002

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

