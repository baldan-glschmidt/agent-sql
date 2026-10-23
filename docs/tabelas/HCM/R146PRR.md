# R146PRR

## Descrição

Provisão - Rateios

---

## Resumo

- Campos: 25
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| MesAno | Date | Não | Competência Provisões |
| TipPrv | Number(004,0) | Não | Tipo de Provisão |
| SeqPrv | Number(001,0) | Não | Sequência Para Saldo Transferido |
| TipVal | Number(002,0) | Não | Tipo de Valor |
| CodRat | Number(009,0) | Não | Código do Rateio |
| BasPrv | Number(011,2) | Sim | Base da Provisão |
| PerVal | Number(013,4) | Sim | Percentual/Qtd Dias Provisionado |
| SalAnt | Number(011,2) | Sim | Saldo Anterior |
| SalTrf | Number(011,2) | Sim | Saldo Transferido |
| AjuPrv | Number(011,2) | Sim | Ajuste da Provisão |
| PrvMes | Number(011,2) | Sim | Valor da Provisão Mês |
| ValPag | Number(011,2) | Sim | Valor Pago no Mês |
| ValAdt | Number(011,2) | Sim | Valor 13° Salário Adiantado |
| ValInd | Number(011,2) | Sim | Valor 13° Salário Indenizado |
| PagMai | Number(011,2) | Sim | Valor Pago a Maior |
| AjuMai | Number(011,2) | Sim | Ajuste Valor Pago a Maior |
| SldAtu | Number(011,2) | Sim | Saldo Atual |
| Anb13s | Number(011,2) | Sim | Adt Não Baixado Mês |
| ValPar | Number(011,2) | Sim | Valor Parcial Pago no Mês |
| CmpAu1 | Number(011,2) | Sim | Campo auxiliar 1 |
| CmpAu2 | Number(011,2) | Sim | Campo auxiliar 2 |
| CmpAu3 | Number(011,2) | Sim | Campo auxiliar 3 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MesAno
- TipPrv
- SeqPrv
- TipVal
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R146PRR_004

**Tabela:** R146DEF

| Origem | Destino |
|--------|---------|
| TipPrv | TipPrv |

### IR_R146PRR_006

**Tabela:** R146PRV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| MesAno | MesAno |
| TipPrv | TipPrv |
| SeqPrv | SeqPrv |
| TipVal | TipVal |

### IR_R146PRR_007

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

