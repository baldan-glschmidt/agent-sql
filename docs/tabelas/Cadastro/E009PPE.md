# E009PPE

## Descrição

Tabelas - Parâmetros por Estados

---

## Resumo

- Campos: 61
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| SigUfs | String(002) | Não | Sigla do estado |
| CodFil | Number(005,0) | Não | Código da filial |
| InsEst | String(025) | Sim | Inscrição estadual no estado |
| PerRep | Number(006,4) | Sim | Percentual de repasse |
| LimIcm | Number(015,2) | Sim | Valor limite de ICMS |
| IcmSco | Number(004,2) | Sim | Percentual de ICMS de saída para contribuintes |
| IcmSnc | Number(004,2) | Sim | Percentual de ICMS de saída para não contribuinte |
| IcmEco | Number(004,2) | Sim | Percentual de ICMS de entrada para contribuinte |
| IcmEnc | Number(004,2) | Sim | Percentual de ICMS de entrada para não contribuinte |
| VenTfp | String(005) | Sim | Transação padrão para NF saída de produtos do estabelecimento a contribuinte |
| VenTfn | String(005) | Sim | Transação padrão para NF saída de produtos do estabelecimento não contribuinte |
| VenTpa | String(005) | Sim | Transação padrão para NF saída de produtos adquiridos p/ comercialização a contribuinte |
| VenTpn | String(005) | Sim | Transação padrão para NF saída de produtos adquiridos p/ comercialização a não contribuinte |
| VenTfs | String(005) | Sim | Transação padrão para NF saída de serviços |
| VenTdp | String(005) | Sim | Transação padrão de devolução de itens de produto |
| VenTds | String(005) | Sim | Transação padrão de devolução de itens de serviço |
| TnsRem | String(005) | Sim | Transação para Notas Fiscais de Remessa |
| CprTnp | String(005) | Sim | Transação padrão para NF de entrada de produtos adquirido |
| CprTns | String(005) | Sim | Transação padrão para nota fiscal de entrada de serviço |
| CprTdp | String(005) | Sim | Transação padrão de devolução de itens de produto |
| CprTds | String(005) | Sim | Transação padrão de devolução de itens de serviço |
| TnsRet | String(005) | Sim | Transação para Notas Fiscais de Retorno |
| VenDsc | Number(005,2) | Sim | Percentual a acrescentar ou diminuir para formação do preço de venda |
| PerDzf | Number(005,2) | Sim | Percentual de desconto Suframa para as notas fiscais de entrada |
| ForRsu | Number(009,0) | Sim | Código do fornecedor padrão para geração do título de retenção de ICMS Substituto |
| TptRsu | String(003) | Sim | Tipo de título padrão para geração do título de retenção de ICMS Substituto |
| TnsRsu | String(005) | Sim | Transação padrão para geração do título de retenção de ICMS Substituto |
| ImpRsu | String(003) | Sim | Código do imposto para cálculo do vencimento de retenção de ICMS Substituto |
| TnsCfp | String(005) | Sim | Transação de produto para NF de saída via cupom fiscal para contribuintes |
| TnsCfs | String(005) | Sim | Transação de serviço para NF de saída via cupom fiscal para contribuintes |
| ImpDav | String(001) | Sim | Permitir imprimir DAV/DAV-OS no ERP |
| ImpPdr | Number(001,0) | Sim | Impressora padrão para DAV/DAV-OS |
| TnsAtp | String(005) | Sim | Código da transação de nota fiscal de assistência técnica de produto |
| TnsAts | String(005) | Sim | Código da transação de nota fiscal de assistência técnica de serviço |
| IcmInt | Number(004,2) | Sim | Percentual de ICMS interestadual para operações com produtos importados |
| BlqNfc | String(001) | Sim | Indicativo se o sistema deve bloquear nota fiscal de consumidor |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal para nota de consumidor que gerou cupom |
| VenTdt | String(005) | Sim | Transação de Devolução de Produto em Taxa |
| CprTct | String(005) | Sim | Transação de Compra de Produto em Taxa |
| VenTrf | String(005) | Sim | Transação padrão para NF saída de transferência entre filiais via devolução |
| VenTsm | String(005) | Sim | Transação padrão para NF de simples remessa |
| TnsDtp | String(005) | Sim | Transação padrão de devolução para transferência entre produtores |
| TnsDfp | String(005) | Sim | Transação padrão de devolução para fixação de preços |
| IcmInd | Number(005,2) | Sim | Percentual de ICMS interno para estado de destino |
| TipBda | Number(002,0) | Sim | Tipo da base de cálculo do diferêncial de aliquota do ICMS. |
| TnsAst | String(005) | Sim | Transação mercadoria de subst. trib. na condição de contribuinte substituído |
| TnsRcp | String(005) | Sim | Transação de recebimento para o produto da nota fiscal de entrada |
| TnsPgp | String(005) | Sim | Transação de pagamento para o produto da nota fiscal de entrada |
| TnsRcs | String(005) | Sim | Transação de recebimento para o serviço da nota fiscal de entrada |
| TnsPgs | String(005) | Sim | Transação de pagamento para o serviço da nota fiscal de entrada |
| TncPnc | String(005) | Sim | Transação de produto para NF de saída via cupom fiscal para não contribuintes |
| TncSnc | String(005) | Sim | Transação de serviço para NF de saída via cupom fiscal para não contribuintes |
| VenTcg | String(005) | Sim | Transação padrão para NF saída de produtos adquiridos em consignação mercantil |
| FcpDfa | String(001) | Sim | Considerar % FCP no cálculo de diferencial de alíquota em operações de compra de imobilizado ou consumo próprio |
| GuiFcp | String(001) | Sim | Indicativo que deve gerar a guia de FCP separadamente da guia do ICMS DIFAL. |
| USU_PrcPcc | Number(005,2) | Não | Percentual a acrescentar ou diminuir p/ formacao Preco Venda Pecas Conveniadas |
| USU_PrcPro | Number(005,2) | Não | Percentual a acrescentar ou diminuir p/ formacao Preco Venda Prod.Nao Conveniado |
| USU_PrcPec | Number(005,2) | Não | Percentual a acrescentar ou diminuir p/ formacao Preco Venda Pecas Nao Conven. |
| USU_PrcPrc | Number(005,2) | Não | Percentual a acrescentar ou diminuir p/ formacao Preco Venda Produto Conveniado |
| USU_aliqicms | Number(006,3) | Sim | Carga Tributaria Icms |

---

## Chave Primária

- CodEmp
- SigUfs
- CodFil

---

## Índices

### E009PPEIndice1

**Tipo:** Não unico

Campos:
- SigUfs

---

## Relacionamentos

### IR_E009PPE_001

**Tabela:** E007UFS

| Origem | Destino |
|--------|---------|
| SigUfs | SigUfs |

