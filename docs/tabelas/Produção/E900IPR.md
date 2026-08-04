# E900IPR

## Descrição

O.P./O.S. - Itens do processo de remessa para terceiros

---

## Resumo

- Campos: 24
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| NumPrc | Number(009,0) | Não | Número sequencial do processo de remessa para terceiros |
| SeqIpr | Number(009,0) | Não | Sequência |
| CodOri | String(003) | Sim | Código da origem |
| NumOrp | Number(009,0) | Sim | Número da OP/OS |
| CodEtg | Number(004,0) | Sim | Código do Estágio Produção (Etapas na Fabricação de um Produto) |
| CodCmp | String(014) | Não | Código do componente |
| CmpDer | String(007) | Sim | Código da derivação do componente |
| QtdPrv | Number(014,5) | Sim | Quantidade proporcional prevista para utilizar |
| QtdRes | Number(014,5) | Sim | Quantidade reservada no estoque |
| QtdUti | Number(014,5) | Sim | Quantidade real utilizada |
| QtdEst | Number(014,5) | Sim | Quantidade física total no estoque |
| QtdDis | Number(014,5) | Sim | Quantidade disponível no estoque |
| QtdMta | Number(014,5) | Sim | Quantidade já movimentada |
| QtdSer | Number(014,5) | Sim | Quantidade remetida de componentes para serviços em terceiros |
| QtdSpa | Number(014,5) | Sim | Quantidade separada no depósito |
| QtdRem | Number(014,5) | Sim | Quantidade a remeter para terceiros |
| CodDep | String(010) | Sim | Código do depósito |
| CodLot | String(050) | Sim | Lote de fabricação do componente |
| UniMed | String(003) | Sim | Unidade de medida do componente |
| CodTns | String(005) | Sim | Código da transação para movimentação de estoque |
| SeqCmp | Number(004,0) | Sim | Sequência do Componente na utilização |
| CodCcu | String(009) | Sim | Código do centro de custos |
| BxaOrp | String(001) | Sim | Se for componente de alguma O.P./O.S., indica se o mesmo é baixado |

---

## Chave Primária

- CodEmp
- NumPrc
- SeqIpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900IPR_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E900IPR_001

**Tabela:** E900CPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| NumPrc | NumPrc |

