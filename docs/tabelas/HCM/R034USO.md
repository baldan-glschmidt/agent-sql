# R034USO

## Descrição

Terceiros - Tipos de Uso

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
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipUso | Number(002,0) | Não | Tipo de Uso |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TipUso

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034USO_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

