# R017HIE

## Descrição

Postos de Trabalho - Hierarquia do Posto - Postos hierarquizados

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da Estrutura de Postos de trabalho |
| CodThp | Number(003,0) | Não | Código do Tipo de hierarquia do posto de trabalho |
| RevHie | Number(003,0) | Não | Código da revisão da hierarquia de postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de trabalho |
| PosPos | String(090) | Sim | Posição do Posto de Trabalho dentro da árvore |
| IdePos | Number(007,0) | Sim | Identificador do posto |

---

## Chave Primária

- EstPos
- CodThp
- RevHie
- PosTra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017HIE_002

**Tabela:** R017RHP

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| CodThp | CodThp |
| RevHie | RevHie |

### IR_R017HIE_003

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

