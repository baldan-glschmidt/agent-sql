# E120ISA

## Descrição

Vendas - Pedidos - Alterações dos Itens de Serviço

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqIsp | Number(003,0) | Não | Sequência de item do serviço |
| DatAlt | Date | Não | Data da alteração do item |
| QtdVen | Number(013,5) | Sim | Quantidade aumentada do item |
| VlrVen | Number(015,2) | Sim | Valor aumentado do item |
| QtdCan | Number(013,5) | Sim | Quantidade cancelada do item |
| VlrCan | Number(015,2) | Sim | Valor cancelado do item |
| IndSig | String(001) | Não | Indicativo se o registro está lançado no SIG |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIsp
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120ISA_003

**Tabela:** E120ISP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| SeqIsp | SeqIsp |

