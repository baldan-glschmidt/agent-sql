# R017HDI

## Descrição

Postos de Trabalho - Revisão descrição - Itens descritos

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
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| DatHis | Date | Não | Data da revisão da descrição do Posto |
| SeqIdp | Number(005,0) | Não | Item de descrição do posto |
| TexIte | String(5000) | Sim | Descrição detalhada do item do Posto |

---

## Chave Primária

- EstPos
- PosTra
- DatHis
- SeqIdp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017HDI_002

**Tabela:** R017HDE

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |
| DatHis | DatHis |

### IR_R017HDI_003

**Tabela:** R017IDP

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| SeqIdp | SeqIdp |

