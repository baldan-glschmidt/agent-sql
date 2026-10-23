# R234RCB

## Descrição

Evento - Recorrência Coffee Break

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| RecHor | Number(004,0) | Não | Recorrência do Horário |
| HorCbk | Number(005,0) | Não | Horário do Início do Coffee Break |
| CodCbk | Number(003,0) | Sim | Código do Tipo de Coffee Break |
| DesPro | String(500) | Sim | Providências |

---

## Chave Primária

- CodEvn
- RecHor
- HorCbk

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234RCB_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234RCB_001

**Tabela:** R234RHO

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |
| RecHor | RecHor |

### IR_R234RCB_003

**Tabela:** R133CBK

| Origem | Destino |
|--------|---------|
| CodCbk | CodCbk |

