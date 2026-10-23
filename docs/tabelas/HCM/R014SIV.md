# R014SIV

## Descrição

Sindicato Valores Anuidade

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| PerAdm | Date | Não | Período de Admissão |
| TipAnu | String(001) | Não | Tipo da Anuidade |
| CmpAnu | Date | Não | Competência |
| NumAnu | Number(002,0) | Não | Número de anos da anuidade |
| ValAnu | Number(011,2) | Sim | Valor/Percentual da Anuidade |
| TetAnu | Number(011,2) | Sim | Máximo pago de anuidade |

---

## Chave Primária

- CodSin
- PerAdm
- TipAnu
- CmpAnu
- NumAnu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014SIV_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

