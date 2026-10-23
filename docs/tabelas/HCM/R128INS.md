# R128INS

## Descrição

Cursos Aperfeiçoamento - Instrutores

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128INS_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R128INS_003

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

