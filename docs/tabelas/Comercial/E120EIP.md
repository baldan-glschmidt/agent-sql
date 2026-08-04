# E120EIP

## Descrição

Vendas - Exclusões de Itens de Produto

---

## Resumo

- Campos: 17
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeEip | Number(009,0) | Não | Identificador de exclusão de item de pedido |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqIpd | Number(004,0) | Não | Sequência de item do pedido |
| CodRep | Number(009,0) | Não | Código do representante do pedido |
| PedPal | Number(008,0) | Sim | Número do pedido no Palmtop |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| CodPro | String(014) | Sim | Código do produto do pedido |
| CodDer | String(007) | Sim | Código da derivação do produto do pedido |
| QtdPed | Number(014,5) | Sim | Quantidade do produto do pedido |
| CodCli | Number(009,0) | Sim | Código do cliente do pedido |
| DatEmi | Date | Sim | Data de emissão do pedido |
| UsuExc | Number(010,0) | Sim | Usuário responsável pela exclusão do pedido |
| DatExc | Date | Sim | Data da exclusão do pedido |
| HorExc | Number(005,0) | Sim | Hora da exclusão do pedido |
| ObsExc | String(100) | Sim | Observação da exclusão do item |

---

## Chave Primária

- IdeEip

---

## Índices

### E120EIPIndice1

**Tipo:** Não unico

Campos:
- CodRep

---

## Relacionamentos

### IR_E120EIP_005

**Tabela:** E090REP

| Origem | Destino |
|--------|---------|
| CodRep | CodRep |

