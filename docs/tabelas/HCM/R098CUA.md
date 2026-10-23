# R098CUA

## Descrição

Cursos do Equipamento

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipEqp | Number(003,0) | Não | Código Tipo de Equipamento |
| CodEqp | Number(006,0) | Não | Código do Equipamento |
| CodCua | Number(009,0) | Não | Código do Curso |

---

## Chave Primária

- NumEmp
- TipEqp
- CodEqp
- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R098CUA_001

**Tabela:** R098TEQ

| Origem | Destino |
|--------|---------|
| TipEqp | TipEqp |

### IR_R098CUA_002

**Tabela:** R098EQP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipEqp | TipEqp |
| CodEqp | CodEqp |

### IR_R098CUA_003

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

