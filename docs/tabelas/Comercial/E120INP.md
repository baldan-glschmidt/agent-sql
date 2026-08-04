# E120INP

## Descrição

Vendas - Pedidos - Indicadores de negócio

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificação única do registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqIpd | Number(004,0) | Não | Sequência de item do pedido |
| CodCli | Number(009,0) | Não | Código do cliente indicador do negócio |

---

## Chave Primária

- IdeUni

---

## Índices

### E120INPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- NumPed
- SeqIpd

---

## Relacionamentos

### IR_E120INP_004

**Tabela:** E120IPD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| SeqIpd | SeqIpd |

