# E043MMP

## Descrição

Tabelas - Modelos de Planos - Máscaras das Classificações

---

## Resumo

- Campos: 20
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMpc | Number(004,0) | Não | Código do modelo de plano |
| CodGcc | Number(001,0) | Não | Código do grupo de contas do modelo de plano |
| MskGcc | String(040) | Não | Máscara do grupo de contas do modelo de plano |
| DefGru | String(001) | Não | Definição do grupo de contas do modelo de plano |
| PosNi1 | Number(001,0) | Sim | Quantidade de posições do nível - 1 |
| PosNi2 | Number(001,0) | Sim | Quantidade de posições do nível - 2 |
| PosNi3 | Number(001,0) | Sim | Quantidade de posições do nível - 3 |
| PosNi4 | Number(001,0) | Sim | Quantidade de posições do nível - 4 |
| PosNi5 | Number(001,0) | Sim | Quantidade de posições do nível - 5 |
| PosNi6 | Number(001,0) | Sim | Quantidade de posições do nível - 6 |
| PosNi7 | Number(001,0) | Sim | Quantidade de posições do nível - 7 |
| PosNi8 | Number(001,0) | Sim | Quantidade de posições do nível - 8 |
| PosNi9 | Number(001,0) | Sim | Quantidade de posições do nível - 9 |
| PosN10 | Number(001,0) | Sim | Quantidade de posições do nível - 10 |
| PosN11 | Number(001,0) | Sim | Quantidade de posições do nível - 11 |
| PosN12 | Number(001,0) | Sim | Quantidade de posições do nível - 12 |
| PosN13 | Number(001,0) | Sim | Quantidade de posições do nível - 13 |
| PosN14 | Number(001,0) | Sim | Quantidade de posições do nível - 14 |
| PosN15 | Number(001,0) | Sim | Quantidade de posições do nível - 15 |
| ForRat | Number(001,0) | Não | Forma de rateio dos lançamentos |

---

## Chave Primária

- CodMpc
- CodGcc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E043MMP_000

**Tabela:** E043MPC

| Origem | Destino |
|--------|---------|
| CodMpc | CodMpc |

