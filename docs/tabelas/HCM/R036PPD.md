# R036PPD

## Descrição

Pensão Judicial - Percentual por Dependente

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodDep | Number(002,0) | Não | Código do Dependente |
| CmpAlt | Date | Não | Competência |
| DepPag | Number(002,0) | Não | Código do Dependente |
| PerPen | Number(005,2) | Sim | Percentual da Pensão |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep
- CmpAlt
- DepPag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R036PPD_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

### IR_R036PPD_005

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DepPag | CodDep |

