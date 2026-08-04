# E120IPD

## Descrição

Vendas - Pedidos - Itens de Produto

---

## Resumo

- Campos: 282
- Chave Primária: 4 campo(s)
- Índices: 6
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqIpd | Number(004,0) | Não | Sequência de item do pedido |
| TnsPro | String(005) | Sim | Transação do item de produto do pedido |
| PedCli | String(020) | Sim | Número do pedido do cliente |
| SeqPcl | String(010) | Sim | Sequência do item no pedido do cliente |
| PedPrv | String(001) | Não | Indicativo se o pedido é de previsão |
| CodPro | String(014) | Sim | Código do produto do pedido |
| CodDer | String(007) | Sim | Código da derivação do produto do pedido |
| CplIpd | String(250) | Sim | Complemento da descrição do produto |
| CodFam | String(006) | Sim | Código da Família do Produto |
| CodAgr | Number(004,0) | Sim | Código de agrupamento para derivação |
| CodTic | String(003) | Sim | Código do ICMS especial |
| CodTrd | String(003) | Sim | Código de redução de impostos |
| CodTst | String(003) | Sim | Código do ICMS substituído |
| CodStp | String(003) | Sim | Código de substituição do PIS |
| CodStc | String(003) | Sim | Código de substituição do COFINS |
| CodDep | String(010) | Sim | Código do depósito a ser baixado o estoque do produto do pedido |
| CodLot | String(050) | Sim | Código do lote de fabricação do produto |
| ResEst | String(001) | Não | Indicativo se o estoque do produto do pedido deve ser reservado |
| QtdPed | Number(014,5) | Não | Quantidade do produto do pedido |
| QtdAen | Number(014,5) | Sim | Quantidade do item do pedido a entregar |
| QtdPoc | Number(014,5) | Sim | Quantidade do produto do pedido a ser produzida ou comprada |
| QtdFat | Number(014,5) | Sim | Quantidade faturada do produto do pedido |
| QtdCan | Number(014,5) | Sim | Quantidade cancelada do produto do pedido |
| QtdAbe | Number(014,5) | Sim | Quantidade em aberto do produto do pedido |
| QtdRae | Number(014,5) | Sim | Quantidade do produto reservado pela análise de embarque |
| QtdNlp | Number(014,5) | Sim | Quantidade Líquida a Produzir após avaliação do Disponível do Estoque |
| QtdRes | Number(014,5) | Sim | Quantidade Reservada no Estoque (p/ cálculo do disponível) |
| UniMed | String(003) | Não | Unidade de medida do produto |
| CodMcp | String(003) | Sim | Moeda ou índice para correção do preço unitário |
| DatMfp | Date | Sim | Data da cotação da moeda para o fechamento do pedido |
| CotMfp | Number(019,10) | Sim | Valor da cotação da moeda para o fechamento do pedido |
| DatMoe | Date | Sim | Data da cotação da moeda para o faturamento do produto |
| CotMoe | Number(019,10) | Sim | Valor da cotação da moeda para o faturamento do produto |
| FecMoe | String(001) | Sim | Indicativo de o valor da cotação para o faturamento do produto é fechado |
| CodTpr | String(004) | Sim | Código da tabela de preço do produto do pedido |
| PreUni | Number(021,10) | Sim | Preço unitário do produto do pedido |
| CodMoe | String(003) | Sim | Código da moeda/índice que o preço unitário está representado |
| PreFix | String(001) | Não | Indicativo se o preço é fixo |
| PerDsc | Number(005,2) | Sim | Percentual de desconto para o produto do pedido |
| PerOfe | Number(010,5) | Sim | Percentual de oferta para o produto do pedido |
| PerAcr | Number(010,5) | Sim | Percentual de acréscimo para o produto do pedido |
| PerIpi | Number(008,4) | Sim | Percentual de IPI do produto do pedido |
| PerIcm | Number(005,2) | Sim | Percentual de ICM do produto do pedido |
| PerCom | Number(005,2) | Sim | Percentual de comissão sobre o produto do pedido |
| DatEnt | Date | Não | Data de previsão de entrega para o produto do pedido |
| DatAne | Date | Não | Data de entrega para análise de embarque |
| DatPoc | Date | Não | Data de previsão de entrega do produto  para considerar na Produção |
| CodPvp | String(008) | Sim | Código do período de vendas/produção |
| NumPrj | Number(008,0) | Sim | Número do projeto |
| CodFpj | Number(004,0) | Sim | Código da fase do projeto |
| CtaFin | Number(007,0) | Sim | Conta financeira reduzida |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| CodCcu | String(009) | Sim | Código do centro de custo |
| VlrFre | Number(015,2) | Sim | Valor frete |
| VlrSeg | Number(015,2) | Sim | Valor seguro |
| VlrEmb | Number(015,2) | Sim | Valor embalagem |
| VlrEnc | Number(015,2) | Sim | Valor encargos financeiros |
| VlrOut | Number(015,2) | Sim | Valor outras despesas |
| VlrDar | Number(015,2) | Sim | Valor para arredondamento |
| VlrFrd | Number(015,2) | Sim | Valor frete destacado |
| VlrOud | Number(015,2) | Sim | Valor outras despesas destacado |
| VlrBru | Number(015,2) | Sim | Valor bruto do produto do pedido |
| VlrDsc | Number(015,2) | Sim | Valor do desconto para o produto do pedido |
| VlrDs1 | Number(015,2) | Sim | Valor do desconto - 1 do cliente |
| VlrDs2 | Number(015,2) | Sim | Valor do desconto - 2 do cliente |
| VlrDs3 | Number(015,2) | Sim | Valor do desconto - 3 do cliente |
| VlrDs4 | Number(015,2) | Sim | Valor do desconto - 4 do cliente |
| VlrOfe | Number(015,2) | Sim | Valor do desconto de Oferta |
| VlrDzf | Number(015,2) | Sim | Valor do desconto referente zona franca |
| VlrBip | Number(015,2) | Sim | Valor base IPI |
| VlrIpi | Number(015,2) | Sim | Valor do IPI para o produto do pedido |
| VlrBic | Number(015,2) | Sim | Valor Base ICMS |
| VlrIcm | Number(015,2) | Sim | Valor do ICMS |
| VlrBsi | Number(015,2) | Sim | Valor base ICMS substituído |
| VlrIcs | Number(015,2) | Sim | Valor do ICMS Substituído para o produto do pedido |
| VlrBsp | Number(015,2) | Sim | Valor base da substituição tributária do PIS |
| VlrStp | Number(015,2) | Sim | Valor da substituição Tributária do PIS |
| VlrBsc | Number(015,2) | Sim | Valor base da substituição tributária da COFINS |
| VlrStc | Number(015,2) | Sim | Valor da substituição Tributária da COFINS |
| VlrBco | Number(015,2) | Sim | Valor base comissão |
| VlrCom | Number(015,2) | Sim | Valor comissão |
| VlrLpr | Number(015,2) | Sim | Valor do produto |
| VlrLou | Number(015,2) | Sim | Valor dos outros valores |
| VlrLiq | Number(015,2) | Sim | Valor líquido do item de produto do pedido |
| VlrFin | Number(015,2) | Sim | Valor válido para o financeiro |
| SitIpd | Number(001,0) | Não | Situação do item do pedido |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do item de produto |
| ObsMot | String(250) | Sim | Observação do motivo da situação do item de produto |
| GerNec | Number(001,0) | Não | Indicativo de geração de necessidades para efeito de produção |
| GerCga | String(001) | Não | Indicativo se gerou Carga de Recursos p/ o Pedido |
| ResMan | String(001) | Não | Indicativo se o Pedido foi Reservado Manualmente |
| IndAed | String(001) | Não | Indicativo se usou a opção de abater o estoque Disponível no Cálculo de Necessidades da Produção |
| NumCtr | Number(006,0) | Sim | Número de Controle |
| DatCpt | Date | Sim | Mês e ano de competência do controle |
| SeqCvp | Number(004,0) | Sim | Sequência do item principal que originou este item (pela estrutura do produto montado ou KIT) |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| QtdPpf | Number(014,5) | Sim | Quantidade do item que está em Pré-Fatura. |
| CmpKit | String(001) | Não | Indica se o componente é uma composição de Kit |
| FilOcp | Number(005,0) | Sim | Código da filial da Ordem de Compra |
| NumOcp | Number(008,0) | Sim | Número da ordem de compra |
| SeqIpo | Number(004,0) | Sim | Sequência de item da ordem de compra |
| UniVen | String(003) | Sim | Unidade de medida de venda do item de produto |
| QtdVen | Number(014,5) | Sim | Quantidade do produto na unidade de medida de venda do item |
| PreVen | Number(021,10) | Sim | Preço unitário do produto na unidade de medida de venda do item |
| PreBru | Number(021,10) | Sim | Preço unitário Bruto do produto do pedido |
| FilCtr | Number(005,0) | Sim | Código da filial do contrato de venda |
| CtrCvs | Number(009,0) | Sim | Número do contrato de serviço que gerou o item de produto |
| CptCvs | Date | Sim | Mês e ano de competência do item de serviço que gerou o item de produto |
| SeqCvs | Number(003,0) | Sim | Sequência do item de serviço do contrato que gerou o item do pedido |
| CodAvc | Number(009,0) | Sim | Código da Análise Valorizada de Custos |
| CodFxa | String(015) | Sim | Código da faixa da grade |
| CodPgr | String(005) | Sim | Código da Proporcionalidade da Grade de Derivações |
| IdxGrd | Number(006,0) | Sim | Indexador da Grade |
| CodMar | String(010) | Sim | Código da Marca/Etiqueta vinculada ao item do pedido |
| CodClc | String(010) | Sim | Código da coleção do item de pedido |
| PerDs1 | Number(005,2) | Sim | Percentual de desconto - 1 do cliente |
| PerDs2 | Number(005,2) | Sim | Percentual de desconto - 2 do cliente |
| PerDs3 | Number(005,2) | Sim | Percentual de desconto - 3 do cliente |
| PerDs4 | Number(005,2) | Sim | Percentual de desconto - 4 do cliente |
| FilPrd | Number(005,0) | Sim | Código da filial de produção do item de produto |
| VlrRis | Number(015,2) | Sim | Valor de retenção de ICMS Substituto |
| IndPce | String(001) | Sim | Indicativo de controle, se existe uma Estrutura de Pedido com componentes configurados |
| IndPcr | String(001) | Sim | Indicativo de controle, se tem Roteiro Produção p/ Pedido com operações configuradas |
| PerPit | Number(004,2) | Sim | Percentual de PIS Retido |
| VlrBpt | Number(015,2) | Sim | Valor base do PIS Retido |
| VlrPit | Number(015,2) | Sim | Soma dos valores do PIS retido |
| PerCrt | Number(004,2) | Sim | Percentual de Cofins Retido |
| VlrBct | Number(015,2) | Sim | Valor base do Cofins Retido |
| VlrCrt | Number(015,2) | Sim | Valor do Cofins Retido |
| PerCsl | Number(004,2) | Sim | Percentual de CSLL Retido |
| VlrBcl | Number(015,2) | Sim | Valor base do CSLL Retido |
| VlrCsl | Number(015,2) | Sim | Valor do CSLL  Retido |
| PerOur | Number(004,2) | Sim | Percentual de Outras Retenções |
| VlrBor | Number(015,2) | Sim | Valor base de Outras Retenções |
| VlrOur | Number(015,2) | Sim | Valor de Outras Retenções |
| PerIrf | Number(004,2) | Sim | Percentual do IRRF |
| VlrBir | Number(015,2) | Sim | Valor base IRRF |
| VlrIrf | Number(015,2) | Sim | Valor do IRRF |
| FilNfc | Number(005,0) | Sim | Código da filial da nota fiscal de entrada gerada pelo item de pedido |
| ForNfc | Number(009,0) | Sim | Código do fornecedor da nota fiscal de entrada gerada pelo item de pedido |
| NumNfc | Number(009,0) | Sim | Número da nota fiscal de entrada gerada pelo item de pedido |
| SnfNfc | String(003) | Sim | Código da série da nota fiscal de entrada gerada pelo item de pedido |
| SeqIpc | Number(003,0) | Sim | Sequência do item na nota fiscal de entrada gerado pelo item de pedido |
| NctLcl | String(020) | Sim | Número de controle de lote do cliente |
| NreCli | String(020) | Sim | Número de remessa do cliente |
| NosIcl | Number(010,0) | Sim | Número de ordem de serviço inicial do cliente |
| NosFcl | Number(010,0) | Sim | Número de ordem de serviço final do cliente |
| NocCl1 | String(020) | Sim | Número de ordem de compra 1 do cliente |
| NocCl2 | String(020) | Sim | Número de ordem de compra 2 do cliente |
| NocCl3 | String(020) | Sim | Número de ordem de compra 3 do cliente |
| CodAgc | String(005) | Sim | Código de agrupamento de produtos para comercial |
| CtrCvp | Number(009,0) | Sim | Número do contrato de produto que gerou o item de produto |
| CptCvp | Date | Sim | Mês e ano de competência do item de produto que gerou o item de produto |
| SeqCtr | Number(003,0) | Sim | Sequência do item de produto do contrato que gerou o item do pedido |
| IndApe | Number(001,0) | Sim | Indicativo da análise do item de pedido pela engenharia |
| ObsIpd | String(999) | Sim | Observação do item de produto do Pedido |
| SeqIsp | Number(003,0) | Sim | Seqüência do item de serviço no pedido (usado para indicar para qual item de serviço o item do pedido pertence) |
| EmpOcp | Number(004,0) | Sim | Código da empresa da ordem de compra |
| VlrBpf | Number(015,2) | Sim | Valor Base do PIS Faturamento |
| PerPif | Number(008,4) | Sim | Percentual do PIS Faturamento |
| VlrPif | Number(015,2) | Sim | Valor do PIS Faturamento |
| VlrBcf | Number(015,2) | Sim | Valor Base do COFINS Faturamento |
| PerCff | Number(008,4) | Sim | Percentual do COFINS Faturamento |
| VlrCff | Number(015,2) | Sim | Valor do COFINS Faturamento |
| PerDs5 | Number(005,2) | Sim | Percentual de desconto - 5 do cliente |
| VlrDs5 | Number(015,2) | Sim | Valor do desconto - 5 do cliente |
| AgrNec | String(025) | Sim | Agrupamento de necessidades |
| AgrPai | String(025) | Sim | Agrupamento de necessidades pai |
| OriRes | String(001) | Sim | Origem da reserva |
| QtdBpf | Number(015,3) | Sim | Quantidade da base do PIS por faturamento |
| AliPif | Number(015,4) | Sim | Alíquota por Valor do PIS por faturamento |
| QtdBcf | Number(015,3) | Sim | Quantidade da base do COFINS por faturamento |
| AliCff | Number(015,4) | Sim | Alíquota por Valor do COFINS por faturamento |
| QtdBip | Number(015,3) | Sim | Quantidade da base do IPI |
| AliIpi | Number(015,4) | Sim | Alíquota por Valor do IPI |
| IndIpm | String(001) | Sim | Indicativo se o item pedido foi dividido para cálculo MRP |
| FilRem | Number(005,0) | Sim | Código da filial |
| SnfRem | String(003) | Sim | Código da série da nota fiscal de saída |
| NfvRem | Number(009,0) | Sim | Número da nota fiscal de saída |
| IpvRem | Number(003,0) | Sim | Sequência do item na nota fiscal de saída |
| CodCnv | Number(004,0) | Sim | Código do convênio |
| CodRep | Number(009,0) | Sim | Código do representante |
| ProMon | String(001) | Sim | Indicativo se o produto exige montagem |
| ProEnt | String(001) | Sim | Indicativo se o produto exige ser entregue |
| PerMgc | Number(014,5) | Sim | Percentual de Margem de Contribuição utilizada para a venda |
| VarSer | String(001) | Sim | Indica o tipo de serviço para o Varejo |
| RetMat | String(001) | Sim | Indicaivo se o produto será retirado no depósito da matriz pelo cliente |
| SenApr | String(050) | Sim | Senha para liberação da pendência de aprovação |
| UsuApr | Number(010,0) | Sim | Usuário responsável pela aprovação |
| DatApr | Date | Sim | Data da aprovação do registro |
| HorApr | Number(005,0) | Sim | Hora da aprovação do registro |
| TipCur | Number(001,0) | Sim | Indicativo do tipo de curso online para varejo |
| CodFin | Number(004,0) | Sim | Código da finalidade de venda |
| CodBar | String(050) | Sim | Código de barras do volume inserido no pedido |
| IndBrd | String(001) | Sim | Indicativo se o item é um brinde promocional |
| BrdMan | String(001) | Sim | Indicativo se o item é um brinde inserido manualmente pelo vendedor |
| DscPrm | String(001) | Sim | Indicativo se o item é um beneficio de promocao com desconto no valor |
| PerJur | Number(005,2) | Sim | Percentual de juros aplicado ao item para a geração das parcelas |
| PerDif | Number(007,4) | Sim | Percentual de diferimento do item de produto |
| BasIdf | Number(015,2) | Sim | Valor base do ICMS diferido |
| PerIdf | Number(005,2) | Sim | Percentual do ICMS diferido do item do pedido |
| VlrIdf | Number(015,2) | Sim | Valor do ICMS diferido do item do pedido |
| CodStr | String(003) | Sim | Situação tributária do I.C.M.S do item do pedido |
| FilNco | Number(005,0) | Sim | Código da filial da nota de cobrança |
| SnfNco | String(003) | Sim | Código da série da nota fiscal de cobrança |
| NumNco | Number(009,0) | Sim | Número da nota fiscal de cobrança |
| SeqNco | Number(003,0) | Sim | Sequência do item na nota fiscal de cobrança |
| MotDes | Number(002,0) | Sim | Motivo desoneração ICMS |
| VlrIcd | Number(015,2) | Sim | ICMS Desonerado |
| SeqRem | Number(010,0) | Sim | Sequência da receita agronômica |
| NumRec | Number(009,0) | Sim | Número da receita |
| SeqRei | Number(010,0) | Sim | Sequência do item |
| IcmAor | Number(005,2) | Sim | Alíquota de ICMS partilhado com o estado remetente |
| IcmVor | Number(015,2) | Sim | Valor de ICMS partilhado com o estado remetente |
| IcmAde | Number(005,2) | Sim | Alíquota de ICMS partilhado com o estado destinatário |
| IcmVde | Number(015,2) | Sim | Valor de ICMS partilhado com o estado destinatário |
| IcmBde | Number(015,2) | Sim | Valor Base ICMS partilha para estado de destino |
| IcmAfc | Number(007,4) | Sim | Alíquota do ICMS para fundo de combate à pobreza na UF de destino |
| IcmVfc | Number(015,2) | Sim | Valor do ICMS para fundo de combate à pobreza na UF de destino |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| VlrTot | Number(015,2) | Sim | Valor total antes de liquidar. Usado no Varejo Terceiros |
| IteCan | String(001) | Sim | Indicativo se o item foi cancelado antes do faturamento (Varejo Terceiros) |
| DscVar | Number(015,2) | Sim | Valor do desconto para o produto do pedido. Usado no Varejo Terceiros |
| AcrVar | Number(015,2) | Sim | Valor do acréscimo para o produto do pedido. Usado no Varejo Terceiros |
| PdsVar | Number(005,2) | Sim | Percentual de desconto para o produto do pedido. Usado no Varejo Terceiros |
| PacVar | Number(010,5) | Sim | Percentual de acréscimo para o produto do pedido. Usado no Varejo Terceiros |
| FilOri | Number(005,0) | Sim | Código da filial de origem da mercadoria |
| ObsEnt | String(250) | Sim | Observações para entrega do produto |
| ForEnt | String(001) | Sim | Forma de entrega do item de pedido |
| NumInt | String(020) | Sim | Número do Documento Externo (Integrado) |
| CmpMtg | String(001) | Sim | Indica se é um componente de um produto montagem |
| IcmBfc | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza na UF de destino |
| BasFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza |
| AliFcp | Number(007,4) | Sim | Alíquota do ICMS para fundo de combate à pobreza |
| VlrFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza |
| BstFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza retido por substituição tributária |
| AstFcp | Number(007,4) | Sim | Alíquota do fundo de combate à pobreza retido por substituição tributária |
| VstFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza retido por substituição tributária |
| VicStd | Number(015,2) | Sim | Valor do ICMS-ST desonerado |
| MtdIst | Number(002,0) | Sim | Motivo desoneração ICMS-ST |
| USU_asttec | Number(003,0) | Sim | Controle Asistencia Tecnica |
| USU_vlrcusprod | Number(013,2) | Sim | Valor Custo Producao |
| USU_vendaliq | Number(013,2) | Sim | Venda Liquida |
| USU_vlrcomi | Number(011,2) | Sim | Valor da Comissao |
| USU_vlrdesp | Number(011,2) | Sim | Valor da Despesas |
| USU_vlrcofins | Number(011,2) | Sim | Valor do Cofins |
| USU_vlrpis | Number(011,2) | Sim | Valor do Pis |
| USU_vlricms | Number(011,2) | Sim | Valor do Icms |
| USU_vlrcpmf | Number(011,2) | Sim | Valor CPMF |
| USU_observ | String(250) | Sim | Observacao Lucro |
| USU_recliqven | Number(013,2) | Sim | Rec.Liquida Venda |
| USU_recbruta | Number(013,2) | Sim | Receita Bruta |
| USU_perclucro | Number(007,2) | Sim | Percentual Lucro |
| USU_indimpl | String(001) | Sim | Indica Nec. Expl.Junto com Implementos |
| USU_numpri | Number(004,0) | Sim | Numero Prioridade |
| USU_ccucausa | String(009) | Sim | Centro de Custo Causador de problemas na producao |
| USU_datlibpav | Date | Sim | Data liberacao pecas avulsas |
| USU_IndAtd | String(001) | Sim | Indicativo se Avalia Todos os Depósitos |
| USU_StsCel | String(001) | Sim | Status de impressão - Controle eletrônico |
| USU_CtrOri | Number(001,0) | Sim | Controle do Comercial da origem de um produto |
| USU_CodEsp | Number(002,0) | Sim | Codigo de Espaçamento |
| USU_IndPrd | String(001) | Sim | Produto deve ser Produzido? |
| USU_DatPoc | Date | Sim | Data de previsão de entrega do produto  para considerar na Produção |
| USU_NumPdp | Number(008,0) | Sim | Número do Pedido Substituído |
| USU_SeqPdp | Number(004,0) | Sim | Sequência Substituído |
| USU_QtdAbt | Number(004,0) | Sim | Quantidade a Abater |
| USU_VlrOri | Number(015,2) | Sim | Valor original do pedido |
| USU_AltPla | String(001) | Sim | Alterar Plaqueta? |
| USU_DatEntPcp | Date | Sim | Data de Entrega Liberado pelo PCP |
| USU_HashSHA256 | String(064) | Sim | Hash gerado pelo sistema que integrou o pedido |
| USU_AvuPrc | String(001) | Sim | Indica se o componente avulso foi processado |
| USU_GerEst | String(001) | Sim | Gerar Estrutura |
| USU_SFNumPed | Number(010,0) | Sim | Salesforce - Num. do Pedido |
| USU_SFIDPed | String(050) | Sim | Salesforce - ID do Pedido |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIpd

---

## Índices

### E120IPDIndice2

**Tipo:** Não unico

Campos:
- CodPro
- CodDer
- DatEnt
- CodEmp
- CodFil

### E120IPDIndice3

**Tipo:** Não unico

Campos:
- DatEnt
- CodPro
- CodDer
- CodEmp
- CodFil

### E120IPDIndice4

**Tipo:** Não unico

Campos:
- CodEmp
- FilNfc
- ForNfc
- SnfNfc
- NumNfc
- SeqIpc
- CodFil

### E120IPDIndice5

**Tipo:** Não unico

Campos:
- EmpOcp
- FilOcp
- NumOcp
- SeqIpo

### E120IPDIndice6

**Tipo:** Não unico

Campos:
- CodEmp
- FilCtr
- CtrCvs
- CptCvs
- SeqCvs

### E120IPDIndice7

**Tipo:** Não unico

Campos:
- QtdRes
- SitIpd
- ResEst
- CodDep

---

## Relacionamentos

### IR_E120IPD_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

