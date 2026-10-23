# R104PDI

## Descrição

JR - Pedidos - Cenário

---

## Resumo

- Campos: 20
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| DatCen | Date | Não | Data do cenário |
| SeqCen | Number(002,0) | Não | Sequência do cenário |
| EmpAut | Number(004,0) | Não | Empresa do autor |
| TipCol | Number(001,0) | Não | Tipo do colaborador autor |
| NumCad | Number(009,0) | Não | Código do colaborador autor |
| CodMtj | Number(003,0) | Não | Código do Motivo |
| SeqPed | Number(002,0) | Não | Sequência do pedido |
| DatIni | Date | Sim | Data de início do direito |
| DatFim | Date | Sim | Data de término do direito |
| VlrRec | Number(011,2) | Sim | Valor Reclamado |
| VlrPro | Number(011,2) | Sim | Valor Provável |
| VlrPos | Number(011,2) | Sim | Valor Possível |
| VlrRem | Number(011,2) | Sim | Valor Remoto |
| PedPro | String(001) | Sim | Pedido Procedente |
| PerCha | Number(003,0) | Sim | Percentual de chance de êxito na visão da empresa |
| ObsPed | String(250) | Sim | Observação sobre o pedido |
| VlrAco | Number(011,2) | Sim | Valor do Acordo da sentença de execução |
| ConPed | Number(001,0) | Sim | Define se o item será calculado ou não |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen
- EmpAut
- TipCol
- NumCad
- CodMtj
- SeqPed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104PDI_003

**Tabela:** R104PDC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |

### IR_R104PDI_007

**Tabela:** R104MTJ

| Origem | Destino |
|--------|---------|
| CodMtj | CodMtj |

