# R128CUR

## Descrição

Cursos Aperfeiçoamento - Recursos Instrucionais

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
| CodRei | Number(004,0) | Não | Código do Recurso Instrucional |
| QtdRei | Number(004,0) | Sim | Quantidade de Recursos Utilizados |

---

## Chave Primária

- CodCua
- CodRei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128CUR_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R128CUR_001

**Tabela:** R140REI

| Origem | Destino |
|--------|---------|
| CodRei | CodRei |

