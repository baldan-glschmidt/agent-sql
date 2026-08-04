# E120NRR

## Descrição

Vendas - Pedidos - Nota referenciada de reembolso da NFS-e

---

## Resumo

- Campos: 16
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
| SeqNrr | Number(003,0) | Não | Sequência da nota fiscal referenciada |
| ChvDoe | String(050) | Sim | Chave do documento eletrônico |
| DatEmi | Date | Sim | Data da emissão da nota fiscal referenciada |
| DatCmp | Date | Sim | Data da competência da nota fiscal referenciada |
| CodFor | Number(009,0) | Sim | Código do fornecedor do documento referenciado |
| RaiDfe | Number(007,0) | Sim | Código do município emissor do documento fiscal que não se encontra no repositório nacional |
| TipNre | Number(001,0) | Sim | Tipo de Nota de Reembolso |
| TipChd | Number(001,0) | Sim | Tipo da Chave do DFe |
| NumNre | String(255) | Sim | Número do documento de reembolso |
| DesNre | String(255) | Sim | Descrição do documento de reembolso |
| TipRee | Number(002,0) | Sim | Tipo de reembolso |
| DesRee | String(150) | Sim | Descrição do reembolso |
| VlrRee | Number(015,2) | Sim | Valor do reembolso |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqNrr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120NRR_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

