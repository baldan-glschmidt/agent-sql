# R008TOB

## Descrição

Totalizadores - Base de Cálculo

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodTot | Number(004,0) | Não | Código do Totalizador |
| CodSeq | Number(003,0) | Não | Sequência |
| TipSin | String(001) | Sim | Sinal (+/-) |
| CodEve | Number(004,0) | Sim | Código do (E,R,C,T) |
| TotBas | Number(004,0) | Sim | Código do Totalizador Base |
| CrtEve | String(003) | Sim | Código Característica |

---

## Chave Primária

- TabEve
- CodTot
- CodSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008TOB_001

**Tabela:** R008TOT

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodTot | CodTot |

