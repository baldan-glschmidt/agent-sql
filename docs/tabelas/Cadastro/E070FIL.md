# E070FIL

## Descrição

Cadastros - Filiais

---

## Resumo

- Campos: 256
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NomFil | String(100) | Não | Razão social da filial da empresa |
| SigFil | String(030) | Não | Nome fantasia da filial da empresa |
| InsEst | String(025) | Sim | Inscrição estadual da filial da empresa |
| InsMun | String(016) | Sim | Inscrição municipal da filial da empresa |
| InsNfs | String(016) | Sim | Inscrição municipal da filial da empresa para impressão na NFS-e |
| NumCgc | Number(015,0) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| DocIde | String(014) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| EndFil | String(100) | Sim | Endereço da filial da empresa |
| CplEnd | String(200) | Sim | Complemento do endereço da filial da empresa (Sala, andar, etc.) |
| CepFil | Number(008,0) | Sim | CEP da filial da empresa |
| CepIni | Number(008,0) | Sim | Faixa inicial do CEP da cidade da filial |
| CodRai | Number(007,0) | Sim | Código da cidade para recolhimento do ISS (Tabela RAIS) |
| BaiFil | String(075) | Sim | Bairro da filial da empresa |
| CidFil | String(060) | Sim | Cidade da filial da empresa |
| SigUfs | String(002) | Sim | Sigla do estado da filial da empresa |
| EndEnt | String(100) | Sim | Endereço de entrega da filial |
| CplEnt | String(200) | Sim | Complemento do endereço de entrega da filial |
| CepEnt | Number(008,0) | Sim | CEP do endereço de entrega da filial |
| CidEnt | String(060) | Sim | Cidade do endereço de entrega da filial |
| EstEnt | String(002) | Sim | Sigla do estado do endereço de entrega da filial |
| EndCob | String(100) | Sim | Endereço de cobrança da filial |
| CplCob | String(200) | Sim | Complemento do endereço de cobrança da filial |
| CepCob | Number(008,0) | Sim | CEP do endereço de cobrança da filial |
| CidCob | String(060) | Sim | Cidade do endereço de cobrança da filial |
| EstCob | String(002) | Sim | Sigla do estado do endereço de cobrança da filial |
| NumFon | String(020) | Sim | Número do telefone da filial da empresa |
| NumFax | String(020) | Sim | Número do fax da filial da empresa |
| CxaPst | Number(006,0) | Sim | Número da caixa postal da filial da empresa |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| TipEmp | Number(002,0) | Sim | Tipo de empresa |
| FilCli | Number(009,0) | Sim | Código da filial como cliente |
| FilFor | Number(009,0) | Sim | Código da filial como fornecedor |
| PedIni | Number(008,0) | Sim | Número inicial para geração do Pedido de Previsão (Quando Pedido não gera número Automático) |
| ZonFra | Number(001,0) | Sim | Indicativo de qual o benefício fiscal da filial |
| CodSuf | String(010) | Sim | Código da empresa/filial junto a Suframa |
| DifAli | String(001) | Não | Indicativo se a filial calcula ou não a diferença de alíquota inter-estadual |
| CriFed | Number(001,0) | Sim | Critério p/ formação do estoque p/ atendimento faturamento/baixas estoque em geral (identificador de regra) |
| QtdDlb | Number(003,0) | Sim | Quantidade de dias para liberação dos estoques bloqueados |
| VenPdi | Date | Sim | Período inicial de validade para movimentação do Vendas |
| VenPdf | Date | Sim | Período final de validade para movimentação do Vendas |
| VenCae | Number(001,0) | Sim | Critério adotado pela filial para efeito de análise de embarque/faturamento |
| VenQdf | Number(003,0) | Sim | Quantidade de dias permitido entre datas de faturamentos |
| VenTcc | String(005) | Sim | Transação padrão de baixa do C. Receber por cancelamento |
| VenTpp | String(005) | Sim | Transação padrão para entrada de pedido de produto |
| VenTps | String(005) | Sim | Transação padrão para entrada de pedido de serviço |
| VenDsu | Number(005,2) | Sim | Percentual de desconto para Suframa |
| VenVmp | Number(015,2) | Sim | Valor mínimo permitido para os pedidos |
| VenLep | Number(004,0) | Sim | Quantidade de dias limite para aceitação de entrega dos pedido |
| VenTcv | String(002) | Sim | Tipo de cota de venda para os representantes |
| VenCep | String(001) | Sim | Indicativo se filial utiliza ou não a tabela de CEP's |
| VenPvp | String(001) | Sim | Indicativo se a filial da empresa utiliza período de vendas/produção |
| VenNpa | String(001) | Sim | Indicativo se o número do pedido de venda é numerado automaticamente |
| VenCfi | String(001) | Sim | Indicativo se os códigos de cliente e fornecedor são iguais |
| VenNtr | String(001) | Sim | Indicativo do critério para definição do número de título do contas a receber |
| VenSnr | String(003) | Sim | Código Padrão da série da nota fiscal de Remessa de Serviço |
| VenQip | Number(003,0) | Sim | De quanto em quanto é o incremento do número de pedido |
| VenSnp | String(003) | Sim | Série padrão para nota fiscal de saída |
| VenQdp | Number(003,0) | Sim | Quantidade de dias anterior ao atual aceito para data de entrega de pedido |
| VenRpd | Number(009,0) | Sim | Código do representante padrão (NF Produtor) |
| VenCcc | String(001) | Sim | Indicativo se o CNPJ e/ou CPF do cliente é obrigatório |
| VenCcr | String(001) | Sim | Indicativo se o CNPJ/CPF/Nº Identificação Fiscal do cliente pode ser repetido |
| VenCrr | String(001) | Sim | Indicativo se o CNPJ/CPF/Nº Identificação Fiscal do representante pode ser repetido |
| VenPse | String(001) | Não | Indicativo se aceita item de pedido sem estoque disponível |
| VenPam | Number(004,0) | Sim | Quantidade máxima de dias de atraso médio aceita na entrada  de pedido |
| VenPma | Number(004,0) | Sim | Quantidade máxima de dias de maior atraso aceita na entrada de pedido |
| VenPpc | Number(004,0) | Sim | Quantidade máxima de pagamentos em cartório aceita na entrada de pedido |
| VenPta | Number(004,0) | Sim | Quantidade máxima de títulos em atraso aceita na entrada de pedido |
| VenPdt | Number(004,0) | Sim | Quantidade de dias de atraso de títulos aceito para entrada de pedido |
| VenPcs | Number(004,0) | Sim | Quantidade máxima de cheques sem fundo aceita na entrada de pedido |
| VenPlc | String(001) | Sim | Indicativo se aceita pedido com estouro de limite de crédito |
| VenFam | Number(004,0) | Sim | Quantidade máxima de dias de atraso médio aceita para faturamento |
| VenFma | Number(004,0) | Sim | Quantidade máxima de dias de maior atraso aceita para faturamento |
| VenFpc | Number(004,0) | Sim | Quantidade máxima de pagamentos em cartório aceita para faturamento |
| VenFta | Number(004,0) | Sim | Quantidade máxima de títulos em atraso aceita para faturamento |
| VenFdt | Number(004,0) | Sim | Quantidade de dias de atraso de títulos aceito para faturamento |
| VenFcs | Number(004,0) | Sim | Quantidade máxima de cheques sem fundo aceita para faturamento |
| VenFlc | String(001) | Sim | Permite faturar mesmo com limite de crédito excedido |
| VenIss | Number(007,4) | Sim | Percentual do ISS válido para a cidade da filial |
| VenIpd | Number(004,0) | Não | Número máximo de itens no Pedido |
| VenApc | Number(004,0) | Sim | Número de dias para aprovação de Pedidos de Cliente Novo |
| VenLvp | Number(004,2) | Sim | Valor Limite para o percentual de variação do peso informado nas telas de controle de entrada e saída de vendas |
| EstPdi | Date | Sim | Período inicial de validade para movimentações dos estoques |
| EstPdf | Date | Sim | Período final de validade para movimentações dos estoques |
| EstPai | Date | Sim | Período inicial anterior de validade para movimentações dos estoques |
| EstPaf | Date | Sim | Período final anterior de validade para movimentações dos estoques |
| EstTei | String(005) | Sim | Transação padrão de entrada por inventário |
| EstTsi | String(005) | Sim | Transação padrão de saída por inventário |
| EstTpr | String(005) | Sim | Transação padrão para requisição de estoques |
| EstUnm | String(001) | Sim | Indicativo se a filial usa numeração automática de documento |
| EstDpf | String(001) | Sim | Indicativo se a filial pode movimentar estoques de depósitos de qualquer filial |
| RecPdi | Date | Sim | Período inicial de validade para movimentação do contas a receber |
| RecPdf | Date | Sim | Período final de validade para movimentação do contas a receber |
| RecPor | String(004) | Sim | Código do portador da empresa que identifica carteira |
| RecCrt | String(002) | Sim | Código de carteira da empresa que identifica carteira |
| RecOcr | String(003) | Sim | Código interno de ocorrência padrão para remessa de títulos |
| RecIns | String(003) | Sim | Código da instrução bancária padrão de inexistência de instrução |
| RecVmt | Number(015,2) | Sim | Valor mínimo aceito para títulos do contas a receber |
| RecDpr | Number(004,0) | Sim | Quantidade de dias limite para prorrogação dos títulos do contas a receber |
| RecMoe | String(003) | Sim | Código de moeda padrão para contas a receber |
| RecJmm | Number(005,2) | Sim | Percentual de juros mora mês padrão para os títulos do contas a receber |
| RecTjr | String(001) | Sim | Tipo de juros mora mês padrão para os títulos do contas a receber |
| RecDtj | Number(004,0) | Sim | Quantidade de dias de tolerância para os juros mora do contas a receber |
| RecMul | Number(005,2) | Sim | Percentual de multa padrão para os títulos do contas a receber |
| RecDtm | Number(004,0) | Sim | Quantidade de dias de tolerância para a multa do contas a receber |
| RecVjm | Number(009,2) | Sim | Valor mínimo dos juros de mora aceito no contas a receber |
| RecVdm | Number(009,2) | Sim | Valor mínimo do desconto aceito no contas a receber |
| RecVmm | Number(009,2) | Sim | Valor mínimo da multa aceito no contas a receber |
| RecAvs | String(001) | Sim | Indicativo do critério de definição de vencimento |
| RecAdc | String(001) | Sim | Indicativo se os descontos concedidos abatem das comissões |
| RecAoc | String(001) | Sim | Indicativo se os outros descontos abatem das comissões |
| RecPcj | String(001) | Sim | Indicativo se a filial paga comissão sobre juros cobrados |
| RecPcm | String(001) | Sim | Indicativo se a filial paga comissão sobre multas cobradas |
| RecPce | String(001) | Sim | Indicativo se paga comissão sobre os encargos financeiros |
| RecPcc | String(001) | Sim | Indicativo se paga comissão sobre a correção monetária |
| RecPco | String(001) | Sim | Indicativo se paga comissão sobre outros acréscimos |
| RecTpm | String(005) | Sim | Transação padrão de entrada manual de títulos |
| RecTac | String(005) | Sim | Transação padrão de entrada de títulos de crédito de clientes |
| RecTes | String(005) | Sim | Transação padrão de entrada de títulos por substituição |
| RecTbp | String(005) | Sim | Transação padrão de baixa de títulos por pagamento |
| RecTba | String(005) | Sim | Transação padrão de baixa de títulos por crédito |
| RecTbs | String(005) | Sim | Transação padrão de baixa de títulos do CR por substituição |
| RecTbc | String(005) | Sim | Transação padrão de baixa para títulos de crédito |
| RecTpc | String(005) | Sim | Trans.padrão de crédito na tesouraria pela baixa no Conta a Receber |
| RecTcc | String(005) | Sim | Transação Desconto Comissão pela Exclusão de Baixa no Contas a Receber |
| CprPdi | Date | Sim | Período inicial de validade para movimentação do compras |
| CprPdf | Date | Sim | Período final de validade para movimentação do compras |
| CprQmc | Number(002,0) | Sim | Quantidade mínima de cotações exigidas pela filial |
| CprAvo | String(001) | Sim | Indicativo se exige a digitação do valor total da NF de entrada |
| CprDnf | Number(008,2) | Sim | Diferença aceita entre o valor informado e o calculado da NF de entrada |
| CprTop | String(005) | Sim | Transação padrão para ordem de compra via produção |
| CprTom | String(005) | Sim | Transação padrão para ordem de compra de produto |
| CprTos | String(005) | Sim | Transação padrão para ordem de compra de serviço |
| CprTfp | String(005) | Sim | Transação padrão para Nota Fiscal de Entrada de Produto |
| CprTfs | String(005) | Sim | Transação padrão para Nota Fiscal de Entrada de Serviço |
| CprTea | String(005) | Sim | Transação padrão de entrada de estoque por ajuste de balança |
| CprTsa | String(005) | Sim | Transação padrão de saída de estoque por ajuste de balança |
| CprSnp | String(003) | Sim | Série padrão para nota fiscal de entrada |
| CprCcf | String(001) | Sim | Indicativo se o CNPJ e/ou CPF do fornecedor é obrigatório |
| CprCfr | String(001) | Sim | Indicativo se o CNPJ/CPF/Nº Identificação Fiscal do fornecedor pode ser repetido |
| CprFss | Number(009,0) | Sim | (descontinuado) Código do fornecedor padrão para geração do título de ISS |
| PagPdi | Date | Sim | Período inicial de validade para movimentação do contas a pagar |
| PagPdf | Date | Sim | Período final de validade para movimentação do contas a pagar |
| PagApr | String(001) | Sim | Indicativo se existe controle de aprovação de pagamento |
| PagDpr | Number(004,0) | Sim | Quantidade de dias limite para prorrogação dos títulos do contas a pagar |
| PagMoe | String(003) | Sim | Código da moeda padrão para títulos do contas a pagar |
| PagJmm | Number(005,2) | Sim | Percentual de juros mora mês padrão para os títulos do contas a pagar |
| PagTjr | String(001) | Sim | Tipo de juros mora mês padrão para os títulos do contas a pagar |
| PagDtj | Number(004,0) | Sim | Quantidade de dias de tolerância para os juros de mora mês do contas a pagar |
| PagMul | Number(005,2) | Sim | Percentual de multa padrão para os títulos do contas a pagar |
| PagDtm | Number(004,0) | Sim | Quantidade de dias de tolerância para a multa do conta a pagar |
| PagTpm | String(005) | Sim | Transação padrão de entrada manual de títulos |
| PagTpf | String(005) | Sim | Transação padrão de entrada de títulos de frete (controle de entradas e saídas) |
| PagTaf | String(005) | Sim | Transação padrão de entrada de títulos de crédito a fornecedores |
| PagTbp | String(005) | Sim | Transação padrão de baixa de títulos por pagamento |
| PagTbc | String(005) | Sim | Transação padrão de baixa para títulos de crédito |
| PagTbs | String(005) | Sim | Transação padrão de baixa de títulos do CP por substituição |
| PagTpc | String(005) | Sim | Transação padrão de débito por emissão de cheque para caixa/bancos |
| PagTcc | String(005) | Sim | Transação padrão de crédito por cancelamento de cheque |
| PagVjm | Number(009,2) | Sim | Valor mínimo dos juros aceito no contas a pagar |
| PagVdm | Number(009,2) | Sim | Valor mínimo do desconto aceito no contas a pagar |
| PagVmm | Number(009,2) | Sim | Valor mínimo da multa aceito no contas a pagar |
| PagTcm | String(005) | Sim | Transação padrão de pagamento de comissão |
| PagTdc | String(005) | Sim | Transação desconto comissão pela baixa de título por cancelamento |
| PagTdi | String(005) | Sim | Transação padrão de desconto de Imposto de Renda sobre comissão |
| PagLir | Number(008,2) | Sim | Valor mínimo aceito no cálculo do IR de comissões pessoas jurídicas |
| PagEev | Number(003,0) | Sim | Quantidade mínima de dias aceito entre a data de entrada e o vencimento de um título |
| CxbPdi | Date | Sim | Período inicial de validade para movimentação da tesouraria |
| CxbPdf | Date | Sim | Período final de validade para movimentação da tesouraria |
| CxbTca | String(005) | Sim | Transação padrão de crédito na tesouraria por crédito de cliente |
| CxbTdc | String(005) | Sim | Transação padrão débito tesouraria por cancelamento baixa título |
| CxbTde | String(005) | Sim | Transação padrão débito tesouraria para despesas de cobrança |
| CxbTdt | String(005) | Sim | Transação padrão de débito por cancelamento de crédito por transferência |
| CxbDec | Number(002,0) | Sim | Quantidade de dias padrão para sugestão período emissão cheque |
| CtbExi | Date | Sim | Data inicial do período contábil permitido para lançamentos |
| CtbExf | Date | Sim | Data final do período contábil permitido para lançamentos |
| CtbPei | Date | Sim | Mês e ano inicial do período permitido para lançamentos |
| CtbPef | Date | Sim | Mês e ano final do período permitido para lançamentos |
| CtbQdl | Number(004,0) | Sim | Quantidade de dias, após data atual, aceito para lançamentos |
| CtbMoe | String(003) | Sim | Código da moeda padrão para contabilidade |
| CtbLog | String(001) | Sim | Indicativo se grava ou não log's dos lançamentos |
| CtbAli | String(001) | Sim | Indicativo se permite ou não alteração de lotes integrados |
| CtbDia | Date | Sim | Data do início das atividades da empresa |
| CtbObs | String(119) | Sim | Objeto social da empresa - principais atividades |
| CtbNrj | String(015) | Sim | Número de identificação do registro da empresa (NIRE) na junta comercial |
| CtbDrj | Date | Sim | Data do registro da empresa na junta comercial |
| CtbNsr | String(100) | Sim | Nome do sócio responsável pela gestão da empresa |
| CtbFsr | String(020) | Sim | Função do sócio responsável |
| CtbCsr | Number(012,0) | Sim | Número do CPF do sócio responsável |
| CtbNcr | String(100) | Sim | Nome do contador responsável |
| CtbFcr | String(001) | Sim | Formação do contador responsável |
| CtbCrc | String(015) | Sim | Número do CRC do contador responsável |
| CtbCcr | Number(012,0) | Sim | Número do CPF do contador |
| CtbCfm | Number(007,0) | Sim | Número do código fiscal do município |
| CtbCae | String(010) | Sim | Código de atividade da empresa junto ao estado |
| CtbCaf | Number(005,0) | Sim | Código de atividade da empresa junto a receita federal |
| CtbFec | String(001) | Sim | Indicativo se a filial efetua fechamento por lote |
| CtbSdt | String(001) | Sim | Indicativo se a data do lançamento é somada para fechamento de lote |
| CtbSde | String(001) | Sim | Indicativo se a conta de débito é somada para fechamento de lote |
| CtbScr | String(001) | Sim | Indicativo se a conta de crédito é somada para fechamento de lote |
| CtbSvl | String(001) | Sim | Indicativo se o valor do lançamento é somado para fechamento de lote |
| CtbShp | String(001) | Sim | Indicativo se o histórico padrão é somado para fechamento de lote |
| CtbHab | String(001) | Sim | Indicativo se a filial está ou não habilitada para receber lançamentos contábeis |
| EfiPdi | Date | Sim | Período inicial de validade para apuração do impostos |
| EfiPdf | Date | Sim | Período final de validade para apuração do impostos |
| EfiFtr | String(001) | Sim | Forma de tributação da filial |
| EfiApi | Number(007,4) | Sim | Percentual da alíquota padrão para o ISS |
| EfiStr | String(001) | Sim | Indicativo se a filial tem qualificação de substituição tributária |
| EfiReg | Number(004,0) | Sim | Código da Regra para integração dos impostos |
| EfiQci | Number(004,0) | Sim | Quantidade de meses para apuração do CIAP |
| PrdTep | String(005) | Sim | Transação padrão de entrada de estoques via produção - OP |
| PrdTsp | String(005) | Sim | Transação padrão de saída de estoques para produção |
| PrdQdd | Number(003,0) | Sim | Quantidade de dias de desembaraço (intervalo OPs finalizadas e Data Entrega) antes da entrega dos pedidos |
| PrdTpp | String(005) | Sim | Transação padrão para geração de pedidos de previsão produção |
| PrdCpp | Number(009,0) | Sim | Código do cliente padrão para geração de pedido de previsão produção |
| PrdRpp | Number(009,0) | Sim | Código do representante para o pedido de previsão produção |
| PrdPpp | String(006) | Sim | Código da condição de pagamento padrão pedido previsão produção |
| PrdTee | String(005) | Sim | Transação padrão para estorno de componentes da produção para o estoque |
| PrdTnr | String(005) | Sim | Transação padrão para remessa componentes da produção para o Terceiros |
| PrdEfi | Number(005,2) | Sim | Percentual de eficiência de produção da filial |
| PedBlo | String(001) | Não | Indicativo se o Pedido fica automaticamente bloqueado na entrada/digitação |
| ComPrz | String(001) | Não | Indicativo se consiste Prazo Médio nas Parcelas Especiais |
| PerCom | Number(004,2) | Sim | Percentual de Comissão padrão para Representante |
| TipSep | String(003) | Sim | Tipo de separação de mercadorias |
| IndRoe | String(001) | Não | Indicativo se a Filial trabalha com Rota de Entrega. |
| CprIef | String(001) | Não | Indicativo se a Inscrição Estadual do fornecedor deve ser válida |
| VenIec | String(001) | Não | Indicativo se a Inscrição Estadual do Cliente deve ser válida |
| RecTia | String(001) | Não | Indicativo se a filial trabalha com instruções automáticas ao baixar/alterar títulos |
| EstFpr | String(005) | Sim | Transação padrão para saída por fracionamento de produtos |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| CodAfi | Number(004,0) | Sim | Código do agrupamento de filiais |
| EenFil | String(018) | Sim | Código do endereço da filial |
| EenEnt | String(018) | Sim | Código do endereço de entrega da filial |
| EenCob | String(018) | Sim | Código do endereço de cobrança da filial |
| BaiEnt | String(075) | Sim | Bairro de entrega da filial |
| BaiCob | String(075) | Sim | Bairro de cobrança da filial |
| NenFil | String(060) | Sim | Número do Endereço da Filial |
| FilMat | String(001) | Sim | Indicativo que a filial é a matriz |
| AgeAnp | Number(010,0) | Sim | Código do agente regulado informante (ARI) conforme cadastro da ANP |
| InsAnp | Number(007,0) | Sim | Código da instalação conforme cadastro da ANP |
| EstUsa | Number(010,0) | Sim | Número do cadastro do usuário que alterou os períodos de estoque |
| EstDta | Date | Sim | Data da alteração dos períodos de estoque |
| EstHra | Number(005,0) | Sim | Hora da alteração dos períodos de estoque |
| IdeUni | Number(009,0) | Não | Identificador único da filial |
| NumIdf | String(040) | Sim | Número de identificação fiscal |
| IntWmw | String(001) | Sim | Indicativo se registro deve integrar com o WMW |
| CodCae | Number(015,0) | Sim | Código do Cadastro de Atividade Econômica da Pessoa Física - CAEPF |
| ExpPix | Number(003,0) | Sim | Quantidade de dias para expiração do PIX após o vencimento do título |
| MecCep | Number(002,0) | Sim | Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador do serviço |
| USU_CmdSapWeb | String(053) | Sim | Campo para Sapiens Web |
| USU_ConPor | String(001) | Sim | Considera Portador do Pedido (e120ped.usu_loginweb) |
| USU_ConFil | String(001) | Sim | Considera Filtros Borderôs |
| USU_IntSF | String(001) | Sim | Integra com Salesforce |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

### E070FILIndice1

**Tipo:** Unico

Campos:
- IdeUni

---

## Relacionamentos

### IR_E070FIL_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

