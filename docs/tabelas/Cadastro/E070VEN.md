# E070VEN

## Descrição

Cadastros - Filiais - Parâmetros Vendas

---

## Resumo

- Campos: 202
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| VenVca | String(001) | Não | Indicativo se o crédito do cliente deve ser verificado na alteração de um pedido ou nota fiscal de saída |
| VenFqp | String(001) | Não | Indicativo se permite faturar uma quantidade acima da quantidade pedida no item de pedido (utilizado como sugestão para cadastro de usuários) |
| VenFve | String(001) | Sim | Ind. se a filial utiliza forma de venda |
| FreMin | Number(015,2) | Sim | Valor mínimo para pagamento de frete |
| FreMax | Number(015,2) | Sim | Valor máximo para pagamento de Frete |
| PerFre | Number(005,2) | Sim | Percentual sobre a Carga para pagamento de Frete |
| IndAge | String(001) | Sim | Indicativo se deve ser consistido o agrupamento de embalagens na formação de embalagens manual |
| BusFat | String(001) | Sim | Indicativo se deve buscar os percentuais e preço do produto/serviço no faturamento não respeitando o que está no pedido |
| ParEsp | String(001) | Sim | Indicativo se os pedidos devem ser gerados com parcelas especiais por default |
| BusUlt | Number(001,0) | Sim | Tipo de busca dos últimos faturamentos para Pedidos |
| QtdUlt | Number(004,0) | Sim | Quantidade de Notas ou meses para busca dos últimos faturamentos. |
| TipRet | String(001) | Sim | Indicativo de como será efetuado o cálculo das retenções de impostos (Cofins/PIS/CSLL) e define a relação com o imposto Outras Retenções |
| RetAci | String(001) | Sim | Indicativo se deve ser gerado o retorno automático dos componentes utilizados para industrialização após a geração da nota de retorno do produto beneficiado(Tipo 5) |
| RvlFre | String(001) | Sim | Tipo de rateio do valor de frete para os itens de produto. |
| RvlFrd | String(001) | Sim | Tipo de rateio do valor de frete destacado para os itens de produto. |
| RvlSeg | String(001) | Sim | Tipo de rateio do valor de seguro para os itens de produto. |
| RvlEmb | String(001) | Sim | Tipo de rateio do valor de embalagens para os itens de produto. |
| RvlEnc | String(001) | Sim | Tipo de rateio do valor de encargos para os itens de produto e serviço. |
| RvlOut | String(001) | Sim | Tipo de rateio do valor de outros para os itens de produto e serviço. |
| RvlDar | String(001) | Sim | Tipo de rateio do valor de arredondamento para os itens de produto e serviço. |
| ConVmr | String(003) | Sim | Indicativo de onde é feito o controle do valor mínimo de retenção de contribuições sociais (Contas a Receber ou Vendas) |
| AbtPrv | String(001) | Sim | Indicativo se deve ser abatido o pedido de previsão no fechamento dos pedidos normais |
| CpdAbp | String(001) | Sim | Indicativo se considera os pedidos em aberto para análise de crédito do pedido |
| CpdAbf | String(001) | Sim | Indicativo se considera os pedidos em aberto para análise de crédito da nota fiscal |
| CtrBla | String(001) | Sim | Indicativo se faz bloqueio de pedido por área |
| CtrDsc | String(001) | Sim | Indicativo se o controle dos descontos 1,2,3,4 e 5 dos pedidos, pré-faturas e notas fiscais é feito por item ou por dados gerais |
| ReaPct | String(001) | Sim | Indicativo se o reajuste dos preços dos contratos de venda deve ser feito individualmente, cada um com sua data e percentual de reajuste |
| AnaEfp | String(001) | Sim | Indicativo se faz a análise e geração de embalagens no fechamento do pedido, aproveitando estoque de vários depósitos |
| CtrVei | String(001) | Sim | Indicativo se a filial controla os veículos através do cadastro de veículos |
| AltPuc | String(001) | Sim | Indicativo se deve alterar o preço unitário nas conversões da unidade de medida de venda de itens de produto do pedido, nota fiscal de saída e pré-faturas |
| UsaTpf | String(001) | Sim | Indicativo se usa tabela de preço de frete para as rotinas de pedidos, pré-faturas e notas fiscais |
| ConDct | String(001) | Sim | Indicativo se permite informar a data do cheque maior que o vencimento do título |
| GerIlo | String(001) | Sim | Indicativo se deve gerar para cada lote informado um item de nota fiscal |
| ComTdv | String(001) | Sim | Indicativo se faz a compensação de títulos na devolução |
| RvlFei | String(001) | Sim | Tipo de rateio do valor de frete de importação para os itens de produtos |
| RvlSei | String(001) | Sim | Tipo de rateio do valor de seguro de importação para os itens de produtos |
| RvlOui | String(001) | Sim | Tipo de rateio do valor de outras despesas de importação para os itens de produto e serviço |
| ConVpa | String(001) | Sim | Indicativo se considera as Pré-Faturas em aberto para análise de crédito da Pré-Fatura |
| DscHcl | String(001) | Sim | Ind. se utiliza desconto por antecipação em títulos do pedido e nota de saída |
| AncGre | String(001) | Sim | Indicativo se efetua a análise de crédito para o grupo de clientes |
| GrePam | Number(004,0) | Sim | Quantidade máxima de dias de atraso médio aceita na entrada de pedido para o grupo de clientes |
| GrePma | Number(004,0) | Sim | Quantidade máxima de dias de maior atraso aceita na entrada de pedido para o grupo de clientes |
| GrePpc | Number(004,0) | Sim | Quantidade máxima de pagamentos em cartório aceita na entrada de pedido para o grupo de clientes |
| GrePta | Number(004,0) | Sim | Quantidade máxima de títulos em atraso aceita na entrada de pedido para o grupo de clientes |
| GrePdt | Number(004,0) | Sim | Quantidade de dias de atraso de títulos aceito para entrada de pedido para o grupo de clientes |
| GrePlc | String(001) | Sim | Indicativo se aceita pedido com estouro de limite de crédito do grupo de clientes |
| GreFam | Number(004,0) | Sim | Quantidade máxima de dias de atraso médio aceita para faturamento para o grupo de clientes |
| GreFma | Number(004,0) | Sim | Quantidade máxima de dias de maior atraso aceita para faturamento para o grupo de clientes |
| GreFpc | Number(004,0) | Sim | Quantidade máxima de pagamentos em cartório aceita para faturamento para o grupo de clientes |
| GreFta | Number(004,0) | Sim | Quantidade máxima de títulos em atraso aceita para faturamento para o grupo de clientes |
| GreFdt | Number(004,0) | Sim | Quantidade de dias de atraso de títulos aceito para faturamento para o grupo de clientes |
| GreFlc | String(001) | Sim | Indicativo se aceita faturamento com estouro de limite de crédito do grupo de clientes |
| CtrRve | String(001) | Sim | Indicativo se controla reserva de veículo para formação de cargas |
| LogTpr | String(001) | Sim | Indicativo se deve gerar um log ao efetuar inclusões/alterações/exclusões nos Itens da tabela de preço de venda |
| LqpPed | Number(004,0) | Sim | Quantidade de protestos aceita como limite para crédito do cliente no pedido |
| LvpPed | Number(015,2) | Sim | Valor limite de protestos para crédito do cliente no pedido |
| LqpNfs | Number(004,0) | Sim | Quantidade de protestos aceita como limite para crédito do cliente na nota fiscal |
| LvpNfs | Number(015,2) | Sim | Valor limite de protestos para crédito do cliente na Nota Fiscal |
| AgpCpg | String(001) | Sim | Indicativo se agrupa em notas fiscais pedidos com condição de pagamento diferente |
| VenTta | String(005) | Sim | Transação padrão para geração de títulos sobre o valor de crédito do pedido |
| VenBpe | String(001) | Sim | Utiliza a data de emissão do pedido para busca de preço na tabela de preço |
| EmbPFA | String(001) | Sim | Indicativo se deve efetuar a formação de embalagens automaticamente nas rotinas de pré-faturas. |
| TipLpe | Number(001,0) | Sim | Forma de análise do pedido pela engenharia |
| UtiCms | String(001) | Sim | Utiliza definições da ligação cliente x marca apenas como sugestões para pedidos |
| UtiLpp | String(001) | Sim | Utiliza lista de preços em pedidos |
| BufFil | String(001) | Sim | Considera outras filiais na busca por últimos faturamentos do pedido |
| AbgBuf | String(249) | Sim | Abrangência de filiais para a busca por últimos faturamentos do pedido |
| BlcEnt | Number(002,0) | Sim | Número da balança de entrada padrão para o controle de entradas e saídas |
| BlcSai | Number(002,0) | Sim | Número da balança de saída padrão para o controle de entradas e saídas |
| BaiEnt | String(075) | Sim | Bairro de entrega da filial |
| BaiCob | String(075) | Sim | Bairro de cobrança da filial |
| BusRec | String(001) | Sim | Indicativo se deve questionar o recálculo do pedido com busca de preço/percentuais em um pedido fechado e forem feitas alterações que afetam os valores do pedido. Utilizando "N" (Não), não questionará e fará o recálculo sem buscar valores. |
| ObrEnt | String(001) | Sim | Obriga informar seqüência de entrega do cliente na Nota Fiscal, Pré Fatura e no Pedido. |
| ObrCob | String(001) | Sim | Obriga informar seqüência de cobrança do cliente na Nota Fiscal, Pré Fatura e no Pedido. |
| IndMvn | String(001) | Sim | Permite informação manual de impostos na digitação de notas fiscais de saída |
| IndCca | String(001) | Sim | Indicativo se haverá necessidade de conferência da carga antes do fechamento da mesma |
| DepFil | String(001) | Sim | Indicativo se o sistema a aceita Pedido/Pré-Fatura/Nota Fiscal com depósito de outra filial |
| MicFat | String(001) | Sim | Manter tributação do I.C.M.S do pedido no faturamento |
| MipFat | String(001) | Sim | Manter tributação do I.P.I. do pedido no faturamento |
| AncVdi | String(001) | Sim | Análisar crédito de clientes ao efetuar vendas à vista e em dinheiro |
| PraCan | Number(003,0) | Sim | Prazo para cancelamento da nota fiscal eletrônica |
| TprBas | String(004) | Sim | Código da tabela de preço a ser utilizado no registro de medicamentos para a NF-e e EFD |
| CtrOad | String(001) | Sim | Indicativo se obriga informar contrato de origem quando o tipo de contrato for adicional |
| BusVal | String(001) | Sim | Buscar valores no recálculo do pedido ou manter a mensagem para o usuário determinar o que deve ser feito |
| GerIte | String(001) | Não | Aplicada a data de entrega dos dados gerais aos itens e recalculada no fechamento do pedido. |
| BusVnf | String(001) | Sim | Buscar valores no recálculo da Nota Fiscal de Saída |
| CtrRea | String(001) | Sim | Indicativo se o controle de reajuste do contrato será pelos dados gerais ou por itens |
| CtrIft | String(001) | Sim | Indicativo se o controle de data de início de faturamento será pelos dados gerais ou por itens |
| ParDie | String(001) | Sim | Considera os dias especiais no vencimento das parcelas das notas fiscais de saída geradas por parcelas especiais de pedidos sem vencimento |
| PerEpf | Number(005,2) | Sim | Percentual máximo excedente da quantidade na formação de embalagens da pré-fatura |
| CliTpr | String(001) | Sim | Define para quando for alterado o cliente alterar também a tabela de preço no pedido conforme as definições do cliente |
| IntNfe | String(001) | Sim | Forma de integração para notas fiscais eletrônicas |
| EmiNfe | Number(002,0) | Sim | Software Emissor NF-e |
| VisNel | String(001) | Sim | Indicativo se a NF-e será visualizada antes do envio |
| CmrNel | String(012) | Sim | Código do modelo do relatório para visualização da NF-e |
| IntNfs | String(001) | Sim | Forma de integração para notas fiscais de serviço eletrônicas |
| AltPar | String(001) | Sim | Permite alterar as parcelas especiais com o pedido fechado desde que não tenha gerado títulos para o pedido. |
| CepIss | String(001) | Sim | CEP utilizado para busca da alíquota de ISS na ligação Serviço x CEP |
| ApfEmb | String(001) | Sim | Indicativo se as pré-faturas já embaladas podem ser agrupadas |
| MprFat | String(001) | Sim | Manter tributação do PIS Retido do pedido no faturamento |
| McrFat | String(001) | Sim | Manter tributação do COFINS Retido do pedido no faturamento |
| McsFat | String(001) | Sim | Manter tributação do CSLL do pedido no faturamento |
| MorFat | String(001) | Sim | Manter tributação de Outras Retenções do pedido no faturamento |
| MirFat | String(001) | Sim | Manter tributação do IRRF do pedido no faturamento |
| MpfFat | String(001) | Sim | Manter tributação do PIS Faturamento do pedido no faturamento |
| McfFat | String(001) | Sim | Manter tributação do COFINS Faturamento do pedido no faturamento |
| PesUmp | String(001) | Sim | Pesagem deve ser realizada na U.M. de estoque do produto |
| CalCsf | String(001) | Sim | Calcula comissão em itens de pedidos e notas fiscais sem valor financeiro |
| LimNfe | Number(015,2) | Sim | Valor limite estabelecido pela SEFAZ para NF-e |
| CanNfa | String(001) | Sim | Cancelar automaticamente notas autorizadas após solicitação de inutilização |
| ReqFca | String(001) | Sim | Gerar requisição no fechamento da carga |
| VenAqk | String(001) | Sim | Permite alteração da quantidade dos componentes do kit em notas fiscais de saída |
| TruEcf | String(001) | Sim | Indicativo se deve Truncar os valores repassados para o ECF |
| BnrPed | String(001) | Não | Buscar o primeiro número livre para a geração de um novo número do pedido |
| AncBon | String(001) | Sim | Análisar crédito de clientes ao utilizar transação de bonificação ou troca |
| CtrEnt | String(001) | Sim | Indicativo se a filial controla a entrega das notas fiscais de saída |
| ExiCmv | String(001) | Sim | Indicativo se exige conferência de volumes no fechamento de uma carga |
| CpoInv | String(001) | Sim | Indicativo se o pedido deve considerar os produtos inativos pelo inventário |
| AcrQcc | Number(004,0) | Sim | Quantidade máxima de dias de atraso para cálculo categoria para análise crédito |
| AcrPfa | Number(015,6) | Sim | Pontuação para clientes acima do atraso para cálculo da categoria crédito |
| AcrVmc | Number(011,2) | Sim | Valor mímino para considerar histórico de compras |
| AcrCca | String(003) | Sim | Categoria do cliente para a análise de crédito para novos clientes |
| AcrMap | Number(002,0) | Sim | Quantidade de envios do pedido para análise |
| AcrLcc | String(001) | Sim | Indicativo se o limite de crédito é digitado ou calculado pelo fator salário |
| AcrTec | Number(001,0) | Sim | Indicativo do tipo de escore considerado para categorizar clientes para crédito |
| AcrCfc | String(003) | Sim | Código da classificação da filial para a análise de crédito |
| AcrQdd | Number(004,0) | Sim | Quantidade de dias de validade de documento do cliente para análise crédito |
| CtrAva | String(001) | Sim | Controle de Avalistas |
| AvaPed | String(001) | Sim | Controle de Avalistas no Pedido |
| AvaNfv | String(001) | Sim | Controle de Avalistas na Nota Fiscal |
| AvaCtr | String(001) | Sim | Controle de Avalistas no Contrato |
| RetPma | String(001) | Sim | ndicaivo se o produto pode ser retirado no depósito da matriz pela filial |
| CalFci | String(001) | Sim | Filial se beneficiará da resolução SF 13/2012 |
| FatFci | String(001) | Sim | Permite faturar o produto sem que haja o cálculo de FCI apurado para o mesmo |
| FciInt | String(001) | Sim | Listar código do FCI em operações internas |
| AmbNfe | Number(001,0) | Sim | Ambiente NF eletrônica, manifestação de destinatário e manifesto eletrônico |
| AmbCte | Number(001,0) | Sim | Identificação do ambiente do conhecimento de transporte eletrônico |
| DetImp | String(001) | Sim | Detalhar impostos nos documentos fiscais de venda a consumidor |
| PonHcl | String(001) | Sim | Ind. se utiliza desconto por pontualidade em títulos do pedido e nota de saída |
| IndPcf | String(001) | Sim | Ind. se o sistema deve fazer a paridade entre contatos do cliente e do fornec. |
| ConPsb | Number(001,0) | Sim | Indica o que será feito, se o peso das saídas não confere com o pedido |
| VenTdb | String(005) | Sim | Transação padrão nota fiscal de produto para devolução via balança |
| RatFic | String(001) | Não | Indicativo se o sistema deve ratear valores de frete em itens isentos de ICMS. |
| IndPre | String(001) | Sim | Indicativo presencial do consumidor |
| NbdIpe | String(001) | Sim | Não buscar o percentual de desconto na importação de pedidos |
| IntMfe | String(001) | Sim | Forma de integração para manifesto de documentos fiscais eletrônicos |
| CneAut | String(001) | Sim | Indicativo para cancelar NFC gerada a partir de uma NFS automaticamente |
| DirRns | String(250) | Sim | Diretório de retorno da nota fiscal de serviço eletrônica |
| StrPez | String(001) | Sim | Situação tributária de redução com percentual de redução zerado |
| GerCtr | String(001) | Sim | Gerar informações de carga tributaria na NFS-e |
| NomFct | String(010) | Sim | Nome da fonte da carga tributaria NFS-e |
| RegAgr | String(100) | Sim | Registro agrícola |
| CodCca | Number(009,0) | Sim | Código da categoria de comercialização de agrotóxico |
| OreFep | String(001) | Sim | Obriga emissão da receita no fechamento do pedido |
| DatAtp | Date | Sim | Data da última integração de dados do parceiro para o receituário agronômico |
| HorAtp | Number(005,0) | Sim | Hora/minuto da útima altualização do dados do receituário vindas do parceiro |
| NviRec | Number(004,0) | Sim | Número de vias para impressão da receita |
| GerPed | String(001) | Sim | Gerar pedido para excesso de peso na devolução |
| TnsFat | String(005) | Sim | Transação padrão para entrada de faturas de vendas |
| EstAsc | String(001) | Sim | Indicativo se a baixa de estoque da nota fiscal é executada de forma assíncrona |
| TitAsc | String(001) | Sim | Indicativo se a geração de títulos do CRE da NF é executada de forma assíncrona |
| TipCdf | Number(001,0) | Sim | Tipo de cálculo do ICMS diferido |
| IndNfr | String(001) | Sim | Indicativo se gera tag para notas referenciadas de notas fiscais. |
| VenPcl | String(001) | Sim | Permite venda de produto não ligado ao cliente |
| IndSud | String(001) | Sim | Sugerir data atual para a data de emissão nos documentos de saída. |
| RefNcc | String(001) | Sim | Indicativo se vai referenciar as NFC-e e CF-e no XML da NF-e caso existir |
| VerPaf | String(005) | Sim | Versão do PAF-ECF que esta filial está credenciada |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |
| BltNfe | String(001) | Sim | Indicativo se é feita a geração automática de boletos da nota fiscal eletrônica |
| BltNfs | String(001) | Sim | Indicativo se é feita a geração automática de boletos da nota fiscal de serviço |
| VecPar | String(001) | Sim | Indicativo se permite parcelas com venc. menor ou igual parcela anterior no pedido |
| LimNfc | Number(015,2) | Sim | Valor limite estabelecido pela SEFAZ para NFC-e |
| RecEst | String(001) | Sim | Valida o número do receituário por estado |
| PsiEve | Number(001,0) | Sim | Indicativo se utiliza prorrogação de suspensão de ICMS por evento eletrônico |
| AmbPsi | Number(001,0) | Sim | Identificação do ambiente para eventos de prorrogação de suspensão de ICMS |
| EmiNlv | String(001) | Sim | Permite emissão de Nota Fiscal com lotes vencidos |
| IntFis | String(001) | Sim | Indicativo se utiliza integração com sistema de gestão de fretes externo |
| CodFca | String(003) | Sim | Fator de Conversão e Atualização do ICMS |
| OriGti | Number(001,0) | Sim | Forma de busca do código GTIN para gerar as tags cEAN e cEANTrib |
| CodMs1 | Number(004,0) | Sim | Código da 1ª mensagem padrão da nota fiscal de saída |
| CodMs2 | Number(004,0) | Sim | Código da 2ª mensagem padrão da nota fiscal de saída |
| CodMs3 | Number(004,0) | Sim | Código da 3ª mensagem padrão da nota fiscal de saída |
| CodMs4 | Number(004,0) | Sim | Código da 4ª mensagem padrão da nota fiscal de saída |
| InfVei | String(001) | Sim | Indicativo se gera as informações de veículos na NF-e em operações dentro da UF |
| FcpFin | String(001) | Sim | Indicativo se calcula o FCP apenas em operações internas para consumidor final |
| IcmEfe | String(001) | Sim | Indicativo se gera informações do ICMS Efetivo (ICMS60 e ICMS500) na NF-e 4.00 |
| ArrAbn | String(001) | Sim | Indicativo para utilizar a regra de arredondamento da ABNT |
| QcoLot | String(001) | Sim | Utiliza quantidade comercial no Lote do XML da NF-e |
| PraCsu | Number(003,0) | Sim | Prazo para cancelamento por substituição da nota fiscal eletrônica |
| CalDes | Number(001,0) | Sim | Forma de cálculo da Desoneração de ICMS |
| IcmDif | String(001) | Sim | Forma de envio do ICMS 51 |
| TnsEea | String(005) | Sim | Transação de estorno de movimento de estoque agrupado |
| SitWmw | String(001) | Sim | Situação do registro no WMW |
| IndAer | String(001) | Sim | Indicativo se utiliza assinatura eletrônica em receituário |
| AmbNsc | Number(001,0) | Sim | Ambiente NFCom |
| TipFat | Number(001,0) | Sim | Tipo faturamento NFCom |
| FinEmi | Number(001,0) | Sim | Finalidade emissão NFCom |
| VerNfs | Number(001,0) | Sim | Indicativo da versão do leiaute da NFS-e |
| SrdBcr | String(003) | Não | Série para emissão de NF de Débito e Crédito |
| FecEnv | String(001) | Sim | Indicativo se Nota Gerada Automaticamente Deve ser Fechada e Enviada ao Sefaz |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070VEN_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

