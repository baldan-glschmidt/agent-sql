# E043RMP

## Descrição

Tabelas - Modelos de Planos - Relacionamento entre Modelos de Planos (De/Para)

---

## Resumo

- Campos: 15
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMpc | Number(004,0) | Não | Código do modelo de plano origem |
| CodMpu | Number(004,0) | Não | Código do modelo de plano de centro de custos origem |
| CodMpa | Number(004,0) | Não | Código do modelo de plano destino |
| SeqMpc | Number(006,0) | Não | Sequência de registro |
| CtaAnt | Number(009,0) | Sim | Código reduzido da conta contábil origem |
| CtaRed | Number(009,0) | Sim | Código reduzido do centro de custo no modelo de plano |
| GruCta | String(006) | Sim | Identificação do Grupo de Conta-Subconta |
| CtaAtu | Number(009,0) | Sim | Código reduzido da conta contábil destino |
| NatCta | Number(002,0) | Sim | Natureza Subconta Correlata |
| CcuAnt | String(009) | Sim | Código do centro de custos origem |
| CodCcu | String(009) | Sim | Código do centro de custo no modelo de plano |
| CcuAtu | String(009) | Sim | Código do centro de custos destino |
| PerRat | Number(007,4) | Sim | Percentual a ser rateado |
| TipCon | String(001) | Sim | Tipo da conta |
| LucExp | String(001) | Sim | Indicativo se a conta/centro de custo são de lucro de exploração |

---

## Chave Primária

- CodMpc
- CodMpu
- CodMpa
- SeqMpc

---

## Índices

### E043RMPIndice2

**Tipo:** Não unico

Campos:
- CodMpc
- CodMpu
- CodMpa
- CtaAnt

### E043RMPIndice3

**Tipo:** Não unico

Campos:
- CodMpa

---

## Relacionamentos

### IR_E043RMP_000

**Tabela:** E043MPC

| Origem | Destino |
|--------|---------|
| CodMpc | CodMpc |

### IR_E043RMP_002

**Tabela:** E043MPC

| Origem | Destino |
|--------|---------|
| CodMpa | CodMpc |

