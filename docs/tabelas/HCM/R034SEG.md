# R034SEG

## Descrição

Seguros do Empregado

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
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodSeg | Number(003,0) | Não | Tipo do seguro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodSeg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034SEG_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R034SEG_003

**Tabela:** R166SEG

| Origem | Destino |
|--------|---------|
| CodSeg | CodSeg |

