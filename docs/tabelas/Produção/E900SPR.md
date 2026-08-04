# E900SPR

## Descrição

OP/OS - Subproduto

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Código da origem |
| NumOrp | Number(009,0) | Não | Número da OP/OS |
| CodEtg | Number(004,0) | Não | Código do estágio de produção |
| SeqSpr | Number(004,0) | Não | Sequência do subproduto no estágio da OP |
| CodPro | String(014) | Não | Código do subproduto |
| CodDer | String(007) | Sim | Código da derivação do subproduto |
| UniMed | String(003) | Não | Unidade de medida de estocagem do subproduto |
| QtdPrv | Number(014,5) | Não | Quantidade prevista de entrada |
| QtdRea | Number(014,5) | Sim | Quantidade realizada de entrada |
| CodTns | String(005) | Não | Código da transação para movimentação de estoque |
| CodDep | String(010) | Sim | Código do depósito de entrada do subproduto |
| CodCcu | String(009) | Não | Código do centro de custos |
| FrmEsp | String(001) | Sim | Indica se a forma de entrada do subproduto será automática ou manual |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqSpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900SPR_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

