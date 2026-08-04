# E120PED

## Descrição

Vendas - Pedidos - Dados Gerais

---

## Resumo

- Campos: 359
- Chave Primária: 3 campo(s)
- Índices: 5
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| TipPed | Number(001,0) | Sim | Tipo do pedido |
| PrcPed | Number(002,0) | Sim | Procedência do pedido |
| TnsPro | String(005) | Sim | Código da transação de pedido para produtos |
| TnsSer | String(005) | Sim | Código da transação de pedido para serviços |
| DatEmi | Date | Não | Data de emissão do pedido |
| HorEmi | Number(005,0) | Sim | Hora de emissão do pedido |
| DatPrv | Date | Sim | Data de previsão do pedido |
| HorPrv | Number(005,0) | Sim | Hora de previsão do pedido |
| ObsPed | String(999) | Sim | Texto da observação |
| CodCli | Number(009,0) | Não | Código do cliente do pedido |
| CatCli | Number(003,0) | Não | Categoria do cliente (prioridade para faturamento) |
| QtdVpf | Number(003,0) | Sim | Quantidade de vezes que o pedido já foi faturado |
| QtdMfp | Number(003,0) | Sim | Quantidade máxima de faturas permitida para o pedido |
| IndAgr | String(001) | Sim | Indicativo se o cliente só aceita grade completa (agrupamento derivação) |
| SeqEnt | Number(005,0) | Sim | Sequência do endereço de entrega do cliente |
| SeqCob | Number(005,0) | Sim | Sequência do endereço de cobrança do cliente |
| SeqCto | Number(005,0) | Sim | Nome da pessoa de contato para o pedido |
| PedCli | String(020) | Sim | Número do pedido do cliente |
| CodRoe | String(003) | Sim | Código da rota de entrega |
| SeqRoe | Number(004,0) | Sim | Sequência do cliente na rota |
| CodRep | Number(009,0) | Não | Código do representante do pedido |
| CodMoe | String(003) | Sim | Código da moeda/índice que o preço unitário está representado |
| CodMcp | String(003) | Sim | Moeda ou índice para correção do preço unitário |
| DatMfp | Date | Sim | Data da cotação da moeda/índice para o fechamento do pedido |
| CotMfp | Number(019,10) | Sim | Valor da cotação da moeda/índice para o fechamento do pedido |
| DatMoe | Date | Sim | Data da cotação da moeda/índice para o faturamento do pedido |
| CotMoe | Number(019,10) | Sim | Valor da cotação da moeda/índice para o faturamento do pedido |
| FecMoe | String(001) | Sim | Indicativo se o valor da cotação para o faturamento é fechado |
| CodFcr | String(003) | Sim | Código da moeda ou índice como fator de correção (financeiro) |
| DatFcr | Date | Sim | Data da cotação da moeda ou índice para o fator de correção (financeiro) |
| CodCpg | String(006) | Não | Código da condição de pagamento |
| PgtAnt | String(001) | Não | Indicativo se o pedido é com pagamento antecipado |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| QtdAbe | Number(014,5) | Sim | Quantidade em aberto do pedido |
| QtdAen | Number(014,5) | Sim | Quantidade do pedido a entregar |
| CodTra | Number(009,0) | Sim | Código da transportadora para o pedido |
| CodRed | Number(009,0) | Sim | Código da transportadora para redespacho do pedido |
| CodVia | String(003) | Sim | Código da via de transporte do pedido |
| PlaVei | String(010) | Sim | Placa do veículo para o transporte do pedido |
| VlrFum | Number(015,2) | Sim | Valor do frete por unidade de medida quando CIF |
| QtdFre | Number(014,5) | Sim | Quantidade base na unidade do produto valida para o valor do frete |
| ForFre | Number(009,0) | Sim | Código do fornecedor para geração título de frete |
| VlrFre | Number(015,2) | Sim | Valor do frete para o pedido |
| CifFob | String(001) | Não | Indicativo se o frete é CIF ou FOB |
| VlrSeg | Number(015,2) | Sim | Valor do seguro para o pedido |
| VlrEmb | Number(015,2) | Sim | Valor das embalagens para o pedido |
| VlrEnc | Number(015,2) | Sim | Valor dos encargos para o pedido |
| VlrOut | Number(015,2) | Sim | Valor das outras despesas para o pedido |
| VlrDar | Number(015,2) | Sim | Valor do desconto para arredondamento do valor total do pedido |
| VlrFrd | Number(015,2) | Sim | Valor frete destacado |
| VlrOud | Number(015,2) | Sim | Valor outras despesas destacado |
| PerDs1 | Number(005,2) | Sim | Percentual de desconto - 1 do cliente |
| PerDs2 | Number(005,2) | Sim | Percentual de desconto - 2 do cliente |
| PerDs3 | Number(005,2) | Sim | Percentual de desconto - 3 do cliente |
| PerDs4 | Number(005,2) | Sim | Percentual de desconto - 4 do cliente |
| VlrBpr | Number(015,2) | Sim | Soma dos valores dos itens de produtos do pedido |
| VlrDpr | Number(015,2) | Sim | Soma dos valores dos descontos dos itens de produtos do pedido |
| VlrBse | Number(015,2) | Sim | Soma dos valores dos itens de serviços do pedido |
| VlrDse | Number(015,2) | Sim | Soma dos valores dos descontos dos itens de serviços do pedido |
| VlrDs1 | Number(015,2) | Sim | Valor do desconto - 1 do cliente |
| VlrDs2 | Number(015,2) | Sim | Valor do desconto - 2 do cliente |
| VlrDs3 | Number(015,2) | Sim | Valor do desconto - 3 do cliente |
| VlrDs4 | Number(015,2) | Sim | Valor do desconto - 4 do cliente |
| VlrOfe | Number(015,2) | Sim | Valor do desconto de Oferta |
| VlrDzf | Number(015,2) | Sim | Valor do desconto referente zona franca |
| VlrBip | Number(015,2) | Sim | Soma dos valores base IPI dos produtos do pedido |
| VlrIpi | Number(015,2) | Sim | Soma dos valores IPI dos produtos do pedido |
| VlrBic | Number(015,2) | Sim | Soma dos valores base ICMS dos produtos do pedido |
| VlrIcm | Number(015,2) | Sim | Soma dos valores ICMS dos produtos do pedido |
| VlrBsi | Number(015,2) | Sim | Soma dos valores base ICMS Substituído dos produtos do pedido |
| VlrSic | Number(015,2) | Sim | Soma dos valores ICMS Substituído dos produtos do pedido |
| VlrBsp | Number(015,2) | Sim | Valor base da substituição tributária do PIS |
| VlrStp | Number(015,2) | Sim | Valor da substituição tributária do PIS |
| VlrBsc | Number(015,2) | Sim | Valor base da substituição tributária da COFINS |
| VlrStc | Number(015,2) | Sim | Valor da substituição tributária da COFINS |
| VlrBis | Number(015,2) | Sim | Soma dos valores base ISS dos serviços do pedido |
| VlrIss | Number(015,2) | Sim | Soma dos valores do ISS dos serviços do pedido |
| VlrBir | Number(015,2) | Sim | Soma dos valores base IRRF dos serviços do pedido |
| VlrIrf | Number(015,2) | Sim | Soma dos valores do IRRF dos serviços do pedido |
| VlrBin | Number(015,2) | Sim | Valor base do INSS |
| VlrIns | Number(015,2) | Sim | Valor do INSS |
| VlrBco | Number(015,2) | Sim | Soma dos valores base para comissões do itens do pedido |
| VlrCom | Number(015,2) | Sim | Soma dos valores das comissões dos itens do pedido |
| VlrLpr | Number(015,2) | Sim | Valor líquido dos itens de produtos do pedido |
| VlrLse | Number(015,2) | Sim | Valor líquido dos itens de serviços do pedido |
| VlrLou | Number(015,2) | Sim | Valor líquido dos valores diversos do pedido |
| VlrLiq | Number(015,2) | Sim | Valor líquido do pedido |
| VlrFin | Number(015,2) | Sim | Valor líquido do pedido para o financeiro |
| VlrAdt | Number(015,2) | Sim | Valor pago como créditos pelo cliente |
| QtdOri | Number(014,5) | Sim | Quantidade original do pedido |
| VlrOri | Number(015,2) | Sim | Valor original do pedido |
| TemPar | String(001) | Não | Indicativo se o pedido tem parcelas especiais |
| CodPor | String(004) | Sim | Código do portador |
| CodCrt | String(002) | Sim | Código da carteira |
| SitPed | Number(001,0) | Não | Situação do pedido |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do pedido |
| ObsMot | String(250) | Sim | Observação do motivo da situação do pedido |
| PedBlo | String(001) | Sim | Indicativo se o pedido está bloqueado ou desbloqueado |
| UsuBlo | Number(010,0) | Sim | Usuário responsável pelo bloqueio ou desbloqueio do pedido |
| DatBlo | Date | Sim | Data do bloqueio ou desbloqueio do pedido |
| HorBlo | Number(005,0) | Sim | Hora do bloqueio ou desbloqueio do pedido |
| IndSig | String(001) | Não | Indicativo se o pedido está lançado no SIG |
| VerCal | Number(004,0) | Sim | Número da versão para os cálculos |
| HorIni | Number(005,0) | Sim | Hora de início da digitação do pedido |
| HorFim | Number(005,0) | Sim | Hora final da digitação do pedido |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do pedido |
| DatGer | Date | Sim | Data da geração do pedido |
| HorGer | Number(005,0) | Sim | Hora da geração do pedido |
| PerFre | Number(005,2) | Sim | Percentual de Frete |
| PerSeg | Number(005,2) | Sim | Percentual de Seguro |
| PerEmb | Number(005,2) | Sim | Percentual de Embalagens |
| PerEnc | Number(005,2) | Sim | Percentual de Encargos |
| PerOut | Number(005,2) | Sim | Percentual de Outras Despesas |
| CodSac | Number(014,0) | Sim | Número do CNPJ ou CPF do sacado |
| DocIdeSac | String(014) | Sim | CNPJ/CPF do sacado |
| CodOpe | Number(009,0) | Sim | Código da Operadora de Telemarketing |
| CodVen | Number(009,0) | Sim | Código do Vendedor |
| PedPal | Number(008,0) | Sim | Número do pedido no Palmtop |
| AcePar | String(001) | Não | Indicativo se o pedido aceita faturamento parcial |
| PerOf1 | Number(005,2) | Sim | Percentual de oferta 1 para o pedido |
| PerOf2 | Number(005,2) | Sim | Percentual de oferta 2 para o pedido |
| UsuFec | Number(010,0) | Sim | Usuário responsável pelo fechamento do pedido |
| DatFec | Date | Sim | Data do fechamento do pedido |
| HorFec | Number(005,0) | Sim | Hora do fechamento do pedido |
| CliRel | Number(009,0) | Sim | Cliente relacionado ao principal, na qual pode ser faturado parte do pedido |
| VlrBcl | Number(015,2) | Sim | Soma dos valores base do CSLL Retido |
| VlrCsl | Number(015,2) | Sim | Soma dos valores do CSLL Retido |
| VlrBpt | Number(015,2) | Sim | Soma dos valores base do PIS Retido |
| VlrPit | Number(015,2) | Sim | Soma dos valores do PIS retido |
| VlrBct | Number(015,2) | Sim | Soma dos valores base do Cofins Retido |
| VlrCrt | Number(015,2) | Sim | Soma dos valores do Cofins Retido |
| VlrBor | Number(015,2) | Sim | Soma dos valores base de Outras Retenções |
| VlrOur | Number(015,2) | Sim | Soma dos valores de Outras Retenções |
| CodMar | String(010) | Sim | Código da Marca/Etiqueta vinculada ao pedido |
| CodSro | String(003) | Sim | Código da Sub Rota |
| FilFat | Number(005,0) | Sim | Código da filial de faturamento do pedido |
| CodCdi | Number(003,0) | Sim | Código do canal de distribuição do pedido |
| CodLip | String(005) | Sim | Código da lista de preço utilizada na venda |
| CepFre | Number(008,0) | Sim | Faixa inicial do CEP para cálculo do frete |
| VlrRis | Number(015,2) | Sim | Valor de retenção de ICMS Substituto |
| AnaEmb | String(001) | Sim | Indicativo se analisou estoque de embalagens para pedido normal |
| NumEmp | String(020) | Sim | Número do empenho do Contrato que gerou o Pedido |
| QtdAne | Number(009,0) | Sim | Quantidade de vezes que o pedido foi analisado pela análise de embarque |
| DatAge | Date | Sim | Data do agendamento da entrega |
| FilNco | Number(005,0) | Sim | Código da filial da nota de cobrança |
| SnfNco | String(003) | Sim | Código da série da nota fiscal de cobrança |
| NumNco | Number(009,0) | Sim | Número da nota fiscal de cobrança |
| ExpWms | Number(001,0) | Sim | Indicativo se o pedido foi exportado para o sistema WMAS |
| VlrBpf | Number(015,2) | Sim | Soma dos valores base do PIS Faturamento dos itens do pedido |
| VlrPif | Number(015,2) | Sim | Soma dos valores do PIS Faturamento dos itens do pedido |
| VlrBcf | Number(015,2) | Sim | Soma dos valores base do COFINS Faturamento dos itens do pedido |
| VlrCff | Number(015,2) | Sim | Soma dos valores do COFINS Faturamento dos itens do pedido |
| CodApc | Number(009,0) | Sim | Código da análise da formação de preço para comércio |
| SomFre | String(001) | Sim | Indicativo se o frete deve ser somado ao valor líquido |
| QtdItp | Number(004,0) | Sim | Quantidade de itens de produtos do pedido |
| QtdIts | Number(004,0) | Sim | Quantidade de itens de serviços do pedido |
| PerDs5 | Number(005,2) | Sim | Percentual de desconto - 5 do cliente |
| VlrDs5 | Number(015,2) | Sim | Valor do desconto - 5 do cliente |
| RotAnx | Number(002,0) | Sim | Código da rotina para controle de arquivos anexos |
| NumAnx | Number(010,0) | Sim | Número do controle de arquivos anexos gerado pelo sistema |
| NumNsu | Number(010,0) | Sim | Número sequencial único do pedido |
| DatNsu | Date | Sim | Data de geração do número sequencial único do pedido |
| HorNsu | Number(005,0) | Sim | Hora de geração do número sequencial único do pedido |
| IndExp | Number(001,0) | Sim | Indicativo se o pedido foi enviado para o ECF |
| FatPed | Number(001,0) | Sim | Indica como o pedido deve ser faturado |
| QtdBpf | Number(015,3) | Sim | Quantidade da base do PIS por faturamento |
| QtdBcf | Number(015,3) | Sim | Quantidade da base do COFINS por faturamento |
| QtdBip | Number(015,3) | Sim | Quantidade da base do IPI |
| NumCes | Number(010,0) | Sim | Número da cesta de produtos comprados no balcão |
| VenCal | String(001) | Sim | Indicativo se a venda foi realizada pelo CallCenter da Loja |
| DesDef | String(040) | Sim | Descrição resumida do defeito da mercadoria |
| AnoVei | String(010) | Sim | Ano de fabricação do veículo |
| NumRen | String(020) | Sim | Renavam |
| DesMod | String(020) | Sim | Descrição do Modelo do Veículo/Produto |
| TipDav | Number(001,0) | Sim | Informa o tipo de venda que está sendo feita |
| VlrEcf | Number(015,2) | Sim | Valor de Arredondamento para ECF sobre o valor líquido total do documento |
| PerEcf | Number(005,2) | Sim | Percentual de Arredondamento para ECF sobre o valor líquido total do documento |
| TemAva | String(001) | Sim | Tem Controle de Avalista |
| CodTab | String(004) | Sim | Código da tabela de preço frete |
| SenApr | String(050) | Sim | Senha para liberação da pendência de aprovação |
| UsuApr | Number(010,0) | Sim | Usuário responsável pela aprovação |
| DatApr | Date | Sim | Data da aprovação do registro |
| HorApr | Number(005,0) | Sim | Hora da aprovação do registro |
| SitPac | Number(002,0) | Sim | Situação do pedido na análise de crédito |
| UsuPac | Number(010,0) | Sim | Usuário responsável pela análise de crédito do pedido |
| QtdPac | Number(002,0) | Sim | Quantidade de envios do pedido para análise |
| CodSaf | String(010) | Sim | Código da safra |
| DatPre | Date | Sim | Data de prestação do serviço |
| IndPre | String(001) | Sim | Indicativo presencial do consumidor |
| CurMil | String(050) | Sim | Hora corrente em milisegundos da última alteração no sistema retaguarda |
| BasIdf | Number(015,2) | Sim | Soma dos valores base do ICMS diferido dos itens do pedido |
| VlrIdf | Number(015,2) | Sim | Soma dos valores de ICMS diferido dos itens do pedido |
| SitMes | Number(001,0) | Sim | Situação da mesclagem |
| VlrIcd | Number(015,2) | Sim | ICMS Desonerado |
| MotWms | Number(006,0) | Sim | Código do motivo de bloqueio para separação no WMS |
| TipEnt | Number(001,0) | Sim | Tipo de entrega |
| ForEnt | String(001) | Sim | Forma de entrega do pedido |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |
| EqfImp | Number(003,0) | Sim | Número do equipamento fiscal que imprimiu o DAV |
| CooImp | Number(009,0) | Sim | Número do Contador da Ordem de Operação (COO) do ECF que imprimiu o DAV |
| CroEcf | Number(006,0) | Sim | Número do contador de reinício do ECF que imprimiu o DAV |
| VlrTot | Number(015,2) | Sim | Valor total antes de liquidar. Usado no Varejo Terceiros |
| NumInt | String(020) | Sim | Número do Documento Externo (Integrado) |
| IdeEvt | String(050) | Sim | Identificador do evento na fila de eventos |
| VlrIor | Number(015,2) | Sim | Soma dos Valores de ICMS partilhado com o estado remetente |
| VlrBde | Number(015,2) | Sim | Soma dos valores da Base de ICMS partilhado com o estado de destino |
| VlrIde | Number(015,2) | Sim | Soma dos valores de ICMS partilhado com o estado destinatário |
| BasFcp | Number(015,2) | Sim | Soma dos valores da base de cálculo do fundo de combate à pobreza |
| VlrFcp | Number(015,2) | Sim | Soma dos valores do fundo de combate à pobreza |
| BstFcp | Number(015,2) | Sim | Soma dos valores das bases de cálculo do FCP retido por substituição tributária |
| VstFcp | Number(015,2) | Sim | Soma dos valores do fundo de combate à pobreza retido por subst. tributária |
| IcmBfc | Number(015,2) | Sim | Soma dos valores da base de cálculo do FCP na UF de destino |
| IcmVfc | Number(015,2) | Sim | Valor do ICMS para fundo de combate à pobreza na UF de destino |
| CepIni | Number(008,0) | Sim | Faixa inicial do CEP da cidade para Transporte/CT-e OS |
| CepFim | Number(008,0) | Sim | Faixa final do CEP da cidade para Transporte/CT-e OS |
| IndItm | String(001) | Sim | Indicativo de intermediador/marketplace |
| CodItm | Number(004,0) | Sim | Código do intermediador da transação |
| CgcItm | Number(014,0) | Sim | CNPJ do intermediador da transação |
| DocIdeItm | String(014) | Sim | CNPJ do intermediador da transação |
| CadItm | String(060) | Sim | Identificador cadastrado no intermediador |
| IdeExt | Number(009,0) | Sim | Número Identificador Externo |
| IdcExt | Number(009,0) | Sim | Identificador Externo Contrato do Registro |
| CtrExt | String(020) | Sim | Número do Contrato Externo |
| CodInt | Number(002,0) | Sim | Código da integração |
| IndPac | String(001) | Sim | Indicativo se o pedido tem prioridade na análise de crédito |
| VdiFcs | Number(015,2) | Sim | Somatório do valor diferido do ICMS relativo ao FCP |
| EfiFcs | Number(015,2) | Sim | Somatório do valor efetivo do ICMS relativo ao FCP |
| VicSdt | Number(015,2) | Sim | Somatório do valor do ICMS-ST desonerado |
| ReiFcx | Number(003,0) | Sim | Quantidade de tentativas de reintegração do pedido com o fluxo de caixa SeniorX |
| QtmBic | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico |
| VmoIcm | Number(015,2) | Sim | Soma dos valores do ICMS monofásico |
| QtmBir | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Retido |
| VmoIcr | Number(015,2) | Sim | Soma dos valores do ICMS Monofásico Retido |
| QtmBif | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Diferido |
| VmoIcf | Number(015,2) | Sim | Soma dos valores do ICMS Monofásico Diferido |
| QtmBid | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Destacado |
| VmoIcd | Number(015,2) | Sim | Soma dos valores do ICMS Monofásico Destacado |
| TipGua | Number(001,0) | Sim | Tipo de Guia Agro |
| UfGuia | String(002) | Sim | UF de emissão da guia |
| SerGui | String(009) | Sim | Série de emissão da guia |
| NumGui | Number(009,0) | Sim | Número da guia |
| IdeSac | String(050) | Sim | Identificador único alfanumérico |
| CodImo | String(020) | Sim | Código da unidade imobiliária NFS-e |
| CodObr | String(020) | Sim | Obra |
| ImoCli | String(020) | Sim | Unidade Imob. de Terceiros NFS-e |
| TpoGov | Number(001,0) | Sim | Tipo de Operação com Entes Governamentais ou outros serviços sobre bens imóveis |
| IndSpf | String(001) | Sim | Indicativo se o serviço é prestado fisicamente |
| CodIop | String(006) | Sim | Código indicador da operação de fornecimento para NFS-e |
| CodDes | Number(009,0) | Sim | Código do Destinatário do serviço prestado |
| USU_desobs | String(250) | Sim | Descricao Observacao |
| USU_tipalt | Number(002,0) | Sim | Tipo Alteracao |
| USU_seqipd | Number(004,0) | Sim | Sequencia Item Pedido |
| USU_valexwork | Number(013,4) | Sim | Valor Exwork |
| USU_valfrete | Number(013,4) | Sim | Valor do Frete |
| USU_valfreint | Number(013,4) | Sim | Valor Frete Interno |
| USU_pcomfun | Number(005,3) | Sim | Percentual Comissao Fundicao |
| USU_loginweb | String(015) | Sim | Login Usuario Web |
| USU_codrev | Number(009,0) | Sim | Cliente Responsavel pelas Vendas |
| USU_datsge | Date | Sim | Data Sugestao de Entrega do Pedido |
| USU_Nomcon | String(030) | Sim | Nome do Contato |
| USU_valfreext | Number(013,4) | Sim | Valor Frete Externo |
| USU_valseguro | Number(013,4) | Sim | Valor do Seguro |
| USU_percomi | Number(006,3) | Sim | Percentual Comissao |
| USU_observa | String(250) | Sim | Observacao Lucro |
| USU_nserie | Number(014,0) | Sim | Numero de Serie |
| USU_pgtmat | String(001) | Sim | Pagto Material pelo Cliente |
| USU_paides | String(004) | Sim | Pais Destino |
| USU_seqcon | Number(001,0) | Sim | Prioridades |
| USU_clides | Number(009,0) | Sim | Cliente Destino |
| USU_DatEntPcp | Date | Sim | Data de Entrega Liberado pelo PCP |
| USU_condpagto | String(025) | Sim | Condicao de pagamento |
| USU_pedcat | Number(012,0) | Sim | Pedido Catalogo |
| USU_qlfped | String(001) | Sim | Qualificacao Pedido |
| USU_temadt | String(001) | Sim | Tem Adiantamento |
| USU_pedfat | String(001) | Sim | Pedido Ja Expedido |
| USU_Maisali | String(001) | Sim | Pedido para Mais Alimento |
| USU_pedsub | Number(008,0) | Sim | Numero do Pedido que o Substituiu |
| USU_datrecpcp | Date | Sim | Data de recebimento do pedido pelo PCP |
| USU_clicat | Number(009,0) | Sim | Cliente aux. do Catalogo Eletronico |
| USU_NumMex | String(010) | Sim | Numero da Mex |
| USU_TemFre | String(001) | Sim | Indicativo se Tem Frete |
| USU_DatRec | Date | Sim | Data de Recebimento Docto.no Pós-Vendas |
| USU_IndAtd | String(001) | Sim | Indicativo se Avalia Todos os Depósitos |
| USU_valexwork2 | Number(013,4) | Sim | Valor Exwork Cliente Final |
| USU_valfrete2 | Number(013,4) | Sim | Valor do Frete Cliente Final |
| USU_valfreint2 | Number(013,4) | Sim | Valor Frete Interno Cliente Final |
| USU_valfreext2 | Number(013,4) | Sim | Valor Frete Internacional Cliente Final |
| USU_valseguro2 | Number(013,4) | Sim | Valor do Seguro Cliente Final |
| USU_VlrCom | Number(011,2) | Sim | Valor da Comissão |
| USU_PerFla | Number(006,3) | Sim | Percentual Taxa Flat |
| USU_VlrFla | Number(011,2) | Sim | Valor Flat Financiado |
| USU_TotFla | Number(011,2) | Sim | Percentual Flat Multiplicado pelo Valor Financiado |
| USU_DatEmb | Date | Sim | Data Último Embalado |
| USU_HorEmb | Number(005,0) | Sim | Hora Último Embalado |
| USU_DatFin | Date | Sim | Data de Finalização do Pedido |
| USU_HorRecPcp | Number(005,0) | Sim | Hora de recebimento do pedido pelo PCP |
| USU_UsuRep | Number(010,0) | Sim | Usuário Representante de Vendas |
| USU_ProEsp | String(001) | Sim | Programação Especial |
| USU_UsuApr | Number(010,0) | Sim | Usuário Depto. Comercial Aprovação do Pedido |
| USU_DatApr | Date | Sim | Data Aprovação Comercial do Pedido |
| USU_SitApr | String(001) | Sim | Aprovação Comercial |
| USU_DatFatVen | Date | Sim | Sugestão Primeiro Vencimento |
| USU_TipConPed | Number(001,0) | Sim | Contato Pedido feito Via |
| USU_ReqCliEsp | Number(001,0) | Sim | Requisitos Especificados pelo Cliente Via |
| USU_ReqCliNDc | Number(001,0) | Sim | Requisitos Não declarados pelo Cliente Via |
| USU_IndPrd | String(001) | Sim | Produto deve ser Produzido? |
| USU_DatDev | Date | Sim | Data Devolvido p/ Comercial (Financeiro) |
| USU_BloFin | String(001) | Sim | Bloqueado por Pendências Financeiras (Financeiro) |
| USU_PedCon | String(001) | Sim | Pedido de Consorcio? (Financeiro) |
| USU_VlrTot | Number(015,2) | Sim | Valor Total (Financeiro) |
| USU_PrePgt | Date | Sim | Previsão de Pagamento (Financeiro) |
| USU_CODCPG | String(006) | Sim | Condição de Pagamento do GECEX |
| USU_PEDWMW | String(015) | Sim | Número do Pedido do WMW |
| USU_CodRepMet | Number(009,0) | Sim | Representante Meta Compartilhada |
| USU_CodRepMet2 | Number(009,0) | Sim | Representante 2 Meta Compartilhada |
| USU_TConRes | String(001) | Sim | Contrato de Reserva de Dominio |
| USU_CodInt | Number(002,0) | Sim | Cód. Integração do Sistema que Integrou o Pedido |
| USU_HashSHA256 | String(064) | Sim | Hash gerado pelo sistema que integrou o pedido |
| USU_DatAlt | Date | Sim | Data de Alteração do Pedido |
| USU_HorAlt | Time | Sim | Hora da Última Alteração |
| USU_EmaEnvInc | String(001) | Sim | E-mail Enviado de Inc. do Pedido |
| USU_CotDigOn | String(001) | Sim | Cotação Digitada Online |
| USU_MetCom | String(001) | Sim | Usa Meta Compartilhada |
| USU_CreEmb | String(001) | Sim | Usar Crédito Embaixadores do Agro |
| USU_DatConCon | Date | Sim | Data de Assinatura do Contrato de Consignação |
| USU_ValConCon | Number(015,0) | Sim | Validade do Contrato de Consignação em Dias |
| USU_SFNumPed | Number(010,0) | Sim | Salesforce - Num. do Pedido |
| USU_SFIDPed | String(050) | Sim | Salesforce - ID do Pedido |
| USU_VlrCre | Number(015,2) | Sim | Valor de Crédito do Programa Sou Mais Baldan Usado no Pedido |
| USU_PedSim | String(001) | Sim | Pedido - Simulação |
| USU_ResPed | String(001) | Sim | Reserva de Pedido |
| USU_GX_NomRes | String(010) | Sim | GECEX - Nome Responsável |
| USU_GX_CodOpe | Number(003,0) | Sim | GECEX - Cód. Operação |
| USU_GX_EmbIni | Date | Sim | GECEX - Data Embarque Previsto |
| USU_GX_EmbFim | Date | Sim | GECEX - Data Embarque Fim |
| USU_GX_Export | Number(010,0) | Sim | GECEX - Cód. Exportador |
| USU_GX_CodImp | Number(010,0) | Sim | GECEX - Cód. Importador |
| USU_GX_CodIdi | Number(002,0) | Sim | GECEX - Cód. Idioma |
| USU_GX_TipFre | Number(001,0) | Sim | GECEX - Tipo do Frete |
| USU_GX_DatCon | Date | Sim | GECEX - Data Confirmação |
| USU_GX_ViaTra | Number(002,0) | Sim | GECEX - Cód. Via Transporte |
| USU_GX_ConVen | String(003) | Sim | GECEX - Cód. Condição de Venda |
| USU_GX_PesBru | Number(011,5) | Sim | GECEX - Peso Bruto |
| USU_GX_BruInf | Number(011,5) | Sim | GECEX - Peso Bruto Informado |
| USU_GX_PesLiq | Number(011,5) | Sim | GECEX - Peso Liquido |
| USU_GX_Volume | String(020) | Sim | GECEX - Volume |
| USU_GX_VolCub | String(100) | Sim | GECEX - Volume Cubico Informado |
| USU_GX_ComPre | Number(005,0) | Sim | GECEX - Composição Preço Unitário |
| USU_GX_EmiPro | Date | Sim | GECEX - Emissão da Proposta |
| USU_GX_LocEmb | Number(003,0) | Sim | GECEX - Cód. Local Embarque |
| USU_GX_LocEnt | Number(003,0) | Sim | GECEX - Cód. Local Entrega |
| USU_GX_LocFre | Number(003,0) | Sim | GECEX - Cód. Local Frete |
| USU_GX_DatInc | Date | Sim | GECEX - Data Inclusão |
| USU_GX_Observ | String(255) | Sim | GECEX - Observação |
| USU_GX_PrzVal | Date | Sim | GECEX - Prazo Validade Proposta |
| USU_PedPai | Number(008,0) | Sim | Pedido Pai (Protótipo) |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed

---

## Índices

### E120PEDIndice2

**Tipo:** Não unico

Campos:
- CodCli
- SitPed
- CodEmp
- CodFil

### E120PEDIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- NumNsu
- TipDav

### E120PEDIndice4

**Tipo:** Não unico

Campos:
- CodRep

### E120PEDIndice5

**Tipo:** Não unico

Campos:
- CodEmp
- CodCpg

### USU_E120PED1

**Tipo:** Não unico

Campos:
- TnsPro
- NumPed
- CodFil
- CodEmp
- PrcPed

---

## Relacionamentos

### IR_E120PED_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E120PED_012

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E120PED_023

**Tabela:** E090REP

| Origem | Destino |
|--------|---------|
| CodRep | CodRep |

### IR_E120PED_033

**Tabela:** E028CPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCpg | CodCpg |

