# R011SBH

## Descrição

Situações do Banco de Horas

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBhr | Number(005,0) | Não | Código do Banco de Horas |
| CodSit | Number(003,0) | Não | Código da Situação |
| SinSit | String(001) | Sim | Sinal da Situação |
| TabEve | Number(003,0) | Sim | Tabela de Eventos |
| CodEve | Number(004,0) | Sim | Código do Evento Associado |
| OrdCom | Number(002,0) | Sim | Ordem Compensação Mesma Data |
| CnvBan | Number(006,3) | Sim | Conversão para Banco de Horas (%) |
| CnvEve | Number(006,3) | Sim | Conversão para Geração de Eventos (%) |
| OrdFec | Number(001,0) | Sim | Ordem Fechamento |

---

## Chave Primária

- CodBhr
- CodSit

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R011SBH_000

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBhr | CodBHr |

### IR_R011SBH_001

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

### IR_R011SBH_003

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

