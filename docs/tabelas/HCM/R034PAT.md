# R034PAT

## Descrição

Modalidades do PAT

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| ModPat | Number(001,0) | Não | Modalidade do PAT |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- ModPat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034PAT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

