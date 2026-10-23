# R074EST

## Descrição

Estados

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPai | Number(004,0) | Não | Código do País |
| CodEst | String(004) | Não | Estado |
| DesEst | String(040) | Sim | Nome do estado |

---

## Chave Primária

- CodPai
- CodEst

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R074EST_000

**Tabela:** R074PAI

| Origem | Destino |
|--------|---------|
| CodPai | CodPai |

