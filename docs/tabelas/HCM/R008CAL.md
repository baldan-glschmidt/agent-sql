# R008CAL

## Descrição

Eventos - Tipos de Cálculo Válidos

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| TipCal | Number(002,0) | Não | Tipo de cálculo em que o evento poderá ocorrer |

---

## Chave Primária

- CodTab
- CodEve
- TipCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008CAL_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

