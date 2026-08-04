# E070CPR

## Descrição

Cadastros - Filiais - Parâmetros Compras

---

## Resumo

- Campos: 163
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| FgeIpf | Number(001,0) | Sim | (descontinuado) Data do Fato gerador IRRF Pessoa Física para geração dos títulos |
| FgeIpj | Number(001,0) | Sim | (descontinuado) Data do Fato gerador IRRF Pessoa Jurídica para geração dos títulos |
| ImpIrf | String(003) | Sim | (descontinuado) Código do imposto para cálculo do vencimento de IRRF |
| ImpIns | String(003) | Sim | (descontinuado) Código do imposto para cálculo do vencimento de INSS/Funrural |
| ImpIss | String(003) | Sim | (descontinuado) Código do imposto para cálculo do vencimento de ISS |
| CprLvp | Number(004,2) | Sim | Valor Limite para o percentual de variação do peso informado nas telas de controle de entrada e saída de compras |
| UtiFnf | String(001) | Sim | Indicativo se é utilizado o fracionamento de produto após a nota fiscal de entrada |
| MnfSoc | Number(015,2) | Sim | Valor máximo permitido para notas fiscais sem documento de origem (Contrato/OC) |
| TnsPsa | String(005) | Sim | Transação padrão do movimento de saída do estoque gerado a partir de uma nota fiscal de entrada de acerto |
| FgeIsf | Number(001,0) | Sim | (descontinuado) Data do Fato gerador ISS Pessoa Física para geração dos títulos |
| FgeIsj | Number(001,0) | Sim | (descontinuado) Data do Fato gerador ISS Pessoa Jurídica para geração dos títulos |
| ExcTit | String(001) | Sim | Excluir título previsto gerado pela OC no fechamento da nota fiscal de entrada |
| VlrMri | Number(015,2) | Sim | Valor máximo de retenção de INSS para pessoas físicas |
| ForIne | Number(009,0) | Sim | (descontinuado) Código do fornecedor padrão para geração do título de INSS da parte da empresa |
| TptIne | String(003) | Sim | (descontinuado) Tipo de título padrão para geração do título de INSS da parte da empresa |
| TnsIne | String(005) | Sim | (descontinuado) Transação padrão para geração do título de INSS da parte da empresa |
| BnrOcp | String(001) | Não | Tipo de busca da numeração das ordens de compra |
| TnsPan | String(005) | Sim | Transação padrão para ordem de compra via análise de reposição |
| OcpAnx | String(001) | Sim | Indicativo se a ordem de compra deve ser enviada em anexo no e-mail ou no corpo da mensagem |
| EmlFig | String(001) | Sim | Indicativo se devem ser enviadas as figuras do HTML em anexo no e-mail dos processos de compras |
| QtdDao | Number(003,0) | Sim | Quantidade de dias anterior ao atual aceito para data de emissão da ordem de compra |
| ForCof | Number(009,0) | Sim | (descontinuado) Código do fornecedor padrão para geração do título de Cofins |
| TptCof | String(003) | Sim | (descontinuado) Tipo de título padrão para geração do título de Cofins |
| TnsCof | String(005) | Sim | (descontinuado) Transação padrão para geração do título de Cofins |
| FgeCof | Number(001,0) | Sim | (descontinuado) Data do Fato gerador Cofins para geração dos títulos |
| ImpCof | String(003) | Sim | (descontinuado) Código do imposto para cálculo do vencimento de Cofins |
| ForPis | Number(009,0) | Sim | (descontinuado) Código do fornecedor padrão para geração do título de PIS |
| TptPis | String(003) | Sim | (descontinuado) Tipo de título padrão para geração do título de PIS |
| TnsPis | String(005) | Sim | (descontinuado) Transação padrão para geração do título de PIS |
| FgePis | Number(001,0) | Sim | (descontinuado) Data do Fato gerador PIS para geração dos títulos |
| ImpPis | String(003) | Sim | (descontinuado) Código do imposto para cálculo do vencimento de Pis |
| ForCsl | Number(009,0) | Sim | (descontinuado) Código do fornecedor padrão para geração do título de CSLL |
| TptCsl | String(003) | Sim | (descontinuado) Tipo de título padrão para geração do título de CSLL |
| TnsCsl | String(005) | Sim | (descontinuado) Transação padrão para geração do título de CSLL |
| FgeCsl | Number(001,0) | Sim | (descontinuado) Data do Fato gerador CSLL para geração dos títulos |
| ImpCsl | String(003) | Sim | (descontinuado) Código do imposto para cálculo do vencimento de CSLL |
| ForOur | Number(009,0) | Sim | (descontinuado) Código do fornecedor padrão para geração do título de Outras Retenções |
| TptOur | String(003) | Sim | (descontinuado) Tipo de título padrão para geração do título de outras retenções |
| TnsOur | String(005) | Sim | (descontinuado) Transação padrão para geração do título de Outras Retenções |
| FgeOur | Number(001,0) | Sim | (descontinuado) Data do Fato gerador Outras Retenções para geração dos títulos |
| ImpOur | String(003) | Sim | (descontinuado) Código do imposto para cálculo do vencimento de Outras Retenções |
| FgeInf | Number(001,0) | Sim | (descontinuado) Data do Fato gerador INSS/Funrural pessoa física para geração dos títulos |
| FgeInj | Number(001,0) | Sim | (descontinuado) Data do Fato gerador INSS/Funrural pessoa jurídica para geração dos títulos |
| TipRet | String(001) | Sim | Indicativo de como será efetuado o cálculo das retenções de impostos (Cofins/PIS/CSLL) e define a relação com o imposto Outras Retenções |
| RvlCfr | String(001) | Sim | Tipo de rateio do valor do conhecimento de frete para efetuar movimento de estoque(acerto) |
| RvlFre | String(001) | Sim | Tipo de rateio do valor de frete para os itens de produto. |
| RvlSeg | String(001) | Sim | Tipo de rateio do valor de seguro para os itens de produto. |
| RvlEmb | String(001) | Sim | Tipo de rateio do valor de embalagens para os itens de produto. |
| RvlEnc | String(001) | Sim | Tipo de rateio do valor de encargos para os itens de produto e serviço. |
| RvlOut | String(001) | Sim | Tipo de rateio do valor de outros para os itens de produto e serviço. |
| RvlDar | String(001) | Sim | Tipo de rateio do valor de arredondamento para os itens de produto e serviço. |
| CreDzf | String(001) | Sim | Indicativo se credita o desconto suframa nas notas fiscais de entrada |
| ConVmr | String(003) | Sim | Indicativo de onde é feito o controle do valor mínimo de retenção de contribuições sociais (Contas a Pagar ou Compras) |
| CtrDsc | String(001) | Sim | Indicativo se o controle dos descontos 1,2,3,4 e 5 nas ordens de compras e notas fiscais de entrada é feito por item ou por dados gerais |
| TnsPsm | String(005) | Sim | Transação Sol. Compra - Manual |
| TnsPsp | String(005) | Sim | Transação Sol. Compra - Produção |
| TnsPst | String(005) | Sim | Transação Sol. Compra - Automática |
| CprNfo | Number(001,0) | Sim | Indicativo se deve ser considerada a parametrização dos itens das notas fiscais dos itens de origem no fechamento das notas fiscais de frete para crédito de IPI, ICMS, PIS e COFINS |
| ConDen | String(001) | Sim | Indicativo se a data de entrada deve ser consistida na digitação ou no fechamento das notas fiscais |
| FinOps | String(001) | Sim | Realizar retorno das OPs ao fechar a nota fiscal de entrada de retorno (tipo 4) |
| GerIlo | String(001) | Sim | Indicativo de deve gerar para cada lote informado um item de nota fiscal |
| TnsPvf | String(005) | Sim | Transação padrão para geração de ordem de compra (venda entre filiais) |
| TnsPtf | String(005) | Sim | Transação padrão para geração de ordem de compra (transferência entre filiais) |
| DevGre | String(001) | Sim | Aceita devolução remessa/retorno de cliente/fornecedor do mesmo grupo |
| AprRct | String(001) | Sim | Indicativo se exige reaprovação do contrato após reajuste |
| DscHfo | String(001) | Sim | Indicativo se utiliza o desconto antecipação definidos no histórico do fornecedor para os títulos gerados via nota fiscal de entrada. |
| AprOcp | String(003) | Sim | Definir se a ordem de compra digitada deve iniciar como "ANA - Análise" ou "PRE - Preparação" no controle de aprovação multinível |
| CanOcp | Number(001,0) | Sim | Permitir ao usuário escolher entre as opções no cancelamento de uma O.C. |
| IndPrv | String(001) | Sim | Indicativo se considera a previsão de entrega na quebra do agrupamento de itens na geração de ordem de compra via solicitação |
| GerNfv | String(001) | Sim | Indicativo se deve gerar uma nota fiscal de saída na filial que enviou a quantidade a maior referente a nota fiscal de entrada que será gerada a partir tela de conferência |
| CprTdv | String(001) | Sim | Indicativo se faz a compensação de títulos na devolução |
| UtiOcp | String(001) | Sim | Aceita somente dia útil para data de entrega dos itens da ordem de compra |
| DppTrf | String(010) | Sim | Depósito padrão para entradas por tranferência |
| EstNft | String(001) | Sim | Indica qual deve ser o estado após a geração da nota fiscal por transferência |
| CtrAba | String(001) | Sim | Indicativo se deve ser feita a consistência do contrato de abastecimento na geração das compras (Cotação e OC) |
| GerApr | String(001) | Sim | Indicativo se o contrato por evento gera aprovação multinível |
| IndCnt | String(001) | Sim | Validar existência da contagem (optando por "Não" o sistema incluirá na mesma contagem) |
| TraCnf | String(001) | Sim | Permitir tratamento de defeitos e excedente na conferência |
| DepDef | String(010) | Sim | Depósito de transferência para produtos com defeito na contagem |
| TnsDef | String(005) | Sim | Transação de transferência para produtos com defeito na contagem |
| DepAct | String(010) | Sim | Depósito de excedente para acerto na contagem |
| TnsAct | String(005) | Sim | Transação de excedente para acerto na contagem |
| SubEnt | String(001) | Sim | Substitui a data de previsão dos itens da ordem de compra na aprovação |
| MoeOsc | String(003) | Sim | Código da moeda padrão para ordens de compra sem contrato de participantes e NF de depósito |
| PerOsc | Number(005,2) | Sim | Percentual da moeda padrão para geração das NFs de depósito |
| CpgFix | String(006) | Sim | Código da condição de pagamento para geração de título na fixação |
| IndNor | String(001) | Sim | Indicativo se utiliza o preço normal na tabela de preço e reposição depósito filiais |
| OcpFec | String(001) | Sim | Indicativo se as ordens serão fechadas na análise de reposição depósito filiais |
| IndBan | String(001) | Sim | Indicativo se utiliza dados bancários do favorecido/fornecedor na geração de títulos previstos na ordem de compra |
| TnsFix | String(005) | Sim | Transação para geração do título do contas a pagar na fixação |
| TptFix | String(003) | Sim | Tipo de título gerado no contas a pagar na fixação |
| TnsRoy | String(005) | Sim | Transação para geração do título de royalty na fixação |
| TptRoy | String(003) | Sim | Tipo de título do royalty na fixação |
| IndGdc | String(001) | Sim | Indicativo se gera débitos de comissão nas entradas de notas fiscais de devolução |
| TipAsl | String(001) | Sim | Indicativo do valor que deve ser utilizado para atualizações de saldos de contratos financeiros com saldo (contratos tipo 10) e contratos por eventos (contratos tipo 11) quando da utilização destes contratos em notas fiscais de entrada |
| AgrDcl | String(001) | Sim | Indicativo se as distribuições das coletas de produtos em fornecedores devem ou não ser agrupadas em um único item de ordem de compra já existente quando se tratar do mesmo produto/serviço |
| OriDig | String(001) | Sim | Indicativo se será aceito no conhecimento de transporte a ligação de notas fiscais de origem na situação digitada |
| FecOri | String(001) | Sim | Indicativo se o sistema deve fechar o conhecimento de transporte quando uma N.F. origem ligada estiver sendo fechada |
| TnsCae | String(005) | Sim | Transação para geração do movimento do custo apropriado para o estoque |
| TnsDce | String(005) | Sim | Transação para geração do movimento dos descontos da classificação da entrada |
| LogTpr | String(001) | Sim | Indicativo se deve gerar um registro de operações na tabela de preço de compra |
| BnrCot | String(001) | Não | Tipo de busca da numeração de processo de cotações |
| HerObs | String(001) | Sim | Herdar as observações das ordens de compra para a nota fiscal de entrada. |
| CprIcf | String(001) | Sim | Indicativo se permite inativar um contrato financeiro que possui títulos gerados |
| CprRco | String(001) | Sim | Indicativo se deve questionar sobre a exclusão títulos efetivos na ordem. |
| DivMen | String(001) | Sim | Tratar divergência a menor |
| DivMai | String(001) | Sim | Tratar divergência a maior |
| PesUmp | String(001) | Sim | Pesagem deve ser realizada na U.M. de estoque do produto |
| AprNfc | String(003) | Sim | Definir se a NF digitada deve iniciar como análise ou preparação |
| ConChv | String(001) | Sim | Consistir a chave eletrônica da nota fiscal de entrada |
| RedBci | String(001) | Sim | Considerar alíquota aplicada na base de cálculo do ICMS importação |
| ManIcm | String(001) | Sim | Indicativo se deve manter o percentual de ICMS da OC na NF |
| ForCur | Number(009,0) | Sim | Código do fornecedor padrão para a comrpa de cursos online |
| ManDes | String(001) | Sim | Indicativo se gera os arquivos de manifestação do destinatário |
| CalDal | String(001) | Sim | Calcular diferencial de alíquota |
| ForCda | String(001) | Sim | Fornecedor do Simples nacional calcula diferencial de alíquota |
| VlrMar | Number(015,2) | Sim | Valor máximo do arredondamento da nota de entrada |
| MsgMri | String(001) | Sim | Exibe mensagem de valor máximo de retenção de INSS atingido |
| CprTpr | String(005) | Sim | Transação padrão ordem de compra de produto para reentrada via devolução |
| CprTnr | String(005) | Sim | Transação padrão nota fiscal de produto para reentrada via devolução |
| PreEnt | String(001) | Sim | Indicativo se terá a possibilidade de pré-entrada na pesagem |
| PosSai | String(001) | Sim | Indicativo se terá a possibilidade de pós-saída na pesagem |
| AprCot | String(003) | Sim | Definir inicialização da cotação no controle de aprovação multinível |
| FrtAfm | Number(001,0) | Sim | Forma de rateio para vlr. adicional frete para renovação da marinha mercante |
| MltEnt | String(001) | Sim | Permite múltiplas entradas de veículos na entrada via balança |
| IndObc | String(001) | Sim | Indicativo se é obrigatório informar uma observação ao cancelar OC na aprovação |
| AgrItf | String(001) | Sim | Agrupar itens na fixação |
| InfNpf | String(001) | Sim | Informar nota fiscal de produtor na fixação |
| HerAnx | String(001) | Sim | Herdar anexos no Processo de Compras (Req./Sol./Cot./O.C.) |
| AnxCot | String(001) | Sim | Incluir anexos no e-mail enviado ao Fornecedor pela Cotação |
| AnxOcp | String(001) | Sim | Incluir anexos no e-mail enviado ao Fornecedor pela Ordem de Compra |
| TipBda | Number(002,0) | Sim | Tipo Cálculo DIFAL para Tipo Cálculo Diferencial Alíquotas - DIFA |
| EnvIep | String(001) | Sim | Enviar IE de Produtor Rural no XML da NF-e |
| QtdTlr | Number(015,3) | Sim | Quantidade máxima para dif. de peso no recebimento entre a pesagem e as notas |
| ExiLot | String(001) | Sim | Exige número de lote ou série na nota fiscal de compra |
| SomFsi | String(001) | Sim | Soma valor do frete e seguro importação no valor unitário dos itens |
| ReaReq | String(001) | Sim | Permite reabilitar requisição atendida via processo de compra |
| ValVig | String(001) | Sim | Indicativo se ira validar a vigência de contrato de compra |
| PerTlr | Number(005,2) | Sim | Percentual permitido para dif. de peso no recebimento entre a pesagem e as notas |
| VerNfe | String(001) | Sim | Versão de geração da Nota Fiscal de Entrada |
| ObgNfp | String(001) | Sim | Obrigar informar nota fiscal de produtor |
| DesIci | String(001) | Sim | Descontar ICMS Interestadual da base DIFAL para Descontar ICMS Interestadual da base Diferencial Alíquotas - DIFA |
| AliBda | Number(001,0) | Sim | Alíquota Base de Cálculo DIFAL para Alíquota Base de Cálculo Diferencial Alíquotas - DIFA |
| CodTst | String(003) | Sim | Código do ICMS substituído para cálculo da presunção do ICMS ST no controle de entrada |
| FunTrc | String(001) | Sim | Funcionamento de uso da transação na tela de Recebimento de Grãos |
| TnsRcg | String(005) | Sim | Transação sugerida no processo de recebimento de grãos (F435CCC) |
| CnoFpf | String(001) | Sim | Emitir contra nota para o Fornecedor pessoa física |
| CidIss | String(001) | Sim | Indicativo do cadastro de origem do código da cidade de tributação para ISS |
| UtiEqi | String(001) | Sim | Indicativo se permite o recebimento de produtos equivalentes |
| LimDal | Number(007,4) | Sim | Percentual de limite mínimo da diferença entre a alíquota interna e a alíquota interestadual para calcular o valor do diferencial de alíquota |
| MoeUpf | String(003) | Sim | *** Descontinuado nesta tabela *** Código da moeda da Unidade Padrão Fiscal |
| FixInt | String(001) | Sim | Indica se o valor do título de fixação será gerado com o valor integral ou somente com o valor liquido |
| EntScl | String(001) | Sim | Indica se deve permitir a entrada via balança com ticket sem classificação |
| DesTck | String(001) | Sim | Indica se desmembra ticket quando pesagem for maior que a quantidade da nota - PJ |
| VlrEvb | Number(001,0) | Sim | Indica a forma de buscar o valor base quando houver diferença de peso que está dentro da tolerância |
| NfsCtg | String(001) | Sim | Permite selecionar notas fiscais de saída em contingência para entrada por transferência (Tipo 11) |
| IntHry | String(001) | Sim | Integra com o Hub de Royalties |
| DatACk | Date | Sim | Data Inicial Agrocheck |
| BloTra | String(001) | Sim | Bloqueia Transferência de Crédito entre Produtores. |
| CerFor | String(001) | Sim | Controlar a certificação dos fornecedores |
| TcaRoy | String(005) | Sim | Transação para cancelamento de título de royalty gerado na compra imediata |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
