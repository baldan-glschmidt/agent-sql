# E120PXS

## Descrição

Vendas - Pedidos - Ligação de Pedido X Pedidos - Serviços

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial do pedido normal |
| NumPed | Number(008,0) | Não | Número do pedido normal |
| SeqIsp | Number(003,0) | Não | Sequência de item do pedido normal |
| SeqPxs | Number(004,0) | Não | Sequência de ligações entre o pedido norma e pedidos de previsão |
| TipLig | Number(001,0) | Não | Tipo de ligação entre o Pedido |
| FilPdp | Number(005,0) | Não | Código da filial do pedido de  previsão |
| NumPdp | Number(008,0) | Não | Número do pedido de previsão |
| SeqPdp | Number(003,0) | Não | Sequência de item do pedido de previsão |
| QtdRem | Number(014,5) | Sim | Quantidade remetida (pedido previsão não explodido) |
| QtdAbt | Number(014,5) | Sim | Quantidade abatida (pedido previsão explodido) |
| QtdRet | Number(014,5) | Sim | Quantidade retornada para o pedido de previsão (cancelamentos) relativa a quantidade abatida do pedido de previsão |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| QtdRer | Number(014,5) | Sim | Quantidade retornada para o pedido de previsão (cancelamentos) relativa a quantidade remetida do pedido de previsão |
| EmpPdp | Number(004,0) | Não | Código da empresa do pedido de  previsão |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIsp
- SeqPxs

---

## Índices

### E120PXSIndice2

**Tipo:** Não unico

Campos:
- FilPdp
- CodEmp
- NumPdp
- SeqPdp

### E120PXSIndice3

**Tipo:** Não unico

Campos:
- EmpPdp
- FilPdp
- NumPdp
- SeqPdp

---

## Relacionamentos

### IR_E120PXS_003

**Tabela:** E120ISP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| SeqIsp | SeqIsp |

### IR_E120PXS_008

**Tabela:** E120ISP

| Origem | Destino |
|--------|---------|
| EmpPdp | CodEmp |
| FilPdp | CodFil |
| NumPdp | NumPed |
| SeqPdp | SeqIsp |

