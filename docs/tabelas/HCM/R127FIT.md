# R127FIT

## Descrição

Custos por Fases Curso de Formação - Itens Custo

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NivCuf | Number(002,0) | Não | Nível de Formação do Curso |
| SeqNiv | Number(002,0) | Não | Sequência do Nível |
| FasCuf | String(003) | Não | Fase do Curso de Formação |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| CodTcu | Number(004,0) | Não | Código do Custo |
| VlrIte | Number(011,2) | Sim | Valor do Item de Custo |

---

## Chave Primária

- NivCuf
- SeqNiv
- FasCuf
- CodOem
- CmpCus
- CodTcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R127FIT_004

**Tabela:** R127FCU

| Origem | Destino |
|--------|---------|
| NivCuf | NivCuf |
| SeqNiv | SeqNiv |
| FasCuf | FasCuf |
| CodOem | CodOem |
| CmpCus | CmpCus |

### IR_R127FIT_005

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

