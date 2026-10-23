# R008SIT

## Descrição

Eventos - Situações Inválidas

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodSit | Number(003,0) | Não | Código da situação para quem o evento não será válido |

---

## Chave Primária

- CodTab
- CodEve
- CodSit

---

## Índices

### R008SITIndice2

**Tipo:** Não unico

Campos:
- CodSit

---

## Relacionamentos

### IR_R008SIT_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

### IR_R008SIT_002

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

