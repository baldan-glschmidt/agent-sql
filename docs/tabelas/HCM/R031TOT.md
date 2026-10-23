# R031TOT

## Descrição

Geração de Escalas - Totalizadores Categorias

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEqp | Number(004,0) | Não | Código da Equipe |
| CodTur | Number(001,0) | Não | Código do Turno |
| CodCat | Number(003,0) | Não | Código da Categoria |
| DatCmp | Date | Não | Data Competência |
| TotCat | String(125) | Sim | Total Colaboradores Por Dia na Categoria |
| TotExt | String(125) | Sim | Total Colaboradores Extras Por Dia na Categoria |

---

## Chave Primária

- CodEqp
- CodTur
- CodCat
- DatCmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R031TOT_002

**Tabela:** R031CAT

| Origem | Destino |
|--------|---------|
| CodCat | CodCat |

