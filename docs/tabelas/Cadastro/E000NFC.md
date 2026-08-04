# E000NFC

## Descrição

Tabelas - Recebimento de Documentos Eletrônicos - Notas Fiscais de Entrada - Dados Gerais

---

## Resumo

- Campos: 257
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CgcFil | Number(015,0) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| DocIdeFil | String(014) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| CgcFor | Number(014,0) | Sim | Número do CNPJ ou CPF do fornecedor |
| DocIdeFor | String(014) | Sim | Número do CNPJ ou CPF do fornecedor |
| ChvNel | String(050) | Não | Chave de acesso da nota fiscal eletrônica |
| NumNfc | Number(009,0) | Sim | Número da nota fiscal de entrada |
| CodSnf | String(003) | Sim | Código da série da nota fiscal de entrada |
| TipNfe | Number(002,0) | Sim | Tipo de nota fiscal de entrada |
| CodEdc | String(003) | Sim | Espécie de documento para fins fiscais |
| CodTri | String(005) | Sim | Código de tributação para emissão da DARF |
| DatEnt | Date | Sim | Data da Entrada da Nota |
| TnsPro | String(005) | Sim | Transação da NF entrada para produtos |
| TnsSer | String(005) | Sim | Transação da NF entrada para serviços |
| NopPro | String(005) | Sim | Natureza de operação para produtos |
| NopSer | String(005) | Sim | Natureza de operação para serviços |
| DatEmi | Date | Sim | Data de emissão da nota fiscal de entrada |
| UfsCic | String(002) | Sim | Sigla do estado base para o cálculo do ICMS |
| CodCpg | String(006) | Sim | Código da condição de pagamento da nota fiscal de entrada |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| CodMoe | String(003) | Sim | Código da moeda que a ordem de compra estava representada |
| DatMoe | Date | Sim | Data da cotação da moeda ou índice da ordem de compra |
| CotMoe | Number(019,10) | Sim | Valor da cotação da moeda ou índice da ordem de compra |
| FecMoe | String(001) | Sim | Indicativo de o valor da cotação é fechado |
| CodFcr | String(003) | Sim | Código da moeda ou índice como fator de correção (financeiro) |
| DatFcr | Date | Sim | Data da cotação da moeda ou índice para o fator de correção (financeiro) |
| QtdEmb | Number(006,0) | Sim | Quantidade de embalagens da nota fiscal |
| CodEmb | Number(004,0) | Sim | Código da embalagem |
| NumEmb | String(030) | Sim | Numeração das embalagens da nota fiscal |
| CodMs1 | Number(004,0) | Sim | Código da mensagem - 1 da nota fiscal de entrada |
| CodMs2 | Number(004,0) | Sim | Código da mensagem - 2 da nota fiscal de entrada |
| CodMs3 | Number(004,0) | Sim | Código da mensagem - 3 da nota fiscal de entrada |
| CodMs4 | Number(004,0) | Sim | Código da mensagem - 4 da nota fiscal de entrada |
| ObsNfc | String(1000) | Sim | Texto da observação |
| PesBru | Number(021,10) | Sim | Peso bruto da nota fiscal de entrada |
| PesLiq | Number(021,10) | Sim | Peso líquido da nota fiscal de entrada |
| PerDs1 | Number(005,2) | Sim | Percentual de desconto 1 |
| PerDs2 | Number(005,2) | Sim | Percentual de desconto 2 |
| PerFin | Number(004,2) | Sim | % de Acréscimo Financeiro |
| VlrDzf | Number(015,2) | Sim | Valor do desconto referente zona franca |
| VlrFre | Number(015,2) | Sim | Valor do frete da nota fiscal de entrada |
| CifFob | String(001) | Sim | Indicativo se o valor do frete é CIF ou FOB |
| VlrSeg | Number(015,2) | Sim | Valor do seguro da nota fiscal de entrada |
| VlrEmb | Number(015,2) | Sim | Valor das embalagens da nota fiscal de entrada |
| VlrEnc | Number(015,2) | Sim | Valor dos encargos financeiros da nota fiscal de entrada |
| VlrOut | Number(015,2) | Sim | Valor de outras despesas da nota fiscal de entrada |
| VlrDar | Number(015,2) | Sim | Valor dos descontos para arredondamento do total da nota de entrada |
| VlrFrd | Number(015,2) | Sim | Valor frete destacado |
| VlrOud | Number(015,2) | Sim | Valor outras despesas destacado |
| VlrBpr | Number(015,2) | Sim | Soma dos valores dos itens de produtos da nota fiscal de entrada |
| VlrDpr | Number(015,2) | Sim | Soma dos descontos dos itens de produtos da nota fiscal de entrada |
| VlrBse | Number(015,2) | Sim | Soma dos valores dos itens de serviços da nota fiscal de entrada |
| VlrDse | Number(015,2) | Sim | Soma dos descontos dos itens de serviços da nota fiscal de entrada |
| VlrDs1 | Number(015,2) | Sim | Valor do desconto 1 |
| VlrDs2 | Number(015,2) | Sim | Valor do desconto 2 |
| VlrBfu | Number(015,2) | Sim | Valor base do Funrural ou INSS dos itens de produto |
| VlrFun | Number(015,2) | Sim | Valor do Funrural ou INSS dos itens de produto |
| VlrBip | Number(015,2) | Sim | Soma dos valores base do IPI dos itens de produtos da NF de entrada |
| VlrIpi | Number(015,2) | Sim | Soma dos valores do IPI dos itens de produtos da NF de entrada |
| VlrBid | Number(015,2) | Sim | Valor base IPI presumido (50% compra no comércio) |
| VlrIpd | Number(015,2) | Sim | Valor total do IPI presumido (50% compra no comércio) |
| VlrBic | Number(015,2) | Sim | Soma dos valores base do ICMS dos itens de produtos da NF de entrada |
| VlrIcm | Number(015,2) | Sim | Soma dos valores do ICMS dos itens de produtos da NF de entrada |
| VlrBsi | Number(015,2) | Sim | Soma dos valores base do ICMS Substituído dos produtos da NF de entrada |
| VlrSic | Number(015,2) | Sim | Soma dos valores do ICMS Substituído dos produtos da NF de entrada |
| VlrBsd | Number(015,2) | Sim | Valor base ICMS substituído destacado |
| VlrIsd | Number(015,2) | Sim | Valor ICMS substituído destacado |
| VlrBsp | Number(015,2) | Sim | Valor base da substituição tributário do PIS |
| VlrStp | Number(015,2) | Sim | Valor total da substituição tributária do PIS |
| VlrBsc | Number(015,2) | Sim | Valor base da substituição tributário da COFINS |
| VlrStc | Number(015,2) | Sim | Valor total da substituição tributária do COFINS |
| VlrBis | Number(015,2) | Sim | Soma dos valores base do ISS dos itens de serviços da NF de entrada |
| VlrIss | Number(015,2) | Sim | Soma dos valores do ISS dos itens de serviços da NF de entrada |
| VlrBir | Number(015,2) | Sim | Soma dos valores base do IRRF dos itens de serviços da NF de entrada |
| VlrIrf | Number(015,2) | Sim | Soma dos valores do IRRF dos itens de serviços da NF de entrada |
| VlrBin | Number(015,2) | Sim | Valor base do INSS |
| VlrIns | Number(015,2) | Sim | Valor do INSS |
| VlrLpr | Number(015,2) | Sim | Total líquido dos itens de produtos da nota fiscal de entrada |
| VlrLse | Number(015,2) | Sim | Total líquido dos itens de serviços da nota fiscal de entrada |
| VlrLou | Number(015,2) | Sim | Total dos valores diversos da nota fiscal de entrada |
| Vlrliq | Number(015,2) | Sim | Total líquido da nota fiscal de entrada |
| VlrInf | Number(015,2) | Sim | Total líquido da nota fiscal de entrada informado para fechamento |
| VlrFin | Number(015,2) | Sim | Valor líquido da nota fiscal para o financeiro |
| SitNfc | String(001) | Sim | Situação da nota fiscal de entrada |
| CodMot | Number(006,0) | Sim | Código do motivo do cancelamento da nota fiscal de entrada |
| VerCal | Number(004,0) | Sim | Número da versão para os cálculos |
| IntImp | String(001) | Sim | Indicativo se a nota foi integrada com gestão de tributos |
| NumLot | Number(009,0) | Sim | Número do lote contábil |
| ForIss | Number(009,0) | Sim | Código do fornecedor p/ geração do título de ISS |
| IndSig | String(001) | Sim | Indicativo se a nota de devolução está lançada no SIG |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| PerFre | Number(005,2) | Sim | Percentual de Frete |
| PerSeg | Number(005,2) | Sim | Percentual de Seguro |
| PerEmb | Number(005,2) | Sim | Percentual de Embalagens |
| PerEnc | Number(005,2) | Sim | Percentual de Encargos |
| PerOut | Number(005,2) | Sim | Percentual de Outras Despesas |
| SeqOrm | Number(005,0) | Sim | Sequência do endereço de origem da mercadoria |
| VlrBpi | Number(015,2) | Sim | Soma dos valores base do PIS a recuperar dos itens de produtos da NF de entrada |
| VlrPis | Number(015,2) | Sim | Soma dos valores do PIS a recuperar dos itens de produtos da NF de entrada |
| ExpWms | Number(001,0) | Sim | Indicativo se a nota fiscal foi exportada para o sistema WMS |
| IndSin | String(001) | Sim | Indicativo se a nota fiscal foi exportada para o Sintegra |
| PrcNfc | Number(001,0) | Sim | Procedência da Nota Fiscal de Entrada |
| VlrBcr | Number(015,2) | Sim | Soma dos valores base do Cofins a recuperar |
| VlrCor | Number(015,2) | Sim | Soma dos valores do Cofins a recuperar |
| VlrBcl | Number(015,2) | Sim | Soma dos valores base do CSLL Retido |
| VlrCsl | Number(015,2) | Sim | Soma dos valores do CSLL Retido |
| VlrBpt | Number(015,2) | Sim | Soma dos valores base do PIS Retido |
| VlrPit | Number(015,2) | Sim | Soma dos valores do PIS retido |
| VlrBct | Number(015,2) | Sim | Soma dos valores base do Cofins Retido |
| VlrCrt | Number(015,2) | Sim | Soma dos valores do Cofins Retido |
| VlrBor | Number(015,2) | Sim | Soma dos valores base de Outras Retenções |
| VlrOur | Number(015,2) | Sim | Soma dos valores de Outras Retenções |
| VlrBii | Number(015,2) | Sim | Soma dos valores base do imposto de importação dos itens de produtos da nota fiscal de entrada |
| VlrIim | Number(015,2) | Sim | Soma dos valores do imposto de importação dos itens de produtos da nota fiscal de entrada |
| NumDoi | String(020) | Sim | Número do documento de importação |
| DatDoi | Date | Sim | Data do registro do documento de importação |
| IntPat | String(001) | Sim | Indicativo se a nota foi integrada com a gestão de patrimônio |
| VlrRis | Number(015,2) | Sim | Valor de retenção de ICMS Substituto |
| VlrOcl | Number(015,2) | Sim | Soma dos valores base original do CSLL Retido (anterior a verificação do valor limite p/ retenção) |
| VlrOpt | Number(015,2) | Sim | Soma dos valores base original do PIS Retido (anterior a verificação do valor limite p/ retenção) |
| VlrOct | Number(015,2) | Sim | Soma dos valores base original do Cofins Retido (anterior a verificação do valor limite p/ retenção) |
| VlrOor | Number(015,2) | Sim | Soma dos valores base original de Outras Retenções (anterior a verificação do valor limite p/ retenção) |
| CodSel | String(020) | Sim | Código da Série Legal da nota fiscal de entrada |
| CodSsl | String(002) | Sim | Código da Subsérie Legal da nota fiscal de entrada |
| PerDs3 | Number(005,2) | Sim | Percentual de desconto 3 |
| PerDs4 | Number(005,2) | Sim | Percentual de desconto 4 |
| PerDs5 | Number(005,2) | Sim | Percentual de desconto 5 |
| VlrDs3 | Number(015,2) | Sim | Valor de desconto 3 |
| VlrDs4 | Number(015,2) | Sim | Valor de desconto 4 |
| VlrDs5 | Number(015,2) | Sim | Valor de desconto 5 |
| BecIpi | Number(015,2) | Sim | Valor base de IPI creditado efetivamente |
| VecIpi | Number(015,2) | Sim | Valor de IPI creditado efetivamente |
| BecIcm | Number(015,2) | Sim | Valor base de ICMS creditado efetivamente |
| VecIcm | Number(015,2) | Sim | Valor ICMS Cred. Efetivamente |
| VlrBie | Number(015,2) | Sim | Valor base do INSS parte empresa |
| VlrIem | Number(015,2) | Sim | Valor do INSS parte empresa |
| VlrFei | Number(015,2) | Sim | Valor de frete de importação |
| VlrSei | Number(015,2) | Sim | Valor de seguro de importação |
| VlrOui | Number(015,2) | Sim | Valor de outras despesas de importação |
| BcoImp | Number(015,2) | Sim | Valor base do cofins a recuperar na importação |
| CofImp | Number(015,2) | Sim | Valor do cofins a recuperar na importação |
| BpiImp | Number(015,2) | Sim | Valor base do pis a recuperar na importação |
| PisImp | Number(015,2) | Sim | Valor do pis a recuperar na importação |
| NumCnt | Number(009,0) | Sim | Número da contagem |
| IdeNfc | String(030) | Sim | Identificador único da nota fiscal do fornecedor |
| NumCtr | Number(006,0) | Sim | Número do Contrato |
| RotNap | Number(002,0) | Sim | Código da rotina para controle de aprovação |
| PerIcf | Number(005,2) | Sim | Percentual de ICMS sobre o frete da nota fiscal de entrada |
| IcmFre | Number(015,2) | Sim | Valor de ICMS sobre o frete da nota fiscal de entrada |
| CliRcb | Number(009,0) | Sim | Código do cliente do recebimento |
| VlrBpf | Number(015,2) | Sim | Soma dos valores base PIS Faturamento dos itens da nota (Estorno devolução) |
| VlrPif | Number(015,2) | Sim | Soma dos valores do PIS Faturamento dos itens da nota fiscal (Estorno devolução) |
| VlrBcf | Number(015,2) | Sim | Soma dos valores base COFINS Faturamento dos itens da nota (Estorno devolução) |
| VlrCff | Number(015,2) | Sim | Soma dos valores do COFINS Faturamento dos itens da nota (Estorno devolução) |
| RotAnx | Number(002,0) | Sim | Código da rotina para controle de arquivos anexos |
| NumAnx | Number(010,0) | Sim | Número do controle de arquivos anexos gerado pelo sistema |
| PlaVei | String(010) | Sim | Placa do veículo de transporte das mercadorias da nota fiscal de entrada |
| CodVia | String(003) | Sim | Via de transporte da nota fiscal de entrada |
| SomFre | String(001) | Sim | Indicativo se o frete deve ser somado ao valor líquido da nota fiscal |
| UfsVei | String(002) | Sim | Sigla do estado do veículo de transporte das mercadorias da nota fiscal de entrada |
| NumInt | String(020) | Sim | Número do Documento Externo (Integrado) |
| FilFix | Number(005,0) | Sim | Código da filial |
| NumFix | Number(009,0) | Sim | Número da Fixação |
| NumOcp | Number(008,0) | Sim | Número da ordem de compra de depósito/a fixar |
| CodEqu | Number(003,0) | Sim | Código do equipamento fiscal |
| NumCfi | Number(009,0) | Sim | Número do cupom fiscal de referência da redução Z |
| TipNdi | String(001) | Sim | Tipo do documento de importação |
| LocDes | String(060) | Sim | Local onde ocorreu o desembaraço aduaneiro |
| DatDes | Date | Sim | Data do desembaraço aduaneiro |
| UfsDes | String(002) | Sim | Sigla da UF onde ocorreu o desembaraço aduaneiro |
| CodExp | Number(009,0) | Sim | Código do exportador (Fornecedor emitente da Nf-e) |
| NumDfs | Number(015,0) | Sim | Número do Documento Fiscal de Serviço |
| QtdBpi | Number(015,3) | Sim | Quantidade da base do PIS a recuperar |
| QtdBco | Number(015,3) | Sim | Quantidade da base do COFINS a recuperar |
| QtdBip | Number(015,3) | Sim | Quantidade da base do IPI |
| QtdBpf | Number(015,3) | Sim | Quantidade da base do PIS por faturamento (Estorno devolução) |
| QtdBcf | Number(015,3) | Sim | Quantidade da base do COFINS por faturamento (Estorno devolução) |
| BasOir | Number(015,2) | Sim | Soma dos valores originais de IRRF (anterior verificação do limite p/ retenção) |
| VlrOir | Number(015,2) | Sim | Soma dos valores base original de Outras Retenções (anterior a verificação do valor limite p/ retenção) |
| VlrSub | Number(015,2) | Sim | Valor do subsídio na nota fiscal de compra |
| TotCit | Number(015,2) | Sim | Valor total do imposto CIDE-Tecnologia |
| CgcTra | Number(014,0) | Sim | Número do CNPJ ou CPF da transportadora |
| DocIdeTra | String(014) | Sim | Número do CNPJ ou CPF da transportadora |
| CgcRed | Number(014,0) | Sim | Número do CNPJ ou CPF do Redespacho |
| DocIdeRed | String(014) | Sim | Número do CNPJ ou CPF do Redespacho |
| CgcOcp | Number(015,0) | Sim | CNPJ Filial OC |
| DocIdeOcp | String(014) | Sim | Número do CNPJ ou CPF da OC |
| StaNfv | Number(001,0) | Sim | Status da Nota Fiscal |
| IndCan | String(001) | Sim | Indicativo de cancelamento |
| VlrIbs | Number(015,2) | Sim | Soma dos valores base do ICMS Simples Nacional dos itens da NF de entrada |
| VlrIsn | Number(015,2) | Sim | Soma dos valores do ICMS Simples Nacional dos itens da NF de entrada |
| VlrAfm | Number(015,2) | Sim | Valor adicional ao frete para renovação da marinha mercante |
| TipItd | Number(001,0) | Sim | Forma de importação quanto à intermediação |
| CgcAdq | Number(014,0) | Sim | CNPJ/CPF do adquirente ou do encomendante |
| DocIdeAdq | String(014) | Sim | CNPJ/CPF do adquirente ou do encomendante |
| UfsAdq | String(002) | Sim | Sigla da UF do adquirente ou do encomendante |
| CodVii | Number(002,0) | Sim | Via de transporte internacional informada na DI |
| TipCte | Number(001,0) | Sim | Informação do tipo do CT-e |
| TipSer | Number(001,0) | Sim | Informação do tipo de serviço do CT-e |
| BasIdf | Number(015,2) | Sim | Soma dos valores base do ICMS diferido dos itens |
| VlrIdf | Number(015,2) | Sim | Soma dos valores de ICMS diferido dos itens |
| GenA01 | String(080) | Sim | Tratamentos externos ao ERP nos dados gerais da nota - A1 |
| GenA02 | String(080) | Sim | Tratamentos externos ao ERP nos dados gerais da nota - A2 |
| GenA03 | String(080) | Sim | Tratamentos externos ao ERP nos dados gerais da nota - A3 |
| GenA04 | String(080) | Sim | Tratamentos externos ao ERP nos dados gerais da nota - A4 |
| GenN01 | Number(015,2) | Sim | Tratamentos externos ao ERP nos dados gerais da nota - N1 |
| GenN02 | Number(015,2) | Sim | Tratamentos externos ao ERP nos dados gerais da nota - N2 |
| GenN03 | Number(015,2) | Sim | Tratamentos externos ao ERP nos dados gerais da nota - N3 |
| GenN04 | Number(015,2) | Sim | Tratamentos externos ao ERP nos dados gerais da nota - N4 |
| VlrIcd | Number(015,2) | Sim | ICMS Desonerado |
| GenA05 | String(080) | Sim | Tratamentos externos ao ERP nos dados gerais da nota - A5 |
| GenA06 | String(080) | Sim | Tratamentos externos ao ERP nos dados gerais da nota - A6 |
| GenN05 | Number(013,2) | Sim | Tratamentos externos ao ERP nos dados gerais da nota - N5 |
| GenN06 | Number(013,2) | Sim | Tratamentos externos ao ERP nos dados gerais da nota - N6 |
| IdeLre | Number(009,0) | Sim | Identificador de registro |
| TipOpe | String(001) | Sim | Tipo de operação do documento eletrônico |
| FinNFe | Number(001,0) | Sim | Finalidade de emissão da NF-e |
| QecIpi | Number(015,3) | Sim | Quantidade da Base de IPI Creditado Efetivamente |
| BasIef | Number(015,2) | Sim | Soma dos valores base do ICMS dos produtos da nota fiscal de saída para entrega futura |
| VlrIef | Number(015,2) | Sim | Soma dos valores do ICMS dos produtos da nota fiscal de saída para entrega futura |
| VlrIor | Number(015,2) | Sim | Soma dos Valores de ICMS partilhado com o estado remetente |
| VlrBde | Number(015,2) | Sim | Soma dos valores da Base de ICMS partilhado com o estado de destino |
| VlrIde | Number(015,2) | Sim | Soma dos valores de ICMS partilhado com o estado destinatário |
| BasFcp | Number(015,2) | Sim | Soma dos valores da base de cálculo do fundo de combate à pobreza |
| VlrFcp | Number(015,2) | Sim | Soma dos valores do fundo de combate à pobreza |
| BstFcp | Number(015,2) | Sim | Soma dos valores das bases de cálculo do FCP retido por substituição tributária |
| VstFcp | Number(015,2) | Sim | Soma dos valores do fundo de combate à pobreza retido por subst. tributária |
| BreFcp | Number(015,2) | Sim | Soma dos valores da Base de cálculo do FCP retido anteriormente por subst. trib. |
| VreFcp | Number(015,2) | Sim | Soma dos valores do FCP retido anteriormente por substituição tributária. |
| IcmBfc | Number(015,2) | Sim | Soma dos valores da base de cálculo do FCP na UF de destino |
| IcmVfc | Number(015,2) | Sim | Soma dos valores do ICMS para fundo de combate à pobreza na UF de destino |
| InsEst | String(025) | Sim | Inscrição estadual do fornecedor |
| VerDoc | Number(005,2) | Sim | Versão do documento eletrônico |
| RaiRem | Number(007,0) | Sim | Código da cidade do remetente da prestação do CTe |
| RaiDes | Number(007,0) | Sim | Código da cidade de destino da prestação do CTe |
| VlrPdg | Number(015,2) | Sim | Soma dos valores de Pedágio |
| InsFil | String(025) | Sim | Inscrição estadual da filial da empresa |
| CodRai | Number(007,0) | Sim | Código da cidade para recolhimento do ISS (Tabela RAIS) |
| VdiFcs | Number(015,2) | Sim | Somatório do valor diferido do ICMS relativo ao FCP |
| EfiFcs | Number(015,2) | Sim | Somatório do valor efetivo do ICMS relativo ao FCP |
| VicSdt | Number(015,2) | Sim | Somatório do valor do ICMS-ST desonerado |
| QtmBic | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico |
| VmoIcm | Number(015,2) | Sim | Soma dos valores do ICMS monofásico |
| QtmBir | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Retido |
| VmoIcr | Number(015,2) | Sim | Soma dos valores do ICMS Monofásico Retido |
| QtmBif | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Diferido |
| VmoIcf | Number(015,2) | Sim | Soma dos valores do ICMS Monofásico Diferido |
| QtmBid | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Destacado |
| VmoIcd | Number(015,2) | Sim | Soma dos valores do ICMS Monofásico Destacado |
| TipAei | String(001) | Sim | Indicativo do tipo de pessoa do adquirente ou do encomendante (Jurídica ou Física) |
| ChvSub | String(050) | Sim | Chave de acesso do Conhecimento de Transporte Eletrônico Substituído |
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| IdeFor | String(050) | Sim | Identificador do fornecedor |
| IdeOrm | String(050) | Sim | Identificador da origem da mercadoria |
| IdeTra | String(050) | Sim | Identificador da transportadora |
| DatPrv | Date | Sim | Data previsão entrega |

---

## Chave Primária

- IdeUni

---

## Índices

### E000NFCIndice1

**Tipo:** Não unico

Campos:
- DocIdeFil
- DocIdeFor
- ChvNel

### E000NFCIndice2

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel

---

## Relacionamentos

Nenhum relacionamento cadastrado.
