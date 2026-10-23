# R128HOR

## Descrição

Cursos Aperfeiçoamento - Horários

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
| CodHcu | Number(006,0) | Não | Código do Horário de Curso |
| SeqHor | Number(003,0) | Sim | Sequência do horário |

---

## Chave Primária

- CodCua
- CodHcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128HOR_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R128HOR_001

**Tabela:** R133HCU

| Origem | Destino |
|--------|---------|
| CodHcu | CodHcu |

