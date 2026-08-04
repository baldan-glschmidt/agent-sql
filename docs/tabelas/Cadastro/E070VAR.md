# E070VAR

## Descrição

Integrações - Varejo - Parâmetros de Integração

---

## Resumo

- Campos: 243
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodInt | Number(002,0) | Não | Código do sistema integrado |
| IndInt | String(001) | Não | Indicativo se a filial possui integração com sistema de varejo |
| CodDep | String(010) | Não | Depósito da Loja |
| CodTpr | String(004) | Não | Tabela de Preço Padrão para o Varejo |
| ValPad | Date | Não | Data de Validade Padrão da Tabela de Preços |
| NumCco | String(014) | Sim | Número da conta interna dos Caixas para receber as movimentações financeiras |
| CarCco | String(014) | Não | Número da conta interna da loja para controle de cartões presentes |
| CodCli | Number(009,0) | Não | Cliente padrão para vendas sem cliente informado |
| TnsPro | String(005) | Não | Transação para venda de produtos sem ST a consumidor final |
| TnsSer | String(005) | Não | Transação para venda de serviços sujeitos a ISS a consumidor final |
| TnsTcr | String(005) | Não | Transação para entrada de títulos à receber |
| TnsTcs | String(005) | Não | Transação para substituição de títulos a receber |
| TnsBcr | String(005) | Não | Transação para baixa de títulos por recebimento |
| TnsBrs | String(005) | Não | Transação para baixa de títulos por substituição |
| TnsBtc | String(005) | Não | Transação para baixa de títulos de crédito |
| TnsBrc | String(005) | Não | Transação para baixa de títulos por aproveitamento de crédito |
| TnsCcp | String(005) | Não | Transação para crédito de cartão presente na tesouraria |
| TnsDcp | String(005) | Não | Transação para débito de cartão presente na tesouraria |
| TnsCdt | String(005) | Não | Transação para créditos diversos na tesouraria |
| TnsDdt | String(005) | Não | Transação para débitos diversos na tesouraria |
| TptSub | String(003) | Não | Tipo de título substituto no contas a receber pelo varejo |
| IndClc | String(001) | Não | Indicativo se a filial deve consistir o limite de crédito dos clientes |
| IndPcc | String(001) | Não | Indicativo se a filial deve manter o pedido aberto caso cancele o cupom fiscal |
| IndBtt | String(001) | Não | Indicativo se deve baixar títulos de troca por aproveitamento de crédito |
| SnfMan | String(003) | Não | Código da série de notas fiscais manuais para consumidor final |
| SnfDev | String(003) | Sim | Código da série de notas fiscais de devolução |
| TptEcf | String(003) | Sim | Tipo de título de crédito para estorno convênio quando comp. estiver faturada |
| TnsEcf | String(005) | Sim | Transação de crédito para estorno convênio quando comp. estiver faturada |
| IndLfd | String(001) | Sim | Indicativo se considera a ligação de filial x depósito |
| TptScf | String(003) | Não | Tipo de título substituto para contas a receber (valor a maior) |
| CodCpg | String(006) | Não | Código da condição de pagamento padrão para vendas |
| MaxIcf | Number(004,0) | Sim | Quantidade máxima de itens no cupom fiscal |
| CcoLoj | String(014) | Sim | Número da conta interna da loja para receber as movimentações |
| TnsCdl | String(005) | Sim | Trans. para créditos diversos na tesouraria da conta da loja |
| TnsDdl | String(005) | Sim | Trans. para débitos diversos na tesouraria da conta da loja |
| VlrPmo | Number(015,2) | Sim | Valor padrão das filiais para pagamento de montagens |
| VlrPfe | Number(015,2) | Sim | Valor padrão das filiais para pagamento de fretes |
| TptMon | String(003) | Sim | Código do tipo de título a pagar para os montadores |
| DvtMon | Number(004,0) | Sim | Dia de vencimento padrão para a geração de títulos aos montadores |
| TnsPmo | String(005) | Sim | Código da transação para título aos montadores |
| TnsSmo | String(005) | Sim | Código da transação para a geração de ordens de serviço aos montadores |
| SerMon | String(014) | Sim | Código do serviço padrão para a geração de ordens de compra aos montadores |
| CodTab | String(004) | Sim | Código da tabela de preço frete |
| CodTra | Number(009,0) | Sim | Código da Transportadora |
| PlaVei | String(010) | Sim | Placa do veículo |
| TraMot | Number(009,0) | Sim | Código da Transportadora do Motorista |
| CodMtr | Number(006,0) | Sim | Código do Motorista |
| TptFre | String(003) | Sim | Código do tipo de título a pagar para os motoristas |
| DvtFre | Number(004,0) | Sim | Dia de vencimento padrão para a geração de títulos aos motoristas |
| TnsPfr | String(005) | Sim | Código da transação para título a ser pago aos motoristas |
| TnsSfr | String(005) | Sim | Código da transação para a geração de ordens de serviço aos motoristas |
| SerFre | String(014) | Sim | Código do serviço padrão para a geração de ordens de compra aos motoristas |
| ExiVsf | String(050) | Sim | Indicativo se exige a venda de serviços financeiros na venda |
| CanCur | Number(004,0) | Sim | Prazo para o cancelamento de cursos (em dias) |
| CodBan | String(003) | Sim | Código do banco que será utilizado nas operações com correspondente bancário |
| TptCbc | String(003) | Sim | Tipo Título C.Receber dos lançamentos com Corresp. Bancário |
| TnsCbc | String(005) | Sim | Código da transação C.Receber dos lançamentos com Corresp. Bancário |
| TnsTrc | String(005) | Sim | Transação do título de troco dos lançamentos com Corresp. Bancário e Recarga |
| TptRec | String(003) | Sim | Tipo Título C.Receber dos lançamentos com Recarga de Celular |
| TnsRec | String(005) | Sim | Código da transação C.Receber dos lançamentos de Recarga de Celular |
| VenRec | String(001) | Sim | Indicativo se a filial vende recarga de celular |
| TpmRes | Number(003,0) | Sim | Tempo padrão para vencimento de reservas de estoque (minutos) |
| QtdDec | Number(001,0) | Sim | Quantidade de casas decimais para o preço |
| ArrTrc | String(001) | Sim | Indicador de Arredondamento ou Truncamento (IAT) |
| RvePdv | String(001) | Sim | Indicativo se gera reservas de estoque para produtos do pedido de venda |
| TpmCpd | Number(003,0) | Sim | Tempo padrão para cancelamento de pedidos não faturados (minutos) |
| ForRcp | Number(002,0) | Sim | Forma de Recebimento no Pedido |
| ImpCfr | String(001) | Sim | Imprimir Controle de Frete quando Imprimir o Cupom |
| ImpCtm | String(001) | Sim | Imprimir Controle de Montagem quando Imprimir o Cupom |
| RecPda | Number(005,2) | Sim | % Desconto por Antecipação |
| RecTda | Number(003,0) | Sim | Quantidade Dias Tolerância  para Desconto por Antecipação |
| RecDbc | Number(003,0) | Sim | Quantidade de dias para bloquear cliente em atraso |
| RecMbc | Number(006,0) | Sim | Código do motivo para bloqueio do cliente em atraso |
| PagEng | String(001) | Sim | Indicativo se deve exigir natureza de gasto para pagamentos |
| ObmRes | String(001) | Sim | Indicativo se o motivo para reserva de estoque é obrigatório |
| ObmBes | String(001) | Sim | Indicativo se o motivo para bloqueio de estoque é obrigatório |
| MotBle | Number(006,0) | Sim | Código do motivo para bloqueio de estoque |
| MotRes | Number(006,0) | Sim | Código do motivo para reserva de estoque |
| TnsEex | String(005) | Sim | Transação padrão para movimentar entradas de séries externas (cursos) |
| TnsSex | String(005) | Sim | Transação padrão para movimentar saídas de séries externas (cursos) |
| TnsEtp | String(005) | Sim | Transação para Entrada de Títulos a Pagar |
| TnsBtp | String(005) | Sim | Transação para Baixa de Títulos a Pagar |
| TnsStp | String(005) | Sim | Transação para substituição de Títulos a Pagar |
| TmpVre | Number(003,0) | Sim | Tempo padrão para cancelamento de reservas sem vencimento (minutos) |
| TnpDev | String(005) | Sim | Código da transação para devolução de mercadorias |
| TciCup | Number(001,0) | Sim | Tipo de código para impressão de produto/serviço no cupom fiscal |
| DocVar | Number(001,0) | Sim | Tipo de documento do varejo |
| TnsBcc | String(005) | Sim | Transação para baixa de títulos por Cancelamento |
| IntCim | String(001) | Sim | Indicativo se o cupom deve ser enviado ao ERP imediatamente após sua finalização |
| LigCnv | Number(001,0) | Sim | Tipo de ligação de convênios |
| TnsSvc | String(005) | Sim | Transação de saída do depósito para reposição de cursos |
| TnsEvc | String(005) | Sim | Transação de entrada no depósito para reposição de cursos |
| TnsEcc | String(005) | Sim | Transação para cancelamento de cursos |
| IndBpf | String(001) | Sim | Indicativo se é permitido baixar parcelas fora da sequência |
| ImpPad | String(150) | Sim | Caminho da impressora padrão da loja |
| TraPor | String(001) | Sim | Indica se títulos podem ser transferidos para portador empresa no pagamento |
| NumCpa | String(001) | Sim | Indicativo se a numeração de cartão presente é automática |
| TipSen | Number(001,0) | Não | Local onde define-se a senha do usuário (representante) do sistema terceiro |
| TnsTfi | String(005) | Sim | Transação padrão de entrada de títulos a receber da financeira |
| TnsTcf | String(005) | Sim | Transação padrão de entrada de títulos a receber do cliente financiamento |
| TnsBfi | String(005) | Sim | Transação padrão de baixa de títulos a receber da financeira |
| TnsBcf | String(005) | Sim | Transação padrão de baixa de títulos contra cliente financiamento |
| TnsTpf | String(005) | Sim | Transação padrão de entrada de títulos a pagar da financeira |
| ValCpr | Number(004,0) | Sim | Quantidade de dias de validade do cartão presente |
| TnsEcp | String(005) | Sim | Transação C.Receber para lançar adiantamento para emissão de cartão presente |
| TptEcp | String(003) | Sim | Tipo título C.Receber para lançar adiantamento para emissão de cartão presente |
| SnfEcp | String(003) | Sim | Código da série da nota lançada na emissão de cartão presente |
| UsaEcp | String(001) | Sim | Indicativo se o sistema de varejo deve habilitar a emissão de cartão presente |
| IniInt | Date | Sim | Data de início da integração |
| CotAnt | String(001) | Sim | Indicativo se deve utilizar a cotação anterior quando não houver para o dia |
| TnsNcp | String(005) | Sim | Transação da nota gerada a partir da inclusão de crédito no cartão presente |
| IndTec | String(001) | Sim | Indicativo se deve efetuar transferência entre contas nas operações do Caixa |
| TnsDpc | String(005) | Sim | Transação para produtos sem ST em notas fiscais de devoluções de vendas |
| TnsDsc | String(005) | Sim | Transação para serviços sujeitos a ISS em notas fiscais de devoluções de vendas |
| IndAtc | String(001) | Sim | Indicativo que a filial é atacadista |
| TpcRcv | Number(001,0) | Sim | Tipo do cálculo do desconto/acréscimo no recebimento de uma venda |
| ObmMvt | String(001) | Sim | Indicativo se o motivo para movimentos de tesouraria |
| SerNce | String(003) | Sim | Série da Nota Fiscal Consumidor Eletrônica |
| TnsNfc | String(005) | Sim | Transação para produtos em notas fiscais a partir de vendas |
| TnsIsv | String(005) | Sim | Transação para venda de serviços por intermediação de venda |
| TnsDev | String(005) | Sim | Transação para emissão de notas fiscais de devolução de compras |
| TnsMan | String(005) | Sim | Transação para emissão de notas manuais |
| TnsOcp | String(005) | Sim | Transação para geração de ordens de compra |
| TnsPed | String(005) | Sim | Transação para geração de pedidos a partir de ordens de compra |
| ImpDav | Number(001,0) | Sim | Tipo de Impressão do DAV |
| TnsRen | String(005) | Sim | Transação para produtos sem ST em notas fiscais de entrada para conserto |
| TnsRes | String(005) | Sim | Transação para produtos sem ST em notas fiscais de remessa para conserto |
| BaiDev | Number(001,0) | Sim | Critério para baixa de títulos de devolução |
| TnsRco | String(005) | Sim | Trans. para produtos sem ST em notas fiscais de entrada de retorno do conserto |
| DiaDev | Number(003,0) | Sim | Quantidade de dias para devolução |
| IndPtm | String(001) | Sim | Permite troca de mercadorias |
| TnsSfe | String(005) | Sim | Trans. p/ prod. sem ST em notas fiscais de simples faturamento de entrega futura |
| TnsDmc | String(005) | Sim | Trans. p/ produtos sem ST em notas fiscais de conserto para devolução ao cliente |
| DepRec | String(010) | Sim | Depósito no qual devem ficar as mercadorias recuperadas |
| SnfNfc | String(003) | Não | Código da série de notas fiscais geradas automaticamente |
| PagTbm | String(005) | Sim | Transação padrão de baixa de títulos a pagar por compensação |
| RecTbm | String(005) | Sim | Transação padrão de baixa de títulos a receber por compensação |
| TnsCcf | String(005) | Não | Transação para entrada de títulos de contrato contra o cliente contratante |
| TnsFcf | String(005) | Não | Transação para entrada de títulos de contrato contra o fornecedor de serviços |
| TitCcf | String(003) | Não | Transação para entrada de títulos de contrato contra o cliente contratante |
| TitFcf | String(003) | Não | Transação para entrada de títulos de contrato para Seguradora/Banco |
| CodCrt | String(002) | Sim | Código da carteira do título a receber do cliente de contrato |
| OriTit | String(003) | Sim | Origem do contrato financeiro |
| UtiVar | String(001) | Sim | Indicativo se a filial utiliza módulo varejo eletromóveis |
| TnsSie | String(005) | Sim | Trans. p/ prod. sem ST em NF de simp. faturamento interestadual de ent. futura |
| TnsRfu | String(005) | Sim | Transação para produtos sem ST em notas fiscais de remessa de entrega futura |
| TnsRue | String(005) | Sim | Trans. p/ produtos sem ST em NF de remessa interestadual de entrega futura |
| TnsSsi | String(005) | Sim | Código da transação |
| TnsMns | String(005) | Sim | Transação de serviços para emissão de notas manuais |
| TnsInc | String(005) | Sim | Transação para serviços de intermediação |
| TnsDsi | String(005) | Sim | Trans. p/ serviços de intermediação de vendas em NF de devoluções de vendas |
| TnsDpn | String(005) | Sim | Trans. p/ prod. sem ST em notas fiscais de anulação de vendas de entrega futura |
| TnsDvs | String(005) | Sim | Transação de devolução de serviços não intermediados |
| TnsBpc | String(005) | Sim | Transação para baixa de títulos de contas a pagar por cancelamento |
| TnsBpb | String(005) | Sim | Transação para baixa de títulos de contas a pagar por abatimento |
| TnsBrb | String(005) | Sim | Transação para baixa de títulos de contas a receber por abatimento |
| MotDsb | Number(006,0) | Sim | Código do motivo para desbloqueio de estoque |
| MotCre | Number(006,0) | Sim | Código do motivo para cancelamento reserva de estoque |
| SnfIva | String(003) | Sim | Série para notas fiscais de intermediação de vendas avulsas |
| TnsNfs | String(005) | Sim | Transação para serviços sujeitos a ISS em notas fiscais a partir de vendas |
| CliPed | Number(009,0) | Sim | Cliente padrão para pedidos no Retaguarda |
| TveFre | Number(001,0) | Sim | Venda de fretes |
| TptCtr | String(003) | Sim | Tipo de Título Padrão dos Contratos de Venda para o Varejo |
| SnfCtr | String(003) | Sim | Origem das Parcelas Padrão dos Contratos de Venda para o Varejo |
| TnsCtr | String(005) | Sim | Transação Padrão dos títulos gerados via Contrato de Venda para o Varejo |
| TnsPrc | String(005) | Sim | Transação para venda de produtos com ST a consumidor final |
| TnsVis | String(005) | Sim | Transação para venda interestadual de serviços sujeitos a ISS a consumidor final |
| TnsSss | String(005) | Sim | Transação para venda de serviços sujeitos a ICMS sem ST a consumidor final |
| TnsIss | String(005) | Sim | Trans. p/ venda interestadual de serv. sujeitos a ICMS sem ST a consumidor final |
| TnsScs | String(005) | Sim | Transação para venda de serviços sujeitos a ICMS com ST a consumidor final |
| TnsIsc | String(005) | Sim | Trans. p/ venda interestadual de serv. sujeitos a ICMS com ST a consumidor final |
| TnsPni | String(005) | Sim | Transação para produtos em notas fiscais interestaduais a partir de vendas |
| TnsSni | String(005) | Sim | Tran. p/ serv. sujeitos a ISS em notas fiscais interestaduais a partir de vendas |
| TnsSic | String(005) | Sim | Transação para serviços sujeitos a ICMS em notas fiscais a partir de vendas |
| TnsSii | String(005) | Sim | Transação para serviços sujeitos a ICMS em notas fiscais a partir de vendas |
| TnsCsf | String(005) | Sim | Trans. p/ prod. com ST em notas fiscais de simples faturamento de entrega futura |
| TnsCsi | String(005) | Sim | Trans. p/ prod. com ST em NF de simp. faturamento interestadual de ent. futura |
| TnsCfu | String(005) | Sim | Transação para produtos com ST em notas fiscais de remessa de entrega futura |
| TnsCre | String(005) | Sim | Trans. p/ produtos com ST em NF de remessa interestadual de entrega futura |
| TnsCrc | String(005) | Sim | Transação para produtos com ST em notas fiscais de remessa para conserto |
| TnsRei | String(005) | Sim | Trans. p/ produtos sem ST em NF de remessa interestadual para conserto |
| TnsCri | String(005) | Sim | Trans. p/ produtos com ST em NF de remessa interestadual para conserto |
| TnsCdm | String(005) | Sim | Trans. p/ produtos com ST em notas fiscais de conserto para devolução ao cliente |
| TnsDmi | String(005) | Sim | Trans. p/ prod. sem ST em NF de conserto para devolução interestadual ao cliente |
| TnsCdi | String(005) | Sim | Trans. p/ prod. com ST em NF de conserto para devolução interestadual ao cliente |
| TnsSai | String(005) | Sim | Transação para saída de produtos em notas fiscais de acerto por inventário |
| TnsPcd | String(005) | Sim | Transação para produtos com ST em notas fiscais de devoluções de vendas |
| TnsDvi | String(005) | Sim | Trans. p/ serviços sujeitos a ISS em NF de devoluções de vendas interestaduais |
| TnsSsd | String(005) | Sim | Trans. p/ serviços suj. a ICMS sem ST em notas fiscais de devoluções de vendas |
| TnsSdi | String(005) | Sim | Trans. p/ serv. sujeitos a ICMS sem ST em NF de devol. de vendas interestaduais |
| TnsScd | String(005) | Sim | Trans. p/ serviços suj. a ICMS com ST em notas fiscais de devoluções de vendas |
| TnsSci | String(005) | Sim | Trans. p/ serv. sujeitos a ICMS com ST em NF de devol. de vendas interestaduais |
| TnsCdp | String(005) | Sim | Trans. p/ prod. com ST em notas fiscais de anulação de vendas de entrega futura |
| TnsPai | String(005) | Sim | Trans. p/ prod. sem ST em NF de anulação de vendas interestadual de ent. futura |
| TnsPci | String(005) | Sim | Trans. p/ prod. com ST em NF de anulação de vendas interestadual de ent. futura |
| TnsPde | String(005) | Sim | Trans. p/ prod. sem ST em notas fiscais de devolução de vendas de entrega futura |
| TnsPce | String(005) | Sim | Trans. p/ prod. com ST em notas fiscais de devolução de vendas de entrega futura |
| TnsPdi | String(005) | Sim | Trans. p/ produtos sem ST em NF de dev. de vendas interestaduais de ent. futura |
| TnsPcf | String(005) | Sim | Trans. p/ produtos com ST em NF de dev. de vendas interestaduais de ent. futura |
| TnsPcc | String(005) | Sim | Transação para produtos com ST em notas fiscais de entrada para conserto |
| TnsPic | String(005) | Sim | Trans. p/ prod. sem ST em notas fiscais de entrada interestadual para conserto |
| TnsPcn | String(005) | Sim | Trans. p/ prod. com ST em notas fiscais de entrada interestadual para conserto |
| TnsRcc | String(005) | Sim | Trans. para produtos com ST em notas fiscais de entrada de retorno do conserto |
| TnsPir | String(005) | Sim | Trans. p/ produtos sem ST em NF de entrada interestadual de retorno do conserto |
| TnsPcr | String(005) | Sim | Trans. p/ produtos com ST em NF de entrada interestadual de retorno do conserto |
| TnsEai | String(005) | Sim | Transação para entrada de produtos em notas fiscais de acerto por inventário |
| ImpCar | String(150) | Sim | Caminho da impressora de carnês da loja |
| TxtCtr | String(9999) | Sim | Texto complementar do contrato de venda |
| TipMvi | Number(001,0) | Não | Tipo de movimento do inventário |
| IndNfc | String(001) | Sim | Modo de operação PDV/Retaguarda |
| VlrMic | Number(011,2) | Sim | Valor mínimo da venda para exigir o cliente |
| TmpSco | Number(003,0) | Sim | Tempo para solicitar contingência (em segundos) |
| TipIda | Number(001,0) | Sim | Tipo de impressão de DANFE NFC-e |
| TipAec | Number(001,0) | Sim | Tipo de ambiente para emissão de NFC-e |
| TmpSde | Number(004,0) | Sim | Tempo para testar comunicação com SDE (em segundos) |
| UrlNfc | String(500) | Sim | Endereço (URL) de conexão com o sistema de Documentos Eletrônicos para NFC-e |
| LogNfc | String(050) | Sim | Usuário p/ autenticação com o sistema de Documentos Eletrônicos para NFC-e |
| SenNfc | String(100) | Sim | Senha p/ autenticação com o sistema de Documentos Eletrônicos para NFC-e |
| UrlCpc | String(500) | Sim | Endereço (URL) para consulta pública do NFC-e |
| UrlDan | String(500) | Sim | Endereço (URL) para consulta do DANFE NFC-e via leitura de QRCode |
| IdeCsc | String(006) | Sim | Código Identificador do CSC |
| NumCsc | String(036) | Sim | Código de Segurança do Contribuinte no Banco de Dados da SEFAZ (CSC) |
| SolVop | String(001) | Sim | Indica se o sistema deverá solicitar os volumes no pedido |
| EntVcd | String(001) | Sim | Indica que a loja permite entregar vendas através do centro de distribuição |
| QtdDcd | Number(004,0) | Sim | Quantidade de dias padrão para previsão de entrega pelo centro de distribuição |
| FdvEft | String(001) | Sim | Tipo NF de origem para devolução ainda não entregue ao cliente |
| IndBei | String(001) | Sim | Indica se o sistema deve bloquear o estoque durante o inventário |
| SnfNfi | String(003) | Sim | Código da série das notas fiscais de saída e entrada de ajustes de inventário |
| FepPed | String(001) | Sim | Forma de entrega padrão para os pedidos de venda |
| MgnEft | Number(001,0) | Sim | Momento de geração da NF de simp. faturamento |
| TnsPsc | String(005) | Sim | Trans. p/ prod. s/ST em NF de remes. simbólica p/ anulação de venda |
| TnsPnc | String(005) | Sim | Trans. p/ prod. c/ST em NF de remes. simbólica p/ anulação de venda |
| TnsSnc | String(005) | Sim | Trans. p/ prod. s/ST em NF de rem. simbólica interest. p/ anulação de venda |
| TnsCnc | String(005) | Sim | Trans. p/ prod. c/ST em NF de rem. simbólica interest. p/ anulação de venda |
| SnfNre | String(003) | Sim | Série para geração de NF remessa para vendas entregues pelo CD |
| SnfNfe | String(003) | Sim | Código da série de notas fiscais eletrônicas geradas automaticamente |
| EnfFir | String(001) | Sim | Emitir notas de saída para a filial que integra com retaguarda |
| ForVcp | Number(009,0) | Sim | Fornecedor padrão para emissão de cartão presente |
| IndSfr | String(001) | Sim | Indicativo se permite a venda de seguro furto e roubo |
| TnsDpi | String(005) | Sim | Trans. para produtos sem ST em notas fiscais de devoluções de vendas interest. |
| TnsDti | String(005) | Sim | Trans. para produtos com ST em notas fiscais de devoluções de vendas interest. |

---

## Chave Primária

- CodEmp
- CodFil
- CodInt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070VAR_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

