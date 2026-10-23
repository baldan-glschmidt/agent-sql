# R014DNC

## Descrição

Dias Não Considerar Nas Férias

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| DatDnc | Date | Não | Dia Não Considerar |
| DesDnc | String(100) | Sim | Descrição do Dia |

---

## Chave Primária

- CodSin
- DatDnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014DNC_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

