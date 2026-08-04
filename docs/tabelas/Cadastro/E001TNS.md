# E001TNS

## Descrição

Tabelas - Transações

---

## Resumo

- Campos: 258
- Chave Primária: 2 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| DesTns | String(060) | Não | Descrição da transação |
| DetTns | String(599) | Não | Detalhamento da transação |
| LisMod | String(003) | Não | Módulo pertencente da transação |
| AceMan | String(001) | Não | Indicativo se a transação aceita ou não lançamentos manuais |
| TnsTel | String(005) | Sim | Código da transação para estorno da transação principal |
| CodFct | String(005) | Sim | Código da forma de contabilização |
| ForRat | Number(001,0) | Sim | Forma de rateio nos lançamentos de origem |
| TnsApj | String(001) | Sim | Indicativo se movimento da transação atualiza controle de projetos |
| CriCtb | String(001) | Sim | Critério de contabilização |
| CodNtg | Number(004,0) | Sim | Código da natureza de gasto |
| CodReg | Number(004,0) | Sim | Código da Regra |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| ComNop | String(005) | Sim | Natureza de operação correspondente (CFOP/CFPS) |
| ComDir | String(001) | Sim | Transação considera valor arredondamento na base do IRRF |
| ComOir | String(001) | Sim | Transação considera outras despesas na base do IRRF |
| ComEir | String(001) | Sim | Transação considera os encargos na base do IRRF |
| ComOdr | String(001) | Sim | Transação considera outras despesas destacadas na base do IRRF |
| ComDin | String(001) | Sim | Transação considera valor arredondamento na base do INSS/Funrural |
| ComOin | String(001) | Sim | Transação considera outras despesas na base do INSS/Funrural |
| ComEin | String(001) | Sim | Transação considera os encargos na base do INSS |
| ComOdn | String(001) | Sim | Transação considera outras despesas destacadas na base do INSS/Funrural |
| ComDis | String(001) | Sim | [INUTILIZADO] - Transação considera valor arredondamento na base do ISS |
| ComOis | String(001) | Sim | [INUTILIZADO] - Transação considera outras despesas na base do ISS |
| ComEis | String(001) | Sim | [INUTILIZADO] - Transação considera os encargos na base do ISS |
| ComOds | String(001) | Sim | [INUTILIZADO] - Transação considera outras despesas destacadas na base do ISS |
| VenUpd | String(001) | Sim | Transação atualiza histórico último pedido |
| VenTcf | String(001) | Sim | Aplicação da natureza de operação |
| VenDev | String(001) | Sim | Transação é de nota fiscal saída por devolução |
| VenFat | String(001) | Sim | Transação considera nota fiscal saída como faturamento e p/ histórico |
| VenAcp | String(001) | Sim | Transação de nota fiscal saída exige pedido de venda |
| VenIcm | String(001) | Sim | Indicativo se a transação isenta do ICMS o item da nota fiscal |
| VenIbi | String(001) | Sim | Transação considera valor do IPI na base do ICMS |
| VenFre | String(001) | Sim | Transação considera o frete na base do ICMS |
| VenSeg | String(001) | Sim | Transação considera o seguro na base do ICMS |
| VenEmb | String(001) | Sim | Transação considera as embalagens na base do ICMS |
| VenEnc | String(001) | Sim | Transação considera os encargos financeiros na base do ICMS |
| VenOut | String(001) | Sim | Transação considera outras despesas na base do ICMS |
| VenDar | String(001) | Sim | Transação considera o valor de arredondamento na base do ICMS |
| VenFrd | String(001) | Sim | Transação considera o frete destacado na base do ICMS |
| VenOud | String(001) | Sim | Transação considera outras despesas destacadas na base do ICMS |
| VenEnt | String(001) | Sim | Forma de escrituração para não tributadas |
| VenIpi | String(001) | Sim | Indicativo se a transação isenta do IPI o item da nota fiscal |
| VenFri | String(001) | Sim | Transação considera o frete na base do IPI |
| VenSei | String(001) | Sim | Transação considera o seguro na base do IPI |
| VenEmi | String(001) | Sim | Transação considera a embalagem na base do IPI |
| VenEni | String(001) | Sim | Transação considera os encargos na base do IPI |
| VenOui | String(001) | Sim | Transação considera outras despesas na base do IPI |
| VenDai | String(001) | Sim | Transação considera valor arredondamento na base do IPI |
| VenFdi | String(001) | Sim | Transação considera o frete destacado na base do IPI |
| VenOdi | String(001) | Sim | Transação considera outras despesas destacadas na base do IPI |
| VenLir | Number(009,2) | Sim | Valor mínimo do IRRF considerado na nota fiscal de saída |
| VenIrf | String(001) | Sim | Indicativo de como a Transação considera o valor IRRF do total da nota fiscal saída |
| VenIfu | String(001) | Sim | Indicativo de como a Transação considera o valor INSS/Funrural do total da nota fiscal saída |
| VenIss | String(001) | Sim | [INUTILIZADO] - Transação considera o ISS na nota fiscal de saída |
| VenDep | String(010) | Sim | Código do depósito padrão para nota fiscal de saída |
| VenEbp | Number(004,0) | Sim | Código da embalagem padrão para nota fiscal de saída |
| VenMs1 | Number(004,0) | Sim | Código da 1ª mensagem padrão da nota fiscal de saída |
| VenMs2 | Number(004,0) | Sim | Código da 2ª mensagem padrão da nota fiscal de saída |
| VenMs3 | Number(004,0) | Sim | Código da 3ª mensagem padrão da nota fiscal de saída |
| VenMs4 | Number(004,0) | Sim | Código da 4ª mensagem padrão da nota fiscal de saída |
| VenTpt | String(003) | Sim | Tipo de título gerado no contas a receber pela transação de NF saída |
| VenMoe | String(003) | Sim | Código de moeda padrão para os títulos gerados no contas a receber |
| VenTnf | String(001) | Sim | Transação soma o valor do item no valor total do financeiro |
| VenCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| VenFin | Number(007,0) | Sim | Conta financeira a classificar |
| VenRed | Number(007,0) | Sim | Conta contábil a classificar |
| VenCcu | String(009) | Sim | Centro de custo a classificar |
| EstEos | String(001) | Sim | Indicativo se a transação é de entrada ou saída |
| EstMov | String(002) | Sim | Tipo do estoque movimentado pela transação |
| EstVmv | String(001) | Sim | Forma de valorização dos movimentos dos estoques de produtos |
| EstCon | String(001) | Sim | Indicativo se a transação considera movimento para efeito de consumo |
| EstCoc | String(001) | Sim | Indicativo se a transação movimenta estoques consignados a clientes |
| EstCof | String(001) | Sim | Indicativo se a transação movimenta estoques consignados de fornecedores |
| EstPru | String(001) | Sim | Indicativo se a transação atualiza preço da última entrada |
| EstPrr | String(001) | Sim | Indicativo se a transação atualiza preço de reposição |
| EstDep | String(010) | Sim | Código do depósito padrão para movimentação dos estoques |
| EstTrf | String(005) | Sim | Transação correspondente de transferência de estoques |
| EstCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| EstFin | Number(007,0) | Sim | Conta financeira a classificar |
| EstRed | Number(007,0) | Sim | Conta contábil a classificar |
| EstCcu | String(009) | Sim | Centro de custo a classificar |
| EstApf | String(001) | Sim | Indicativo se movimento de estoque atualiza plano financeiro |
| RecDec | String(001) | Sim | Transação adiciona (entradas) ou subtrai (baixas) dos saldos duplicatas, outros ou créditos |
| RecAdc | String(001) | Sim | Transação é de crédito de cliente |
| RecTpb | String(002) | Sim | Tipo de baixa gerada pela transação no contas a receber |
| RecAsh | String(001) | Sim | Transação atualiza saldos nos históricos dos clientes, grupo e portador |
| RecHis | String(001) | Sim | Transação atualiza outros dados nos históricos dos clientes |
| RecCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| RecFin | Number(007,0) | Sim | Conta financeira a classificar |
| RecRed | Number(007,0) | Sim | Conta contábil a classificar |
| RecCcu | String(009) | Sim | Centro de custo a classificar |
| CprIcm | String(001) | Sim | Indicativo se a transação isenta do ICMS o item da nota fiscal |
| CprUoc | String(001) | Sim | Transação atualiza históricos das últimas compras |
| CprHen | String(001) | Sim | Transação atualiza históricos das entradas de notas fiscais |
| CprTcf | String(001) | Sim | Aplicação da natureza de operação |
| CprDev | String(001) | Sim | Transação é de nota fiscal de entrada de devolução |
| CprAoc | String(001) | Sim | Transação nota fiscal de entrada exige ordem de compra |
| CprLir | Number(009,2) | Sim | Valor mínimo do IRRF considerado na nota fiscal de entrada |
| CprIrf | String(001) | Sim | Indicativo de como a Transação considera o valor IRRF do total da nota fiscal de entrada |
| CprIfu | String(001) | Sim | Ind. de como a Transação considera o valor INSS/Funrural do total da NFE/OC |
| CprIss | String(001) | Sim | Indicativo de como a Transação considera o valor do ISS na nota fiscal entrada |
| CprDep | String(010) | Sim | Código do depósito padrão para entrada das notas fiscais |
| CprMs1 | Number(004,0) | Sim | Código da 1ª mensagem padrão da nota fiscal de entrada |
| CprMs2 | Number(004,0) | Sim | Código da 2ª mensagem padrão da nota fiscal de entrada |
| CprMs3 | Number(004,0) | Sim | Código da 3ª mensagem padrão da nota fiscal de entrada |
| CprMs4 | Number(004,0) | Sim | Código da 4ª mensagem padrão da nota fiscal de entrada |
| CprTpt | String(003) | Sim | Tipo de título gerado no contas a pagar pela transação NF de entrada |
| CprMoe | String(003) | Sim | Código moeda padrão para os títulos gerados no contas a pagar |
| CprIbi | String(001) | Sim | Transação considera o IPI na base de ICMS |
| CprFre | String(001) | Sim | Transação considera frete na base do ICMS |
| CprSeg | String(001) | Sim | Transação considera o seguro na base do ICMS |
| CprEmb | String(001) | Sim | Transação considera a embalagem na base do ICMS |
| CprEnc | String(001) | Sim | Transação considera os encargos financeiro na base do ICMS |
| CprOut | String(001) | Sim | Transação considera as outras despesas na base do ICMS |
| CprDar | String(001) | Sim | Transação considera arredondamento na base do ICMS |
| CprFrd | String(001) | Sim | Transação considera o frete destacado na base do ICMS |
| CprOud | String(001) | Sim | Transação considera outras despesas destacadas na base do ICMS |
| CprRic | String(001) | Sim | Indicativo se a transação recupera o ICMS |
| CprCda | String(001) | Sim | Indicativo se a transação calcula a diferença de alíquota |
| CprEnt | String(001) | Sim | Forma de escrituração para não tributadas |
| CprFri | String(001) | Sim | Transação considera o frete na base do IPI |
| CprSei | String(001) | Sim | Transação considera o seguro na base do IPI |
| CprEmi | String(001) | Sim | Transação considera a embalagem na base do IPI |
| CprEni | String(001) | Sim | Transação considera os encargos na base do IPI |
| CprOui | String(001) | Sim | Transação considera outras despesas na base do IPI |
| CprDai | String(001) | Sim | Transação considera o arredondamento na base do IPI |
| CprFdi | String(001) | Sim | Transação considera o frete destacado na base do IPI |
| CprOdi | String(001) | Sim | Transação considera outras despesas destacadas na base do IPI |
| CprRip | String(001) | Sim | Indicativo se a transação recupera o IPI |
| CprTnf | String(001) | Sim | Transação soma o valor do item no valor total do financeiro |
| CprCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| CprFin | Number(007,0) | Sim | Conta financeira a classificar |
| CprRed | Number(007,0) | Sim | Conta contábil a classificar |
| CprCcu | String(009) | Sim | Centro de custo a classificar |
| PagDec | String(001) | Sim | Transação adiciona (Entradas) ou subtrai (Baixas) dos saldos duplicatas, outros ou créditos |
| PagAdf | String(001) | Sim | Indicativo se a transação é de crédito a fornecedor ou representante |
| PagTpb | String(002) | Sim | Tipo de baixa gerada pela transação no contas a pagar |
| PagAsh | String(001) | Sim | Indicativo se a transação atualiza saldos nos históricos dos fornecedores |
| PagHis | String(001) | Sim | Indicativo se a transação atualiza outros dados nos históricos dos fornecedores |
| PagVbc | String(001) | Sim | Formação do valor base para cálculo do IR nas comissões |
| PagTir | String(001) | Sim | Indicativo se a transação é de imposto de renda para comissões |
| PagCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| PagFin | Number(007,0) | Sim | Conta financeira a classificar |
| PagRed | Number(007,0) | Sim | Conta contábil a classificar |
| PagCcu | String(009) | Sim | Centro de custo a classificar |
| PagTco | String(001) | Sim | Indicativo se a transação é de COFINS |
| PagGir | String(001) | Sim | Indicativo se a transação gera título de IRF |
| PagItr | String(001) | Sim | Indicativo se a transação é de IRF |
| PagVbs | String(001) | Sim | Formação do valor base para cálculo do ISS nas comissões |
| PagDcc | String(001) | Sim | Indicativo se a Comissão é de Débito ou Crédito |
| PagTis | String(001) | Sim | Indicativo se a transação é de ISS |
| CxbDec | String(001) | Sim | Transação na Tesouraria é de Débito ou Crédito |
| CxbTrf | String(005) | Sim | Transação correspondente de transferência no caixa e bancos |
| CxbChe | String(001) | Sim | Transação é de débito por cheque ou aviso de débito |
| CxbCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| CxbFin | Number(007,0) | Sim | Conta financeira de receita a classificar |
| CxbFdc | Number(007,0) | Sim | Conta financeira de despesa a classificar |
| CxbRed | Number(007,0) | Sim | Conta contábil de receita a classificar |
| CxbRdc | Number(007,0) | Sim | Conta contábil de despesa a classificar |
| CxbCcu | String(009) | Sim | Centro de custo a classificar para a conta de receita |
| CxbCdc | String(009) | Sim | Centro de custo a classificar para a conta de despesa |
| CxbTmf | String(001) | Sim | Indicativo se a transação é de CPMF |
| PrjCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| PrjFin | Number(007,0) | Sim | Conta financeira de receita a classificar |
| PrjFdc | Number(007,0) | Sim | Conta financeira de despesa a classificar |
| PrjCcu | String(009) | Sim | Centro de custo a classificar para a conta de receita |
| PrjCdc | String(009) | Sim | Centro de custo a classificar para a conta de despesa |
| PrjDec | String(001) | Sim | Transação do Movimento é de Débito ou Crédito |
| PatMov | Number(002,0) | Sim | Tipo de movimentação do bem no patrimônio |
| PatTrf | String(001) | Sim | Tipo de transferência do bem |
| PatDed | String(001) | Sim | Tipo de desdobramento do bem |
| PatBai | String(001) | Sim | Tipo de baixa do bem |
| PatCal | String(001) | Sim | Indicativo se a transação executa cálculo |
| PatRca | Number(004,0) | Sim | Código da regra para formação dos cálculos específicos da transação |
| PatDat | String(001) | Sim | Indicativo se a data de referência é igual a data do último cálculo |
| PatAcr | String(001) | Sim | Tipo de Acréscimo |
| PatTpd | String(001) | Sim | Indicativo se a transação é a padrão do tipo de movimento (PatMov) |
| PatMot | Number(006,0) | Sim | Código do motivo para observação referente a transação |
| SitTns | String(001) | Sim | Situação da transação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| ComIir | String(001) | Não | Indica se o ISS compõe a base de cálculo do IRRF |
| CprTin | String(001) | Sim | (descontinuado) Indicativo se no fechamento da nota fiscal deve ser gerado título de INSS/Funrural |
| ComLin | Number(009,2) | Sim | Valor mínimo do INSS considerado na nota fiscal |
| FveTns | String(010) | Sim | Hierarquia da Forma de Venda |
| FveDec | String(001) | Sim | Indicativo se pode liberar formas de vendas inferiores |
| VenLgt | String(001) | Sim | Indicativo se a guia de tráfego deve ser liberada automaticamente na geração da PF ou NF |
| CprTis | String(001) | Sim | (descontinuado) Indicativo se no fechamento da nota fiscal deve ser gerado título de ISS |
| VenTip | String(001) | Sim | Tipo da Venda |
| ComIng | String(001) | Sim | Indicativo se o item de serviço da nota fiscal deve ser considerado como um desconto e diminuir os valores do total da nota |
| CprRpi | String(001) | Sim | [INUTILIZADO] - Indicativo se a transação recupera o PIS |
| CprIbp | String(001) | Sim | [INUTILIZADO] - Transação considera o IPI na base de PIS |
| CprFrp | String(001) | Sim | [INUTILIZADO] - Transação considera frete na base do PIS |
| CprSep | String(001) | Sim | [INUTILIZADO] - Transação considera o seguro na base do PIS |
| CprEmp | String(001) | Sim | [INUTILIZADO] - Transação considera a embalagem na base do PIS |
| CprEnp | String(001) | Sim | [INUTILIZADO] - Transação considera os encargos financeiro na base do PIS |
| CprOup | String(001) | Sim | [INUTILIZADO] - Transação considera as outras despesas na base do PIS |
| CprDap | String(001) | Sim | [INUTILIZADO] - Transação considera arredondamento na base do PIS |
| CprFdp | String(001) | Sim | [INUTILIZADO] - Transação considera o frete destacado na base do PIS |
| CprOdp | String(001) | Sim | [INUTILIZADO] - Transação considera outras despesas destacadas na base do PIS |
| ComNat | String(005) | Sim | Nova natureza de operação (CFOP) correspondente a transação(utilizada devido transição conforme ajuste SINIEF 7/2002) |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| ComStr | String(003) | Sim | Situação tributária padrão para a transação |
| ComTic | String(003) | Sim | Código do ICMS especial padrão para a transação |
| ComTrd | String(003) | Sim | Código de redução de impostos |
| ComTst | String(003) | Sim | Código do ICMS substituído padrão para a transação |
| CprTie | String(001) | Sim | (descontinuado) Indicativo se no fechamento da nota fiscal deve ser gerado título de INSS para a parte da Empresa |
| ComSip | Number(001,0) | Sim | Indicativo se ICMS deve ser somado ou diminuído do preço unitário ou do valor líquido do item |
| EstCqm | String(001) | Sim | Indicativo se deve ser considerada a quantidade ao fazer o movimento de estoque(Somente quando valorizados pelo movimento) |
| ComCim | String(001) | Sim | Indicativo se deve ser considerado apenas os valores de impostos para o movimento de estoque |
| ComSsg | String(001) | Sim | Soma seguro sobre frete |
| CprCve | String(001) | Sim | Indicativo se o item da nota fiscal de entrada deve ser considerado ao fazer a valorização dos estoques pelo conhecimento de frete |
| VenEco | String(001) | Sim | [INUTILIZADO] - Transação considera os encargos financeiros na base do Cofins |
| VenOuc | String(001) | Sim | [INUTILIZADO] - Transação considera as outras despesas na base do Cofins |
| VenDac | String(001) | Sim | [INUTILIZADO] - Transação considera arredondamento na base do Cofins |
| VenOdc | String(001) | Sim | [INUTILIZADO] - Transação considera outras despesas destacadas na base do Cofins |
| VenLco | Number(009,2) | Sim | [INUTILIZADO] - Valor mínimo Cofins Retido considerado na nota fiscal de saída |
| VenCof | String(001) | Sim | [INUTILIZADO]- Transação considera valor Cofins Retido no total da nota de saída |
| VenEnp | String(001) | Sim | [INUTILIZADO] - Transação considera os encargos financeiros na base do PIS |
| VenOup | String(001) | Sim | [INUTILIZADO] - Transação considera as outras despesas na base do PIS |
| VenDap | String(001) | Sim | [INUTILIZADO] - Transação considera arredondamento na base do PIS |
| VenOdp | String(001) | Sim | [INUTILIZADO] - Transação considera outras despesas destacadas na base do PIS |
| VenLpi | Number(009,2) | Sim | [INUTILIZADO] - Valor mínimo do PIS Retido considerado na nota fiscal de saída |
| VenPis | String(001) | Sim | [INUTILIZADO] - Transação considera valor PIS Retido no total da nota de saída |
| VenEnl | String(001) | Sim | Transação considera os encargos financeiro na base do CSLL |
| VenOul | String(001) | Sim | Transação considera as outras despesas na base do CSLL |
| VenDal | String(001) | Sim | Transação considera arredondamento na base do CSLL |
| VenOdl | String(001) | Sim | Transação considera outras despesas destacadas na base do CSLL |
| VenLcl | Number(009,2) | Sim | Valor mínimo do CSLL considerado na nota fiscal |
| VenCsl | String(001) | Sim | Indicativo de como a Transação considera o valor  do CSLL do total da nota fiscal |
| VenEno | String(001) | Sim | Transação considera os encargos financeiro na base de Outras Retenções |
| VenOuo | String(001) | Sim | Transação considera as outras despesas na base de Outras Retenções |
| VenDao | String(001) | Sim | Transação considera arredondamento na base do Out. Ret. |
| VenOdo | String(001) | Sim | Transação considera outras despesas destacadas na base de Outras Retenções |
| VenLor | Number(009,2) | Sim | Valor mínimo de Outras Retenções considerado na nota fiscal |
| VenOur | String(001) | Sim | Indicativo de como a Transação considera o valor  de Outras Retenções do total da nota fiscal |
| TnsCip | String(001) | Sim | Indica se a transação é ou não considerada na formação do índice de crédito do CIAP |
| EstCam | String(001) | Sim | Indicativo de onde será acumulada a quantidade do movimento de estoque na rotina de acúmulos mensais |
| EstWms | String(001) | Sim | Indicativo se a transação de estoque integra o movimento com o WMS |
| EstEsv | String(001) | Sim | Indicativo se a transação de entrada do tipo "M" aceitará movimentos sem valor |
| SomSub | Number(001,0) | Sim | Somar ou subtrair o valor no plano financeiro/centro de custos |
| USU_tnsprd | String(001) | Sim | Considera para CAT |
| USU_tnscar | String(001) | Sim | Considera carga |
| USU_IntSF | String(001) | Sim | Integra com Salesforce |
| USU_UsosSF | Number(002,0) | Sim | Usos no Salesforce |
| USU_ApeSF | String(999) | Sim | Apelido para Salesforce |
| USU_TipMer | String(001) | Sim | Tipo do Mercado |
| USU_SitSF | String(001) | Sim | Situação no Salesforce |
| USU_IntXpl | String(001) | Sim | Integra Senior Flow |

---

## Chave Primária

- CodEmp
- CodTns

---

## Índices

### E001TNSIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodTns
- CodFct

### USU_E001TNS2

**Tipo:** Não unico

Campos:
- LisMod
- CodEmp
- CodTns
- RecDec
- DesTns

### USU_E001TNS1

**Tipo:** Não unico

Campos:
- LisMod
- CodEmp
- CodTns

---

## Relacionamentos

### IR_E001TNS_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

