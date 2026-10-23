# R008VIN

## Descrição

Eventos - Vínculos Inválidos

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
| CodVin | Number(002,0) | Não | Código do Vínculo |

---

## Chave Primária

- CodTab
- CodEve
- CodVin

---

## Índices

### R008VINIndice2

**Tipo:** Não unico

Campos:
- CodVin

---

## Relacionamentos

### IR_R008VIN_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

### IR_R008VIN_002

**Tabela:** R022VIN

| Origem | Destino |
|--------|---------|
| CodVin | CodVin |

