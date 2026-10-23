# R577CPE

## Descrição

Competência - Revisão - Competências essenciais

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
| CodCpt | Number(009,0) | Não | Código da Competência |
| RevCpt | String(010) | Não | Código da Revisão da Competência |
| CodCpE | String(024) | Não | Competência essencial que originou a competência |

---

## Chave Primária

- CodCpt
- RevCpt
- CodCpE

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R577CPE_001

**Tabela:** R577REV

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |

### IR_R577CPE_002

**Tabela:** R577ORG

| Origem | Destino |
|--------|---------|
| CodCpE | CodCpE |

