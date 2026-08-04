# E075PRO

## Descrição

Cadastros - Produtos

---

## Resumo

- Campos: 311
- Chave Primária: 2 campo(s)
- Índices: 6
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| DesPro | String(100) | Não | Descrição usual do produto |
| CplPro | String(050) | Sim | Descrição complementar do Produto |
| DesNfv | String(099) | Sim | Descrição do produto para impressão na nota fiscal |
| CodFam | String(006) | Não | Código da Família do Produto |
| UniMed | String(003) | Não | Código da Unidade de Medida do produto p/ Estoque |
| UniMe2 | String(003) | Sim | Código da 2ª unidade de medida (utilizada na ficha técnica para tipo produzido) |
| UniMe3 | String(003) | Sim | Código da 3ª unidade de medida |
| TipPro | String(001) | Não | Tipo do produto |
| CodOri | String(003) | Não | Código de Origem do Produto |
| NumOri | Number(004,0) | Não | Número de Nível do Produto na Estrutura |
| CodMdp | String(008) | Sim | Código da Máscara de derivação que o produto pode utilizar |
| CodMod | String(014) | Sim | Código do Modelo p/ Produto Fabricado ou Montagem |
| CodRot | String(014) | Sim | Código do Roteiro de Produção p/ Produto Fabricado |
| CodAge | String(005) | Sim | Código de agrupamento de materiais/produtos para estoques |
| CodAgp | String(005) | Sim | Código de agrupamento de materiais/produtos para produção |
| CodAgu | String(005) | Sim | Código de agrupamento de materiais/produtos para custos |
| CodAgc | String(005) | Sim | Código de agrupamento de materiais/produtos para compras ou vendas |
| CodAgf | String(005) | Sim | Código de agrupamento de materiais/produtos para Impostos |
| CodClf | String(003) | Sim | Código interno da classificação fiscal do produto |
| CodStr | String(003) | Sim | Código da situação tributária do produto |
| PerIpi | Number(008,4) | Sim | Percentual de IPI válido para o produto |
| RecIpi | String(001) | Não | Indicativo se o Produto recupera ou não IPI |
| TemIcm | String(001) | Não | Indicativo se  o produto tem ou não ICMS |
| CodTic | String(003) | Sim | Código do ICMS Especial |
| CodTrd | String(003) | Sim | Código de redução de impostos |
| CodTst | String(003) | Sim | Código de ICMS Substituído |
| CodStp | String(003) | Sim | Código da substituição tributária do PIS |
| CodStc | String(003) | Sim | Código da substituição tributária do COFINS |
| RecIcm | String(001) | Não | Indicativo se o produto recupera ou não ICMS |
| CodRoy | Number(004,0) | Sim | Código de royalty |
| QtdMlt | Number(012,5) | Sim | Quantidade Múltipla para cálculo da geração de Ordem produção/compra |
| QtdMin | Number(012,5) | Sim | Quantidade Mínima para uma Ordem produção/compra |
| QtdMax | Number(012,5) | Sim | Quantidade Máxima para uma Ordem produção/compra |
| QtdGop | Number(012,5) | Sim | Quantidade Máxima para cada Guia de Produção (p/ não utilizar guias informe = 0) |
| BxaOrp | String(001) | Não | Se for componente de alguma OP, indica se o mesmo é baixado |
| CodPr2 | String(014) | Sim | Código do Produto associado para Entrada estoque 2ª qualidade |
| DerPr2 | String(007) | Sim | Código da Derivação  Produto p/ 2ª qualidade (se não informado assume 1ª qualidade) |
| CodPr3 | String(014) | Sim | Código do Produto associado para Entrada estoque 3ª qualidade |
| DerPr3 | String(007) | Sim | Código da Derivação Produto p/ 3ª qualidade (se não informado assume 1ª qualidade) |
| CodPr4 | String(014) | Sim | Código do Produto reaproveitado associado ao titular p/ entrada estoque sucatas/rebarbas/refugos na Produção |
| DerPr4 | String(007) | Sim | Código da Derivação do Produto reaproveitado (se não informado, então assume derivação do titular) |
| ProStq | String(001) | Sim | Produto é Utilizado para Estocar 2ª, 3ª Qualidade ou Reaproveitado (refugo) |
| SitPro | String(001) | Não | Situação do produto (Ativo ou Inativo) |
| RotPro | String(001) | Sim | Roteiro Informado é Utilizado p/ todas as Derivações do Produto (S=Sim, N=Não) |
| UsoCus | String(001) | Sim | Gerou Ficha de Custos (Produto Produzidos/Montagem) |
| IndMis | String(001) | Não | Indicativo que o produto é produzido mas também pode ser comprado (Misto) |
| IndVen | String(001) | Não | Indicativo se o produto pode ser vendido/faturado (item pedido e NF saída) |
| IndCpr | String(001) | Sim | Indicativo se o produto pode ser comprado. |
| IndReq | String(001) | Não | Indicativo se o produto pode ser requisitado (movimento estoque) |
| IndKit | String(001) | Não | Indicativo que o produto produzido é um "Kit" c/ vários produtos agregados p/ venda (não gera OP) |
| MatDir | String(001) | Não | Indicativo se o Material é Direto (produto comprado que é utilizado p/ fabricação de produtos produzidos) |
| ClaPro | Number(001,0) | Não | Classe do produto |
| IndPpc | String(001) | Não | Indicativo se o produto tem controle por cliente |
| IndFpr | String(001) | Não | Indicativo se a ligação de produto x fornecedor é usada p/ obter parâmetros fiscais |
| CodNtg | Number(004,0) | Sim | Código da natureza de gasto |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| CtaDcd | Number(007,0) | Sim | Conta contábil reduzida - 5 |
| CtaDci | Number(007,0) | Sim | Conta contábil reduzida - 6 |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pelo geração do registro |
| HorGer | Number(005,0) | Sim | Hora do cadastro do registro |
| DatGer | Date | Sim | Data do cadastro do registro |
| DepPad | String(010) | Sim | Depósito padrão p/ Produto |
| CtrVld | String(001) | Não | Indicativo da forma de controle da data de validade nos estoques |
| CtrLot | String(001) | Não | Controla Entrada/Saída no Estoque por  Lote |
| LotBas | String(001) | Sim | Lote base para geração de outro lote (lote componente -> lote produto OP) |
| CtrSep | String(001) | Não | Controla Entrada/Saídas no Estoque  por Série |
| QtdMve | Number(012,5) | Sim | Quantidade Múltipla para Vendas |
| CodRef | String(040) | Sim | Código da Referência |
| CodPin | String(020) | Sim | Código do Plano de Inspeção |
| NotFor | Number(005,2) | Sim | Nota mínima necessária para a aprovação de um fornecedor. |
| ExgCcl | String(001) | Sim | Indicativo se o produto exige certificado de classificação |
| EmiGtr | String(001) | Sim | Indicativo se é emitida a guia de tráfego para o produto |
| UsuAlt | Number(010,0) | Sim | Código do usuário responsável pelo alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| SomIim | String(001) | Sim | Indicativo se calcula ICMS importação nas notas fiscais de importação e ordens de compra |
| RecPis | String(001) | Sim | Indicativo se o produto recupera ou não PIS |
| TriPis | String(001) | Sim | Indicativo se o produto tem tributação de PIS ou não |
| TriCof | String(001) | Sim | Indicativo se o produto tem tributação de COFINS ou não |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para integração |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| ExpWms | Number(001,0) | Sim | Indicativo se o produto foi exportado para o sistema WMS |
| TipInt | Number(001,0) | Sim | Tipo de Integração |
| CodFif | String(010) | Sim | Código fiscal federal do produto |
| CodFie | String(060) | Sim | Código Fiscal Estadual |
| CodFim | String(010) | Sim | Código fiscal municipal do produto |
| RecCof | String(001) | Sim | Indicativo se as notas fiscais poderão ter recuperação de COFINS |
| SomIil | String(001) | Sim | Indicativo se deve ser somado o valor do ICMS no valor líquido das notas fiscais de importação e ordens de compra |
| CalDzf | String(001) | Sim | Indicativo se deve ser calculado o desconto Suframa para o produto nas entradas |
| UniPad | String(003) | Sim | U.M. padrão para movimentação de estoque manual |
| CodMar | String(010) | Sim | Código da Marca/Etiqueta do produto |
| CodClc | String(010) | Sim | Código da coleção do produto |
| CodAgm | String(005) | Sim | Código de agrupamento de materiais/produtos para preço |
| FilPrd | Number(005,0) | Sim | Código da filial de produção do produto |
| TolQmx | Number(005,3) | Sim | Tolerância da quantidade máxima defininida no produto |
| GerOrp | String(001) | Não | Indica se o produto gera ordem de produção. |
| CodPdv | Number(010,0) | Sim | Código interno no PDV |
| PerIrf | Number(004,2) | Sim | Percentual do IRRF previsto para venda do produto |
| PerPis | Number(004,2) | Sim | Percentual de PIS retido válido para o produto |
| PerCof | Number(004,2) | Sim | Percentual de COFINS retido válido para o produto |
| PerCsl | Number(004,2) | Sim | Percentual de CSLL válido para o produto |
| PerOur | Number(004,2) | Sim | Percentual de Outras Retenções válido para o produto |
| ConMon | String(001) | Sim | Considerar o produto produzido como montagem na busca da estrutura |
| PerFun | Number(004,2) | Sim | Percentual de Funrural do Produto para Notas Fiscais de Saídas |
| CodAga | String(005) | Sim | Código da forma de agrupamento para aprovação multinível |
| SomIps | String(001) | Sim | Indicativo se calcula PIS importação nas notas fiscais de importação e ordens de compra |
| SomIco | String(001) | Sim | Indicativo se calcula COFINS importação nas notas fiscais de importação e ordens de compra |
| SomIpl | String(001) | Sim | Indicativo se deve ser somado o valor do PIS no valor líquido das notas fiscais de importação e ordens de compra |
| SomIcl | String(001) | Sim | Indicativo se deve ser somado o valor do COFINS no valor líquido das notas fiscais de importação e ordens de compra |
| IndOct | String(001) | Sim | Indica se os produtos/serviços podem ser orçados |
| IndSpr | String(001) | Sim | Indicativo se Serviço é Produzido |
| CodEnd | String(020) | Sim | Código do endereçamento do produto |
| PesBru | Number(011,5) | Sim | Peso bruto do produto |
| PesLiq | Number(011,5) | Sim | Peso líquido do produto |
| TolPes | Number(005,3) | Sim | % tolerância do peso líquido do produto ou do lote |
| VolPro | Number(011,5) | Sim | Volume do produto |
| RotAnx | Number(002,0) | Sim | Código da rotina para controle de arquivos anexos |
| NumAnx | Number(010,0) | Sim | Número do controle de arquivos anexos gerado pelo sistema |
| ProImp | Number(002,0) | Sim | Indicativo do tipo de produto para impostos |
| BasRec | String(001) | Não | Base recálculo quantidade OP/componentes |
| CodAnp | Number(009,0) | Sim | Código de produto da ANP |
| ProEpe | Number(001,0) | Sim | Enquadramento de Produto Específico (Meramente informativo para NF-e) |
| CtrVis | String(001) | Não | Controla valor individual da série |
| DatVis | Date | Sim | Data da última alteração do controle do valor individual da série |
| HorVis | Number(005,0) | Sim | Hora da última alteração do controle de valor individual da série |
| IndFrt | String(001) | Sim | Indicativo se a origem é de ferramentas |
| FrtEqp | String(001) | Sim | Indicativo se as Ferramentas serão usadas como equipamentos |
| GrpFrt | String(004) | Sim | Código do grupo padrão de manutenção de ferramentas |
| ConEne | Number(002,0) | Sim | Classe de consumo de energia elétrica ou gás |
| ConAgu | Number(002,0) | Sim | Classe de fornecimento de água |
| TipLig | Number(002,0) | Sim | Tipo de ligação |
| GruTen | Number(002,0) | Sim | Código do grupo de tensão |
| TipMfr | String(001) | Sim | Tipo movimento da ferramenta na produção (Manual/Automático) |
| UniFrt | String(001) | Sim | Unidade de medida de utilização da ferramenta |
| CstIpi | String(002) | Sim | Código da situação tributária de IPI nas operações de venda |
| CstPis | String(002) | Sim | Código da situação tributária de PIS nas operações de venda |
| CstCof | String(002) | Sim | Código da situação tributária de COFINS nas operações de venda |
| TprPis | String(004) | Sim | Código da tabela de tributação para o cálculo de PIS por unidade de medida |
| TprCof | String(004) | Sim | Código da tabela de tributação para o cálculo de COFINS por unidade de medida |
| TprIpi | String(004) | Sim | Código da tabela de tributação para o cálculo de IPI por unidade de medida |
| RegTri | String(001) | Sim | Regime tributário de apuração da contribuição social |
| IdePro | String(020) | Sim | Identificação rápida do produto (para leitura de código de barras) |
| QtdAfe | Number(004,0) | Sim | Quantidade do produto a ser pesada para aferição (amostra) |
| IndAfe | String(001) | Sim | Tipo de aferição/conversão de peso |
| CstIpc | String(002) | Sim | Código da situação tributária de IPI nas operações de compra |
| CstPic | String(002) | Sim | Código da situação tributária de PIS nas operações de compra |
| CstCoc | String(002) | Sim | Código da situação tributária de COFINS nas operações de compra |
| OriMer | String(001) | Sim | Origem fiscal da mercadoria |
| NatPis | Number(005,0) | Sim | Natureza da receita do PIS |
| NatCof | Number(005,0) | Sim | Natureza da receita do COFINS |
| LarPro | Number(011,5) | Sim | Largura do produto |
| AltPro | Number(011,5) | Sim | Altura do produto |
| ComPro | Number(011,5) | Sim | Comprimento do produto |
| BasCre | Number(002,0) | Sim | Código da base de cálculo do crédito |
| ProMon | String(001) | Sim | Indicativo se o produto exige montagem |
| ProEnt | String(001) | Sim | Indicativo se o produto exige ser entregue |
| VarPro | String(001) | Sim | Indica o tipo de produto para comércio |
| ProFol | String(001) | Sim | Indicativo se o produto está fora de linha e não pode sofrer reposição externa |
| ProVes | String(001) | Sim | Indicativo se o produto pode ser vendido separadamente |
| QtdVol | Number(004,0) | Sim | Quantidade de volumes para compor o produto |
| ExiNfe | String(001) | Sim | Indicativo se o produto exige que seja emitido uma NF-e no momento da venda |
| PrzRec | Number(004,0) | Sim | Prazo de recuperação para oferecer a garantia estendida após a venda |
| UniWms | String(003) | Sim | Unidade de medida para o controle de estoque (acondicionamento) no WMS. |
| FinCrp | Number(007,0) | Sim | Conta financeira de receita(saída) padrão para efeito de rateio |
| FinCdp | Number(007,0) | Sim | Conta financeira de despesa(entrada) padrão para efeito de rateio |
| PerPim | Number(008,4) | Sim | Percentual de PIS de importação diferenciado |
| PerCim | Number(008,4) | Sim | Percentual de COFINS de importação diferenciado |
| IteFis | String(060) | Sim | Código fiscal do item |
| DesFis | String(255) | Sim | Descrição fiscal do item |
| CodAgg | String(005) | Sim | Código do agrupamento para garantia estendida |
| ParCom | String(001) | Sim | Indicativo se o produto é participante do processo de comissão |
| TmpDse | Number(009,0) | Sim | Tempo limite de desuso sugerido para as séries da ferramenta (em dias) |
| IndIcp | String(001) | Sim | Indicativo se OPs do produto permitem a incorporação de produtos |
| LimIcp | Number(004,0) | Sim | Percentual limite de incorporação de produtos na OP |
| CodIcl | Number(004,0) | Sim | Código do item de classificação para melhoria de PH |
| MotDes | Number(002,0) | Sim | Motivo desoneração ICMS |
| PerSen | Number(004,2) | Sim | Percentual do imposto SENAR/SENAT do produto para notas fiscais de saídas |
| CodBic | String(003) | Sim | Código da modalidade da base de cálculo do ICMS |
| AgrCcr | String(001) | Sim | Controle de crédito de ICMS para o agronegócio |
| AgrQcr | Number(003,0) | Sim | Quantidade de meses para recuperação do crédito do ICMS do agronegócio |
| ZesSba | String(001) | Sim | Indicativo se deve zerar o estoque nas saídas via balança |
| IndVol | String(001) | Sim | Indicativo se é usado como volume (sugestão para as derivações) |
| ImpScf | String(001) | Sim | Imprime série no cupom fiscal independente de controle por série |
| CodCor | Number(004,0) | Sim | Código da Cor |
| VltPro | Number(001,0) | Sim | Voltagem do produto |
| PerGas | Number(007,4) | Sim | Percentual de Gás Natural Nacional - GLGNn para o produto GLP |
| UniBcp | String(003) | Sim | Código da Unidade de Medida Base para cálculo de preço |
| PerDif | Number(007,4) | Sim | Percentual de diferimento do produto |
| ModFab | String(001) | Sim | Modelo de Fabricação do produto para ficha técnica |
| TipFte | String(001) | Sim | Tipo de ficha técnica utilizada na geração do SPED Fiscal EFD |
| CodPri | String(004) | Sim | Código da tabela de presunção IRPJ |
| CodPrc | String(004) | Sim | Código da tabela de presunção CSLL |
| EmiRec | String(001) | Sim | Indicativo se o produto exige que seja emitida receita agronômica |
| IdePar | String(100) | Sim | Código de identificação do parceiro |
| CodEnq | Number(003,0) | Sim | Código de enquadramento legal do IPI |
| CodCes | String(007) | Sim | Código especificador da substituição tributária |
| TipCic | Number(001,0) | Sim | Tipo de Crédito ICMS |
| FicCat | Number(002,0) | Sim | Ficha CAT 83/09 |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| IndEnc | String(001) | Sim | Indicativo se é um produto sob encomenda. |
| TprPii | String(004) | Sim | Código da tabela de tributação para o cálculo do PIS Importação por unidade de medida |
| TprCoi | String(004) | Sim | Código da tabela de tributação para o cálculo do COFINS Importação por uni. de medida |
| PerIfp | Number(004,2) | Sim | Percentual do IRRF para Empresa Pública ou equiparada do Produto. |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |
| AprAgr | String(001) | Sim | Indica se deve apresentar a produção de forma agrupada na apuração do bloco K |
| IndAco | String(001) | Sim | Indicativo se é ato cooperado. |
| IntZfm | String(001) | Sim | Identificará se está sujeito ao processo de internação na ZFM. |
| ProDci | String(001) | Sim | Identificará o tipo do produto para a DCI. |
| IdeMia | Number(009,0) | Sim | Identificador dos Multiplicadores |
| UtiDum | String(001) | Sim | Indica se a integração do BlocoK usa a quantidade de casas decimais do cadastro |
| PerDii | Number(007,4) | Sim | Percentual de desconto ICMS importação |
| AdmTmp | String(001) | Sim | Indica se o produto deve calcular admissão temporária de tributos de importação |
| ClaAlc | Number(002,0) | Sim | Classificação do produto para a produção de açúcar e álcool |
| CiaTst | String(003) | Sim | Código de ICMS Antecipação |
| PerGlp | Number(007,4) | Sim | Percentual do GLP derivado do petróleo no produto GLP |
| PerGni | Number(007,4) | Sim | Percentual de Gás Natural Importado - GLGNi para o produto GLP |
| DesAnp | String(095) | Sim | Descrição do produto conforme ANP |
| VlrPar | Number(015,2) | Sim | Valor de partida (por quilograma sem ICMS) |
| ClaCni | Number(004,0) | Sim | Classificação Convênio ICMS 115/2013 |
| TipUti | Number(002,0) | Sim | Tipo de utilização |
| OriGti | Number(001,0) | Sim | Forma de busca do código GTIN para gerar as tags cEAN e cEANTrib |
| CatPro | String(050) | Sim | Código da Categoria vinculada a um produto |
| GruIst | String(001) | Sim | Indica se deve gerar o grupo de Repasse de ICMS ST na NF-e mesmo com CST 60 |
| PerGil | Number(004,2) | Sim | Percentual de GILRAT - Grau Incid. Incapac. Laborat. Decor. Riscos Amb. de Trab. |
| IndVma | String(001) | Sim | Indicativo se o valor do imposto deve ser calculado considerando a tabela de valor mínimo por unidade de medida |
| ProCsg | String(001) | Sim | Indicativo se o produto é consignado |
| TipPbk | String(001) | Sim | Tipo de produção |
| IdeRen | Number(009,0) | Sim | Identificador do Registro da Natureza de Rendimento |
| NatRen | String(009) | Sim | Natureza Rendimentos |
| TipRes | Number(002,0) | Sim | Tipo de Resíduo Produzido |
| Art119 | String(001) | Sim | NCM enquadrada no art. 119 do RICMS/2017 do Paraná |
| ClaCat | String(250) | Sim | Classificação da categoria |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| UniMet | String(003) | Sim | Código da Unidade de Medida de Medida para Etiqueta |
| FatCet | Number(007,4) | Sim | Fator de Conversão para Etiqueta |
| ColIsi | String(001) | Sim | Considerar no I-Simp |
| DisCol | String(001) | Sim | Dispensa Coleta (I-Simp) |
| TipGti | Number(001,0) | Sim | Tipo de código GTIN |
| TprImo | String(004) | Sim | Código Tabela tributação ICMS Monofásico |
| ProMis | String(014) | Sim | Produto Misturado |
| PerMis | Number(007,4) | Sim | Índice de Mistura |
| TipCbt | Number(002,0) | Sim | Tipo de Combustível |
| CalFaf | String(001) | Sim | Indicativo se deve ser calculado o fator de ajuste de fruição |
| ProSuf | String(012) | Sim | Número do processo na Suframa para CBS zero |
| USU_ccudes | String(010) | Sim | Centro Custo Destino |
| USU_necprn | String(001) | Sim | Nec. por prev. |
| USU_prores | String(001) | Sim | Reestruturado |
| USU_resrev | String(020) | Sim | Resp. Revisao |
| USU_datrev | Date | Sim | Data Revisao |
| USU_revdes | String(005) | Sim | Revisao Desenho |
| USU_fordes | String(030) | Sim | Formato Desenho |
| USU_finame | Number(007,0) | Sim | Finame |
| USU_itemgav | Number(003,0) | Sim | Item na Gaveta |
| USU_gaveta | Number(003,0) | Sim | Numero da Gaveta |
| USU_dersub | String(007) | Sim | Der. Subst. ICMS |
| USU_prdctl | String(001) | Sim | Produto Controlado Qualidade |
| USU_letra | String(002) | Sim | Letra que esta no Catalogo |
| USU_usuexped | String(001) | Sim | Usa na Expedicao |
| USU_pagina | Number(005,0) | Sim | Pagina do Catalogo |
| USU_pecpro | String(030) | Sim | Para que Produto e a Peca |
| USU_prosub | String(040) | Sim | Desenho Referente ao Codigo de Produto Substituto |
| USU_indpep | String(001) | Sim | Indica Usa Producao |
| USU_proctl | String(001) | Sim | Produto Controlado |
| USU_codcli | String(014) | Sim | Codigo da Peca do Cliente |
| USU_INDCPA | String(001) | Sim | Indica Comprado |
| USU_MedCorte | String(040) | Sim | Medida de Corte da Peca |
| USU_exppro | String(001) | Sim | Exportar catalogo |
| USU_codfot | String(020) | Sim | USU_codfot |
| USU_codlin | String(010) | Sim | Linha Producao |
| USU_observ | String(120) | Sim | Observacao Nao Pode ser Vendido |
| USU_desorp | String(006) | Sim | Destino OP |
| USU_despcs | String(006) | Sim | Destino pecas produzidas |
| USU_nrchap | String(015) | Sim | Numero da Chapelona |
| USU_subgru | Number(004,0) | Sim | Sub-Grupo de Implementos |
| USU_CodSig | String(050) | Sim | Sigla da Legenda |
| USU_prudD012 | Number(002,0) | Sim | Produzir D 0 D -1 D -2 |
| USU_Kanban | String(001) | Sim | Peca Controladas por KanBan |
| USU_codpra | Number(003,0) | Sim | Prateleira |
| USU_codpos | Number(003,0) | Sim | Posicao |
| USU_filasup | Number(003,0) | Sim | Rua Supermercado |
| USU_codniv | String(001) | Sim | Nivel |
| USU_codcel | Number(004,0) | Sim | Código Célula |
| USU_lado | String(001) | Sim | Lado Rua |
| USU_DatCadEmb | Date | Sim | Data de Cadastramento de Embalagem no MWS-Toledo |
| USU_TipApa | String(001) | Sim | Tipo Aparafusado |
| USU_SeqCelPrd | Number(007,0) | Sim | Sequência de célula de produção |
| USU_GruCelPrd | String(020) | Sim | Grupo de Célula de Produção |
| USU_CelAlt | Number(004,0) | Sim | Código célula alternativa |
| USU_GruCelAlt | String(020) | Sim | Grupo de Célula de Produção Alternativo |
| USU_SeqCelAlt | Number(007,0) | Sim | Sequência de célula de produção Alternativa |
| USU_UsuCpr | Number(010,0) | Sim | Usuário responsável pela compra do item solicitado |
| USU_CapPro | String(020) | Sim | Capacidade do Produto |
| USU_CodAgl | String(005) | Sim | Agrupamento para Logística |
| USU_GrpReg | Number(003,0) | Sim | WMS - Grupo Região para Logística (armazenamento) |
| USU_FrqCmp | Number(003,0) | Sim | Frequência de Compra |
| USU_IndRes | String(001) | Sim | Indica se o Produto é Restritivo para o Drummer (S/N) |
| USU_DESCOM | String(120) | Sim | Título para Sites |
| USU_DESMET | String(200) | Sim | Descrição (Meta Tag Description) |
| USU_ObsPro | String(150) | Sim | Observação do Produto |
| USU_GRUCPR | Number(010,0) | Sim | Grupo de Compras |
| USU_CodSuc | String(014) | Sim | Codigo da Sucata |
| USU_CODPLR | String(010) | Sim | Código do Pilar |
| USU_SUBPLR | String(010) | Sim | Código do Sub Pilar |
| USU_Aal | String(011) | Sim | Número AAL |

---

## Chave Primária

- CodEmp
- CodPro

---

## Índices

### E075PROIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- TipPro

### E075PROIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFam

### E075PROIndice3

**Tipo:** Não unico

Campos:
- UniMed

### E075PROIndice4

**Tipo:** Não unico

Campos:
- CodEmp
- CodOri

### USU_E075PRO1

**Tipo:** Não unico

Campos:
- CodPro
- CodOri
- CodFam
- TipPro

### USU_E075PRO2

**Tipo:** Não unico

Campos:
- CodEmp
- TipPro
- CodPro

---

## Relacionamentos

### IR_E075PRO_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E075PRO_005

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

### IR_E075PRO_006

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

### IR_E075PRO_010

**Tabela:** E083ORI

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |

