# E440NFC

## Descrição

Compras - Notas Fiscais de Entrada - Dados Gerais

---

## Resumo

- Campos: 253
- Chave Primária: 5 campo(s)
- Índices: 3
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| TipNfe | Number(002,0) | Sim | Tipo de nota fiscal de entrada |
| CodEdc | String(003) | Sim | Espécie de documento para fins fiscais |
| CodTri | String(005) | Sim | Código de tributação para emissão da DARF |
| DatEnt | Date | Sim | Data da Entrada da Nota |
| TnsPro | String(005) | Sim | Transação da NF entrada para produtos |
| TnsSer | String(005) | Sim | Transação da NF entrada para serviços |
| NopPro | String(005) | Sim | Natureza de operação para produtos |
| NopSer | String(005) | Sim | Natureza de operação para serviços |
| DatEmi | Date | Não | Data de emissão da nota fiscal de entrada |
| UfsCic | String(002) | Sim | Sigla do estado base para o cálculo do ICMS |
| CodCpg | String(006) | Não | Código da condição de pagamento da nota fiscal de entrada |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| CodMoe | String(003) | Sim | Código da moeda que a ordem de compra estava representada |
| DatMoe | Date | Sim | Data da cotação da moeda ou índice da ordem de compra |
| CotMoe | Number(019,10) | Sim | Valor da cotação da moeda ou índice da ordem de compra |
| FecMoe | String(001) | Sim | Indicativo de o valor da cotação é fechado |
| CodFcr | String(003) | Sim | Código da moeda ou índice como fator de correção (financeiro) |
| DatFcr | Date | Sim | Data da cotação da moeda ou índice para o fator de correção (financeiro) |
| CodTra | Number(009,0) | Sim | Código da transportadora da nota fiscal de entrada |
| CodRed | Number(009,0) | Sim | Código da transportadora de redespacho da nota fiscal de entrada |
| QtdEmb | Number(006,0) | Sim | Quantidade de embalagens da nota fiscal |
| CodEmb | Number(004,0) | Sim | Código da embalagem |
| NumEmb | String(030) | Sim | Numeração das embalagens da nota fiscal |
| CodMs1 | Number(004,0) | Sim | Código da mensagem - 1 da nota fiscal de entrada |
| CodMs2 | Number(004,0) | Sim | Código da mensagem - 2 da nota fiscal de entrada |
| CodMs3 | Number(004,0) | Sim | Código da mensagem - 3 da nota fiscal de entrada |
| CodMs4 | Number(004,0) | Sim | Código da mensagem - 4 da nota fiscal de entrada |
| ObsNfc | String(1000) | Sim | Texto da observação |
| PesBru | Number(014,5) | Sim | Peso bruto da nota fiscal de entrada |
| PesLiq | Number(014,5) | Sim | Peso líquido da nota fiscal de entrada |
| PerDs1 | Number(005,2) | Sim | Percentual de desconto 1 |
| PerDs2 | Number(005,2) | Sim | Percentual de desconto 2 |
| PerFin | Number(004,2) | Sim | % de Acréscimo Financeiro |
| VlrDzf | Number(015,2) | Sim | Valor do desconto referente zona franca |
| VlrFre | Number(015,2) | Sim | Valor do frete da nota fiscal de entrada |
| CifFob | String(001) | Não | Indicativo se o valor do frete é CIF ou FOB |
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
| SitNfc | String(001) | Não | Situação da nota fiscal de entrada |
| CodMot | Number(006,0) | Sim | Código do motivo do cancelamento da nota fiscal de entrada |
| VerCal | Number(004,0) | Sim | Número da versão para os cálculos |
| IntImp | String(001) | Não | Indicativo se a nota foi integrada com gestão de tributos |
| NumLot | Number(009,0) | Sim | Número do lote contábil |
| ForIss | Number(009,0) | Sim | Código do fornecedor p/ geração do título de ISS |
| IndSig | String(001) | Não | Indicativo se a nota de devolução está lançada no SIG |
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
| FilApr | Number(005,0) | Sim | Código da filial da aprovação quando controle da rotina for por filial |
| NumApr | Number(010,0) | Sim | Número da aprovação gerado pelo sistema |
| SitApr | String(003) | Sim | Situação do controle de aprovação |
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
| ChvNel | String(050) | Sim | Chave de acesso da nota fiscal eletrônica |
| SomFre | String(001) | Sim | Indicativo se o frete deve ser somado ao valor líquido da nota fiscal |
| UfsVei | String(002) | Sim | Sigla do estado do veículo de transporte das mercadorias da nota fiscal de entrada |
| NumInt | String(020) | Sim | Número do Documento Externo (Integrado) |
| FilFix | Number(005,0) | Sim | Código da filial |
| NumFix | Number(009,0) | Sim | Número da Fixação |
| FilOcp | Number(005,0) | Sim | Código da filial da ordem de compra de depósito/a fixar |
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
| VlrImp | Number(015,2) | Sim | Valor da parcela importada do exterior |
| UsuFec | Number(010,0) | Sim | Usuário responsável pelo fechamento da nota fiscal de entrada |
| DatFec | Date | Sim | Data do fechamento da nota fiscal de entrada |
| HorFec | Number(005,0) | Sim | Hora do fechamento da nota fiscal de entrada |
| DatInv | Date | Sim | Data base do inventário |
| FilCes | Number(005,0) | Sim | Filial do controle de Entrada/Saída para pesagem |
| DatCes | Date | Sim | Data do controle de Entrada/Saída para pesagem |
| SeqCes | Number(006,0) | Sim | Sequência de entrada na data |
| TipDev | Number(001,0) | Sim | Tipo de devolução escolhida no processo de saída de mercadorias |
| CodSaf | String(010) | Sim | Código da safra |
| VlrBsn | Number(015,2) | Sim | Valor base do Senar dos itens de produto |
| VlrSen | Number(015,2) | Sim | Valor do Senar dos itens de produto |
| VlrIbs | Number(015,2) | Sim | Soma dos valores base do ICMS Simples Nacional dos itens da NF de entrada |
| VlrIsn | Number(015,2) | Sim | Soma dos valores do ICMS Simples Nacional dos itens da NF de entrada |
| VlrAfm | Number(015,2) | Sim | Valor adicional ao frete para renovação da marinha mercante |
| TipItd | Number(001,0) | Sim | Forma de importação quanto à intermediação |
| CgcAdq | Number(014,0) | Sim | CNPJ/CPF do adquirente ou do encomendante |
| DocIdeAdq | String(014) | Sim | CNPJ/CPF do adquirente ou do encomendante |
| UfsAdq | String(002) | Sim | Sigla da UF do adquirente ou do encomendante |
| CodVii | Number(002,0) | Sim | Via de transporte internacional informada na DI |
| VlrInt | Number(015,2) | Sim | Valor total de intermediação de serviços na nota de entrada |
| TipCte | Number(001,0) | Sim | Informação do tipo do CT-e |
| TipSer | Number(001,0) | Sim | Informação do tipo de serviço do CT-e |
| BasIdf | Number(015,2) | Sim | Soma dos valores base do ICMS diferido dos itens da nota fiscal de entrada |
| VlrIdf | Number(015,2) | Sim | Soma dos valores de ICMS diferido dos itens da nota fiscal de entrada |
| ReaTcp | Date | Sim | Data da realocação do título para controle de projetos |
| DisNfc | Number(001,0) | Sim | Disponibilidade da nota fiscal de compra |
| VlrIcd | Number(015,2) | Sim | ICMS Desonerado |
| CodRai | Number(007,0) | Sim | Código da cidade para recolhimento do ISS (Tabela RAIS) |
| SomOcl | Number(015,2) | Sim | Soma dos valores originais de CSLL (anterior verificação limite retenção) |
| SomOpt | Number(015,2) | Sim | Soma dos valores originais de PIS (anterior verificação limite retenção) |
| SomOct | Number(015,2) | Sim | Soma dos valores originais de Cofins (anterior verificação limite retenção) |
| SomOor | Number(015,2) | Sim | Soma dos val. orig. de Out. Ret. (anterior verif. do valor limite p/ retenção) |
| OriInv | String(001) | Sim | Nota gerada apartir de inventário (S-Originada, outro valor-não originada) |
| ValNfc | String(001) | Sim | Valorização da Nota Fiscal de Entrada de Frete |
| SeqEnt | Number(005,0) | Sim | Sequencia do endereço de entrega |
| QtbCim | Number(015,3) | Sim | Quantidade da base do COFINS a recuperar na importação |
| QtbPim | Number(015,3) | Sim | Quantidade da base do PIS a recuperar na importação |
| VlrTer | Number(015,2) | Sim | Valor cobrado em nome de terceiros |
| QecIpi | Number(015,3) | Sim | Quantidade da Base de IPI Creditado Efetivamente |
| DatPta | Date | Sim | Data de permanência da nota no território aduaneiro. |
| TipRaf | Number(001,0) | Sim | Tipo de recuperação de ICMS sobre acréscimo financeiro |
| BasIef | Number(015,2) | Sim | Soma dos valores base do ICMS dos produtos da nota fiscal de entrada para entrega futura |
| VlrIef | Number(015,2) | Sim | Soma dos valores do ICMS dos produtos da nota fiscal de entrada para entrega futura |
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
| IcmVfc | Number(015,2) | Sim | Valor do ICMS para fundo de combate à pobreza na UF de destino |
| VerDoc | Number(005,2) | Sim | Versão do documento eletrônico |
| RaiRem | Number(007,0) | Sim | Código da cidade do remetente da prestação do CTe |
| RaiDes | Number(007,0) | Sim | Código da cidade de destino da prestação do CTe |
| BasApe | Number(015,2) | Sim | Base de cálculo da aposentadoria especial |
| VlrApe | Number(015,2) | Sim | Valor da aposentadoria especial |
| VlrBgi | Number(015,2) | Sim | Base de cálculo do GILRAT |
| VlrGil | Number(015,2) | Sim | Valor do GILRAT |
| VlrPdg | Number(015,2) | Sim | Soma dos valores de Pedágio |
| DatPre | Date | Sim | Data de prestação do serviço |
| USU_TNIVAPR | String(100) | Sim | Nivel Aprovação |
| USU_TPROWOF | String(020) | Sim | Indentificador Processo |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf

---

## Índices

### E440NFCIndice2

**Tipo:** Não unico

Campos:
- CodFor
- SitNfc
- CodEmp
- CodFil

### E440NFCIndice3

**Tipo:** Não unico

Campos:
- DatEnt
- NumLot
- SitNfc
- CodFil
- CodEmp

### USU_E440NFC1

**Tipo:** Não unico

Campos:
- SitNfc
- DatEnt
- CodEmp
- CodFil
- CodFor
- TnsSer
- NumNfc

---

## Relacionamentos

### IR_E440NFC_002

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E440NFC_004

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E440NFC_015

**Tabela:** E028CPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCpg | CodCpg |

