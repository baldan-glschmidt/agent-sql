# R128RCF

## Descrição

Cursos Aperfeiçoamento - Pré-Requisito Curso Formação

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso |
| CodCuf | Number(004,0) | Não | Código do Curso Pré-Requisito |
| EqvPre | Number(004,0) | Sim | Grupo de Equivalência Específica para Definição de Turmas (Pré-requisitos) |

---

## Chave Primária

- CodCua
- CodCuf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128RCF_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R128RCF_001

**Tabela:** R127CUF

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |

