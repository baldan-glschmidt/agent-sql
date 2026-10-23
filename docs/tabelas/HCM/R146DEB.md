# R146DEB

## Descrição

Provisão - Base dos Tipos de Valores

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPrv | Number(004,0) | Não | Tipo de Provisão |
| TipVal | Number(002,0) | Não | Tipo de Valor |
| CodTab | Number(003,0) | Não | Código Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodTot | Number(004,0) | Não | Código do Totalizador |
| CrtEve | String(003) | Não | Característica do Evento |
| SinBas | String(001) | Sim | Sinal da Base |

---

## Chave Primária

- TipPrv
- TipVal
- CodTab
- CodEve
- CodTot
- CrtEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R146DEB_000

**Tabela:** R146DEF

| Origem | Destino |
|--------|---------|
| TipPrv | TipPrv |

### IR_R146DEB_001

**Tabela:** R146DET

| Origem | Destino |
|--------|---------|
| TipPrv | TipPrv |
| TipVal | TipVal |

