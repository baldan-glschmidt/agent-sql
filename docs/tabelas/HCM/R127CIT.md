# R127CIT

## Descrição

Custos por Cursos de Formação - Itens Custo

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCuf | Number(004,0) | Não | Código do Curso de Formação |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| CodTcu | Number(004,0) | Não | Código do Custo |
| VlrIte | Number(011,2) | Sim | Valor do Item de Custo |

---

## Chave Primária

- CodCuf
- CodOem
- CmpCus
- CodTcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R127CIT_002

**Tabela:** R127CCU

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |
| CodOem | CodOem |
| CmpCus | CmpCus |

### IR_R127CIT_003

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

