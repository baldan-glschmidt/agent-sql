# R020RMO

## Descrição

Rateio Mão de Obra em Percentual

---

## Resumo

- Campos: 7
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
| CmpRef | Date | Não | Competência do Rateio |
| RatRmo | Number(009,0) | Não | Código Rateio M.O. |
| ConRat | Number(001,0) | Sim | Considera Rateio |
| PerRmo | Number(005,2) | Sim | % Rateio M.O. |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpRef
- RatRmo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R020RMO_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

