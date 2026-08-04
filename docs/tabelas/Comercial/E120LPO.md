# E120LPO

## Descrição

Vendas - Pedidos - Ligação de Pedido X Ordens Compra

---

## Resumo

- Campos: 11
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqIpd | Number(004,0) | Não | Sequência de item do pedido |
| EmpOcp | Number(004,0) | Não | Código da empresa da Ordem de Compra |
| FilOcp | Number(005,0) | Não | Código da filial da Ordem de Compra |
| NumOcp | Number(008,0) | Não | Número da ordem de compra |
| SeqIpo | Number(004,0) | Não | Sequência do item de produto |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do pedido |
| DatGer | Date | Sim | Data da geração do pedido |
| HorGer | Number(005,0) | Sim | Hora da geração do pedido |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIpd
- EmpOcp
- FilOcp
- NumOcp
- SeqIpo

---

## Índices

### E120LPOIndice1

**Tipo:** Não unico

Campos:
- EmpOcp
- FilOcp
- NumOcp
- SeqIpo

---

## Relacionamentos

### IR_E120LPO_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

### IR_E120LPO_003

**Tabela:** E120IPD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| SeqIpd | SeqIpd |

### IR_E120LPO_007

**Tabela:** E420IPO

| Origem | Destino |
|--------|---------|
| EmpOcp | CodEmp |
| FilOcp | CodFil |
| NumOcp | NumOcp |
| SeqIpo | SeqIpo |

