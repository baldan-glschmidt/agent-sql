# E046RAT

## Descrição

Contábil - Lançamentos - Rateios

---

## Resumo

- Campos: 14
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| FilOri | Number(005,0) | Não | Código da filial |
| NumMat | Number(009,0) | Não | Número da Tabela |
| FilRat | Number(005,0) | Não | Código da filial |
| CtaRed | Number(007,0) | Sim | Número Reduzido Conta Contábil |
| CodCCu | String(009) | Sim | Código do centro de custos |
| CCuRec | String(009) | Sim | Código do centro de custos |
| DatLct | Date | Não | Data de lançamento base do rateio |
| PerRat | Number(007,4) | Sim | Percentual de rateio para o centro de resultado |
| VlrRat | Number(017,2) | Sim | Valor do rateio para o centro de resultado |
| DebCre | String(001) | Não | Indicativo se o lançamento é debito ou crédito |
| SitRat | Number(001,0) | Não | Situação do rateio do lançamento |
| SeqDis | Number(009,0) | Não | Sequência da Distribuição |
| NumLct | Number(010,0) | Não | Número sequencial do lançamento |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
