# R161PAR

## Descrição

Bs - Parcelas Empréstimos

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CmpEmp | Date | Não | Data Empréstimo |
| DatDes | Date | Não | Data Desconto |
| SeqDes | Number(002,0) | Não | Sequência |
| DatAlt | Date | Sim | Data Alteração |
| VlrPar | Number(011,2) | Sim | Valor Parcela |
| VlrOri | Number(011,2) | Sim | Valor Parcela |
| IntFol | Number(002,0) | Sim | Status |
| CodCal | Number(005,0) | Sim | Código do Cálculo |
| SitAlt | String(001) | Sim | Parcela Alterada |
| ObsPar | String(040) | Sim | Observação da Parcela |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpEmp
- DatDes
- SeqDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R161PAR_003

**Tabela:** R161EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpEmp | CmpEmp |

