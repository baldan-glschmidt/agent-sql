# E013AGP

## Descrição

Cadastros - Formas de Agrupamento para Produtos

---

## Resumo

- Campos: 24
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodAgp | String(005) | Não | Código da forma de agrupamento dos produtos |
| DesAgp | String(030) | Não | Descrição da forma de agrupamento dos produtos |
| AbrAgp | String(010) | Não | Abreviatura da forma de agrupamento dos produtos |
| TipAgp | String(001) | Não | Código do tipo de agrupamento dos produtos |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| CodFif | String(010) | Sim | Código Fiscal Federal do Agrupamento |
| CodFie | String(060) | Sim | Código Fiscal Estadual |
| CodFim | String(010) | Sim | Código Fiscal Municipal do Agrupamento |
| MgcMin | Number(015,6) | Sim | Percentual de margem de contribuição mínima |
| MgcLim | Number(015,6) | Sim | Percentual de margem de contribuição limite |
| PerVen | Number(024,12) | Sim | Percentual adicional do vendedor no cálculo da margem |
| AplAtx | String(004) | Sim | Código da aplicação do autotexto |
| CodAtx | Number(010,0) | Sim | Código do autotexto |
| PreRef | Number(024,12) | Sim | Preço de referência vinculada a margem de contribuição |
| IndAco | String(001) | Sim | Indicativo se é ato cooperado. |
| USU_CtaCtb1 | Number(007,0) | Não | Conta Contabil Reduzida - 1 |
| USU_CtaCtb2 | Number(007,0) | Não | Conta Contabil Reduzida - 2 |
| USU_CtaCtb3 | Number(007,0) | Não | Conta Contabil Reduzida - 3 |
| USU_CtaCtb4 | Number(007,0) | Não | Conta Contabil Reduzida - 4 |

---

## Chave Primária

- CodEmp
- CodAgp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
