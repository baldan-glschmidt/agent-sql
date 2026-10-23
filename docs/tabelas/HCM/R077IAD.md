# R077IAD

## Descrição

Avaliação detalhada - Itens

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAva | Number(004,0) | Não | Código da Avaliação detalhada |
| CodIte | Number(003,0) | Não | Código do item de avaliação |
| DesIte | String(1600) | Sim | Descrição do item da avaliação |
| CodTbn | Number(003,0) | Sim | Código da Tabela de Notas |

---

## Chave Primária

- CodAva
- CodIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077IAD_000

**Tabela:** R077CAD

| Origem | Destino |
|--------|---------|
| CodAva | CodAva |

### IR_R077IAD_003

**Tabela:** R201TBN

| Origem | Destino |
|--------|---------|
| CodTbn | CodTbn |

