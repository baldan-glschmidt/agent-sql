# R031PAE

## Descrição

Parâmetros da Geração de Escalas

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEqp | Number(004,0) | Não | Código da Equipe |
| DatCmp | Date | Não | Data Competência |
| CodTur | Number(001,0) | Não | Código do Turno |
| CodCat | Number(003,0) | Não | Código da Categoria |
| MinDCT | Number(002,0) | Sim | Número Mínimo de Dias Consecutivos de Trabalho |
| MaxDCT | Number(002,0) | Sim | Número Máximo de Dias Consecutivos de Trabalho |
| MinDCF | Number(002,0) | Sim | Número Mínimo de Dias Consecutivos de Folga |
| MaxDCF | Number(002,0) | Sim | Número Máximo de Dias Consecutivos de Folga |
| ObsPar | String(200) | Sim | Observação da Geração de Escalas |
| LisDia | String(125) | Sim | Lista Colaboradores Dia |

---

## Chave Primária

- CodEqp
- DatCmp
- CodTur
- CodCat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R031PAE_000

**Tabela:** R031EQP

| Origem | Destino |
|--------|---------|
| CodEqp | CodEqp |

### IR_R031PAE_003

**Tabela:** R031CAT

| Origem | Destino |
|--------|---------|
| CodCat | CodCat |

