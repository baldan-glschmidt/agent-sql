# R008EVR

## Descrição

Eventos de Reembolsos de Comodatários

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCid | Number(007,0) | Não | Código da Cidade |
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| DatAlt | Date | Não | Data da Alteração do Usuário do Veículo |
| IndIce | Number(012,3) | Sim | Índice do Evento de Reembolso |
| TipEvr | String(001) | Sim | Tipo de Evento de Reembolso |

---

## Chave Primária

- CodCid
- CodTab
- CodEve
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008EVR_000

**Tabela:** R074CID

| Origem | Destino |
|--------|---------|
| CodCid | CodCid |

### IR_R008EVR_001

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |

### IR_R008EVR_002

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

