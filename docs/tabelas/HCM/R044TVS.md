# R044TVS

## Descrição

Tipos de Vales - Situações

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodVal | Number(004,0) | Não | Código do Vale |
| CodSit | Number(003,0) | Não | Código da Situação |

---

## Chave Primária

- TabEve
- CodVal
- CodSit

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044TVS_000

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

