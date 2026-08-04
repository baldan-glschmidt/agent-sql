# E120PPD

## Descrição

Vendas - Pedidos - Itens de Produto - Complementar

---

## Resumo

- Campos: 20
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
| SeqIpd | Number(004,0) | Não | Sequência de item do pedido |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| VdiFcp | Number(015,2) | Sim | Valor diferido do ICMS relativo ao FCP |
| EfiFcp | Number(015,2) | Sim | Valor efetivo do ICMS relativo ao FCP |
| QtmBic | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico |
| VmoIcm | Number(015,2) | Sim | Valor do ICMS Monofásico |
| AliImo | Number(007,4) | Sim | Alíquota ad rem ICMS Monofásico |
| QtmBir | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Retido |
| VmoIcr | Number(015,2) | Sim | Valor do ICMS Monofásico Retido |
| AliImr | Number(007,4) | Sim | Alíquota ad rem ICMS Monofásico Retido |
| QtmBif | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Diferido |
| VmoIcf | Number(015,2) | Sim | Valor do ICMS Monofásico Diferido |
| AliImf | Number(007,4) | Sim | Percentual de Diferimento do ICMS Monofásico |
| QtmBid | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Destacado |
| VmoIcd | Number(015,2) | Sim | Valor do ICMS Monofásico Destacado |
| AliImd | Number(007,4) | Sim | Alíquota ad rem ICMS Monofásico Destacado |
| AliMor | Number(007,4) | Sim | Alíquota ad rem ICMS Monofásico Original |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIpd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120PPD_003

**Tabela:** E120IPD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| SeqIpd | SeqIpd |

