# E120EPE

## Descrição

Vendas - Exclusões de Pedidos

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeEpe | Number(009,0) | Não | Identificador de exclusão de pedidos |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| CodRep | Number(009,0) | Não | Código do representante do pedido |
| PedPal | Number(008,0) | Sim | Número do pedido no Palmtop |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| UsuExc | Number(010,0) | Sim | Usuário responsável pela exclusão do pedido |
| DatExc | Date | Sim | Data da exclusão do pedido |
| HorExc | Number(005,0) | Sim | Hora da exclusão do pedido |
| ObsExc | String(100) | Sim | Observação da exclusão do registro |

---

## Chave Primária

- IdeEpe

---

## Índices

### E120EPEIndice1

**Tipo:** Não unico

Campos:
- CodRep

---

## Relacionamentos

### IR_E120EPE_004

**Tabela:** E090REP

| Origem | Destino |
|--------|---------|
| CodRep | CodRep |

