# R104PRV

## Descrição

JR - Cenário - Provisão

---

## Resumo

- Campos: 14
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 1

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
| CmpPrv | Date | Não | Competência de atualização da provisão |
| TipPrv | Number(004,0) | Não | Tipo de Provisão |
| TipVal | Number(002,0) | Não | Tipo de Valor |
| SalAnt | Number(011,2) | Sim | Valor do saldo anterior de provisão |
| PrvMes | Number(011,2) | Sim | Valor da provisão do mês |
| SalAtu | Number(011,2) | Sim | Valor do saldo atual da provisão |
| VlrCal | Number(011,2) | Sim | Valor calculado |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen
- EmpAut
- TipCol
- NumCad
- CmpPrv
- TipPrv
- TipVal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104PRV_003

**Tabela:** R104PDC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |

