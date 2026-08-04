# E091RFC

## Descrição

Tabelas - Plano Financeiro - Relacionamentos com Centros de Custos

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodRfc | Number(003,0) | Não | Código do relacionamento entre plano financeiro e centro de custos |
| DesRfc | String(040) | Não | Descrição do relacionamento entre conta financeiro X centro de custo |
| CtaFin | Number(007,0) | Não | Número reduzido da conta financeira |
| CtaFi2 | Number(007,0) | Sim | Número reduzido da conta financeira 2 |
| CodCcu | String(009) | Não | Código do centro de custos |
| CodCc2 | String(009) | Sim | Código do centro de custos 2 |
| MskRes | String(250) | Sim | Máscara resultante para inversão gerencial |
| ObsRcc | String(250) | Sim | Observação do relacionamento |

---

## Chave Primária

- CodEmp
- CodRfc

---

## Índices

### E091RFCIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CtaFin

### E091RFCIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodCcu

---

## Relacionamentos

### IR_E091RFC_003

**Tabela:** E091PLF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CtaFin | CtaFin |

### IR_E091RFC_005

**Tabela:** E044CCU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCcu | CodCcu |

