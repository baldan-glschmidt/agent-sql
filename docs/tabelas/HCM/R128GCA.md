# R128GCA

## Descrição

Grupo Cursos Aperfeiçoamento Equivalente - Cursos

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GruCua | Number(004,0) | Não | Código do grupo de cursos equivalentes |
| CodCua | Number(009,0) | Não | Código do Curso |

---

## Chave Primária

- GruCua
- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128GCA_000

**Tabela:** R128GRU

| Origem | Destino |
|--------|---------|
| GruCua | GruCua |

### IR_R128GCA_001

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

