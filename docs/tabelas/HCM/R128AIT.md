# R128AIT

## Descrição

Custos por Assunto - Itens Custo

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
| CodAss | Number(004,0) | Não | Código do Assunto |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| CodTcu | Number(004,0) | Não | Código do Custo |
| VlrIte | Number(011,2) | Sim | Valor do Item de Custo |

---

## Chave Primária

- CodAss
- CodOem
- CmpCus
- CodTcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128AIT_002

**Tabela:** R128ACU

| Origem | Destino |
|--------|---------|
| CodAss | CodAss |
| CodOem | CodOem |
| CmpCus | CmpCus |

### IR_R128AIT_003

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

