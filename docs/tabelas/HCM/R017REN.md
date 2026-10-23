# R017REN

## Descrição

Reestruturação dos Postos de trabalho - Postos - Deficiências

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
| CodRee | Number(004,0) | Não | Código da reestruturação dos Postos de trabalho |
| SeqReg | Number(009,0) | Não | Sequencia do posto |
| CodDef | Number(002,0) | Não | Indica a deficiência permitida para atuar no posto de trabalho |

---

## Chave Primária

- CodRee
- SeqReg
- CodDef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017REN_001

**Tabela:** R017REP

| Origem | Destino |
|--------|---------|
| CodRee | CodRee |
| SeqReg | SeqReg |

### IR_R017REN_002

**Tabela:** R022DEF

| Origem | Destino |
|--------|---------|
| CodDef | CodDef |

