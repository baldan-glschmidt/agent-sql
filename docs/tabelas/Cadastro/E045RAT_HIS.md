# E045RAT_HIS

## Descrição

Tabelas - Histórico - Plano Contábil - Rateios

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodMpc | Number(004,0) | Não | Código do modelo de plano |
| CtaRed | Number(007,0) | Não | Número reduzido da conta contábil a ratear |
| CodCcu | String(009) | Não | Código do centro de custos a ratear |
| PerRat | Number(007,4) | Não | Percentual a ser rateado para o centro de custo |

---

## Chave Primária

- CodEmp
- CodMpc
- CtaRed
- CodCcu

---

## Índices

### E045RAT_HISIndice1

**Tipo:** Não unico

Campos:
- CodMpc

---

## Relacionamentos

### IR_E045RAT_HIS_001

**Tabela:** E043MPC

| Origem | Destino |
|--------|---------|
| CodMpc | CodMpc |

### IR_E045RAT_HIS_002

**Tabela:** E045PLA_HIS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMpc | CodMpc |
| CtaRed | CtaRed |

