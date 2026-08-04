# E900SOP

## Descrição

O.P./O.S. - Serviços Executados por Terceiros

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
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção da O.P./O.S. |
| SeqRot | Number(004,0) | Não | Sequência da operação no Roteiro que utiliza o Serviço (0 = quando serviço é p/ o Estágio) |
| SeqSop | Number(004,0) | Não | Sequência |
| CodSer | String(014) | Sim | Código do Serviço  realizado por outra Empresa |
| CodFor | Number(009,0) | Sim | Código do Fornecedor do Serviço |
| TmpPrv | Number(009,3) | Sim | Tempo Previsto p/ o serviço (em dias) |
| QtdHor | Number(011,2) | Sim | Quantidade de horas prevista p/ o serviço |
| QtdHrr | Number(011,2) | Sim | Quantidade real de horas p/ o serviço |
| NumOcp | Number(008,0) | Sim | Número da Ordem de Compra de Serviço gerada p/ necessidade da OP |
| SeqIso | Number(004,0) | Sim | Item da Ordem Compra de Serviço |
| NumSol | Number(009,0) | Sim | Número da solicitação de compra de serviço |
| SeqSol | Number(006,0) | Sim | Sequência do item na solicitação de compras de serviço |
| CodFil | Number(005,0) | Sim | Filial do Serviço |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação do produto |
| QtdPrv | Number(014,5) | Não | Quantidade prevista do produto/derivação para o fornecedor. Atributo |
| QtdUti | Number(014,5) | Sim | Quantidade utilizada do serviço |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqRot
- SeqSop

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900SOP_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900SOP_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

