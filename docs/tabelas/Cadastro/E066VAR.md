# E066VAR

## Descrição

Integrações - Varejo - Parâmetros da Forma de Pagamento

---

## Resumo

- Campos: 56
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFpg | Number(002,0) | Não | Código da forma de pagamento |
| CodEqu | Number(003,0) | Não | Código do equipamento fiscal |
| CodEcf | String(003) | Não | Código da finalizadora para ECF |
| DesEcf | String(016) | Não | Descrição da forma de pagamento para ECF |
| FpgTro | Number(002,0) | Não | Código da forma de pagamento para fornecer troco |
| PerAcr | Number(010,5) | Sim | Percentual de acréscimo da forma de pagamento |
| PerDsc | Number(005,2) | Sim | Percentual de desconto da forma de pagamento |
| MaxTro | Number(015,2) | Sim | Valor máximo para troco da pagamento |
| MaxSan | Number(015,2) | Sim | Valor máximo para realização da sangria no caixa |
| VlrLim | Number(015,2) | Sim | Valor limite aceito para a forma de pagamento |
| BloTit | String(001) | Não | Indicativo se está bloqueada para operação de recebimento de títulos |
| BloDsc | String(001) | Não | Indicativo se a forma de pagamento está bloqueada para cupons com desconto |
| BloCli | String(001) | Não | Indicativo se está bloqueada para cupom com cliente não cadastrado |
| IndBxt | String(001) | Não | Indicativo se deve baixar títulos à vista para esta forma de pagamento |
| NomFav | String(040) | Sim | Nome do favorecido para impressão de cheque |
| TexCpv | String(3999) | Sim | Texto para impressão de comprovante |
| MaxPar | Number(003,0) | Sim | Quantidade máxima de parcelas aceitas na forma de pagamento |
| SitReg | String(001) | Não | Situação do registro |
| DisCxa | String(001) | Sim | a forma de pagamento estará disponível para uso no sistema de caixa. |
| DigVlr | String(001) | Sim | Especifica se o valor para a forma de pagamento pode ser digitado no CAIXA. |
| FinRap | String(001) | Sim | Indica ao caixa que a forma de pagamento é uma finalizadora rápida |
| RebEnt | String(001) | Sim | Indica se a forma de pagamento poderá ser utilizada para recebimento |
| PosSan | String(001) | Sim | Indica se a forma de pagamento poderá ser utilizada para sangria. |
| AbeGav | String(001) | Sim | Indica se deverá ser aberta a gaveta (caso exista). |
| TipFin | Number(001,0) | Sim | Especifica o tipo de financiamento para vendas parceladas recebidas em cartão. |
| VlrMin | Number(015,2) | Sim | Especifica o valor mínimo para a forma de pagamento. |
| LeiCmc | String(001) | Sim | Especifica se a leitura dos dados de cheque será por CMC7 ou Manual |
| ImpBom | String(001) | Sim | Indica se deverá ser impresso a mensagem bom para (Somente cheques) |
| NroVia | Number(002,0) | Sim | Especifica a quantidade de vias adicionais de comprovante |
| TexRec | String(250) | Sim | Texto para impressão de recibo de pagamento. |
| BloCbc | String(001) | Sim | Indica se bloqueia a forma de pagamento em recebimentos por Corresp. Bancário |
| BloRec | String(001) | Sim | Indica se bloqueia a forma de pagamento em recebimentos de Recarga de Celular |
| IndPes | String(001) | Sim | Indicativo se a forma de pagamento possui parcelamento pelo estabelecimento |
| PerPre | String(001) | Sim | Indicativo se a forma de pagamento permite pré-datado |
| ImpCre | String(001) | Sim | Indica se deverá ser impresso comprovante de recebimento |
| ImpTcd | String(001) | Sim | Indica se deverá ser impresso termo de confissão de dívida |
| TexCfd | String(1999) | Sim | Texto para impressão de termo de confissão de dívida |
| ViaCfd | Number(002,0) | Sim | Especifica a quantidade de vias para o termo de confissão de dívida |
| ImpCne | Number(001,0) | Sim | Indica se deverá ser imprimir o carnê. |
| ViaCne | Number(002,0) | Sim | Especifica a quantidade de vias para o carnê |
| ParAdm | String(001) | Sim | Indicativo se a forma de pagamento possui parcelamento pela administradora |
| ParCdc | String(001) | Sim | Indicativo se a forma de pagamento possui parcelamento por CDC |
| PerTrc | String(001) | Sim | Indicativo se a forma de pagamento permite troco |
| CodMoe | String(003) | Sim | Código da moeda ou índice a ser utilizado com esta forma de pagamento |
| ConLcc | String(001) | Sim | Indicativo se consiste o limite de crédito disponível do cliente para esta forma |
| BloVen | String(001) | Sim | Indica se bloqueia a forma de pagamento para vendas |
| ImpPag | String(001) | Sim | Indica se deverá ser impresso comprovante de Pagamento |
| ImpBol | String(001) | Sim | Indica se será impresso boleto para a forma de pagamento |
| CodPor | String(004) | Sim | Código do portador que será atribuído ao título gerado pela forma de pagamento |
| CodCrt | String(002) | Sim | Código da carteira que será atribuída ao título gerado pela forma de pagamento |
| ProTef | String(040) | Sim | Produto TEF da rede de cartão |
| DisPed | String(001) | Sim | Indicatio se a forma de pagamento estará disponível para uso no pedido do Retaguarda |
| ResDsc | String(001) | Sim | Indicativo de aplicação da restrição do percentual de desconto no uso desta forma |
| MaxDsc | Number(005,2) | Sim | Percentual máximo permitido de desconto para uso na venda com esta forma |

---

## Chave Primária

- CodEmp
- CodFil
- CodFpg
- CodEqu

---

## Índices

### E066VARIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFpg

---

## Relacionamentos

### IR_E066VAR_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E066VAR_002

**Tabela:** E066FPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFpg | CodFpg |

