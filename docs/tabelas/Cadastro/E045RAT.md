# E045RAT

## Descrição

Tabelas - Plano Contábil - Rateios

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CtaRed | Number(007,0) | Não | Número reduzido da conta contábil a ratear |
| CodCcu | String(009) | Não | Código do centro de custos a ratear |
| PerRat | Number(007,4) | Não | Percentual a ser rateado para o centro de custo |

---

## Chave Primária

- CodEmp
- CtaRed
- CodCcu

---

## Índices

### E045RATIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodCcu

---

## Relacionamentos

### IR_E045RAT_001

**Tabela:** E045PLA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CtaRed | CtaRed |

### IR_E045RAT_002

**Tabela:** E044CCU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCcu | CodCcu |

