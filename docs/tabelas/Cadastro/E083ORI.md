# E083ORI

## Descrição

Cadastros - Origens de Produto

---

## Resumo

- Campos: 111
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodOri | String(003) | Não | Código da Origem do Produto |
| DesOri | String(040) | Não | Descrição da Origem do Produto |
| NumOri | Number(004,0) | Não | Nível da Origem, na árvore Hierárquica do Produto Acabado Final |
| TipPro | String(001) | Não | Tipo de produto |
| DepPad | String(010) | Sim | Depósito padrão p/ Produtos desta Origem (Fazer Reservas) |
| BxaAgr | String(001) | Não | Permite Baixa agrupada de vários componentes de O.Ps./O.Ss. gerando um só movimento de estoque (S=Sim, N=Não) |
| BxaMov | String(001) | Não | Tipos de Baixa de Componentes durante a Movimentação de O.Ps./O.Ss. |
| IndQbx | String(001) | Sim | Indicativo se baixa componentes no ato ou se utiliza agendador (usado em baixas automáticas) |
| BxaEst | String(001) | Sim | Indica se as O.Ps./O.Ss. dessa origem baixam os compon. pela estrutura ou pela O.P./O.S. proporcional à quantidade movimentada |
| ResCmp | String(001) | Não | Reserva manual do estoque de componentes para O.P./O.S. (S=Sim, N=Não) |
| MovPar | String(001) | Não | Permite Movimentação parcial das O.Ps./O.Ss. por Estágios ou Operações (S/N) |
| MopGrd | String(001) | Sim | Movimenta OPs em Grade (é gerado movto de OP para todas as derivações) |
| GerOpr | String(001) | Não | Acompanhamento da movimentação da O.P./O.S. por operações (S=Sim, N=Não) |
| CtrVld | String(001) | Não | Indicativo da forma de controle da data de validade nos estoques |
| CtrSep | String(001) | Não | Controla Entrada/Saídas no Estoque por Série |
| CtrLot | String(001) | Não | Controla Entrada/Saída no Estoque por  Lote |
| GerLot | String(001) | Sim | Gerar lote para o produto da OP |
| LotPad | String(050) | Sim | Código do Lote Padrão |
| CtrQld | String(001) | Não | Controla Qualidade de 2ª e 3ª nas Movimentações e Entrada Estoque OPs |
| CtrRfg | String(001) | Não | Controla Refugos de produção nas Movimentações e Entrada Estoque O.Ps. |
| EntEpi | String(001) | Sim | Dá entrada no estoque em processos intermediários da qtde refugada |
| CtrGop | String(001) | Não | Controla OP com guias (sub-divisões de uma OP) de produção no movimento de OP |
| GerFil | String(001) | Sim | Gera cálculo necessidades explodindo aberto por filial para primeiro nível abaixo da árvore hierárquica |
| GerPed | String(001) | Não | Gera cálculo necessidades explodindo aberto por pedido para primeiro nível abaixo da árvore hierárquica |
| AgrIpd | String(001) | Não | Gera cálculo necessidade agrupando itens do mesmo pedido, sem rastreamento por item (Compras/Produção) para primeiro nível abaixo da árvore hierárquica |
| AgrNbc | String(001) | Não | Gera cálculo necessidades de compras agrupadas (sem rastreamento das O. Compra) para primeiro nível abaixo da árvore hierárquica |
| DisNec | String(001) | Não | Gera cálculo necessidades, abatendo estoque disponível de componentes automaticamente (Intermediários/materiais) para primeiro nível abaixo da árvore hierárquica |
| GerRla | String(001) | Sim | Reserva lotes automaticamente para os componentes da O.P./O.S. na Geração de O.Ps./O.Ss. |
| SitCal | String(001) | Sim | Situação do Cálculo Necessidades/Geração O.P./O.S. (A=Ativo, I=Inativo) |
| CodPvp | String(008) | Sim | Código do último Período do Cálculo de Necessidades |
| CnfNec | String(001) | Não | Gera Cálculo Necessidades c/ a Exigência de Confirmação de Necessidades Compras/Produção para nível abaixo da árvore hierárquica (Válido p/ Cálculo Mono-Nível) |
| IniPvp | String(001) | Não | Gera O.Ps./O.Ss. com Data de Início do Período ao qual está Vinculada (S=Sim, N=Não) |
| OrpDer | String(001) | Não | Gera OPs para cada Produto/Derivação do Produto (Não junta por Derivação) |
| MltPed | String(001) | Sim | Gera Ordens de Produção/Serviço para vários Pedidos e/ou Períodos |
| IncPro | String(001) | Não | Indicativo se é permitido incluir produtos novos em O.P. já gerada |
| GerSol | String(001) | Não | Gerar Solicitação de Compras Automática no Cálculo de Necessidades, sem pré-avaliação da Área de Administração de Materiais (Estoque) para nível abaixo da árvore hierárquica |
| GerAgr | String(001) | Não | Gera OPs por Agrupamento de Derivação do Produto (junta por Agrupamento Derivação) |
| MovOpd | String(001) | Não | Permite Movimentação das O.Ps./O.Ss. Identificando o Operador (S=Sim, N=Não) |
| QtdBas | Number(011,4) | Sim | Quantidade Base p/ Geração de Ficha de Custos (Produto Produzido/Montagem) |
| UsaFrq | String(001) | Não | Utiliza Tempo Frequencial nos Roteiros de Fabricação |
| UsaFix | String(001) | Não | Utiliza quantidade fixa do Modelo para considerar no Cálculo de Necessidades |
| UsaAux | String(001) | Não | Permite alterar Unidade de Medida do Produto COMPRADO e P.DIRETA proposta pela Família (Não totaliza volumes por Família) |
| MovPrl | String(001) | Não | Permite movimento parcial por operador (mais de um operador) p/ mesma operação |
| OpdOrp | String(001) | Não | Permite (S=Sim, N=Não) movimentação de várias O.Ps./O.Ss. pelo mesmo Operador ao mesmo tempo (Todas em andamento) |
| ObrPrv | String(001) | Não | [DEPRECADO] Obrigatório produzir a quantidade prevista não permitindo excedê-la |
| DisXpl | String(001) | Não | Indicativo p/ trazer marcado opção de Abater estoque disponível p/pedidos, na Explosão Necessidades |
| SerXpl | String(001) | Não | Indicativo se gera Solicitação de Serviços na Geração de O.P./O.S. |
| AcePrv | String(001) | Não | Consiste na entrada de pedido se aceita além da previsão (Pedido Previsão) |
| CodReg | Number(004,0) | Sim | Código da Regra (0001 é utilizada p/ personalizar inclusão de campos no movimento OP) |
| CodMs1 | String(008) | Sim | Código da Máscara para 1ª parte do código da série/lote fabricação de produtos desta Família |
| CodMs2 | String(008) | Sim | Código da Máscara para 2ª parte do código da série/lote fabricação de produtos desta Família |
| CodMs3 | String(008) | Sim | Código da Máscara para 3ª parte do código da série/lote fabricação de produtos desta Família |
| CodMs4 | String(008) | Sim | Código da Máscara para 4ª parte do código da série/lote fabricação de produtos desta Família |
| PrdTsp | String(005) | Sim | Transação padrão de saída de estoques para produção |
| PrdTep | String(005) | Sim | Transação padrão de entrada de estoques via produção - OP |
| NotFor | Number(005,2) | Sim | Nota mínima necessária para a aprovação de um fornecedor |
| AgrNbp | String(001) | Não | Gera cálculo necessidades de produção agrupadas (sem rastreamento) para nível atual da árvore hierárquica |
| DepIql | String(010) | Sim | Código do depósito padrão para inspeção de qualidade |
| GopEop | String(001) | Não | Indica o tipo de controle de Guias |
| TolExc | Number(009,3) | Não | Tolerância excedente a quantidade prevista nas OPs desta origem |
| CodEso | String(005) | Sim | Espécie da Origem do Produto |
| TipInt | Number(001,0) | Sim | Tipo de Integração |
| CodMar | String(010) | Sim | Código da Marca/Etiqueta da origem |
| AbtPrv | String(001) | Sim | Indicativo se deve ser abatido o pedido de previsão dos produtos desta origem no fechamento dos pedidos normais (É necessário que a filial esteja com "Não" para ser considerado) |
| UtiTci | String(001) | Não | Utiliza tabela de contagem individual das unidades nos movtos da OP (E900CCB) |
| IndCee | String(001) | Não | Indicativo se a OP permite gerar subproduto |
| GerOrp | String(001) | Não | Indica se o produto gera Ordem de Produção/Serviço |
| GerVer | String(001) | Sim | Gera versão automaticamente da ficha técnica |
| VerMan | String(001) | Não | Permite gerar o número da versão de forma manual ou automática da ficha técnica |
| DefDat | Number(001,0) | Sim | Cálculo da definição das datas dos estágios/operações das OPs |
| IndSpr | String(001) | Sim | Indicativo se o serviço é produzido |
| TelEmo | String(001) | Sim | Informar especificações de movimentos de O.Ps./O.Ss. |
| IndSmt | String(001) | Sim | Indica se o serviço é de manutenção de equipamentos |
| TelEiq | String(001) | Sim | Mostrar a tela de inspeções de movimentos de O.Ps. automaticamente |
| MovInp | String(001) | Sim | Indica se a O.P./O.S. pode ser movimentada com inspeções pendentes |
| SusInp | String(001) | Sim | Indica se a O.P./O.S. será suspensa quando houver inspeções não-conforme |
| ProImp | Number(002,0) | Sim | Indicativo do tipo de produto para impostos |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| ConIni | String(001) | Sim | Indica se as datas/horas de início dos apontamentos devem ser consistidos |
| InpSgq | String(001) | Sim | Tipo da inspeção da Qualidade |
| CtrVis | String(001) | Não | Controla valor individual da série |
| DatVis | Date | Sim | Data da última alteração do controle do valor individual da série |
| HorVis | Number(005,0) | Sim | Hora da última alteração do controle de valor individual da série |
| IndFrt | String(001) | Sim | Indicativo se a origem é de ferramentas |
| FrtEqp | String(001) | Sim | Indicativo se os Produtos/Ferramentas serão usadas como equipamentos para integração com manutenção |
| GrpFrt | String(004) | Sim | Código do grupo padrão de ferramentas/produtos |
| GerIpm | String(001) | Sim | [DEPRECADO] Indicativo se permite subdividir itens de pedidos para MRP |
| ObrDef | String(001) | Sim | Obriga informar os defeitos nos apontamentos de OPs |
| VarPro | String(001) | Sim | Indica o tipo de produto para o Varejo |
| FinOeo | String(001) | Não | Forma finalização estágio/operação (Automático - qtde real. X prev.; Manual) |
| ProMon | String(001) | Sim | Indicativo se o produto exige montagem |
| IndEca | String(001) | Sim | Indicativo se estorna componentes usados na fabricação automaticamente |
| VolAut | String(001) | Sim | Indicativo se deve gerar volumes automaticamente para o produto |
| IndIcp | String(001) | Sim | Indicativo se OPs da origem permitem a incorporação de produtos |
| CmpCob | String(001) | Sim | Indicativo se, por padrão, componentes de OS são cobrados |
| ModFab | String(001) | Sim | Modelo de Fabricação do produto para ficha técnica |
| TipFte | String(001) | Sim | Tipo de ficha técnica utilizada na geração do SPED Fiscal EFD |
| MomBxa | String(001) | Sim | Indica em que momento deve ser baixado os componentes da OP |
| FrmBxa | String(001) | Sim | Sugestão da forma de baixa de componentes podendo ser automática ou manual |
| IndEnc | String(001) | Sim | Indicativo se é um produto sob encomenda. |
| IndAco | String(001) | Sim | Indicativo se é ato cooperado. |
| IndM21 | String(001) | Sim | Indicativo se é um produto para gerar notas fiscais de saída no modelo 21 |
| FrmEsp | String(001) | Sim | Sugestão da forma de entrada do subproduto podendo ser automática ou manual |
| USU_numapt | String(003) | Sim | Nro para Apontamento de OP |
| USU_expcat | String(001) | Sim | Exportar catalogo |

---

## Chave Primária

- CodEmp
- CodOri

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
