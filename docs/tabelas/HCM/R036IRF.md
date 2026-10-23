# R036IRF

## Descrição

Intervalos p/ Desconto de IR

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
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodDep | Number(002,0) | Não | Código do dependente |
| CmpIni | Date | Não | Competência de inicio  de desconto do IR |
| CmpFim | Date | Sim | Competência final de desconto do IR |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep
- CmpIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R036IRF_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

