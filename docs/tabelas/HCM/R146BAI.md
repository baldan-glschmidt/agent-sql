# R146BAI

## Descrição

Provisão - Baixas

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPrv | Number(004,0) | Não | Tipo de Provisão |
| CodTab | Number(003,0) | Não | Código Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| TipBai | Number(001,0) | Sim | Tipo da Baixa |
| SinBas | String(001) | Sim | Sinal da Base |

---

## Chave Primária

- TipPrv
- CodTab
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R146BAI_000

**Tabela:** R146DEF

| Origem | Destino |
|--------|---------|
| TipPrv | TipPrv |

### IR_R146BAI_002

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

