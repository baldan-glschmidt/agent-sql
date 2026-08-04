# E900DLS

## Descrição

O.P./O.S. - Quantidades Entrada, Vencimento, Lote, Série

---

## Resumo

- Campos: 20
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Origem do produto/serviço fabricado na O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodPro | String(014) | Não | Código do Produto |
| CodDer | String(007) | Não | Código da Derivação |
| SeqDls | Number(006,0) | Não | Sequência de movimento de item |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção da O.P./O.S. |
| SeqRot | Number(004,0) | Sim | Sequência lógica da Operação no Roteiro de Produção |
| CodDep | String(010) | Sim | Código do depósito |
| DatEnt | Date | Sim | Data da entrada do produto no depósito |
| DatVlt | Date | Sim | Data de validade do produto no depósito |
| CodLot | String(050) | Sim | Código do Lote de Fabricação para estocagem |
| LotBas | String(050) | Sim | Lote do componente base responsável pela geração do lote do produto acabado |
| NumSep | String(050) | Sim | Número de série do produto |
| QtdRes | Number(014,5) | Sim | Quantidade a ser reservada do estoque |
| QtdBlo | Number(014,5) | Sim | Quantidade de estoque bloqueado manualmente |
| ProOrp | String(014) | Sim | Código do Produto/Serviço da O.P./O.S. |
| DerOrp | String(007) | Sim | Código da Derivação da O.P./O.S. |
| IndPro | String(001) | Sim | Indicativo se é Produto da OP |
| ObsDls | String(250) | Sim | Texto da observação |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodPro
- CodDer
- SeqDls

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900DLS_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900DLS_006

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

