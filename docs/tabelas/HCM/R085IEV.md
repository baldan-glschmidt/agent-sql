# R085IEV

## Descrição

Orçamento - Base Cálculo - Eventos

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IteOrc | Number(003,0) | Não | Código do Item |
| SeqIte | Number(002,0) | Não | Sequência Item |
| CodTab | Number(003,0) | Sim | Código da Tabela Eventos |
| CodEve | Number(004,0) | Sim | Código do Evento |
| SinBas | String(001) | Sim | Sinal Base |

---

## Chave Primária

- IteOrc
- SeqIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085IEV_000

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

### IR_R085IEV_002

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |

### IR_R085IEV_003

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

