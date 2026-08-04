# E120DER

## Descrição

Vendas - Pedidos - Deduções e Reduções IBS/CBS

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqDer | Number(003,0) | Não | Sequência da dedução/redução |
| TipDer | Number(002,0) | Não | Tipo da dedução/redução |
| DesDer | String(150) | Sim | Descrição da dedução/redução |
| VlrDer | Number(015,2) | Não | Valor da dedução/redução |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqDer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120DER_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

