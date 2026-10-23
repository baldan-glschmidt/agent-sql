# R127NIT

## Descrição

Custos por Nível Curso de Formação - Itens Custo

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
| NivCuf | Number(002,0) | Não | Nível de Formação do Curso |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| CodTcu | Number(004,0) | Não | Código do Custo |
| VlrIte | Number(011,2) | Sim | Valor do Item de Custo |

---

## Chave Primária

- NivCuf
- CodOem
- CmpCus
- CodTcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R127NIT_002

**Tabela:** R127NCU

| Origem | Destino |
|--------|---------|
| NivCuf | NivCuf |
| CodOem | CodOem |
| CmpCus | CmpCus |

### IR_R127NIT_003

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

