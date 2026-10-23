# R010TOB

## Descrição

Base Totalizadores de Situações

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTot | Number(004,0) | Não | Código do Totalizador |
| CodSit | Number(003,0) | Não | Código da Situação |
| SinSit | String(001) | Sim | Sinal da Situação no Totalizador (+/-) |

---

## Chave Primária

- CodTot
- CodSit

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R010TOB_000

**Tabela:** R010TOT

| Origem | Destino |
|--------|---------|
| CodTot | CodTot |

### IR_R010TOB_001

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

