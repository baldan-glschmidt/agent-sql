# R127TAG

## Descrição

Cursos de Formação - Tags

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
| CodCuf | Number(004,0) | Não | Código do Curso |
| SeqTag | Number(002,0) | Não | Sequência da Tag de Curso de Formação |
| NomTag | String(050) | Sim | Tag de Curso de Formação |

---

## Chave Primária

- CodCuf
- SeqTag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R127TAG_000

**Tabela:** R127CUF

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |

