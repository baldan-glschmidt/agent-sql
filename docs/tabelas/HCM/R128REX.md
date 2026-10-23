# R128REX

## Descrição

Cursos Aperfeiçoamento - Pré-Requisito Exames

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
| CodExa | Number(004,0) | Não | Código Exame |

---

## Chave Primária

- CodCua
- CodExa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128REX_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R128REX_001

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

