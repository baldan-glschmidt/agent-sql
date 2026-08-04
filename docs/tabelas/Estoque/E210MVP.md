# E210MVP

## Descrição

Estoques - Movimentos

---

## Resumo

- Campos: 146
- Chave Primária: 6 campo(s)
- Índices: 6
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
| SeqMov | Number(006,0) | Não | Sequência de movimento na data de movimentação |
| DatFec | Date | Não | Data base para o fechamento do estoque |
| SeqFec | Number(006,0) | Não | Sequência base para o fechamento do estoque |
| FilDep | Number(005,0) | Não | Código da filial que o depósito pertence |
| MskDep | String(018) | Sim | Máscara do depósito |
| NivDep | Number(001,0) | Sim | Nível do depósito conforme a máscara |
| CodTns | String(005) | Não | Código da transação de movimentação de estoque |
| EstMov | String(002) | Não | Tipo do estoque movimentado |
| EstEos | String(001) | Não | Entrada ou saída de estoque |
| EstVmv | String(001) | Não | Forma de valorização do movimento |
| OriOrp | String(003) | Sim | Código da Origem de Produto da OP (Quando Movimento é de uma OP específica) |
| NumDoc | Number(009,0) | Sim | Número de documento base da movimentação |
| DatFab | Date | Sim | Data de fabricação do lote |
| HorFab | Number(005,0) | Sim | Hora de fabricação do lote do produto |
| DatEnt | Date | Sim | Data da entrada do produto no depósito |
| DatVlt | Date | Sim | Data de validade do lote |
| HorVlt | Number(005,0) | Sim | Hora de validade do lote do produto |
| CodLot | String(050) | Sim | Código do Lote de Fabricação para estocagem |
| NumSep | String(050) | Sim | Número de série do produto |
| ObsMvp | String(250) | Sim | Observação do fechamento de estoque |
| QtdMov | Number(014,5) | Sim | Quantidade do movimento |
| VlrMov | Number(015,2) | Sim | Valor do movimento |
| QtdAnt | Number(014,5) | Sim | Quantidade em estoque antes do movimento |
| VlrAnt | Number(015,2) | Sim | Valor do estoque antes do movimento |
| QtdEst | Number(014,5) | Sim | Quantidade em estoque total após o movimento |
| VlrEst | Number(015,2) | Sim | Valor em estoque total após o movimento |
| PrmEst | Number(021,10) | Sim | Preço Médio do estoque total |
| ProTrf | String(014) | Sim | Código do produto transferido (para movimentos de transferência) |
| DerTrf | String(007) | Sim | Código da derivação do produto transferido (p/ movimentos de transferência) |
| DepTrf | String(010) | Sim | Código do depósito transferido (para movimentos de transferência) |
| SeqTrf | Number(006,0) | Sim | Sequência de movimento transferido (p/ movimentos de transferência) |
| UsuRes | Number(010,0) | Sim | Número do cadastro do usuário responsável pelo movimento |
| CodCcu | String(009) | Sim | Código do centro de custo do usuário responsável |
| UsuRec | Number(010,0) | Sim | Usuário recebedor do produto solicitado |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| NumPrj | Number(008,0) | Sim | Número do projeto |
| CodFpj | Number(004,0) | Sim | Código da fase do projeto |
| CtaFin | Number(007,0) | Sim | Conta financeira reduzida |
| LctFin | String(001) | Não | Indicativo se o movimento foi lançado no plano financeiro |
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
| UsuDig | Number(010,0) | Sim | Número do cadastro do usuário digitador |
| DatDig | Date | Sim | Data da digitação do movimento |
| HorDig | Number(005,0) | Sim | Hora da digitação do movimento |
| CodLig | Number(009,0) | Sim | Código da ligação do movimento |
| MotMvp | String(250) | Sim | Observação do movimento de estoque |
| DatInv | Date | Sim | Data base do inventário |
| ExpWms | Number(001,0) | Sim | Indicativo se o movimento de estoque foi exportado para o sistema WMS |
| VlrDm1 | Number(014,5) | Sim | Valor Dimensão 1 |
| VlrDm2 | Number(014,5) | Sim | Valor Dimensão 2 |
| VlrDm3 | Number(014,5) | Sim | Valor Dimensão 3 |
| VlrDm4 | Number(014,5) | Sim | Valor Dimensão 4 |
| VlrDm5 | Number(014,5) | Sim | Valor Dimensão 5 |
| VlrDm6 | Number(014,5) | Sim | Valor Dimensão 6 |
| EstWms | String(001) | Sim | Indicativo se a transação de estoque integra o movimento com o WMS |
| EstCoc | String(001) | Sim | Indicativo se o movimento é consignado a clientes |
| EstCof | String(001) | Sim | Indicativo se o movimento é consignado de fornecedores |
| FilPed | Number(005,0) | Sim | Código da filial do item de pedido que gerou o movimento |
| NumPed | Number(008,0) | Sim | Número do pedido do item de pedido que gerou o movimento |
| SeqIpd | Number(004,0) | Sim | Sequência de item do pedido que gerou o movimento |
| UtiRep | String(001) | Sim | Indicativo se movimento já foi utilizado na análise de reposição |
| FilAne | Number(005,0) | Sim | Código da filial da análise de embarque |
| NumAne | Number(012,0) | Sim | Número da análise de embarque |
| NumPfa | Number(009,0) | Sim | Número da pré-fatura |
| SeqPes | Number(003,0) | Sim | Sequência do item na pré-fatura |
| LotDes | String(050) | Sim | Código do Lote do produto no qual o lote em questão foi utilizado |
| CodEtg | Number(004,0) | Sim | Estágio de Produção |
| SeqCmp | Number(004,0) | Sim | Sequência do Componente na utilização |
| AceFec | String(001) | Sim | Indicativo se este movimento foi inserido pelo fechamento dos estoques |
| UltMdi | String(001) | Sim | Indicativo se o movimento em questão é o último movimento do dia para este produto/derivação/depósito |
| CodBem | String(020) | Sim | Código do bem principal |
| FilCle | Number(005,0) | Sim | Código da filial da coleta |
| NumCle | Number(008,0) | Sim | Número da coleta que gerou o movimento |
| VlrCm1 | Number(015,2) | Sim | Valor do movimento de estoque convertido para a moeda estrangeira 1 |
| DatCm1 | Date | Sim | Data da cotação da moeda entrangeira 1 |
| CotCm1 | Number(019,10) | Sim | Cotação da moeda estrangeira 1 |
| VlrCm2 | Number(015,2) | Sim | Valor do movimento de estoque convertido para a moeda estrangeira 2 |
| DatCm2 | Date | Sim | Data da cotação da moeda entrangeira 2 |
| CotCm2 | Number(019,10) | Sim | Cotação da moeda estrangeira 2 |
| SepDes | String(050) | Sim | Número de Série do produto no qual o componente em questão foi utilizado |
| CodSlt | String(010) | Sim | Código do status do lote |
| PerGer | Number(005,2) | Sim | Percentual de germinação |
| PerPur | Number(005,2) | Sim | Percentual de pureza |
| PerUmi | Number(005,2) | Sim | Percentual de umidade |
| DatTes | Date | Sim | Data do teste do produto |
| CodEnd | String(020) | Sim | Código do endereçamento de produto |
| CodSaf | String(010) | Sim | Código da safra |
| CodTrm | String(010) | Sim | Código do tratamento |
| CodBnf | String(010) | Sim | Código do beneficiamento |
| CodCat | String(010) | Sim | Código do categoria do lote |
| VlrIcm | Number(015,2) | Sim | Valor de ICMS |
| PrmIcm | Number(015,6) | Sim | Preço Médio do valor total de ICMS |
| IcmAcf | Number(015,2) | Sim | Valor total de ICMS acumulado para a filial |
| CodPne | Number(004,0) | Sim | Código da peneira |
| CodEtp | Number(004,0) | Sim | Código da espécie/cultura |
| CodCul | Number(004,0) | Sim | Código da cultivar |
| NumTer | String(010) | Sim | Número do termo de conformidade |
| NumAog | String(010) | Sim | Número do atestado de origem genética |
| NumCer | String(010) | Sim | Número do certificado de sementes |
| NumBol | String(010) | Sim | Número do boletim de análise de sementes |
| NumAmo | String(010) | Sim | Número da amostra |
| AmoNum | Number(004,0) | Sim | Número da Amostra |
| FilNfo | Number(005,0) | Sim | Código da filial da nota fiscal de entrada origem da nota fiscal de frete |
| NumNfo | Number(009,0) | Sim | Número da nota fiscal de entrada origem da nota fiscal de frete |
| SnfNfo | String(003) | Sim | Código da série da nota fiscal de entrada origem da nota fiscal de frete |
| ForNfo | Number(009,0) | Sim | Código do fornecedor da nota fiscal de entrada origem da nota fiscal de frete |
| IndFab | String(001) | Sim | Indicativo se o lote se trata de lote de fabricante |
| CodFab | String(010) | Sim | Código do fabricante |
| LotFab | String(050) | Sim | Código de lote do fabricante |
| VltFab | Date | Sim | Data de validade do produto do fabricante |
| ProFab | String(021) | Sim | Código do produto no fabricante |
| CodMar | String(010) | Sim | Código da marca do produto |
| EstNeg | String(001) | Sim | Indicativo se depósito aceita ou não estoque negativo na geração do movimento |
| CalMmf | String(001) | Sim | Indicativo se o movimento calcula média mensal fixa |
| SeqSpr | Number(004,0) | Sim | Sequência do subproduto da OP |
| IndMpc | String(001) | Sim | Indicativo de movimento de atendimento de produto comprado via requisição |
| FilOcr | Number(005,0) | Sim | Filial da ocorrência da assistência técnica |
| NumOcr | Number(009,0) | Sim | Número da Ocorrência (Protocolo) |
| CodMot | Number(006,0) | Sim | Código do motivo da observação ou situação |
| NumFix | Number(009,0) | Sim | Número da Fixação |
| NumLan | Number(009,0) | Sim | Número sequencial do lançamento destinado ao controle do crédito acumulado |
| PerTrf | Number(007,4) | Sim | Percentual do movimento |
| CodFtr | Number(009,0) | Sim | Código do fornecedor para os movimentos consignados em operação triangular |
| IdeUG7 | String(036) | Sim | Identificador único G7 |
| USU_NumLan | Number(009,0) | Sim | Numero Lancamento CAT83 |
| USU_CCUOBS | String(250) | Sim | Centro de Custo Causador Observação |
| USU_CCUCIE | String(001) | Sim | Centro de Custo Causador Ciente |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodDep
- DatMov
- SeqMov

---

## Índices

### E210MVPIndice2

**Tipo:** Não unico

Campos:
- NumNfc
- CodFor
- CodEmp
- FilNfc
- SeqIpc

### E210MVPIndice3

**Tipo:** Não unico

Campos:
- CodSnf
- NumNfv
- CodEmp
- CodFil
- SeqIpv

### E210MVPIndice4

**Tipo:** Não unico

Campos:
- DatMov
- CodEmp
- CodPro
- CodDer
- CodDep
- SeqMov

### E210MVPIndice5

**Tipo:** Não unico

Campos:
- CodEmp
- CodLig
- EstEos
- EstMov

### E210MVPIndice6

**Tipo:** Não unico

Campos:
- FilDep
- UltMdi
- CodPro
- CodDer
- CodDep
- CodEmp
- EstMov
- DatMov

### E210MVPIndice7

**Tipo:** Não unico

Campos:
- NumDoc
- DatMov
- OriOrp
- CodEmp

---

## Relacionamentos

### IR_E210MVP_003

**Tabela:** E210EST

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |
| CodDep | CodDep |

