# R008ATI

## Descrição

Eventos - Atividades Válidas

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodAti | Number(004,0) | Não | Código da Atividade do Professor |

---

## Chave Primária

- CodTab
- CodEve
- CodAti

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008ATI_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

### IR_R008ATI_002

**Tabela:** R171ATI

| Origem | Destino |
|--------|---------|
| CodAti | CodApf |

