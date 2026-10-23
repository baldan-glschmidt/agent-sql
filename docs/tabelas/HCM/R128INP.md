# R128INP

## Descrição

Cursos Aperfeiçoamento - Instrutores (Pessoas)

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
| CodPes | Number(009,0) | Não | Código da Pessoa |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |

---

## Chave Primária

- CodPes
- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128INP_000

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

### IR_R128INP_001

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

