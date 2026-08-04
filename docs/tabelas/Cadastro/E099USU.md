# E099USU

## Descrição

Cadastros - Usuários

---

## Resumo

- Campos: 255
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do Usuário |
| NumEmp | Number(004,0) | Sim | Empresa do empregado ou usuário |
| TipCol | Number(001,0) | Sim | Tipo de colaborador |
| NumCad | Number(009,0) | Sim | Número do cadastro do empregado ou usuário |
| SupIme | Number(010,0) | Sim | Código do superior imediato |
| CodCcu | String(009) | Sim | Código do centro de custo do empregado, usuário, comprador... |
| IntNet | String(100) | Sim | Endereço Eletrônico (E-Mail) |
| EmpAti | Number(004,0) | Sim | Código da empresa ativa |
| FilAti | Number(005,0) | Sim | Código da filial ativa |
| GerAus | String(001) | Não | Indicativo se o usuário pode alterar a situação do usuário |
| FpgObr | String(001) | Não | Indicativo se o usuário é obrigado a informar a forma de pagamento |
| PstAti | Number(003,0) | Sim | Posto ativo |
| VenTbp | String(001) | Não | Indicativo se o usuário pode aceitar pedidos e notas fiscais de saída sem tabela de preço |
| VenNsp | String(001) | Não | Indicativo se o usuário pode emitir nota fiscal de saída sem pedido |
| VenPar | String(001) | Não | Indicativo se o usuário pode alterar o representante dos pedidos ou notas |
| VenPap | String(001) | Não | Indicativo se o usuário pode alterar o preço dos pedidos ou notas |
| VenPds | String(001) | Não | Indicativo se o usuário pode alterar o desconto dos pedidos ou notas |
| VenPip | String(001) | Não | Indicativo se o usuário pode alterar o IPI dos pedidos ou notas |
| VenPic | String(001) | Não | Indicativo se o usuário pode alterar o ICMS dos pedidos ou notas |
| VenPco | String(001) | Não | Indicativo se o usuário pode alterar a comissão dos pedidos ou notas |
| VenPis | String(001) | Não | Indicativo se o usuário pode alterar o ISS dos pedidos ou notas |
| VenPir | String(001) | Não | Indicativo se o usuário pode alterar o IRRF dos pedidos ou notas |
| VenPin | String(001) | Não | Indicativo se o usuário pode alterar o INSS dos pedidos ou notas |
| VenPfu | String(001) | Não | Indicativo se o usuário pode alterar o funrural dos pedidos ou notas |
| VenAun | String(001) | Sim | Indicativo se usuário pode alterar número da última nota gerada |
| VenAtp | String(001) | Sim | Indicativo se o usuário pode alterar a tabela de preço do cliente |
| VenAcl | String(001) | Sim | Indicativo se o usuário pode alterar a situação do cliente |
| VenAre | String(001) | Sim | Indicativo se o usuário pode alterar a situação do representante |
| VenAsp | String(001) | Sim | Indicativo se o usuário pode alterar a situação de pedido |
| VenLpd | String(001) | Sim | Indicativo se o usuário pode liberar pedido de venda |
| VenAcv | String(001) | Sim | Indicativo se o usuário pode alterar a situação do contrato de venda |
| VenAns | String(001) | Sim | Indicativo se o usuário pode alterar a situação da NF de saída |
| VenLns | String(001) | Sim | Indicativo se o usuário pode liberar NF de saída |
| VenAsr | String(001) | Sim | Indicativo se o usuário pode alterar a senha do representante |
| VenRat | String(001) | Sim | Indicativo se usuário pode alterar os rateios definidos no vendas |
| VenPae | String(001) | Sim | Indicativo se o usuário pode alterar os parâmetros de análise de embarque |
| VenAdg | String(001) | Sim | Indicativo se o usuário pode alterar os dados gerais da NF |
| VenApi | String(001) | Sim | Indicativo se o usuário pode alterar o peso/quantidade informada nas telas de controle de entrada e saída |
| EstAes | String(001) | Sim | Indicativo se o usuário pode alterar a situação do estoque |
| EstRat | String(001) | Sim | Indicativo se usuário pode alterar os rateios definidos no estoque |
| EstPlp | String(001) | Sim | Indicativo se usuário pode efetuar a ligação de produtos a depósitos |
| RecPgr | String(001) | Sim | Indicativo se o usuário pode gravar o recálculo da consulta do C.Receber |
| RecAvr | String(001) | Sim | Indicativo se o usuário pode alterar o vencimento no C.Receber |
| RecAvl | String(001) | Sim | Indicativo se o usuário pode alterar o valor no contas a receber |
| RecRat | String(001) | Sim | Indicativo se usuário pode alterar os rateios definidos no contas a receber |
| CprMac | Number(015,2) | Sim | Valor máximo para aprovação de cotação de compra |
| CprMoc | Number(015,2) | Sim | Valor máximo para ordem de compra |
| CprPap | String(001) | Não | Indicativo se o usuário pode alterar o preço das OC ou notas |
| CprPds | String(001) | Não | Indicativo se o usuário pode alterar o desconto das OC ou notas |
| CprPip | String(001) | Não | Indicativo se o usuário pode alterar o IPI das OC ou notas |
| CprPic | String(001) | Não | Indicativo se o usuário pode alterar o ICMS das OC ou notas |
| CprPis | String(001) | Não | Indicativo se o usuário pode alterar o ISS das OC ou notas |
| CprPir | String(001) | Não | Indicativo se o usuário pode alterar o IRRF das OC ou notas |
| CprPin | String(001) | Não | Indicativo se o usuário pode alterar o INSS das OC ou notas |
| CprPfu | String(001) | Não | Indicativo se o usuário pode alterar o Funrural das OC ou notas |
| CprVno | Number(005,2) | Sim | Percentual de diferença aceito no preço unitário do item entre a OC x NFE |
| CprQno | Number(005,2) | Sim | Percentual de diferença aceito na quantidade do item da OC x NFE |
| CprVdn | Number(015,2) | Sim | Diferença de valor aceito entre o valor líquido da OC x NFE |
| CprPdn | Number(005,2) | Sim | Percentual de diferença aceito entre o valor líquido da OC x NFE |
| CprApd | String(001) | Sim | Indicativo se o usuário pode aprovar entrada de NF entrada com diferença |
| CprAfo | String(001) | Sim | Indicativo se o usuário pode alterar a situação do fornecedor |
| CprAoc | String(001) | Sim | Indicativo se o usuário pode alterar a situação da ordem de compra |
| CprAcc | String(001) | Sim | Indicativo se o usuário pode alterar a situação do contrato de compra |
| CprAne | String(001) | Sim | Indicativo se o usuário pode alterar a situação da NF de Entrada |
| CprRat | String(001) | Sim | Indicativo se usuário pode alterar os rateios definidos no compras |
| CprAdg | String(001) | Sim | Indicativo se o usuário pode alterar os dados gerais da NF Entrada |
| CprAcf | String(001) | Sim | Indicativo se o usuário pode alterar condição de pagamento no processo de fixação |
| CprAtx | String(001) | Sim | Indicativo se o usuário pode alterar as taxas no processo de fixação ou devolução |
| CprAhf | String(001) | Sim | Indicativo se o usuário pode alterar a hora no processo de fixação |
| PagMax | Number(015,2) | Sim | Valor máximo permitido para aprovação pagamento contas a pagar |
| PagPgr | String(001) | Sim | Indicativo se o usuário pode gravar recálculo da consulta do C.Pagar |
| PagAvp | String(001) | Sim | Indicativo se o usuário pode alterar o vencimento no C. Pagar |
| PagAvl | String(001) | Sim | Indicativo se o usuário pode alterar o valor no contas a pagar |
| PagEev | String(001) | Sim | Usuário aceita vencimento menor que quantidade dias entre entrada e vencimento da filial |
| PagRat | String(001) | Sim | Indicativo se usuário pode alterar os rateios definidos no contas a pagar |
| CxbDcp | Number(003,0) | Sim | Quantidade de dias aceita para cheques pré-datados |
| CxbApm | String(001) | Sim | Indicativo se o usuário pode alterar preparação de movimento tesouraria |
| CxbRat | String(001) | Sim | Indicativo se usuário pode alterar os rateios definidos na tesouraria |
| CtbDac | String(001) | Sim | Indicativo do direito de acesso do usuário a contabilidade |
| CtbAlt | String(001) | Sim | Indicativo se o usuário pode incluir/alterar lotes |
| CtbClt | String(001) | Sim | Indicativo se o usuário pode consultar lotes |
| CtbAlc | String(001) | Sim | Indicativo se o usuário pode incluir/alterar lançamentos |
| CtbClc | String(001) | Sim | Indicativo se o usuário pode consultar lançamentos |
| CtbArt | String(001) | Sim | Indicativo se o usuário pode incluir/excluir/alterar rateios |
| CtbCrt | String(001) | Sim | Indicativo se o usuário pode consultar rateios |
| CtbAor | String(001) | Sim | Indicativo se o usuário pode incluir/excluir/alterar orçamentos |
| CtbCor | String(001) | Sim | Indicativo se o usuário pode consultar orçamentos |
| CtbAct | String(001) | Sim | Indicativo se o usuário pode incluir/excluir/alterar contas |
| CtbAhp | String(001) | Sim | Indicativo se o usuário pode incluir/excluir/alterar históricos padrões |
| CtbAcf | String(001) | Sim | Indicativo se o usuário pode incluir/excluir/alterar configurações da filial |
| CtbLfl | String(001) | Sim | Indicativo se o usuário pode lançar fora do limite de lançamentos |
| CtbZer | String(001) | Sim | Indicativo se o usuário pode efetuar zeramento |
| PrdDpa | Number(004,0) | Sim | Quantidade de dias permitido para antecipar a data de entrega para produção |
| PrdDpp | Number(004,0) | Sim | Quantidade de dias permitido para postecipar a data de entrega para produção |
| SitUsu | String(001) | Não | Situação do Usuário |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do usuário |
| ObsMot | String(250) | Sim | Observação do motivo da situação do usuário |
| UsuMot | Number(010,0) | Sim | Usuário responsável pelo motivo da situação do usuário |
| DatMot | Date | Sim | Data do motivo da situação do usuário |
| HorMot | Number(005,0) | Sim | Hora do motivo da situação do usuário |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| CodCli | Number(009,0) | Sim | Código do cliente ligado ao usuário |
| CodFor | Number(009,0) | Sim | Código do fornecedor ligado ao usuário |
| CodRep | Number(009,0) | Sim | Código do representante ligado ao usuário |
| CodTra | Number(009,0) | Sim | Código da transportadora ligado ao usuário |
| CodPor | String(004) | Sim | Código interno do portador  ligado ao usuário (carteira, representante, advogado, bancos, etc.) |
| VenFqp | String(001) | Sim | Indicativo se o usuário pode faturar uma quantidade acima da quantidade pedida no item de pedido |
| CprPqt | String(001) | Não | Indicativo se o usuário pode alterar o quantidade das OC ou notas |
| PorObr | String(001) | Não | Indicativo se usuário deve informar o código do Portador |
| VenLpv | String(001) | Sim | Indicativo se o usuário pode aprovar o pedido pela área de Vendas (Bloqueio por Áreas) |
| VenLpf | String(001) | Sim | Indicativo se o usuário pode aprovar o pedido pela área Financeira (Bloqueio por Áreas) |
| VenLpc | String(001) | Sim | Indicativo se o usuário pode aprovar o pedido pela área de Compras (Bloqueio por Áreas) |
| VenLpp | String(001) | Sim | Indicativo se o usuário pode aprovar o pedido pela área de Produção (Bloqueio por Áreas) |
| CprApi | String(001) | Sim | Indicativo se o usuário pode alterar o peso/quantidade informada nas telas de controle de entrada e saída de compras |
| EstGsa | String(001) | Sim | Indicativo se o usuário pode gerar solicitação de compra automática no atendimento |
| EstAdr | String(001) | Sim | Indicativo se o usuário pode alterar a data da requisição |
| EstAgc | String(001) | Sim | Indicativo se o usuário pode alterar o agrupamento de compras |
| VenLpa | String(001) | Sim | Indicativo se o usuário pode liberar pedido de venda bloqueado pelo parâmetro da filial |
| PrjLfd | String(001) | Sim | Pode fazer lançamentos para projetos em filiais dif. da logada |
| DisRra | String(001) | Sim | Indicativo se o usuário pode reabilitar o Romaneio de Acerto |
| DisInr | String(001) | Sim | Indicativo se o usuário pode incluir notas no Romaneio de Acerto |
| DisEnr | String(001) | Sim | Indicativo se o usuário pode excluir notas no Romaneio de Acerto |
| CprFpo | String(001) | Sim | Indicativo se o usuário é obrigado a informar a forma de pagamento |
| RecArf | String(001) | Sim | Indicativo se o usuário pode alterar o rateio de títulos do C.Receber com o período da filial fechado |
| PagArf | String(001) | Sim | Indicativo se o usuário pode alterar o rateio de títulos do C.Pagar com o período da filial fechado |
| CapArf | String(001) | Sim | Indicativo se o usuário pode alterar o rateio das comissões com o período da filial fechado |
| CxbArf | String(001) | Sim | Indicativo se o usuário pode alterar o rateio de movimentos da Tesouraria com o período da filial fechado |
| CtbElt | String(001) | Sim | Indicativo se o usuário pode excluir lotes |
| CtbElc | String(001) | Sim | Indicativo se o usuário pode excluir lançamentos |
| AprDft | String(001) | Sim | Indicativo se o usuário pode ou não aprovar defeitos ou não conformidades |
| AprDoc | String(001) | Sim | Indica se o usuário pode aprovar documentos do SGQ |
| PrjNus | String(001) | Sim | Indica o nível do usuário para acesso aos orçamentos para projetos |
| CprPec | String(001) | Sim | Indicativo se o usuário pode excluir cotações |
| CprFoc | Number(001,0) | Sim | Tipo de filtro utilizado para permitir visualização e alteração de ordens de compra |
| CprFcp | Number(001,0) | Sim | Tipo de filtro utilizado para permitir visualização e alteração do contrato de compra |
| VenPof | String(001) | Sim | Indicativo se o usuário pode alterar o percentual de oferta dos pedidos ou notas |
| CprPsc | String(001) | Sim | Indicativo se o usuário pode alterar o percentual de sugestão de compra da ligação fornecedor produto |
| MltLgn | String(001) | Sim | Indicativo se o sistema aceita múltiplos acessos simultâneos desse usuário |
| NomSer | String(100) | Sim | Nome do servidor de SMTP |
| PorSer | Number(004,0) | Sim | Porta do servidor de SMTP |
| AutUsu | String(001) | Sim | Indicativo se o servidor de SMTP exige autenticação de usuário |
| UsuAut | String(050) | Sim | Usuário para autenticação de e-mail |
| SenAut | String(030) | Sim | Senha do usuário para autenticação de e-mail |
| AltRem | String(001) | Sim | Indicativo se este usuário pode alterar o remetente da mensagem |
| VenPtn | String(001) | Não | Indicativo se o usuário pode alterar a transação do pedido |
| VenPca | String(001) | Não | Indicativo se o usuário pode alterar a categoria do cliente do pedido |
| VenLpi | String(001) | Sim | Indicativo se o usuário pode aprovar o pedido pela área de Impostos (Bloqueio por Áreas) |
| VenPfp | String(001) | Sim | Indicativo se o usuário pode alterar a filial de produção do pedido |
| PatDfl | String(001) | Sim | Indicativo se o usuário movimenta bens de filiais diferentes da logada |
| VenPcd | String(001) | Sim | Indicativo se o usuário pode alterar o canal de distribuição do pedido |
| MpcAct | String(001) | Sim | Indicativo se o usuário pode incluir/excluir/alterar modelo de plano contábil |
| CtbLtc | String(001) | Sim | Indicativo se o usuário pode alterar lotes de terceiros independente da hierarquia |
| PatTde | String(001) | Sim | Indicativo se o usuário cadastra bens com taxas diferentes das espécies |
| VenScv | String(001) | Sim | Indicativo se o usuário pode saltar competência nos contratos de vendas |
| ConQar | String(001) | Sim | Indicativo se o usuário pode aprovar quantidade superior nas requisições |
| UsuCfe | String(001) | Sim | Modalidade do usuário na gestão de distribuição |
| CprScc | String(001) | Sim | Indicativo se o usuário pode saltar competência nos contratos de compras |
| VenAtv | String(001) | Sim | Indicativo se o usuário pode alterar a tabela de preço nos itens do Pedido |
| VenAtf | String(001) | Sim | Indicativo se o usuário pode alterar a tabela de preço nos itens da Nota Fiscal de Saída |
| ImpRat | String(001) | Sim | Indicativo se usuário pode alterar os rateios definidos no impostos |
| DirNel | String(250) | Sim | Diretório onde deve ser gravado o arquivo de exportação da nota fiscal eletrônica |
| VenCns | String(001) | Sim | Indicativo se o usuário pode cancelar a NF de saída |
| VenRns | String(001) | Sim | Indicativo se o usuário pode reabilitar NF de saída emitida |
| MpcAcf | String(001) | Sim | Indicativo se o usuário pode incluir/excluir/alterar modelo de plano financeiro |
| MpcAcc | String(001) | Sim | Indicativo se o usuário pode incluir/excluir/alterar modelo de centro de custo |
| MpcAca | String(001) | Sim | Indicativo se o usuário pode incluir/excluir/alterar modelo de plano de composição auxiliar |
| DatSin | Date | Sim | Data de sincronização do registro do usuário entre o sistema e a tecnologia |
| HorSin | Number(005,0) | Sim | Hora de sincronização do registro do usuário entre o sistema e a tecnologia |
| VenAir | String(001) | Sim | Indicativo se o usuário pode alterar o índice de reajuste do contrato de venda |
| AprSct | String(001) | Sim | Indica se o usuário tem permissão para aprovar uma solicitação orçamento |
| PrjTso | String(001) | Sim | Permite usuário realizar transferência de saldos de orçamentos multi-empresas |
| CpoCpf | String(001) | Sim | Indicativo se o o pedido/oc deverão ser cancelados ao cancelar/excluir a pré-fatura |
| CprRca | String(001) | Sim | Indicativo se o usuário tem permissão de reabilitar/cancelar uma nota fiscal de entrada |
| CleQtd | String(001) | Sim | Indicativo se usuário pode alterar peso e quantidade recebida na coleta de produtos em fornecedores |
| ClePrc | String(001) | Sim | Indicativo se o usuário pode alterar  a coleta de produtos em fornecedores processada |
| ConRec | String(001) | Sim | Indicativo se o usuário precisa confirmar o recebimento do item da requisição |
| VenSpp | String(001) | Sim | Indicativo se o usuário pode alterar a situação de pedido previsão |
| PrdEpb | String(001) | Sim | Indicativo se o usuário tem permissão para executar cálculo de necessidades de pedidos bloqueados |
| VenAse | String(001) | Sim | Indicativo se o usuário pode alterar a situação do embarque |
| VenIfc | String(001) | Sim | Indicativo se o usuário pode alterar a data de início de faturamento do contrato |
| DirCte | String(250) | Sim | Diretório onde deve ser gravado o arquivo de exportação do conhecimento de transporte eletrônico |
| CprIgc | String(001) | Sim | Indicativo se o usuário pode gerar uma nova contagem |
| CprAsc | String(001) | Sim | Indicativo se o usuário pode alterar a situação de uma contagem na própria tela |
| CprAqc | String(001) | Sim | Indicativo se o usuário pode alterar a quantidade em uma contagem |
| TurTrb | Number(001,0) | Sim | Turno de trabalho do operador |
| CodCel | String(004) | Sim | Célula de produção onde o operador está alocado |
| PrdOpd | String(001) | Sim | Indica se o operador está trabalhando em alguma O.P./O.S. |
| OpdOrp | String(001) | Sim | Permite movimentação de várias O.Ps./O.Ss. ao mesmo tempo |
| VenCst | String(001) | Sim | Indicativo se o usuário pode alterar a situação tributária na gestão de vendas |
| CprCst | String(001) | Sim | Indicativo se o usuário pode alterar a situação tributária na gestão de compras |
| DirNes | String(250) | Sim | Diretório onde deve ser gravado o arquivo de exportação da nota fiscal eletrônica de serviço |
| CanNfe | String(001) | Sim | Indicativo se o usuário pode cancelar uma NF-e com prazo de cancelamento expirado |
| VenSdg | String(001) | Sim | Solicitar o diretório de gravação de arquivos em sessões abertas via middleware |
| DatAfi | String(001) | Sim | Indica se o usuário pode alterar na tabela de histórico a data fiscal |
| IndAst | String(001) | Sim | Indica se o usuário poderá ser responsável por ocorrências |
| AltInp | String(001) | Sim | Indica se o usuário pode alterar inspeções já finalizadas |
| CxbPgp | String(001) | Sim | Gerar a preparação na tesouraria (com origem na tesouraria) já processada |
| AstOrp | String(001) | Sim | Indica se o usuário pode gerar O.P. ou O.S. para atender ocorrências |
| AstSor | String(001) | Sim | Indica se o usuário pode gerar solicitação de orçamento para atender ocorrências |
| AstNfv | String(001) | Sim | Indica se o usuário pode gerar N.F. para atender ocorrências |
| AstPed | String(001) | Sim | Indica se o usuário pode gerar pedido para atender ocorrências |
| RecAcd | String(001) | Sim | Indicativo se usuário pode alterar valores no critério de distribuição |
| PagAcd | String(001) | Sim | Indicativo se usuário pode alterar valores no critério de distribuição |
| PagDet | Number(001,0) | Sim | Data base para cálculo do reajuste |
| MaxLgn | Number(004,0) | Sim | Número máximo de acessos simultâneos ao sistema |
| ParEsp | String(001) | Sim | Indicativo se o usuário pode alterar as parcelas especiais na fixação de preços |
| VenCnp | String(001) | Sim | Indicativo se o usuário pode alterar os períodos de créditos do convênio |
| IndMre | String(001) | Sim | Indicativo se o usuário manipula requisições no processo de carga |
| AstPsi | String(001) | Sim | Indica se o usuário pode gerenciar produtos e serviços na ocorrência |
| AstEto | String(001) | Sim | Indica se o usuário pode excluir trâmites de uma ocorrência |
| ExaOcp | String(001) | Sim | Permite excluir o controle de aprovação da ordem de compra |
| VenAva | String(001) | Sim | Indicativo se o usuário pode alterar controle de avalistas |
| ManAge | String(001) | Sim | Indicativo se o usuário pode alterar, inserir ou excluir os agendamentos |
| ConAge | String(001) | Sim | Indicativo se o usuário pode consultar os agendamentos |
| PatEmp | String(001) | Sim | Indicativo se o usuário pode alterar alguns campos de títulos de empréstimos |
| AltMon | String(001) | Sim | Indicativo se o usuário pode alterar pendências de montagem |
| AltEbq | String(001) | Sim | Indicativo se o usuário pode alterar pendências de embarque |
| AudPfa | String(001) | Sim | Indicativo se o usuário pode auditar cargas. |
| AltNnu | String(001) | Sim | Indicativo se usuário pode alterar o nosso número da impressão de bloquetos |
| SenApr | String(001) | Sim | Indicativo se o usuário pode gerar senha para aprovação de pedidos |
| CobPdj | String(001) | Sim | Indicativo se o usuário pertence ao departamento jurídico da empresa |
| CobAtc | String(001) | Sim | Indicativo se o usuário pode alterar títulos que estejam em cobrança |
| AcrCcm | String(001) | Sim | Indicativo se o usuário pode categorizar o cliente manualmente para crédito |
| PerExs | String(001) | Sim | Indicativo se o usuário pode excluir Solicitação a partir da Cotação de Preço |
| PerFpc | Number(001,0) | Sim | Tipo de permissão para a formação preços |
| IndAnt | String(001) | Sim | Ind. se usuário tem permissão para informar descontos por antecipação |
| IndPon | String(001) | Sim | Ind. se usuário tem permissão para informar descontos por pontualidade |
| IndQgo | String(001) | Sim | Ind. se usuário tem permissão para informar qtde. mult. min. máx. na geração OP |
| VenLce | String(001) | Não | Indicativo se o usuário tem permissão de liberar cargas para uso do estoque. |
| SimFec | String(001) | Não | Ind. se o usuário tem permissão simular o fechamento da nota fiscal de entrada |
| CprPos | String(001) | Sim | Ind. se o usuário tem permissão para fechar uma pesagem com pós-saída |
| RepVar | Number(009,0) | Sim | Código do representante ligado ao usuário para o sistema de loja |
| PrpOcp | String(001) | Sim | Gerar a preparação na tesouraria (com origem no C.Pagar) já processada |
| PerAcf | String(001) | Sim | Indicativo se pode alterar o tipo de faturamento do acréscimo no contrato |
| NomUsu | String(255) | Sim | Nome do usuário |
| PerUni | String(001) | Não | Permitir alterar o preço unitário do item a fixar sem vínculo com contrato |
| CprBlo | String(001) | Sim | Indicativo se o usuário pode acessar a rotina de bloqueio de produtos |
| PerCnl | String(001) | Sim | Ind. se o usuário pode cancelar tickets fechados usando a tela de manutenção |
| CprPse | String(001) | Sim | Indicativo se o usuário pode alterar o SENAR/SENAT das OC ou notas |
| VenPse | String(001) | Sim | Indicativo se o usuário pode alterar o SENAR/SENAT dos Pedidos ou notas |
| ObsMob | String(001) | Sim | Registrar o motivo de cancelamento do pedido tratado pelo aplicativo móvel |
| ObsMol | String(001) | Sim | Registrar o motivo de liberação do pedido tratado pelo aplicativo móvel |
| ObsMor | String(001) | Sim | Registrar o motivo de reabilitação do pedido tratado pelo aplicativo móvel |
| DirMdf | String(250) | Sim | Diretório onde deve ser gravado o arquivo de exportação do Manifesto Eletrônico de Documentos |
| VenCpd | String(001) | Sim | Indicativo se o usuário pode cancelar pedidos. |
| VenRpd | String(001) | Sim | Indicativo se o usuário pode reabilitar pedidos. |
| RebNfi | String(001) | Sim | Indicativo se o usuário pode reabilitar a nota fiscal de inventário. |
| USU_IndSup | String(001) | Sim | Indica Superior |
| USU_CodRep | Number(009,0) | Sim | Representante vinculado ao usuário |
| USU_AdminFV | String(001) | Sim | Força de Vendas - Admin |
| USU_NUMCAD | Number(009,0) | Sim | Matricula |
| USU_BloAut | String(001) | Sim | Bloqueio Automatico |

---

## Chave Primária

- CodEmp
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E099USU_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

