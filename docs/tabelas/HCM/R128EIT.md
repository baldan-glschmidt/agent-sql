# R128EIT

## Descrição

Custos Reembolso Específico - Itens Custo

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRee | Number(004,0) | Não | Código do reembolso específico |
| CmpCus | Date | Não | Competência do Item de Custo |
| CodTcu | Number(004,0) | Não | Código do Custo |
| VlrIte | Number(011,2) | Sim | Valor do Item de Custo |

---

## Chave Primária

- CodRee
- CmpCus
- CodTcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128EIT_000

**Tabela:** R128RES

| Origem | Destino |
|--------|---------|
| CodRee | CodRee |

### IR_R128EIT_001

**Tabela:** R128ECU

| Origem | Destino |
|--------|---------|
| CodRee | CodRee |
| CmpCus | CmpCus |

### IR_R128EIT_002

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

