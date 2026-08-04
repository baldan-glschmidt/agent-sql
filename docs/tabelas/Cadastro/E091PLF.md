# E091PLF

## Descrição

Tabelas - Plano Financeiro - Contas

---

## Resumo

- Campos: 20
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CtaFin | Number(007,0) | Não | Número reduzido da conta financeira |
| DesCta | String(080) | Não | Nomenclatura da conta financeira |
| AbrCta | String(020) | Não | Abreviatura da conta financeira |
| DefGru | String(001) | Não | Definição do grupo da conta financeira |
| MskFin | String(040) | Não | Máscara do grupo que a conta financeira pertence |
| ClaFin | String(030) | Não | Classificação da conta financeira |
| GruFin | Number(002,0) | Não | Grupo que a conta financeira pertence |
| NivFin | Number(002,0) | Não | Nível da conta financeira |
| PosFin | Number(001,0) | Não | Quantidade de posições do nível da conta financeira |
| AnaSin | String(001) | Não | Indicativo se a conta financeira é sintética ou analítica |
| NatFin | String(001) | Não | Indicativo se a natureza da conta financeira e credora ou devedora |
| ForRat | Number(001,0) | Sim | Forma de rateio da conta financeira |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida relacionada a conta financeira |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| TipCfc | String(001) | Sim | Tipo da conta financeira para efeito de fluxo de caixa |
| SeqCfc | Number(007,0) | Sim | Sequência da conta financeira para efeito de fluxo de caixa |
| SitFin | String(001) | Não | Situação da conta financeira |

---

## Chave Primária

- CodEmp
- CtaFin

---

## Índices

### E091PLFIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- ClaFin

---

## Relacionamentos

Nenhum relacionamento cadastrado.
