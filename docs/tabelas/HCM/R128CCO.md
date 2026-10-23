# R128CCO

## Descrição

Cursos Aperfeiçoamento - Cursos Contidos

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
| CodCua | Number(009,0) | Não | Código do Curso |
| CodCur | Number(009,0) | Não | Código do Curso Contido |

---

## Chave Primária

- CodCua
- CodCur

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128CCO_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R128CCO_001

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCur | CodCua |

