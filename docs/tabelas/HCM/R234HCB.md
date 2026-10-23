# R234HCB

## Descrição

Evento - Horário Coffee Break

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| DatIni | Date | Não | Data Inicial do Horário |
| HorIni | Number(005,0) | Não | Hora Inicial do horário |
| HorCbk | Number(005,0) | Não | Horário do Início do Coffee Break |
| CodCbk | Number(003,0) | Sim | Código do Tipo de Coffee Break |
| DesPro | String(500) | Sim | Providências |

---

## Chave Primária

- CodEvn
- DatIni
- HorIni
- HorCbk

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234HCB_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234HCB_004

**Tabela:** R133CBK

| Origem | Destino |
|--------|---------|
| CodCbk | CodCbk |

