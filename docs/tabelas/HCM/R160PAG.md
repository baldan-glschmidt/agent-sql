# R160PAG

## Descrição

BS - Pagamentos Avulsos

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Número do Colaborador |
| CmpEpt | Date | Não | Competência Empréstimo |
| SeqEpt | Number(002,0) | Não | Sequência Empréstimo |
| DatPag | Date | Não | Data Pagamento |
| VlrPag | Number(011,2) | Sim | Valor Pago |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpEpt
- SeqEpt
- DatPag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R160PAG_004

**Tabela:** R160EPT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpEpt | CmpEpt |
| SeqEpt | SeqEpt |

