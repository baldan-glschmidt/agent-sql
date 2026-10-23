# R104RES

## Descrição

JR - Cenário - Resultado Cálculo

---

## Resumo

- Campos: 22
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| DatCen | Date | Não | Período de início do direito |
| SeqCen | Number(002,0) | Não | Sequência do cenário |
| EmpAut | Number(004,0) | Não | Empresa do autor |
| TipCol | Number(001,0) | Não | Tipo do colaborador autor |
| NumCad | Number(009,0) | Não | Código do colaborador autor |
| CmpCal | Date | Não | Competência de cálculo |
| CodMtj | Number(003,0) | Não | Código do Pedido |
| TipOpe | Number(001,0) | Sim | Tipo de Operação do Pedido |
| RefPed | Number(013,4) | Sim | Referência do pedido |
| VlrBas | Number(013,4) | Sim | Valor da base de cálculo |
| BasCal | Number(011,2) | Sim | Valor utilizado como base de cálculo (Composição da Base) |
| VlrCal | Number(011,2) | Sim | Valor calculado |
| VlrJur | Number(011,2) | Sim | Valor dos juros |
| VlrCor | Number(011,2) | Sim | Valor da correção |
| RefCal | Number(011,2) | Sim | Outras referências relacionadas ao cálculo do pedido |
| BasRra | Number(011,2) | Sim | Base de Cálculo RRA |
| BfeRra | Number(011,2) | Sim | Base de Cálculo RRA Férias |
| B13Rra | Number(011,2) | Sim | Base de Cálculo RRA 13º Salário |
| InsRra | Number(011,2) | Sim | INSS Cálculo RRA |
| ValInd | Number(016,8) | Sim | Índice/Percentual Correção |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen
- EmpAut
- TipCol
- NumCad
- CmpCal
- CodMtj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104RES_003

**Tabela:** R104PDC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |

### IR_R104RES_008

**Tabela:** R104MTJ

| Origem | Destino |
|--------|---------|
| CodMtj | CodMtj |

