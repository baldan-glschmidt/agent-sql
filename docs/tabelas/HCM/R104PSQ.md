# R104PSQ

## Descrição

JR - Pedidos - Sequência de Cálculo - Cenário

---

## Resumo

- Campos: 9
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
| SeqCal | Number(003,0) | Não | Sequência de cálculo do pedido |
| CodMtj | Number(003,0) | Não | Código do Motivo |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen
- EmpAut
- TipCol
- NumCad
- SeqCal
- CodMtj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104PSQ_003

**Tabela:** R104PDC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |

### IR_R104PSQ_008

**Tabela:** R104MTJ

| Origem | Destino |
|--------|---------|
| CodMtj | CodMtj |

