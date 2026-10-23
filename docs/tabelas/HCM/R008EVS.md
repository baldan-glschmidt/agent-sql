# R008EVS

## Descrição

Situações Base Cálculo dos Eventos

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodSit | Number(003,0) | Não | Código da Situação |
| SinSit | String(001) | Sim | Sinal da Situação na Base do Evento |
| TraHor | String(001) | Sim | Tratamento das Horas da Situação |
| TraDsr | String(001) | Sim | Somar as Horas do DSR no Afastamento |

---

## Chave Primária

- CodTab
- CodEve
- CodSit

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008EVS_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

### IR_R008EVS_002

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

