# R128RCA

## Descrição

Cursos Aperfeiçoamento - Pré-Requisito Curso Aperfeiçoamento

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
| CodCur | Number(009,0) | Não | Código do Curso Pré-Requisito |
| EqvPre | Number(004,0) | Sim | Grupo de Equivalência Específica para Definição de Turmas (Pré-requisitos) |

---

## Chave Primária

- CodCua
- CodCur

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128RCA_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R128RCA_001

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCur | CodCua |

