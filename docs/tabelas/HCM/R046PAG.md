# R046PAG

## Descrição

Controle de Pagamento

---

## Resumo

- Campos: 21
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CmpPag | Date | Não | Competência |
| SeqPag | Number(002,0) | Não | Sequência |
| OriPag | Number(002,0) | Sim | Rotina Origem |
| DatPag | Date | Sim | Data do Pagto |
| ValOri | Number(011,2) | Sim | Valor Original a ser Pago |
| ValPag | Number(011,2) | Sim | Valor Pago |
| DatRf1 | Date | Sim | Data de Referência 1 |
| DatRf2 | Date | Sim | Data de Referência 2 |
| CodCal | Number(005,0) | Sim | Código Cálculo Gerador |
| SitPag | Number(001,0) | Sim | Situação |
| DatGer | Date | Sim | Data Geração |
| HorGer | Number(005,0) | Sim | Hora Geração |
| ForPag | Number(002,0) | Sim | Forma de Pagamento |
| SeqVal | Number(002,0) | Sim | Sequência do Vale no Dia |
| SeqChe | Number(005,0) | Sim | Seq |
| NumChe | Number(007,0) | Sim | Número Sequencial do Cheque |
| CodDep | Number(002,0) | Sim | Código do dependente |
| SeqPjp | Number(003,0) | Sim | Sequência do Pagamento da Pensão |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpPag
- SeqPag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R046PAG_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

