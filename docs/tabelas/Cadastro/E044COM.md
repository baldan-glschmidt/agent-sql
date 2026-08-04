# E044COM

## Descrição

Cadastros - Composição de Lançamentos

---

## Resumo

- Campos: 16
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumTab | Number(009,0) | Não | Número da Tabela |
| NumLct | Number(010,0) | Não | Número sequencial do lançamento |
| CtaRed | Number(007,0) | Sim | Número Reduzido Conta Contábil |
| CodCCu | String(009) | Sim | Código do centro de custos |
| FilRat | Number(005,0) | Não | Código da filial |
| DatLct | Date | Não | Data de lançamento base do rateio |
| PerRat | Number(007,4) | Sim | Percentual de rateio para o centro de resultado |
| VlrRat | Number(014,4) | Sim | Valor do rateio para o centro de resultado |
| DebCre | String(001) | Não | Indicativo se o lançamento é debito ou crédito |
| SitRat | Number(001,0) | Não | Situação do rateio do lançamento |
| CCuOri | String(009) | Sim | Centro de custo de origem |
| ObsLct | String(300) | Sim | Observação |
| CodHpd | Number(004,0) | Não | Código do histórico padrão |
| SeqDis | Number(009,0) | Não | Sequência da Distribuição |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
