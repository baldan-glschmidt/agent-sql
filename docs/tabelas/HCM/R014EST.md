# R014EST

## Descrição

Sindicato - Estabilidade

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| CodSit | Number(003,0) | Não | Código da Situação |
| GerEst | String(001) | Sim | Gerar Estabilidade |
| DiaEst | Number(004,0) | Sim | Dias Estabilidade |
| CodEtb | Number(002,0) | Sim | Código da Estabilidade |
| NumMax | Number(004,0) | Sim | Máximo Dias Estabilidade |

---

## Chave Primária

- CodSin
- CodSit

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014EST_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

### IR_R014EST_001

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

