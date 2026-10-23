# R047DEP

## Descrição

CIF - Cadastro de Dependentes

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCif | Number(003,0) | Não | Código de Integração Financeira |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodDep | Number(002,0) | Não | Código do Dependente |

---

## Chave Primária

- CodCif
- NumEmp
- TipCol
- NumCad
- CodDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R047DEP_000

**Tabela:** R047CIF

| Origem | Destino |
|--------|---------|
| CodCif | CodCif |

### IR_R047DEP_004

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

