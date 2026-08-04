# E120EEB

## Descrição

Vendas - Pedidos - Embalagens para Embarque

---

## Resumo

- Campos: 6
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
| SeqIpd | Number(004,0) | Não | Sequência de item de produto do pedido |
| NumEmb | String(030) | Não | Número da embalagem de estocagem onde estão embalados os componentes do item de pedido |
| SitEmb | Number(001,0) | Sim | Situação da Embalagem |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIpd
- NumEmb

---

## Índices

### E120EEBIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- NumEmb

---

## Relacionamentos

### IR_E120EEB_003

**Tabela:** E120IPD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| SeqIpd | SeqIpd |

### IR_E120EEB_004

**Tabela:** E210EMB

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| NumEmb | NumEmb |

