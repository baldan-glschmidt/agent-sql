# E001TCP

## Descrição

Tabelas - Transações - Compras

---

## Resumo

- Campos: 179
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| CprRpi | String(001) | Sim | Indicativo se a transação recupera o PIS |
| CprIbp | String(001) | Sim | Transação considera o IPI na base de PIS |
| CprFrp | String(001) | Sim | Transação considera frete na base do PIS |
| CprSep | String(001) | Sim | Transação considera o seguro na base do PIS |
| CprEmp | String(001) | Sim | Transação considera a embalagem na base do PIS |
| CprEnp | String(001) | Sim | Transação considera os encargos financeiro na base do PIS |
| CprOup | String(001) | Sim | Transação considera as outras despesas na base do PIS |
| CprDap | String(001) | Sim | Transação considera arredondamento na base do PIS |
| CprFdp | String(001) | Sim | Transação considera o frete destacado na base do PIS |
| CprOdp | String(001) | Sim | Transação considera outras despesas destacadas na base do PIS |
| CprRco | String(001) | Sim | Indicativo se a transação recupera o Cofins |
| CprIbc | String(001) | Sim | Transação considera o IPI na base de Cofins |
| CprSec | String(001) | Sim | Transação considera o seguro na base do Cofins |
| CprFrc | String(001) | Sim | Transação considera frete na base do Cofins |
| CprEmc | String(001) | Sim | Transação considera a embalagem na base do Cofins |
| CprEco | String(001) | Sim | Transação considera os encargos financeiro na base do Cofins |
| CprOuc | String(001) | Sim | Transação considera as outras despesas na base do Cofins |
| CprDac | String(001) | Sim | Transação considera arredondamento na base do Cofins |
| CprFdc | String(001) | Sim | Transação considera o frete destacado na base do Cofins |
| CprOdc | String(001) | Sim | Transação considera outras despesas destacadas na base do Cofins |
| CprCof | String(001) | Sim | Indicativo de como a Transação considera o valor  do Cofins do total da nota fiscal entrada |
| CprTco | String(001) | Sim | (descontinuado) Indicativo se no fechamento da nota fiscal deve ser gerado título de Cofins |
| CprLco | Number(009,2) | Sim | Valor mínimo da Retenção do Cofins considerado na nota fiscal de entrada |
| CprPis | String(001) | Sim | Indicativo de como a Transação considera o valor  do PIS do total da nota fiscal entrada |
| CprTpi | String(001) | Sim | (descontinuado) Indicativo se no fechamento da nota fiscal deve ser gerado título de PIS |
| CprLpi | Number(009,2) | Sim | Valor mínimo da Retenção do PIS considerado na nota fiscal de entrada |
| CprEnl | String(001) | Sim | Transação considera os encargos financeiro na base do CSLL |
| CprOul | String(001) | Sim | Transação considera as outras despesas na base do CSLL |
| CprDal | String(001) | Sim | Transação considera arredondamento na base do CSLL |
| CprOdl | String(001) | Sim | Transação considera outras despesas destacadas na base do CSLL |
| CprLcl | Number(009,2) | Sim | Valor mínimo do CSLL considerado na nota fiscal de entrada |
| CprCsl | String(001) | Sim | Indicativo de como a Transação considera o valor  do CSLL do total da nota fiscal entrada |
| CprTcl | String(001) | Sim | (descontinuado) Indicativo se no fechamento da nota fiscal deve ser gerado título de CSLL |
| CprEno | String(001) | Sim | Transação considera os encargos financeiro na base de Outras Retenções |
| CprOuo | String(001) | Sim | Transação considera as outras despesas na base de Outras Retenções |
| CprDao | String(001) | Sim | Transação considera arredondamento na base do Out. Ret. |
| CprOdo | String(001) | Sim | Transação considera outras despesas destacadas na base de Outras Retenções |
| CprLor | Number(009,2) | Sim | Valor mínimo de Outras Retenções considerado na nota fiscal de entrada |
| CprOur | String(001) | Sim | Indicativo de como a Transação considera o valor  de Outras Retenções do total da nota fiscal entrada |
| CprTor | String(001) | Sim | (descontinuado) Indicativo se no fechamento da nota fiscal deve ser gerado título de Outras Retenções |
| FreIim | String(001) | Sim | Transação considera o frete na base do II |
| SegIim | String(001) | Sim | Transação considera o seguro na base do II |
| EmbIim | String(001) | Sim | Transação considera a embalagem na base do II |
| EncIim | String(001) | Sim | Transação considera os encargos na base do II |
| OutIim | String(001) | Sim | Transação considera outras despesas na base do II |
| DarIim | String(001) | Sim | Transação considera valor arredondamento na base do II |
| FrdIim | String(001) | Sim | Transação considera o frete destacado na base do II |
| OudIim | String(001) | Sim | Transação considera outras despesas destacadas na base do II |
| IimIpi | String(001) | Sim | Transação considera valor do II na base do IPI |
| IimIcm | String(001) | Sim | Transação considera valor do II na base do ICMS |
| CalDzf | String(001) | Sim | Indicativo se deve ser calculado o desconto Suframa para a nota fiscal de entrada |
| SubPis | String(001) | Sim | Transação considera ICMS Substituto na base de PIS a recuperar |
| SubCof | String(001) | Sim | Transação considera ICMS Substituto na base de COFINS a recuperar |
| GerPed | String(001) | Sim | Indicativo se gera pedido para o item no fechamento da nota fiscal de entrada ou ordem de compra |
| OriVmo | Number(001,0) | Sim | Origem do valor do movimento de estoque nas notas de devoluções, retornos e transferências |
| CprFim | String(001) | Sim | Soma valor de frete de importação na base do ICMS |
| CprSim | String(001) | Sim | Soma valor de seguro de importação na base do ICMS |
| CprOim | String(001) | Sim | Soma valor de outras despesas de importação na base do ICMS |
| CprFii | String(001) | Sim | Soma valor do frete de importação na base do IPI |
| CprSii | String(001) | Sim | Soma valor de seguro de importação na base do IPI |
| CprOii | String(001) | Sim | Soma valor de outras despesas de importação na base do IPI |
| FriIim | String(001) | Sim | Soma valor de frete de importação na base do II |
| SgiIim | String(001) | Sim | Soma valor de seguro de importação na base do II |
| OtiIim | String(001) | Sim | Soma valor de outras despesas de importação na base do II |
| CprFip | String(001) | Sim | Soma valor de frete de importação na base do PIS |
| CprSip | String(001) | Sim | Soma valor de seguro de importação na base do PIS |
| CprOip | String(001) | Sim | Soma valor de outras despesas de importação na base do PIS |
| CprFic | String(001) | Sim | Soma valor de frete de importação na base do cofins |
| CprSic | String(001) | Sim | Soma valor de seguro de importação na base do cofins |
| CprOic | String(001) | Sim | Soma valor de outras despesas de importação na base do cofins |
| TemCnt | String(001) | Sim | Indica se a nota necessita ou não de conferência |
| NfcHro | String(001) | Sim | Indicativo se a nota fiscal de entrada herda o rateio da origem (ordem de compra, nota fiscal de saída ou contrato) |
| GerCnt | String(001) | Sim | Indicativo se deve gerar conferência automática no momento do fechamento da NF Entrada (Somente se necessita conferência) |
| CprCtr | String(001) | Sim | Transação nota fiscal de entrada exige contrato |
| CstIpi | String(002) | Sim | Código da situação tributária de IPI |
| CstPis | String(002) | Sim | Código da situação tributária de PIS |
| CstCof | String(002) | Sim | Código da situação tributária de COFINS |
| TnsBnf | String(001) | Sim | Indicativo se a transação é utilizada para movimentos de entrada de bonificação |
| TipRgr | Number(001,0) | Sim | Tipo de recebimento |
| ReaPed | String(001) | Sim | Indicativo se a transação reabilita o pedido vinculado a nota fiscal de saída utilizada como origem |
| TriCit | String(001) | Sim | Indicativo se a transação tributa CIDE-Tecnologia |
| IndRci | String(001) | Sim | Indicativo se a transação permite retorno de componentes industrializados |
| ObrCps | String(001) | Sim | Indicativo se é obrigatório informar o código de produto/serviço nas NFE |
| ObrFxt | String(001) | Sim | Indicativo se é obrigatória a ligação família/produto/serviço X transação |
| ObrFxf | String(001) | Sim | Indicativo se é obrigatória a ligação Família/Produto/Serviço X Fornecedor |
| SomIps | String(001) | Sim | Indicativo se calcula PIS importação nas notas fiscais de importação e ordens de compra |
| SomIco | String(001) | Sim | Indicativo se calcula COFINS importação nas notas fiscais de importação e ordens de compra |
| IndCco | String(001) | Sim | Indicativo se a ordem de compra participa do controle de cota de compra |
| ObrTxf | String(001) | Sim | Indicativo se é obrigatória a ligação transação X conta financeira |
| CprArs | String(001) | Sim | Transação considera valor arredondamento na base do SENAR/SENAT |
| CprOse | String(001) | Sim | Transação considera outras despesas na base do SENAR/SENAT |
| CprEse | String(001) | Sim | Transação considera os encargos na base do SENAR/SENAT |
| CprOds | String(001) | Sim | Transação considera outras despesas destacadas na base do SENAR/SENAT |
| CprIse | String(001) | Sim | Indicativo como transação considera SENAR/SENAT no total da nota fiscal entrada |
| CprBic | String(003) | Sim | Código da modalidade da base de cálculo do ICMS padrão para a transação |
| IndIsv | String(001) | Sim | Indicativo se a transação é utilizada para intermediação de serviços |
| DscBip | String(001) | Sim | Considerar descontos na base de cálculo do IPI |
| CprIpp | String(001) | Sim | Transação considera a subtração do IPI Presumido na base do PIS |
| CprIpc | String(001) | Sim | Transação considera a subtração do IPI Presumido na base do COFINS |
| CprAim | String(001) | Sim | Soma valor adicional ao frete para renovação da marinha mercante na base do ICMS |
| PerDif | Number(007,4) | Sim | Percentual de diferimento da transação de compra |
| RecIst | String(001) | Sim | Indicativo se deve recuperar o valor do ICMS ST no CIAP |
| RecDai | String(001) | Sim | Indicativo se deve recuperar o valor do Difa. no CIAP |
| IcmDes | String(001) | Sim | Indicativo se a transação considera desoneração de ICMS |
| CodPri | String(004) | Sim | Código da tabela de presunção IRPJ |
| CodPrc | String(004) | Sim | Código da tabela de presunção CSLL |
| TipCdv | String(001) | Não | Tipo de cálculo para devolução |
| CprTax | String(001) | Sim | Indicativo se a transação é de compra de taxa |
| CodEnq | Number(003,0) | Sim | Código de enquadramento legal do IPI |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| PisRbi | String(001) | Sim | PIS a Recuperar Base ICMS |
| CofRbi | String(001) | Sim | COFINS a Recuperar Base ICMS |
| PisDes | String(001) | Sim | Indicativo de como a transação considera o ICMS desonerado na base do PIS |
| CofDes | String(001) | Sim | Indicativo de como a transação considera o ICMS desonerado na base do COFINS |
| IpiDes | String(001) | Sim | Indicativo de como a transação considera o ICMS desonerado na base do IPI |
| IimPre | String(001) | Sim | Somar valor do II ao preço unitário do item na NFE |
| ArrCid | String(001) | Sim | Transação considera valor arredondamento na base CIDE |
| OutCid | String(001) | Sim | Transação considera outras despesas na base CIDE |
| EncCid | String(001) | Sim | Transação considera os encargos na base CIDE |
| OudCid | String(001) | Sim | Transação considera outras despesas destacadas na base CIDE |
| EstNft | Number(001,0) | Sim | Indica qual deve ser o estado após a geração da nota fiscal por transferência |
| CprLin | Number(009,2) | Sim | Valor mínimo da Retenção do INSS considerado na nota fiscal de entrada |
| ConAtr | String(001) | Sim | Controla ATR (Açúcar Total Recuperável) médio |
| NatOps | Number(001,0) | Sim | Natureza da operação de serviço |
| CprPod | String(001) | Sim | Considera PIS Importação no valor de outras despesas no XML |
| CprCod | String(001) | Sim | Considera Cofins Importação no valor de outras despesas no XML |
| ZerVlr | String(001) | Sim | Zerar valor contábil/mercadoria das notas fiscais na integração para tributos |
| CprImb | String(001) | Sim | Crédito do ICMS referente compra de imobilizado na nota fiscal |
| PadPii | Number(008,5) | Sim | Percentual Diário da Admissão Temporária do Imposto Importação |
| PadIpi | Number(008,5) | Sim | Percentual Diário da Admissão Temporária do IPI Importação |
| PadPis | Number(008,5) | Sim | Percentual Diário da Admissão Temporária do PIS Importação |
| PadCof | Number(008,5) | Sim | Percentual Diário da AdmissãoTemporária do Cofins Importação |
| PadCid | Number(008,5) | Sim | Percentual Diário da Admissão Temporária do CIDE Combustíveis |
| PadAfr | Number(008,5) | Sim | Percentual Diário da Admissão Temporária do Adicional ao Frete para Renovação da Marinha Mercante |
| IndRpp | String(001) | Sim | Indicativo se a transação é de recebimento de preço de pauta |
| InsIrf | String(001) | Sim | Transação considera INSS na base do IRRF |
| IssDdi | String(001) | Sim | Indicativo se deve descontar o valor de dedução da base do ISS |
| InsDdi | String(001) | Sim | Indicativo se deve descontar o valor de dedução da base do INSS/Funrural |
| OpeCpr | String(001) | Sim | Tipo da operação de compra |
| CprIcp | String(001) | Sim | Desconta o valor de ICMS da base de cálculo do PIS |
| CprIcc | String(001) | Sim | Desconta o valor ICMS da base de cálculo do COFINS |
| ExpSsv | String(001) | Sim | Indica se exporta informação para Siscoserv |
| CiaTst | String(003) | Sim | Código de ICMS Antecipação |
| DifRem | String(001) | Sim | Calcula DIFAL nas Notas Fiscais de Entrada do Tipo 7 - Remessa |
| TemIne | String(001) | Sim | Indicativo se usa o percentual de INSS Empresa da ligação Fornecedor X Serviço/Serviço/Fornecedor |
| ProInd | String(001) | Sim | Considerar na integração de terceirização do Bloco K |
| PdgBic | String(001) | Sim | Indicativo de como a transação considera o Pedágio na base do ICMS |
| CprLis | Number(009,2) | Sim | Valor mínimo do ISS considerado na nota fiscal de entrada |
| IpiOut | String(001) | Sim | Forma de geração do valor de IPI devolvido em devoluções e retornos |
| MovCes | String(001) | Sim | Movimenta o controle de entradas e saídas de produtos. |
| TipAre | Number(002,0) | Sim | Código do ajuste da contribuição previdenciária sobre a receita bruta - REINF |
| GerMde | String(001) | Sim | Transação permite Geração de Manifesto |
| PrcLcr | String(001) | Sim | Processar ligação nota fiscal de compra e retorno. |
| EntPaa | String(001) | Sim | Indicativo se é inclusa no Programa de Aquisição de Alimentos (PAA) |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| IdbIss | String(001) | Sim | Indicativo de como será lançado a dedução base de cálculo do ISS nos Arq. Fis. |
| SalPru | String(001) | Sim | Indica se transação soma ou subtrai do saldo do produtor rural |
| RetFun | String(001) | Sim | Indica se transação retém valor de FUNRURAL |
| RetSen | String(001) | Sim | Indica se transação retém valor de SENAR/SENAT |
| CodCoa | Number(005,0) | Sim | Código do Cadastro de Operações |
| PrcLcs | String(001) | Sim | Processar ligação com nota fiscal de cobrança de serviço |
| RegEsp | String(001) | Sim | Exportar na EFD como Nota Fiscal emitida por regime especial ou norma específica |
| DscSte | String(001) | Sim | Destaca o valor do ICMS ST destacado do valor do estoque |
| CxbLpr | Number(001,0) | Sim | Tipo de lançamento para Livro Caixa Digital do Produtor Rural |
| EcoIid | String(001) | Sim | Emitir Contra Nota |
| TnsEcn | String(005) | Sim | Transação de emissão da contra nota |
| AcrIdf | String(001) | Sim | Adicionar o valor do ICMS Diferido no valor líquido do item |
| BasPis | String(001) | Sim | Desconta o valor do ICMS do item ligado na base do PIS / Consignação |
| BasCof | String(001) | Sim | Desconta o valor do ICMS do item ligado na base do COFINS / Consignação |
| RecCbs | String(001) | Sim | Indicativo se a transação recupera CBS |
| RecIbs | String(001) | Sim | Indicativo se a transação recupera IBS |
| FinCib | String(003) | Sim | Aplicação da CBS/IBS |
| TipRdv | String(001) | Não | Tipo de cálculo para devolução CBS/IBS |
| ModOpe | String(002) | Sim | Modalidade da Operação NFE ABI |
| NatOIm | String(002) | Sim | Natureza da Operação NFE ABI |
| DetOpe | String(002) | Sim | Detalhamento da Operação NFE ABI |
| TpeMim | String(002) | Sim | Tipo do Emitente NFE ABI |

---

## Chave Primária

- CodEmp
- CodTns

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
