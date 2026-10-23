# R146VIN

## Descrição

Provisão - Vínculos

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPrv | Number(004,0) | Não | Tipo de Provisão |
| CodVin | Number(002,0) | Não | Código do Vínculo |

---

## Chave Primária

- TipPrv
- CodVin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R146VIN_000

**Tabela:** R146DEF

| Origem | Destino |
|--------|---------|
| TipPrv | TipPrv |

### IR_R146VIN_001

**Tabela:** R022VIN

| Origem | Destino |
|--------|---------|
| CodVin | CodVin |

