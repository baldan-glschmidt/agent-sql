# R034FIL

## Descrição

Nascimento Filhos

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodDep | Number(002,0) | Não | Código do Dependente |
| NasFil | Date | Sim | Data nascimento do filho |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034FIL_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

