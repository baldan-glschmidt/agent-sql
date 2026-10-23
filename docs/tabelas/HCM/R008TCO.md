# R008TCO

## Descrição

Eventos - Tipos de Contrato Inválidos

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
| CodEve | Number(004,0) | Não | Evento |
| TipCon | Number(002,0) | Não | Tipo de contrato para quem o evento não será válido |

---

## Chave Primária

- CodTab
- CodEve
- TipCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008TCO_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

