# R078TBT

## Descrição

Times - Blocos de Habilidades Técnicas - OBSOLETA

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTim | String(008) | Não | Código do Time |
| DatHab | Date | Não | Data da Última Revisão das Habilidades do Time |
| BloHte | String(004) | Não | Bloco de Habilidades Técnicas |

---

## Chave Primária

- CodTim
- DatHab
- BloHte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R078TBT_000

**Tabela:** R078TIM

| Origem | Destino |
|--------|---------|
| CodTim | CodTim |

### IR_R078TBT_002

**Tabela:** R077BLO

| Origem | Destino |
|--------|---------|
| BloHte | BloHte |

