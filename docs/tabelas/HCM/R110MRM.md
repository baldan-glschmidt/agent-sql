# R110MRM

## Descrição

Receitas Médicas - Remédios

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodAte | Number(006,0) | Não | Código do Atendente |
| NumRec | Number(006,0) | Não | Número da Receita |
| CodRem | Number(006,0) | Não | Código do Medicamento |
| PreRem | String(500) | Sim | Prescrisão do Medicamento |
| QtdRem | Number(010,4) | Sim | Quantidade de medicação receitada |
| CodApr | Number(003,0) | Sim | Cód. forma de apresentação do medicamento doado |

---

## Chave Primária

- NumEmp
- CodAte
- NumRec
- CodRem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110MRM_002

**Tabela:** R110MRC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodAte | CodAte |
| NumRec | NumRec |

### IR_R110MRM_003

**Tabela:** R110REM

| Origem | Destino |
|--------|---------|
| CodRem | CodRem |

