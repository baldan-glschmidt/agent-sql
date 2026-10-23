# R040TOT

## Descrição

Totalizadores dos Períodos de Férias

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
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodTot | Number(004,0) | Não | Totalizador |
| DesTot | String(025) | Sim | Descrição do Totalizador |

---

## Chave Primária

- TabEve
- CodTot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R040TOT_000

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

