# R161MOT

## Descrição

Bs - Motivo de Empréstimo

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMtv | Number(003,0) | Não | Código Motivo |
| DesMot | String(040) | Sim | Descrição do Motivo |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Sim | Código do Evento |
| RgrEve | Number(003,0) | Sim | Regra Específica do Evento |
| VlrJur | Number(013,4) | Sim | Valor Juros |
| TipMot | Number(002,0) | Sim | Tipo Motivo |

---

## Chave Primária

- CodMtv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R161MOT_003

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

