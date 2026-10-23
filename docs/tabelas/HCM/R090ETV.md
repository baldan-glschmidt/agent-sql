# R090ETV

## Descrição

EPI por Tipo de Visita

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
| TipVis | Number(003,0) | Não | Tipo da Visita |
| CodEpi | Number(008,0) | Não | Código do EPI |

---

## Chave Primária

- TipVis
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090ETV_000

**Tabela:** R090TVI

| Origem | Destino |
|--------|---------|
| TipVis | TipVis |

### IR_R090ETV_001

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

