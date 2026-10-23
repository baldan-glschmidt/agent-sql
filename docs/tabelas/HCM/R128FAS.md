# R128FAS

## Descrição

Cursos Aperfeiçoamento - Fases

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso |
| FasCua | String(003) | Não | Fase do Curso de Aperfeiçoamento |
| DesFas | String(030) | Sim | Descrição da Fase do Curso Aperfeiçoamento |

---

## Chave Primária

- CodCua
- FasCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128FAS_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

