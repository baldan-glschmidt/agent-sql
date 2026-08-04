# E140PAR

## Descrição

Vendas - Notas Fiscais de Saída - Parcelas

---

## Resumo

- Campos: 72
- Chave Primária: 5 campo(s)
- Índices: 3
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| CodPar | Number(003,0) | Não | Sequência de parcelas da nota fiscal de saída |
| CodCrp | String(003) | Sim | Código do grupo a receber |
| NumTit | String(015) | Sim | Número do título a ser gerado no contas a receber |
| CodTpt | String(003) | Sim | Código do tipo de título a ser gerado no contas a receber |
| CodFcr | String(003) | Sim | Código da moeda ou índice como fator de correção (financeiro) |
| DatFcr | Date | Sim | Data da cotação da moeda ou índice para o fator de correção (financeiro) |
| VctPar | Date | Não | Data de vencimento da parcela da nota fiscal de saída |
| VlrPar | Number(015,2) | Não | Valor da parcela da nota fiscal de saída |
| PerDdp | Number(005,2) | Sim | Percentual de desconto da parcela da nota fiscal de saída |
| QtdDdd | Number(003,0) | Sim | Quantidade de dias de tolerância para o desconto da parcela |
| CodPor | String(004) | Não | Código do portador a ser lançado o título no contas a receber |
| CodCrt | String(002) | Não | Código da carteira a ser lançado o título no contas a receber |
| CodNtg | Number(004,0) | Sim | Código da natureza de gasto |
| ObsPar | String(250) | Sim | Texto da observação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| GerBai | String(001) | Sim | Indicativo se, no momento da geração do título, o mesmo é baixado automaticamente. |
| TnsBai | String(005) | Sim | Código da Transação de Baixa Automática |
| DatNeg | Date | Sim | Data base dos valores negociados (data até) |
| DscNeg | Number(015,2) | Sim | Valor do desconto negociado a ser concedido ao título a receber |
| CatTef | String(128) | Sim | Código de Autorização da Transação para Pagamentos Eletrônicos |
| NsuTef | String(100) | Sim | Número Sequencial Único da Transação TEF (Host - Operadora) |
| CodSac | Number(014,0) | Sim | Código do sacado |
| DocIdeSac | String(014) | Sim | Código do sacado |
| CheBan | String(003) | Sim | Número do banco na FEBRABAN do cheque |
| CheAge | String(007) | Sim | Número da agência do banco do cheque |
| CheCta | String(014) | Sim | Número da conta no banco do cheque |
| CheNum | String(010) | Sim | Número do cheque no banco |
| CodBar | String(050) | Sim | Código de barras do cheque (CMC7) |
| CatExt | String(100) | Sim | Código de autorização externo |
| CodOpe | Number(004,0) | Sim | Código da operadora |
| CarCov | String(100) | Sim | Número do cartão convênio |
| CarPre | String(050) | Sim | Código do Cartão Presente |
| CodCnv | Number(004,0) | Sim | Código do convênio |
| VlrTro | Number(015,2) | Sim | Valor do troco dado ao cliente da venda. |
| FpgTro | Number(002,0) | Sim | Código da forma de pagamento |
| DepCnv | Number(004,0) | Sim | Código do Dependente |
| VlrDdp | Number(015,2) | Sim | Valor do desconto da parcela da nota fiscal |
| DscAnt | Number(004,2) | Sim | Percentual de desconto por antecipação para os títulos gerados |
| DscPon | Number(004,2) | Sim | Percentual de desconto por pontualidade para os títulos gerados |
| JurVen | String(001) | Sim | Indicativo se o sistema deve calcular juros/multa desde a data da venda |
| DatPpt | Date | Sim | Data do provável pagamento do título |
| LocTit | String(050) | Sim | Localizador do título para retaguarda/loja |
| VlrInt | Number(015,2) | Sim | Valor de intermediação de serviços da parcela |
| NumPfi | String(015) | Sim | Número da proposta da financeira que originou o título |
| QtdPar | Number(003,0) | Sim | Quantidade de parcelas escolhidas no cartão |
| TipCar | String(001) | Sim | Tipo do cartão utilizado pela operadora |
| ParTit | Number(003,0) | Sim | Número da parcela |
| CodFin | Number(004,0) | Sim | Código da financeira que é a detentora da parcela |
| EntPar | String(001) | Sim | Parcela é uma entrada |
| TitBan | String(020) | Sim | Número do título no banco (nosso número) |
| JrsNeg | Number(015,2) | Sim | Valor dos juros negociados |
| MulNeg | Number(015,2) | Sim | Valor da multa negociada |
| OutNeg | Number(015,2) | Sim | Valor de outros valores negociados |
| TipInt | String(001) | Sim | Tipo Integração do processo de pagamento com o sistema de automação da empresa |
| CgcCre | String(014) | Sim | CNPJ da Credenciadora de cartão de crédito e/ou débito |
| BanOpe | String(002) | Sim | Bandeira da operadora de cartão de crédito e/ou débito |
| IndPag | String(001) | Sim | Indicativo da forma de pagamento |
| IdeTxi | String(035) | Sim | Identificação da Transação - TXID PIX exclusivo integração varejo / GS |
| CgcTpp | Number(014,0) | Sim | CNPJ do estabelecimento onde o pagamento foi processado |
| DocIdeTpp | String(014) | Sim | CNPJ do estabelecimento onde o pagamento foi processado |
| UfsPgr | String(002) | Sim | Sigla da UF do CNPJ do estabelecimento onde o pagamento foi processado |
| CgcBpr | Number(014,0) | Sim | CNPJ do estabelecimento beneficiário do pagamento |
| DocIdeBpr | String(014) | Sim | CNPJ do estabelecimento beneficiário do pagamento |
| IdeTpg | String(040) | Sim | Identificador do terminal de pagamento |
| IdeSac | String(050) | Sim | Identificador único do sacado |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- CodPar

---

## Índices

### E140PARIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf
- CodPar

### E140PARIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodPor

### E140PARIndice3

**Tipo:** Não unico

Campos:
- CodCrt

---

## Relacionamentos

### IR_E140PAR_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

### IR_E140PAR_004

**Tabela:** E020PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| CodPar | CodPar |

### IR_E140PAR_014

**Tabela:** E039POR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPor | CodPor |

### IR_E140PAR_015

**Tabela:** E033CRT

| Origem | Destino |
|--------|---------|
| CodCrt | CodCrt |

