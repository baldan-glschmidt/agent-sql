# R104BHV

## Descrição

JR - Base Histórico de Valores - Cenário

---

## Resumo

- Campos: 11
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
| CmpHis | Date | Não | Competência de referência do histórico |
| CodMtj | Number(003,0) | Não | Código do Motivo do Pedido |
| VlrBas | Number(011,2) | Sim | Valor da Base |
| VlrHis | Number(011,2) | Sim | Valor histórico ou de refefência |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen
- EmpAut
- TipCol
- NumCad
- CmpHis
- CodMtj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104BHV_003

**Tabela:** R104PDC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |

### IR_R104BHV_008

**Tabela:** R104MTJ

| Origem | Destino |
|--------|---------|
| CodMtj | CodMtj |

