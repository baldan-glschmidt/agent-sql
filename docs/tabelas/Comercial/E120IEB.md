# E120IEB

## Descrição

Vendas - Pedidos - Itens do Embarque

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| NumEbp | Number(004,0) | Não | Número do embarque do pedido |
| SeqIpd | Number(004,0) | Não | Sequência de item de produto do pedido ligado ao embarque |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- NumEbp
- SeqIpd

---

## Índices

### E120IEBIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- NumPed
- SeqIpd

---

## Relacionamentos

### IR_E120IEB_003

**Tabela:** E120EBP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| NumEbp | NumEbp |

### IR_E120IEB_004

**Tabela:** E120IPD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| SeqIpd | SeqIpd |

