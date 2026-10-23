# R014ASI

## Descrição

Situações Desconsideradas para Aviso Prévio

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| DatAlt | Date | Não | Data Alteração Aviso Prévio |
| CodSit | Number(003,0) | Não | Código da Situação |

---

## Chave Primária

- CodSin
- DatAlt
- CodSit

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014ASI_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

### IR_R014ASI_001

**Tabela:** R014AVP

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |
| DatAlt | DatAlt |

### IR_R014ASI_002

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

