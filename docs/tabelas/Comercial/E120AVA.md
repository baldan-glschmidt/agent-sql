# E120AVA

## Descrição

Vendas - Pedidos - Avalistas

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqAva | Number(008,0) | Não | Sequência dos avalistas |
| CodAva | Number(009,0) | Não | Código do Avalista |
| VlrFin | Number(015,2) | Sim | Valor líquido do pedido para o financeiro |
| ObsPed | String(250) | Sim | Texto da observação do pedido |
| ObsAva | String(250) | Sim | Texto do avalista |
| SitAva | String(001) | Sim | Situação da observação |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqAva

---

## Índices

### E120AVAIndice1

**Tipo:** Não unico

Campos:
- CodAva

---

## Relacionamentos

### IR_E120AVA_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

### IR_E120AVA_004

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodAva | CodCli |

