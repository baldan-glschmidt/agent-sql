# E070FIN

## Descrição

Cadastros - Filiais - Parâmetros Financeiros

---

## Resumo

- Campos: 250
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| VenCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| VenFin | Number(007,0) | Sim | Conta financeira a classificar |
| VenRed | Number(007,0) | Sim | Conta contábil a classificar |
| VenCcu | String(009) | Sim | Centro de custo a classificar |
| EstCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| EstFin | Number(007,0) | Sim | Conta financeira a classificar |
| EstRed | Number(007,0) | Sim | Conta contábil a classificar |
| EstCcu | String(009) | Sim | Centro de custo a classificar |
| RecCfd | Number(007,0) | Sim | Conta financeira padrão para os descontos do contas a receber |
| RecCcd | String(009) | Sim | Centro de custo padrão para os descontos do contas a receber |
| RecCfo | Number(007,0) | Sim | Conta financeira padrão para outros descontos do contas a receber |
| RecCco | String(009) | Sim | Centro de custo padrão para outros descontos do contas a receber |
| RecCfj | Number(007,0) | Sim | Conta financeira padrão para os juros do contas a receber |
| RecCcj | String(009) | Sim | Centro de custo padrão para os juros do contas a receber |
| RecCfm | Number(007,0) | Sim | Conta financeira padrão para a multa do contas a receber |
| RecCcm | String(009) | Sim | Centro de custo padrão para a multa do contas a receber |
| RecCfe | Number(007,0) | Sim | Conta financeira padrão para os encargos do contas a receber |
| RecCce | String(009) | Sim | Centro de custo padrão para os encargos do contas a receber |
| RecCfc | Number(007,0) | Sim | Conta financeira padrão para a correção monetária do contas a receber |
| RecCcc | String(009) | Sim | Centro de custo padrão para a correção monetária do contas a receber |
| RecCfa | Number(007,0) | Sim | Conta financeira padrão para outros acréscimos do contas a receber |
| RecCca | String(009) | Sim | Centro de custo padrão para outros acréscimos do contas a receber |
| RecCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| RecFin | Number(007,0) | Sim | Conta financeira a classificar |
| RecRed | Number(007,0) | Sim | Conta contábil a classificar |
| RecCcu | String(009) | Sim | Centro de custo a classificar |
| RecTnd | String(005) | Sim | Transação padrão para geração do título de nota de débito |
| RecTtn | String(003) | Sim | Tipo de título padrão para geração do título de nota de débito |
| RecVnd | Number(009,2) | Sim | Valor mínimo para geração do título de nota de débito |
| RecTbm | String(005) | Sim | Transação padrão de baixa de títulos por compensação |
| RecFrj | String(003) | Sim | Código da fórmula de reajuste do título a receber |
| RecJoa | String(001) | Sim | Indicativo se considera o valor de outros acréscimos da Fórmula de Reajuste para cálculo de juros do contas a receber |
| RecMoa | String(001) | Sim | Indicativo se considera o valor de outros acréscimos da Fórmula de Reajuste para cálculo de multa do contas a receber |
| RecJod | String(001) | Sim | Indicativo se considera o valor de outros descontos da Fórmula de Reajuste para cálculo de juros do contas a receber |
| RecTvc | String(005) | Sim | Transação padrão para geração da valorização de correção da multimoeda do contas a receber |
| RecTvo | String(005) | Sim | Transação padrão para geração da valorização de outros descontos da multimoeda do contas a receber |
| RecTtc | String(003) | Sim | Tipo de título padrão para título de taxa de deflação |
| RecTnc | String(005) | Sim | Transação padrão de entrada de título de taxa de deflação |
| RecTrc | String(005) | Sim | Transação padrão de baixa de título de taxa de deflação |
| RecTth | String(003) | Sim | Tipo de título padrão para título de cheque |
| RecTnh | String(005) | Sim | Transação padrão de entrada de título de cheque |
| RecAts | Number(005,0) | Sim | Código layout da importação na substituição do título |
| RecApf | Number(005,0) | Sim | Código layout da exportação de pendências financeiras - PEFIN |
| RecBpf | Number(005,0) | Sim | Código layout da exportação de pendências financeiras - RELATO |
| RecNpf | String(003) | Sim | Natureza de Operação padrão para geração de pendências financeiras |
| RecMpf | String(002) | Sim | Motivo da Baixa padrão para baixa de pendências financeiras |
| RecDpf | String(250) | Sim | Diretório padrão para arquivos de remessa de pendências financeiras |
| RecRpf | Number(009,0) | Sim | Número de controle do arquivo de remessa para pendência financeira |
| RecTta | String(003) | Sim | Tipo de título padrão para entrada de título de crédito |
| RecMvo | String(001) | Sim | Indicativo se o valor da multa será calculada sobre valor em aberto do título a receber (se não, será sobre original) |
| RecTts | String(003) | Sim | Tipo de título padrão para entrada de título por substituição |
| RecTbt | String(005) | Sim | Transação padrão de baixa de títulos por pagamento |
| RecTec | String(005) | Sim | Transação padrão de entrada de títulos de cartão crédito/débito |
| RecTsc | String(005) | Sim | Transação padrão de baixa de títulos por substituição por cartão |
| CprCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| CprFin | Number(007,0) | Sim | Conta financeira a classificar |
| CprRed | Number(007,0) | Sim | Conta contábil a classificar |
| CprCcu | String(009) | Sim | Centro de custo a classificar |
| PagCfd | Number(007,0) | Sim | Conta financeira padrão para os descontos do contas a pagar |
| PagCcd | String(009) | Sim | Centro de custo padrão para os descontos do contas a pagar |
| PagCfo | Number(007,0) | Sim | Conta financeira padrão para outros descontos do contas a pagar |
| PagCco | String(009) | Sim | Centro de custo padrão para outros descontos do contas a pagar |
| PagCfj | Number(007,0) | Sim | Conta financeira padrão para os juros do contas a pagar |
| PagCcj | String(009) | Sim | Centro de custo padrão para os juros do contas a pagar |
| PagCfm | Number(007,0) | Sim | Conta financeira padrão para a multa do contas a pagar |
| PagCcm | String(009) | Sim | Centro de custo padrão para a multa do contas a pagar |
| PagCfe | Number(007,0) | Sim | Conta financeira padrão para os encargos do contas a pagar |
| PagCce | String(009) | Sim | Centro de custo padrão para os encargos do contas a pagar |
| PagCfc | Number(007,0) | Sim | Conta financeira padrão para a correção monetária do contas a pagar |
| PagCcc | String(009) | Sim | Centro de custo padrão para a correção monetária do contas a pagar |
| PagCfa | Number(007,0) | Sim | Conta financeira padrão para outros acréscimos do contas a pagar |
| PagCca | String(009) | Sim | Centro de custo padrão para outros acréscimos do contas a pagar |
| PagCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| PagFin | Number(007,0) | Sim | Conta financeira a classificar |
| PagRed | Number(007,0) | Sim | Conta contábil a classificar |
| PagCcu | String(009) | Sim | Centro de custo a classificar |
| PagFoc | Number(009,0) | Sim | Código do fornecedor padrão para geração do título de COFINS |
| PagTtc | String(003) | Sim | Tipo de título padrão para geração do título de COFINS |
| PagTrc | String(005) | Sim | Transação padrão para geração do título de COFINS |
| PagCic | String(003) | Sim | Código do imposto para buscar o percentual do imposto de COFINS para geração do título |
| PagTbi | String(005) | Sim | Transação padrão por baixa de IRF |
| PagIrf | Number(015,2) | Sim | Valor mínimo do título de IRRF |
| PagIir | String(001) | Sim | Indicativo se trabalha com IR |
| PagApp | String(001) | Sim | Indicativo se existe permite baixa parcial em títulos aprovados |
| PagTpe | String(005) | Sim | Transação padrão de débito por Pagamento Eletrônico |
| PagTba | String(005) | Sim | Transação padrão de baixa de títulos por crédito |
| PagTbm | String(005) | Sim | Transação padrão de baixa de títulos por compensação |
| PagTvc | String(005) | Sim | Transação padrão para geração da valorização de correção da multimoeda do contas a pagar |
| PagTvo | String(005) | Sim | Transação padrão para geração da valorização de outros descontos da multimoeda do contas a pagar |
| PagAre | Number(005,0) | Sim | Código Layout Exportação do Encontro de Contas |
| PagAte | Number(005,0) | Sim | Código Layout Importação Encontro de Contas |
| PagGtr | String(001) | Sim | Indicativo se gera título de IR no pagamento da comissão |
| PagGts | String(001) | Sim | Indicativo se gera título de ISS no pagamento da comissão |
| PagGtn | String(001) | Sim | Indicativo se gera título de INSS no pagamento da comissão |
| PagTds | String(005) | Sim | Transação padrão de desconto de ISS sobre comissão |
| PagEba | String(001) | Sim | Indicativo se o título continua aprovado após a exclusão da baixa |
| PagTes | String(005) | Sim | Transação padrão de entrada de títulos por substituição |
| PagEtc | String(005) | Sim | Transação padrão de entrada de títulos de curto prazo |
| PagEtl | String(005) | Sim | Transação padrão de entrada de títulos de longo prazo |
| PagTdn | String(005) | Sim | Transação padrão de desconto de INSS sobre comissão |
| PagAts | Number(005,0) | Sim | Código layout da importação na substituição do título |
| PagVmn | Number(015,2) | Sim | Valor máximo de retenção de INSS para representantes pessoas físicas |
| PagTbe | String(005) | Sim | Transação padrão de baixa por Pagamento Eletrônico |
| PagTnm | String(005) | Sim | Transação padrão de entrada de título de pagamento de comissão |
| PagTtm | String(003) | Sim | Tipo de título padrão para entrada de título de pagamento de comissão |
| PagTta | String(003) | Sim | Tipo de título padrão para entrada de título de crédito |
| PagBcc | String(005) | Sim | Transação de baixa de crédito por cancelamento NFS |
| PagMvo | String(001) | Sim | Indicativo se o valor da multa será calculada sobre valor em aberto do título a pagar (se não, será sobre original) |
| PagTts | String(003) | Sim | Tipo de título padrão para entrada de título por substituição |
| CxbCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| CxbFin | Number(007,0) | Sim | Conta financeira de receita a classificar |
| CxbFdc | Number(007,0) | Sim | Conta financeira de despesa a classificar |
| CxbRed | Number(007,0) | Sim | Conta contábil de receita a classificar |
| CxbRdc | Number(007,0) | Sim | Conta contábil de despesa a classificar |
| CxbCcu | String(009) | Sim | Centro de custo a classificar para a conta de receita |
| CxbCdc | String(009) | Sim | Centro de custo a classificar para a conta de despesa |
| CxbTdr | String(005) | Sim | Transação padrão débito tesouraria para retenção de impostos |
| CxbTce | String(005) | Sim | Transação padrão crédito tesouraria por encontro contas |
| CxbTcr | String(005) | Sim | Transação padrão de crédito por recebimento de cheques\outros |
| CxbTtc | String(003) | Sim | Tipo de título padrão para entrada de título de contrato de aplicação/captação de recursos |
| CxbTnc | String(005) | Sim | Transação padrão de entrada de título de contrato de aplicação/captação de recursos |
| CxbSnc | String(003) | Sim | Código da série de notas fiscais para geração dos títulos de contrato de aplicação/captação de recursos |
| CxbTmc | String(005) | Sim | Transação padrão de crédito de contrato de aplicação/captação de recursos |
| CxbTmd | String(005) | Sim | Transação padrão de débito de contrato de aplicação/captação de recursos |
| CxbTct | String(005) | Sim | Transação padrão de crédito de transferências entre contas |
| CxbTdt | String(005) | Sim | Transação padrão de débito de transferências entre contas |
| CxbPrr | String(005) | Sim | Transação de provisão de rendimentos |
| CxbPen | String(005) | Sim | Transação de provisão de encargos |
| CxbPpa | String(005) | Sim | Transação de provisão de parcela |
| CxbPpr | String(005) | Sim | Transação de provisão de prestação |
| CxbPir | String(005) | Sim | Transação de provisão de IRRF |
| CxbPio | String(005) | Sim | Transação de provisão de IOF |
| CxbPcm | String(005) | Sim | Transação de provisão de CPMF |
| CxbEpr | String(005) | Sim | Transação de estorno provisão de rendimentos |
| CxbEpe | String(005) | Sim | Transação de estorno provisão de encargos |
| CxbEpa | String(005) | Sim | Transação de estorno provisão de parcela |
| CxbEpp | String(005) | Sim | Transação de estorno provisão de prestação |
| CxbEpi | String(005) | Sim | Transação de estorno provisão de IRRF |
| CxbEpf | String(005) | Sim | Transação de estorno provisão de IOF |
| CxbEpc | String(005) | Sim | Transação de estorno provisão de CPMF |
| CxbLre | String(005) | Sim | Transação de realização de rendimentos |
| CxbLen | String(005) | Sim | Transação de realização de encargos |
| CxbLpa | String(005) | Sim | Transação de realização de parcela |
| CxbLpr | String(005) | Sim | Transação de realização de prestação |
| CxbLir | String(005) | Sim | Transação de realização de IRRF |
| CxbLio | String(005) | Sim | Transação de realização de IOF |
| CxbLcp | String(005) | Sim | Transação realização de CPMF |
| CxbErr | String(005) | Sim | Transação de estorno realização de rendimentos |
| CxbEri | String(005) | Sim | Transação de estorno realização de IRRF |
| CxbErf | String(005) | Sim | Transação de estorno realização de IOF |
| CxbErc | String(005) | Sim | Transação de estorno realização de CPMF |
| CxbPmr | String(001) | Sim | Indicativo se gera provisão para meses retroativos a data base |
| CxbApp | String(005) | Sim | Transação padrão de atualização da conta empréstimo de pagamento da amortização |
| CxbApj | String(005) | Sim | Transação padrão de atualização da conta empréstimo de pagamento de juros |
| CxbApo | String(005) | Sim | Transação padrão de atualização da conta empréstimo de pagamento de acréscimos |
| CxbApd | String(005) | Sim | Transação padrão de atualização da conta empréstimo de pagamento de descontos |
| CxbAea | String(005) | Sim | Transação padrão de estorno da conta empréstimo de pagamento da amortização |
| CxbAej | String(005) | Sim | Transação padrão de estorno da conta empréstimo de pagamento de juros |
| CxbAeo | String(005) | Sim | Transação padrão de estorno da conta empréstimo de pagamento de acréscimos |
| CxbAed | String(005) | Sim | Transação padrão de estorno da conta empréstimo de pagamento de descontos |
| CxbCjr | String(005) | Sim | Transação padrão de crédito para correção de juros de prestações de empréstimos |
| CxbDjr | String(005) | Sim | Transação padrão de débito para correção de juros de prestações de empréstimos |
| CxbCpr | String(005) | Sim | Transação padrão de crédito para correção de prestações de empréstimos |
| CxbDpr | String(005) | Sim | Transação padrão de débito para correção de prestações de empréstimos |
| CxbCmo | String(005) | Sim | Transação padrão de crédito para correção monetária de prestações de empréstimos |
| CxbDmo | String(005) | Sim | Transação padrão de débito para correção monetária de prestações de empréstimos |
| CxbCec | String(005) | Sim | Transação estorno crédito de correção monetária de prestações de empréstimos |
| CxbCed | String(005) | Sim | Transação estorno débito de correção monetária de prestações de empréstimos |
| CxbPcc | String(005) | Sim | Transação pagamento crédito correção monetária de prestações de empréstimos |
| CxbPcd | String(005) | Sim | Transação pagamento débito correção monetária de prestações de empréstimos |
| CxbCep | String(005) | Sim | Transação estorno pgto. crédito correção monetária de prestações de empréstimos |
| CxbDep | String(005) | Sim | Transação estorno pgto. débito correção monetária de prestações de empréstimos |
| CxbTar | String(005) | Sim | Transação de lançamento de débito da tarifa da captação de recursos |
| CxbIof | String(005) | Sim | Transação de lançamento de débito do IOF da captação de recursos |
| CxbDac | String(005) | Sim | Transação padrão de atualização da conta empréstimo de adimplência |
| CxbDad | String(005) | Sim | Transação padrão de atualização da conta empréstimo de pagamento de adimplência |
| CxbAdc | String(005) | Sim | Transação padrão de atualização da conta empréstimo de antecipação |
| CxbAdd | String(005) | Sim | Transação padrão de atualização da conta empréstimo de pagamento de antecipação |
| PatLim | Number(015,2) | Sim | Valor mínimo de inclusão de bens |
| PatAli | String(001) | Sim | Acréscimo Considera Valor Mínimo Inclusão |
| PatIdd | String(001) | Sim | Indica se o acréscimo pode ter taxa de desvalorização oficial diferente do bem principal |
| PatInv | String(001) | Sim | Indicativo se há controle de investimentos |
| PatIdp | String(001) | Sim | Indicador de início da desvalorização oficial |
| PatIcu | String(001) | Sim | Indica se há integração com a área de custos |
| PatIco | String(001) | Sim | Indica se há integração com a gestão de compras |
| PatUfc | String(001) | Sim | Indica que o cadastramento de bens exige fechamento |
| PatUct | String(001) | Sim | Indica se exige conta contábil no cadastro dos bens |
| PatUfo | String(001) | Sim | Indica se exige fornecedor no cadastro dos bens |
| PatUor | String(001) | Sim | Indicativo se utiliza organograma de setores para controle de localização |
| PatUdp | String(001) | Sim | Indica se permite alterar a taxa de desvalorização do bem |
| PatUcc | String(001) | Sim | Indica se exige centro de custo no cadastro dos bens |
| PatAnt | Date | Sim | Data do processamento anterior ao último apurado para o Patrimônio |
| PatAtu | Date | Sim | Data do último processamento apurado para o Patrimônio. |
| PatPdi | Date | Sim | Período inicial de validade para movimentação do patrimônio |
| PatPdf | Date | Sim | Período final de validade para movimentação do patrimônio |
| PatIdv | String(001) | Sim | Indicador de início de desvalorização por vida útil |
| PatBvz | String(001) | Sim | Indica se permite a entrada de bem com valor zero |
| PatIdg | String(001) | Sim | Indicador de início da desvalorização gerencial |
| PrjPdi | Date | Sim | Período inicial de validade para movimentação para projetos |
| PrjPdf | Date | Sim | Período final de validade para movimentação para projetos |
| RecLot | String(001) | Sim | Indica se os movimentos de baixa utilizarão número de lote |
| PagToc | String(005) | Sim | Transação de ordem de compra padrão do pagamento de comissão |
| PagSoc | String(014) | Sim | Código do serviço de ordem de compra padrão do pagamento de comissão |
| RecEpr | String(001) | Sim | Atribuir data de processamento a de entrada ao efetivar título previsto de CRE |
| PagEpr | String(001) | Sim | Atribuir data de processamento a de entrada ao efetivar título previsto de CPA |
| PagTpp | String(005) | Sim | Transação padrão de entrada de títulos de previsão |
| PagBdc | String(005) | Sim | Transação de baixa de duplicata por cancelamento NFS |
| RecCms | String(001) | Sim | Indicativo se gera comissão em baixa por substituição |
| GerTjs | String(001) | Sim | Indicativo se gera título de juros separado do título da prestação |
| GerDif | String(001) | Sim | Indicativo se gera a diferença do empréstimo na primeira ou última prestação |
| RecTbd | String(005) | Sim | Transação padrão de baixa de títulos por crédito oriundo de devolução de venda |
| PagTbd | String(005) | Sim | Transação padrão de baixa de títulos por crédito oriundo de devolução de compra |
| PagTei | String(005) | Sim | Transação padrão de entrada de títulos de impostos da captação |
| CobQdp | Number(004,0) | Sim | Quantidade de dias mínimos para título ser considerado uma perda |
| CobPpp | String(004) | Sim | Código do portador padrão título considerado como perda |
| CobPdj | String(004) | Sim | Código do portador padrão do departamento jurídico |
| CobQdj | Number(004,0) | Sim | Quantidade de dias mínimos para envio para departamento jurídico |
| CobVdj | Number(009,2) | Sim | Valor mínimo do título para envio para departamento jurídico |
| CobApc | Number(004,0) | Sim | Código do acionamento padrão realizado pelo cliente |
| CobOpr | String(001) | Sim | Indicativo se obriga os parâmetros na renegociação de títulos em cobrança |
| CobOba | String(001) | Sim | Tipo padrão de ocorrência de baixa de título na empresa para envio assessoria |
| CxbCrc | String(005) | Sim | Transação padrão de crédito para recebimento de cartão |
| CxbCbc | String(005) | Sim | Transação padrão de créditos diversos de cartão |
| CxbDbc | String(005) | Sim | Transação padrão de débito para tarifas de cartão |
| RecRbc | String(005) | Sim | Transação padrão de baixa por recebimento de cartão |
| RecBdc | String(005) | Sim | Transação padrão de baixa diversa de cartão |
| TnsCap | String(005) | Sim | Transação padrão para gerar contas a pagar na apuração de comissão de vendas |
| CodRep | Number(009,0) | Sim | Código do representante padrão da filial |
| PagPtd | String(001) | Sim | Indicativo se o título previsto volta a ter valor inicial após sua desaprovação |
| RecQrb | Number(003,0) | Sim | Dias acrescidos ao vencimento do título para impressão de boletos |
| CobCpp | String(001) | Sim | Considera o atraso dos títulos da nota fiscal pela primeira parcela |
| PerGds | Number(001,0) | Sim | Permite gerar devolução de saldo na baixa do Contas a Receber |
| TnsEpd | String(005) | Sim | Transação de entrada do C. Pagar para devolução de saldo na baixa do C.Receber |
| TptDpr | String(003) | Sim | Tipo de título para gerar C.Pagar da devolução de saldo na baixa do C.Receber |
| CtaDpr | String(014) | Sim | Conta interna para lançar devolução de saldo na baixa do C.Receber |
| TnsTdt | String(005) | Sim | Transação de débito na tesouraria da devolução de saldo na baixa do C.Receber |
| TnsDcp | String(005) | Sim | Transação do C.Pagar para baixa da devolução de saldo originada do C.Receber |
| UsuAde | Number(010,0) | Sim | Usuário responsável pela aprovação da devolução de saldo na baixa do C.Receber |
| PerDsp | Number(001,0) | Sim | Permite gerar devolução de saldo na baixa do contas a pagar |
| TnsEdp | String(005) | Sim | Transação de entrada do c. receber para devolução de saldo na baixa do c.pagar |
| TptDdp | String(003) | Sim | Tipo de título para gerar c.receber da devolução de saldo na baixa do c.pagar |
| CtaDdp | String(014) | Sim | Conta interna para lançar devolução de saldo na baixa do c.pagar |
| TnsTdp | String(005) | Sim | Transação de crédito na tesouraria da devolução de saldo na baixa do c.pagar |
| TnsDcr | String(005) | Sim | Transação do c.receber para baixa da devolução de saldo originada do c.pagar |
| EerTes | String(001) | Sim | Renegociação de títulos exige entrada para títulos enviados ao SPC/Serasa |
| CxbPev | String(005) | Sim | Transação de provisão de encargos sobre o valor em aberto |
| PagBcr | String(005) | Sim | Transação de Baixa de Duplicata por Cancelamento de Contrato |
| DesLcp | String(001) | Sim | Desconsidera movimentos para o LCDPR |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070FIN_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

