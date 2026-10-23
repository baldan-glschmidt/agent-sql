# R048CLB

## Descrição

CLC - Base

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
| CodClc | Number(004,0) | Não | Código Lançamento Contábil |
| SeqBas | Number(003,0) | Não | Sequência |
| SinBas | String(001) | Sim | Sinal do CLC Base |
| TerFpa | Number(004,0) | Sim | Código do Convênio (Terceiros do FPAS) |
| ClcBas | Number(004,0) | Sim | CLC Base Cálculo |
| TotBas | Number(004,0) | Sim | Código do Totalizador |
| CodEve | Number(004,0) | Sim | Código do Evento |

---

## Chave Primária

- TabEve
- CodClc
- SeqBas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R048CLB_001

**Tabela:** R048CLC

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodClc | CodClc |

