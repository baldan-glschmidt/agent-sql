# R008EVB

## Descrição

Eventos - Base de Cálculo

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodSeq | Number(003,0) | Não | Sequência |
| SinBas | String(001) | Sim | Sinal da Base |
| TipBas | Number(002,0) | Sim | Tipo da Base |
| EveBas | Number(004,0) | Sim | Código da Verba |
| CmpAu1 | Number(009,0) | Sim | Campo Auxiliar 1 |
| CmpAu2 | String(020) | Sim | Campo Auxiliar 2 |

---

## Chave Primária

- CodTab
- CodEve
- CodSeq

---

## Índices

### R008EVBIndice2

**Tipo:** Não unico

Campos:
- CodTab
- EveBas

---

## Relacionamentos

### IR_R008EVB_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

### IR_R008EVB_005

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| EveBas | CodEve |

