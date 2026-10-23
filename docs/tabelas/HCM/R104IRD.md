# R104IRD

## Descrição

JR - Cenário - Resultado Cálculo, dedução por Dependentes

---

## Resumo

- Campos: 12
- Chave Primária: 10 campo(s)
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
| CodDep | Number(002,0) | Não | Código do Dependente |
| CpfDep | Number(011,0) | Sim | Número do CPF do Dependente |
| VlrDed | Number(015,2) | Sim | Valor da dedução da base cálculo |

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
- CodDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104IRD_008

**Tabela:** R104RES

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |
| EmpAut | EmpAut |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpCal | CmpCal |
| CodMtj | CodMtj |

### IR_R104IRD_009

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

