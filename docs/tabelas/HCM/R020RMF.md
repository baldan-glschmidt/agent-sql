# R020RMF

## Descrição

Rateio Mão de Obra - Contas Financeiras

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CmpRef | Date | Não | Competência do Rateio |
| RatRmo | Number(009,0) | Não | Código Rateio M.O. |
| ConFin | Number(007,0) | Não | Conta Financeira |
| PerFin | Number(005,2) | Sim | % Conta Financeira |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpRef
- RatRmo
- ConFin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R020RMF_004

**Tabela:** R020RMO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpRef | CmpRef |
| RatRmo | RatRmo |

