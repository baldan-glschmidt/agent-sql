# R044VPA

## Descrição

Parcelas Vales / Compras

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatPag | Date | Não | Data de Pagamento do Vale |
| SeqVal | Number(002,0) | Não | Sequência do Vale no Dia |
| SeqPar | Number(003,0) | Não | Sequência da Parcela |
| ValBru | Number(011,2) | Sim | Valor bruto do adiantamento |
| ValLiq | Number(011,2) | Sim | Valor líquido do adiantamento |
| CodCal | Number(005,0) | Sim | Código de Cálculo |
| TipVpa | String(001) | Sim | Tipo de Pgto da Parcela |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatPag
- SeqVal
- SeqPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044VPA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

