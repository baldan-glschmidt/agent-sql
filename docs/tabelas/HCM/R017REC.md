# R017REC

## Descrição

Reestruturação dos Postos de trabalho - Postos - Cargos

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRee | Number(004,0) | Não | Código da reestruturação dos Postos de trabalho |
| SeqReg | Number(009,0) | Não | Sequencia do posto |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos do Posto de Trabalho |
| CarPos | String(024) | Não | Código do Cargo do Posto de Trabalho |

---

## Chave Primária

- CodRee
- SeqReg
- EstCar
- CarPos

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017REC_001

**Tabela:** R017REP

| Origem | Destino |
|--------|---------|
| CodRee | CodRee |
| SeqReg | SeqReg |

### IR_R017REC_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CarPos | CodCar |

