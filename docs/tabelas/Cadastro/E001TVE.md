# E001TVE

## Descrição

Tabelas - Transações - Vendas

---

## Resumo

- Campos: 128
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| VenPge | String(001) | Sim | Indicativo se deverá gerar nota fiscal de entrada para os itens no fechamento do pedido |
| CalFun | String(001) | Sim | Indicativo se calcula Funrural nas Notas Fiscais de Saídas. |
| NfvHro | String(001) | Sim | Indicativo se a nota fiscal de saída herda o rateio da origem (pedido, contrato de venda ou nota fiscal de entrada) |
| OpeVen | String(001) | Sim | Tipo da operação de venda |
| TriPif | String(001) | Sim | Indicativo se a transação tributa PIS Faturamento |
| TriCff | String(001) | Sim | Indicativo se a transação tributa COFINS Faturamento |
| VenEnp | String(001) | Sim | Transação considera os encargos financeiro na base do PIS (Todas as modalidades) |
| VenOup | String(001) | Sim | Transação considera as outras despesas na base do PIS (Todas as modalidades) |
| VenDap | String(001) | Sim | Transação considera arredondamento na base do PIS (Todas as modalidades) |
| VenOdp | String(001) | Sim | Transação considera outras despesas destacadas na base do PIS (Todas as modalidades) |
| VenLpi | Number(009,2) | Sim | Valor mínimo do PIS Retido considerado na nota fiscal de saída |
| VenPis | String(001) | Sim | Indicativo de como a Transação considera o valor  do PIS retido no total da nota fiscal de saída |
| VenEco | String(001) | Sim | Transação considera os encargos financeiro na base do Cofins (Todas as modalidades) |
| VenOuc | String(001) | Sim | Transação considera as outras despesas na base do Cofins (Todas as modalidades) |
| VenDac | String(001) | Sim | Transação considera arredondamento na base do Cofins (Todas as modalidades) |
| VenOdc | String(001) | Sim | Transação considera outras despesas destacadas na base do Cofins (Todas as modalidades) |
| VenLco | Number(009,2) | Sim | Valor mínimo do Cofins retido considerado na nota fiscal de saída |
| VenCof | String(001) | Sim | Indicativo de como a transação considera o valor  do Cofins retido no total da nota fiscal saída |
| VenIbp | String(001) | Sim | Transação considera o IPI na base de PIS (Todas as modalidades) |
| VenFrp | String(001) | Sim | Transação considera frete na base do PIS (Todas as modalidades) |
| VenSep | String(001) | Sim | Transação considera o seguro na base do PIS (Todas as modalidades) |
| VenEmp | String(001) | Sim | Transação considera a embalagem na base do PIS (Todas as modalidades) |
| SubPis | String(001) | Sim | Transação considera ICMS Substituto na base de PIS  (Todas as modalidades) |
| VenIbc | String(001) | Sim | Transação considera o IPI na base de Cofins  (Todas as modalidades) |
| VenFrc | String(001) | Sim | Transação considera frete na base do Cofins (Todas as modalidades) |
| VenSec | String(001) | Sim | Transação considera o seguro na base do Cofins (Todas as modalidades) |
| VenEmc | String(001) | Sim | Transação considera a embalagem na base do Cofins (Todas as modalidades) |
| SubCof | String(001) | Sim | Transação considera ICMS Substituto na base de COFINS (Todas as modalidades) |
| ComDis | String(001) | Sim | Transação considera valor arredondamento na base do ISS |
| ComOis | String(001) | Sim | Transação considera outras despesas na base do ISS |
| ComEis | String(001) | Sim | Transação considera os encargos na base do ISS |
| ComOds | String(001) | Sim | Transação considera outras despesas destacadas na base do ISS |
| VenIss | String(001) | Sim | Indicativo de como a Transação considera o ISS na nota fiscal saída |
| VenLis | Number(009,2) | Sim | Valor mínimo do ISS considerado na nota fiscal de saída |
| VenCtp | String(001) | Sim | Indicativo de que o sistema permite cancelar ou reabilitar o pedido mesmo quando os títulos do contas a receber gerados por este estiverem movimentados |
| CstIpi | String(002) | Sim | Código da situação tributária de IPI |
| CstPis | String(002) | Sim | Código da situação tributária de PIS |
| CstCof | String(002) | Sim | Código da situação tributária de COFINS |
| ConRic | String(001) | Sim | Indicativo se o valor da redução de ICMS deve ser considerado na soma/subtração do ICMS no preço unitário do item ou valor líquido |
| TriCid | String(001) | Sim | Indicativo se a transação tributa CIDE |
| NatOps | Number(001,0) | Sim | Natureza da operação de serviço |
| VenAcn | String(001) | Sim | Transação de nota fiscal saída exige nota fiscal de entrada |
| VenIsq | String(001) | Sim | Código de Tributação do ISSQN |
| RetAci | String(001) | Sim | Indicativo se os componentes de industrialização são inseridos na mesma NFS |
| NatPis | Number(005,0) | Sim | Natureza da receita do PIS |
| NatCof | Number(005,0) | Sim | Natureza da receita do COFINS |
| ObrCps | String(001) | Sim | Indicativo se é obrigatório informar o código de produto/serviço nas NFS |
| ObrFxt | String(001) | Sim | Indicativo se é obrigatória a ligação família/produto/serviço X transação |
| GerMon | String(001) | Sim | Indicativo se a transação gera pendências de montagem |
| GerEnt | String(001) | Sim | Indicativo se a transação gera pendências de entrega |
| ObrTxf | String(001) | Sim | Indicativo se é obrigatória a ligação transação X conta financeira |
| PedLvc | String(001) | Sim | Indicativo se o pedido aceita lotes vencidos |
| VenDdi | String(001) | Sim | Indicativo se deve descontar o valor de dedução da base do ISS |
| IcmDes | String(001) | Sim | Indicativo se a transação considera desoneração de ICMS |
| IndIsv | String(001) | Sim | Indicativo se a transação é utilizada para intermediação de serviços |
| CalSen | String(001) | Sim | Indicativo se calcula SENAR/SENAT nas notas fiscais de saídas |
| VenArs | String(001) | Sim | Transação considera valor arredondamento na base do SENAR/SENAT |
| VenOse | String(001) | Sim | Transação considera outras despesas na base do SENAR/SENAT |
| VenEse | String(001) | Sim | Transação considera os encargos na base do SENAR/SENAT |
| VenOds | String(001) | Sim | Transação considera outras despesas destacadas na base do SENAR/SENAT |
| VenIse | String(001) | Sim | Indicativo como a transação considera SENAR/SENAT no total da nota fiscal saída |
| VenBic | String(003) | Sim | Código da modalidade da base de cálculo do ICMS padrão para a transação |
| IndPre | String(001) | Sim | Indicativo presencial do consumidor |
| DscBip | String(001) | Sim | Considerar descontos na base de cálculo do IPI |
| IpiOut | String(001) | Sim | Forma de geração do valor de IPI devolvido em devoluções e retornos |
| VenIpp | String(001) | Sim | Transação considera a subtração do IPI Presumido na base do PIS |
| VenIpc | String(001) | Sim | Transação considera a subtração do IPI Presumido na base do COFINS |
| PerDif | Number(007,4) | Sim | Percentual de diferimento da transação de venda |
| CodPri | String(004) | Sim | Código da tabela de presunção IRPJ |
| CodPrc | String(004) | Sim | Código da tabela de presunção CSLL |
| TipCdv | String(001) | Não | Tipo de cálculo para devolução |
| ExiIss | Number(001,0) | Sim | Exigibilidade de ISS |
| VenTax | String(001) | Sim | Indicativo se a transação é de devolução de taxa |
| CodEnq | Number(003,0) | Sim | Código de enquadramento legal do IPI |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| VenRca | String(001) | Sim | Indica que será gerado receituario quando essa flag estiver como sim |
| PisFbi | String(001) | Sim | PIS Faturamento Base ICMS |
| CofFbi | String(001) | Sim | COFINS Faturamento Base ICMS |
| PisDes | String(001) | Sim | Indicativo de como a transação considera o ICMS desonerado na base do PIS |
| CofDes | String(001) | Sim | Indicativo de como a transação considera o ICMS desonerado na base do COFINS |
| IpiDes | String(001) | Sim | Indicativo de como a transação considera o ICMS desonerado na base do IPI |
| ZerVlr | String(001) | Sim | Zerar valor contábil/mercadoria das notas fiscais na integração para tributos |
| PrzRet | Number(004,0) | Sim | Prazo de retorno das mercadorias para fins de suspensão de ICMS (em dias) |
| PisOut | String(001) | Sim | Considera o valor de PIS como despesa acessória em devoluções de compra |
| CofOut | String(001) | Sim | Considera o valor de COFINS como despesa acessória em devoluções de compra |
| DesIcp | String(001) | Sim | Desconta o valor de ICMS da base de cálculo do PIS |
| DesIcc | String(001) | Sim | Desconta o valor de ICMS da base de cálculo do COFINS |
| DesIsp | String(001) | Sim | Desconta o valor de ISS da base de cálculo do PIS Faturamento e a Recuperar |
| DesIsc | String(001) | Sim | Desconta o valor de ISS da base de cálculo do COFINS Faturamento e a Recuperar |
| ExpSsv | String(001) | Sim | Indica se exporta informação para Siscoserv |
| ConOic | String(001) | Sim | Considerar Outros ICMS como receita tributada no cálculo do índice do CIAP. |
| IndFca | String(001) | Sim | Indica se deve ser considerado Fator de Conversão e Atualização do ICMS |
| ConVcs | String(001) | Sim | Considerar Valor Contábil das operações de venda com substituição tributária como Valor Tributado no cálculo do índice do CIAP. |
| ConVtr | String(001) | Sim | Considerar valor isento de ICSM como tributado no cálculo do índice do CIAP |
| IntWmw | String(001) | Sim | Indicativo se registro deve integrar com o WMW |
| PdgBic | String(001) | Sim | Indicativo de como a transação considera o Pedágio na base do ICMS |
| IcmRes | String(001) | Sim | Direito ao ressarcimento de ICMS ST |
| MovCes | String(001) | Sim | Movimenta o controle de entradas e saídas de produtos. |
| TipAre | Number(002,0) | Sim | Código do ajuste da contribuição previdenciária sobre a receita bruta - REINF |
| NumPsu | String(030) | Sim | Número do Processo de Suspensão da exigibilidade ISS |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| IdbIss | String(001) | Sim | Indicativo de como será lançado a dedução base de cálculo do ISS nos Arq. Fis. |
| SalPru | String(001) | Sim | Indica se transação soma ou subtrai do saldo do produtor rural |
| RetFun | String(001) | Sim | Indica se transação retém valor de FUNRURAL |
| RetSen | String(001) | Sim | Indica se transação retém valor de SENAR/SENAT |
| CodCoa | Number(005,0) | Sim | Código do Cadastro de Operações |
| RegEsp | String(001) | Sim | Exportar na EFD como Nota Fiscal emitida por regime especial ou norma específica |
| DevVlr | String(001) | Sim | Transação de nota fiscal de saída por devolução apenas de valor. |
| RefSig | String(001) | Sim | Indicativo se deve gerar o XML com sigilo Fiscal da NF-e referenciada. |
| CxbLpr | Number(001,0) | Sim | Tipo de lançamento para Livro Caixa Digital do Produtor Rural |
| IrrDes | String(001) | Sim | Descontar ICMS desonerado da base de IRRF. |
| ParEma | String(001) | Sim | Participa da análise de estoque mínimo automatizado |
| CalFus | String(001) | Sim | Calcula FUST |
| CalFnt | String(001) | Sim | Calcula FUNTTEL |
| BasPis | String(001) | Sim | Desconta o valor do ICMS do item ligado na base do PIS / Consignação |
| BasCof | String(001) | Sim | Desconta o valor do ICMS do item ligado na base do COFINS / Consignação |
| FinCib | String(003) | Sim | Aplicação da CBS/IBS |
| VenTnl | String(001) | Sim | Transação soma o valor do item no valor total líquido da nota |
| TrcIcm | String(001) | Sim | Indicativo se a transação calcula Transferência de Crédito de ICMS |
| GerAnt | String(001) | Sim | Indicativo se Permite Gerar Nota De Débito com Pagamento Antecipado |
| EstCre | String(001) | Sim | Indica se a transação é utilizada para estorno de crédito da CBS/IBS |
| OpeDoa | String(001) | Sim | Indica se a transação é uma operação de doação |
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
