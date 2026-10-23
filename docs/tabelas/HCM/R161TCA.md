# R161TCA

## Descrição

Bs - Tipos de cálculo na solicitação de empréstimo

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
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
| TipCal | Number(002,0) | Não | Tipo de Cálculo |
| PerDes | Number(005,2) | Sim | Perc. Desconto |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpEmp
- TipCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R161TCA_003

**Tabela:** R161EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpEmp | CmpEmp |

