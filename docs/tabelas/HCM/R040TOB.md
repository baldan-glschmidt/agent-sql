# R040TOB

## Descrição

Base dos Totalizadores

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodTot | Number(004,0) | Não | Código do totalizador |
| SeqTot | Number(003,0) | Não | Sequência |
| TipSin | String(001) | Sim | Sinal |
| TipSom | Number(001,0) | Sim | Tipo de Soma |
| CodEve | Number(004,0) | Sim | Código do Evento |
| TotBas | Number(004,0) | Sim | Código do Totalizador |
| CrtEve | String(003) | Sim | Característica |

---

## Chave Primária

- TabEve
- CodTot
- SeqTot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R040TOB_001

**Tabela:** R040TOT

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodTot | CodTot |

