# R008TOT

## Descrição

Totalizadores de Eventos

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodTot | Number(004,0) | Não | Código do Totalizador |
| DesTot | String(040) | Sim | Descrição do Totalizador |
| TipSom | Number(001,0) | Sim | Tipo de Soma |

---

## Chave Primária

- TabEve
- CodTot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008TOT_000

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

