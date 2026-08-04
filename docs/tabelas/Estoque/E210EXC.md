# E210EXC

## Descrição

Estoques - Movimentos Excluídos

---

## Resumo

- Campos: 29
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto movimentado |
| CodDer | String(007) | Não | Código da derivação do produto movimentado |
| CodDep | String(010) | Não | Código do depósito movimentado |
| DatMov | Date | Não | Data da movimentação do estoque |
| SeqExc | Number(006,0) | Não | Sequência de exclusão do movimento |
| CodTns | String(005) | Não | Código da transação de movimentação de estoque |
| EstMov | String(002) | Não | Tipo do estoque movimentado |
| EstEos | String(001) | Não | Entrada ou saída de estoque |
| OriOrp | String(003) | Sim | Código da Origem de Produto da OP (Quando Movimento é de uma OP específica) |
| NumDoc | Number(009,0) | Sim | Número de documento base da movimentação |
| QtdMov | Number(014,5) | Sim | Quantidade do movimento |
| VlrMov | Number(015,2) | Sim | Valor do movimento |
| NumEme | Number(009,0) | Sim | Número do documento de entrada do movimento de estoque |
| SeqEme | Number(004,0) | Sim | Sequência do produto no documento de movimento de estoque |
| CodFil | Number(005,0) | Sim | Código da filial da nota fiscal de saída |
| CodSnf | String(003) | Sim | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Sim | Número da Nota Fiscal de Saída |
| SeqIpv | Number(003,0) | Sim | Sequência do item na nota fiscal de saída |
| CodCli | Number(009,0) | Sim | Código do cliente para os movimentos consignados |
| FilOcp | Number(005,0) | Sim | Código da filial da Ordem de Compra |
| NumOcp | Number(008,0) | Sim | Número da ordem de compra |
| SeqIpo | Number(004,0) | Sim | Sequência de item da ordem de compra |
| FilNfc | Number(005,0) | Sim | Código da filial da nota fiscal de entrada |
| CodFor | Number(009,0) | Sim | Código do fornecedor para os movimentos consignados |
| NumNfc | Number(009,0) | Sim | Número da Nota Fiscal de Entrada |
| SnfNfc | String(003) | Sim | Código da série da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Sim | Sequência do item da nota fiscal de entrada |
| ExpWms | Number(001,0) | Sim | Indicativo se a exclusão do movimento de estoque foi exportado para o sistema WMS |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodDep
- DatMov
- SeqExc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E210EXC_003

**Tabela:** E210EST

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |
| CodDep | CodDep |

