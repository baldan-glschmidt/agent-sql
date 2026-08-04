# E210OBS

## Descrição

Estoques - Observações

---

## Resumo

- Campos: 67
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto movimentado |
| CodDer | String(007) | Não | Código da derivação do produto movimentado |
| CodDep | String(010) | Não | Código do depósito movimentado |
| DatObs | Date | Não | Data base da observação |
| SeqObs | Number(006,0) | Não | Sequência da observação |
| TipObs | String(001) | Não | Tipo da observação |
| TexObs | String(250) | Sim | Texto da observação |
| CodTns | String(005) | Sim | Código da transação de movimentação de estoque |
| EstMov | String(002) | Sim | Tipo do estoque movimentado |
| EstEos | String(001) | Sim | Entrada ou saída de estoque |
| DatMov | Date | Sim | Data do movimento do estoque |
| SeqMov | Number(006,0) | Sim | Sequência de movimento na data de movimentação |
| DatFec | Date | Sim | Data base para o fechamento do estoque |
| SeqFec | Number(006,0) | Sim | Sequência base para o fechamento do estoque |
| FilDep | Number(005,0) | Sim | Código da filial que o depósito pertence |
| MskDep | String(018) | Sim | Máscara do depósito |
| NivDep | Number(001,0) | Sim | Nível do depósito conforme a máscara |
| EstVmv | String(001) | Sim | Forma de valorização do movimento |
| DatFab | Date | Sim | Data de fabricação do lote |
| DatEnt | Date | Sim | Data da entrada do produto no depósito |
| DatVlt | Date | Sim | Data de validade do lote de fabricação |
| CodLot | String(050) | Sim | Código do lote de fabricação para estocagem |
| NumSep | String(050) | Sim | Número de série do produto |
| NumDoc | Number(009,0) | Sim | Número de documento base da movimentação |
| ObsMvp | String(250) | Sim | Texto da observação do movimento de estoque |
| QtdMov | Number(014,5) | Sim | Quantidade de movimento do estoque |
| VlrMov | Number(015,2) | Sim | Valor do movimento de estoque |
| QtdAnt | Number(014,5) | Sim | Quantidade em estoques antes do movimento |
| VlrAnt | Number(015,2) | Sim | Valor do estoque antes do movimento |
| QtdEst | Number(014,5) | Sim | Quantidade em estoque total após o movimento |
| VlrEst | Number(015,2) | Sim | Valor em estoque total após o movimento |
| PrmEst | Number(021,10) | Sim | Preço Médio do estoque total |
| ProTrf | String(014) | Sim | Código do produto transferido para movimentos de transferência |
| DerTrf | String(007) | Sim | Código da derivação do produto transferido p/ movimentos de transferência |
| DepTrf | String(010) | Sim | Código do depósito transferido para movimentos de transferência |
| UsuRes | Number(010,0) | Sim | Número do cadastro do usuário responsável pelo movimento |
| CodCcu | String(009) | Sim | Código do centro de custo do usuário responsável |
| UsuRec | Number(010,0) | Sim | Usuário recebedor do produto solicitado |
| NumPrj | Number(008,0) | Sim | Número do projeto |
| CodFpj | Number(004,0) | Sim | Código da fase do projeto |
| CtaFin | Number(007,0) | Sim | Conta financeira reduzida |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| LctFin | String(001) | Sim | Indicativo se o movimento foi lançado no plano financeiro |
| NumLot | Number(009,0) | Sim | Número do lote contábil |
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
| OriOrp | String(003) | Sim | Código da Origem de Produto da OP (Quando Movimento é de uma OP específica) |
| UsuDig | Number(010,0) | Sim | Número do cadastro do usuário digitador |
| DatDig | Date | Sim | Data da digitação do movimento |
| HorDig | Number(005,0) | Sim | Hora da digitação do movimento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodDep
- DatObs
- SeqObs

---

## Índices

### E210OBSIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- DatObs
- CodPro
- CodDer
- CodDep
- SeqObs

---

## Relacionamentos

### IR_E210OBS_002

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

