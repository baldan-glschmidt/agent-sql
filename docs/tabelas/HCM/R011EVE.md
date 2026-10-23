# R011EVE

## Descrição

Eventos do Banco de Horas

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBHr | Number(005,0) | Não | Código do Banco de Horas |
| CodSit | Number(003,0) | Não | Código da Situação |
| CodTab | Number(003,0) | Não | Código da Tabela de Eventos |
| EveCre | Number(004,0) | Sim | Evento dos Crédito Não Compensados |
| EveDeb | Number(004,0) | Sim | Evento do Débito Não Compensados |

---

## Chave Primária

- CodBHr
- CodSit
- CodTab

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R011EVE_000

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBHr | CodBHr |

### IR_R011EVE_001

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

### IR_R011EVE_002

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |

