# R010CSE

## Descrição

Eventos Positivo/Negativo do Saldo

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSal | Number(002,0) | Não | Código do Saldo |
| TabEve | Number(003,0) | Não | Código Tabela de Eventos |
| EvePos | Number(004,0) | Sim | Código Evento p/ Saldo Positivo |
| EveNeg | Number(004,0) | Sim | Código Evento p/ Saldo Negativo |
| EvePag | Number(004,0) | Sim | Eventos dos Pagamentos de Saldos |

---

## Chave Primária

- CodSal
- TabEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R010CSE_000

**Tabela:** R010CSA

| Origem | Destino |
|--------|---------|
| CodSal | CodSal |

### IR_R010CSE_001

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

