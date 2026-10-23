# R128TAG

## Descrição

Cursos Aperfeiçoamento - Tags

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
| SeqTag | Number(003,0) | Não | Sequência da Tag de Curso de Aperfeiçoamento |
| NomTag | String(050) | Sim | Tag de Cursos de Aperfeiçoamento |

---

## Chave Primária

- CodCua
- SeqTag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128TAG_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

