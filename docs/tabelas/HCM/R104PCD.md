# R104PCD

## Descrição

JR - Pedidos Cenário - Detalhado

---

## Resumo

- Campos: 22
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 3

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
| DatIni | Date | Não | Data de início do direito |
| DatFim | Date | Sim | Data de término do direito |
| VlrRec | Number(011,2) | Sim | Valor Reclamado |
| QtdHor | Number(010,0) | Sim | Quantidade de horas reclamadas |
| PerIte | Number(008,5) | Sim | Percentual a ser considerado no cálculo do pedido |
| QtdDia | Number(004,0) | Sim | Quantidade de dias reclamados |
| ForCal | Number(001,0) | Sim | Forma de cálculo (salário do colaborador/paradigma) |
| RefDSR | String(001) | Sim | Reflexo no cálculo do DSR |
| RefFer | String(001) | Sim | Reflexo no cálculo das Férias |
| Ref13s | String(001) | Sim | Reflexo no cálculo do 13° Salário |
| RefAvi | String(001) | Sim | Reflexo no cálculo do aviso prévio |
| ObsPed | String(250) | Sim | Observação sobre o pedido |
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
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104PCD_003

**Tabela:** R104PDC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |

### IR_R104PCD_007

**Tabela:** R104MTJ

| Origem | Destino |
|--------|---------|
| CodMtj | CodMtj |

### IR_R104PCD_008

**Tabela:** R104PDI

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |
| EmpAut | EmpAut |
| TipCol | TipCol |
| NumCad | NumCad |
| CodMtj | CodMtj |
| SeqPed | SeqPed |

