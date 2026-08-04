# E120DLS

## Descrição

Vendas - Pedidos - Entrada, Vencimento, Lote, Série

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqIpd | Number(004,0) | Não | Sequência de item do pedido |
| SeqDls | Number(006,0) | Não | Sequência de movimento de item |
| CodDep | String(010) | Sim | Código do depósito |
| DatEnt | Date | Sim | Data da entrada do produto no depósito |
| DatVlt | Date | Sim | Data de validade do produto no depósito |
| CodLot | String(050) | Sim | Código do Lote de Fabricação para estocagem |
| NumSep | String(050) | Sim | Número de série do produto |
| QtdEst | Number(014,5) | Sim | Quantidade a ser movimentada do estoque |
| ObsDls | String(250) | Sim | Texto da observação |
| QtdPed | Number(014,5) | Sim | Quantidade pedida do lote do item de pedido |
| DatFab | Date | Sim | Data de fabricação do lote |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIpd
- SeqDls

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120DLS_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

### IR_E120DLS_003

**Tabela:** E120IPD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| SeqIpd | SeqIpd |

