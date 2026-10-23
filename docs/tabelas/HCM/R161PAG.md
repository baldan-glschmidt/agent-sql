# R161PAG

## Descrição

Bs - Pagamentos e Quitações

---

## Resumo

- Campos: 8
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
| DatAlt | Date | Não | Data Pagamento |
| TipPag | String(001) | Não | Tipo do Pagamento |
| VlrPag | Number(011,2) | Sim | Valor Pago |
| ParPag | Number(002,0) | Sim | Número de Parcelas Pagas |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpEmp
- DatAlt
- TipPag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R161PAG_003

**Tabela:** R161EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpEmp | CmpEmp |

