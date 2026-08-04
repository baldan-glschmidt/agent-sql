# E140NFV

## Descrição

Vendas - Notas Fiscais de Saída - Dados Gerais

---

## Resumo

- Campos: 254
- Chave Primária: 4 campo(s)
- Índices: 8
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| TipNfs | Number(002,0) | Sim | Tipo da nota fiscal de saída |
| CodEdc | String(003) | Sim | Espécie de documento para fins fiscais |
| TnsPro | String(005) | Sim | Transação de faturamento para produtos |
| TnsSer | String(005) | Sim | Transação de faturamento para serviços |
| NopPro | String(005) | Sim | Natureza de operação para produtos |
| NopSer | String(005) | Sim | Natureza de operação para serviços |
| DatEmi | Date | Não | Data de emissão da nota fiscal de saída |
| CodCli | Number(009,0) | Não | Código do cliente da nota fiscal de saída |
| SeqEnt | Number(005,0) | Sim | Sequência do endereço de entrega do cliente |
| SeqCob | Number(005,0) | Sim | Sequência do endereço de cobrança do cliente |
| CodRoe | String(003) | Sim | Código da rota de entrega do cliente |
| SeqRoe | Number(004,0) | Sim | Sequência da rota de entrega do cliente |
| CodRai | Number(007,0) | Sim | Código da cidade para recolhimento do ISS (Tabela RAIS) |
| CodRep | Number(009,0) | Não | Código do representante da nota fiscal de saída |
| CodCpg | String(006) | Não | Código da condição de pagamento da nota fiscal de saída |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| CodMoe | String(003) | Sim | Código da moeda ou índice que o pedido estava representado |
| DatMoe | Date | Sim | Data base da cotação da moeda ou índice para conversão |
| CotMoe | Number(019,10) | Sim | Valor da cotação da moeda ou índice para conversão |
| FecMoe | String(001) | Sim | Indicativo de o valor da cotação é fechado |
| CodFcr | String(003) | Sim | Código da moeda ou índice como fator de correção (financeiro) |
| DatFcr | Date | Sim | Data da cotação da moeda ou índice para o fator de correção (financeiro) |
| DatSai | Date | Sim | Data da saída das mercadorias da nota fiscal de saída |
| HorSai | Number(005,0) | Sim | Hora da saída das mercadorias da nota fiscal de saída |
| CodTra | Number(009,0) | Sim | Código da transportadora da nota fiscal de saída |
| CodRed | Number(009,0) | Sim | Código da transportadora para redespacho da nota fiscal de saída |
| CodVia | String(003) | Sim | Via de transporte da nota fiscal de saída |
| PlaVei | String(010) | Sim | Placa do veículo de transporte das mercadorias da nota fiscal de saída |
| QtdEmb | Number(006,0) | Sim | Quantidade de embalagens da nota fiscal de saída |
| CodEmb | Number(004,0) | Sim | Código da embalagem |
| NumEmb | String(030) | Sim | Numeração das embalagens da nota fiscal de saída |
| CodMs1 | Number(004,0) | Sim | Código da mensagem - 1 da nota fiscal de saída |
| CodMs2 | Number(004,0) | Sim | Código da mensagem - 2 da nota fiscal de saída |
| CodMs3 | Number(004,0) | Sim | Código da mensagem - 3 da nota fiscal de saída |
| CodMs4 | Number(004,0) | Sim | Código da mensagem - 4 da nota fiscal de saída |
| ObsNfv | String(999) | Sim | Texto da observação da Nota Fiscal |
| PesBru | Number(014,5) | Sim | Peso bruto da nota fiscal de saída |
| PesLiq | Number(014,5) | Sim | Peso líquido da nota fiscal de saída |
| NumRom | String(010) | Sim | Número do romaneio de embarque |
| MeiTra | String(020) | Sim | Referência do meio de transporte (Navio, Vôo, etc.) |
| TerTra | String(020) | Sim | Terminal do meio de transporte |
| DatSmt | Date | Sim | Data da saída do meio de transporte |
| DatCtm | Date | Sim | Data da carga do terminal do meio de transporte |
| LocEmb | String(020) | Sim | Local de embarque da mercadoria (porto, aeroporto, etc.) |
| LocDes | String(020) | Sim | Local de destino da mercadoria (porto, aeroporto, etc.) |
| DatCmc | Date | Sim | Data da chegada da mercadoria no cliente |
| HorCmc | Number(005,0) | Sim | Hora da chegada da mercadoria no cliente |
| PerDs1 | Number(005,2) | Sim | Percentual de desconto - 1 do cliente |
| PerDs2 | Number(005,2) | Sim | Percentual de desconto - 2 do cliente |
| PerDs3 | Number(005,2) | Sim | Percentual de desconto - 3 do cliente |
| PerDs4 | Number(005,2) | Sim | Percentual de desconto - 4 do cliente |
| VlrFre | Number(015,2) | Sim | Valor do frete da nota fiscal de saída |
| CifFob | String(001) | Sim | Indicativo se o valor do frete é CIF ou FOB |
| VlrSeg | Number(015,2) | Sim | Valor do seguro da nota fiscal de saída |
| VlrEmb | Number(015,2) | Sim | Valor das embalagens da nota fiscal de saída |
| VlrEnc | Number(015,2) | Sim | Valor dos encargos financeiros da nota fiscal de saída |
| VlrOut | Number(015,2) | Sim | Valor de outras despesas da nota fiscal de saída |
| VlrDar | Number(015,2) | Sim | Valor dos descontos para arredondamento do total da nota fiscal |
| VlrFrd | Number(015,2) | Sim | Valor frete destacado |
| VlrOud | Number(015,2) | Sim | Valor outras despesas destacado |
| VlrBpr | Number(015,2) | Sim | Soma dos valores dos itens de produtos da nota fiscal de saída |
| VlrDpr | Number(015,2) | Sim | Soma dos descontos dos itens de produtos da nota fiscal de saída |
| VlrBse | Number(015,2) | Sim | Soma dos valores dos itens de serviços da nota fiscal de saída |
| VlrDse | Number(015,2) | Sim | Soma dos descontos dos itens de serviços da nota fiscal de saída |
| VlrDs1 | Number(015,2) | Sim | Valor do desconto - 1 do cliente |
| VlrDs2 | Number(015,2) | Sim | Valor do desconto - 2 do cliente |
| VlrDs3 | Number(015,2) | Sim | Valor do desconto - 3 do cliente |
| VlrDs4 | Number(015,2) | Sim | Valor do desconto - 4 do cliente |
| VlrDzf | Number(015,2) | Sim | Valor do desconto referente zona franca |
| VlrBfu | Number(015,2) | Sim | Valor base do funrural |
| VlrFun | Number(015,2) | Sim | Valor do funrural |
| VlrBip | Number(015,2) | Sim | Soma dos valores base do IPI dos itens de produtos da nota fiscal de saída |
| VlrIpi | Number(015,2) | Sim | Soma dos valores do IPI dos itens de produtos da nota fiscal de saída |
| VlrBid | Number(015,2) | Sim | Valor base IPI destacado/presumido (50% compra no comércio) |
| VlrIpd | Number(015,2) | Sim | Valor do IPI destacado/presumido (50% compra no comércio) |
| VlrBic | Number(015,2) | Sim | Soma dos valores base do ICMS dos itens de produtos da nota fiscal de saída |
| VlrIcm | Number(015,2) | Sim | Soma dos valores do ICMS dos itens de produtos da nota fiscal de saída |
| VlrBsi | Number(015,2) | Sim | Soma dos valores base do ICMS Substituído dos produtos da nota fiscal de saída |
| VlrSic | Number(015,2) | Sim | Soma dos valores do ICMS Substituído dos produtos da nota fiscal de saída |
| VlrBsd | Number(015,2) | Sim | Valor base ICMS substituído destacado |
| VlrIsd | Number(015,2) | Sim | Valor ICMS substituído destacado |
| VlrBsp | Number(015,2) | Sim | Valor base da substituição tributária do PIS |
| VlrStp | Number(015,2) | Sim | Valor da substituição tributária do PIS |
| VlrBsc | Number(015,2) | Sim | Valor base da substituição tributária da COFINS |
| VlrStc | Number(015,2) | Sim | Valor da substituição tributária do COFINS |
| VlrBis | Number(015,2) | Sim | Soma dos valores base do ISS dos itens de serviços da nota fiscal de saída |
| VlrIss | Number(015,2) | Sim | Soma dos valores do ISS dos itens de serviços da nota fiscal de saída |
| VlrBir | Number(015,2) | Sim | Soma dos valores base do IRRF dos itens de serviços da nota fiscal de saída |
| VlrIrf | Number(015,2) | Sim | Soma dos valores do IRRF dos itens de serviços da nota fiscal de saída |
| VlrBin | Number(015,2) | Sim | Valor base do INSS |
| VlrIns | Number(015,2) | Sim | Valor do INSS |
| VlrBco | Number(015,2) | Sim | Soma dos valores base comissões dos itens da nota fiscal de saída |
| VlrCom | Number(015,2) | Sim | Soma dos valores comissões dos itens da nota fiscal de saída |
| VlrLpr | Number(015,2) | Sim | Total líquido dos itens de produtos da nota fiscal de saída |
| VlrLse | Number(015,2) | Sim | Total líquido dos itens de serviços da nota fiscal de saída |
| VlrLou | Number(015,2) | Sim | Total dos valores diversos da nota fiscal de saída |
| Vlrliq | Number(015,2) | Sim | Total líquido da nota fiscal de saída |
| VlrFin | Number(015,2) | Sim | Valor líquido da nota fiscal para o financeiro |
| QtdItp | Number(003,0) | Sim | Quantidade de itens de produtos da nota fiscal de saída |
| QtdIts | Number(003,0) | Sim | Quantidade de itens de serviços da nota fiscal de saída |
| QtdDup | Number(004,0) | Sim | Quantidade de emissões das duplicatas da nota fiscal de saída |
| QtdBlo | Number(004,0) | Sim | Quantidade de emissões dos bloquetos da nota fiscal de saída |
| QtdEmi | Number(002,0) | Sim | Quantidade de emissões da nota fiscal de saída |
| PreImp | Number(009,0) | Sim | Número pré-impresso do formulário da nota fiscal |
| SitNfv | String(001) | Não | Situação da nota fiscal de saída |
| CodMot | Number(006,0) | Sim | Código do motivo da situação |
| ObsMot | String(250) | Sim | Observação do bloqueio ou desbloqueio da nota fiscal |
| NfvBlo | String(001) | Sim | Indicativo se a nota fiscal está bloqueada ou desbloqueada |
| UsuBlo | Number(010,0) | Sim | Usuário responsável pelo bloqueio ou desbloqueio da nota |
| DatBlo | Date | Sim | Data do bloqueio ou desbloqueio da nota |
| HorBlo | Number(005,0) | Sim | Hora do bloqueio ou desbloqueio da nota |
| VerCal | Number(004,0) | Sim | Número da versão para os cálculos |
| IntImp | String(001) | Não | Indicativo se a nota foi integrada com gestão de tributos |
| NumLot | Number(009,0) | Sim | Número do lote contábil |
| IndSig | String(001) | Não | Indicativo se a nota fiscal está lançada no SIG |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração na nota fiscal |
| DatGer | Date | Sim | Data da geração da nota fiscal |
| HorGer | Number(005,0) | Sim | Hora da geração da nota fiscal |
| PerFre | Number(005,2) | Sim | Percentual de Frete |
| PerSeg | Number(005,2) | Sim | Percentual de Seguro |
| PerEmb | Number(005,2) | Sim | Percentual de Embalagens |
| PerEnc | Number(005,2) | Sim | Percentual de Encargos |
| PerOut | Number(005,2) | Sim | Percentual de Outras Despesas |
| CptFat | Date | Sim | Competência Faturada |
| CodSac | Number(014,0) | Sim | Número do CNPJ ou CPF do sacado |
| DocIdeSac | String(014) | Sim | Código do sacado |
| PerIcf | Number(005,2) | Sim | Percentual de ICMS sobre o Frete da nota fiscal de saída |
| IcmFre | Number(015,2) | Sim | Valor de ICMS sobre o Frete da nota fiscal de saída |
| NumGtr | Number(006,0) | Sim | Número da Guia de Tráfego para SPFC |
| VlrBpi | Number(015,2) | Sim | Soma dos valores base do PIS(Estorno Devolução) dos itens de produtos da NF de Saída |
| VlrPis | Number(015,2) | Sim | Soma dos valores do PIS a recuperar (Estorno Devolução) dos itens de produtos da NF de Saída |
| PerOf1 | Number(005,2) | Sim | Percentual de oferta 1 para a Nota |
| PerOf2 | Number(005,2) | Sim | Percentual de oferta 2 para a Nota Fiscal |
| RemDes | String(001) | Sim | Indicativo se o cliente da transportadora é Remetente ou Destinatário |
| TipRde | String(001) | Sim | Indicativo do tipo de pessoa do remetente/destinatário (Jurídica ou Física) |
| CgcRde | Number(014,0) | Sim | Número do CNPJ ou CPF do remetente/destinatário |
| DocIdeRde | String(014) | Sim | Número do CNPJ ou CPF do remetente/destinatário |
| InsRde | String(025) | Sim | Inscrição estadual do remetente/destinatário |
| EstRde | String(002) | Sim | Sigla do estado do remetente/destinatário |
| MunRde | String(060) | Sim | Cidade do remetente/destinatário |
| UfsVei | String(002) | Sim | Sigla do estado do veículo de transporte das mercadorias da nota fiscal de saída |
| KmtDis | Number(008,2) | Sim | Distância em quilômetros a percorrer com o veículo de transporte das mercadorias |
| ForCal | Number(001,0) | Sim | Indicativo da forma de cálculo do valor do frete |
| IndSin | String(001) | Sim | Indicativo se a nota fiscal foi exportada para o Sintegra |
| PrcNfv | Number(002,0) | Sim | Procedência da Nota Fiscal de Saída |
| CodCl1 | Number(009,0) | Sim | Código do cliente (Remetente) |
| CodCl2 | Number(009,0) | Sim | Código do cliente (Destinatário) |
| SecCat | Number(015,2) | Sim | Valor do SEC/CAT |
| VlrAde | Number(015,2) | Sim | Valor ADEME |
| VlrTco | Number(015,2) | Sim | Valor da taxa de coleta |
| VlrPdg | Number(015,2) | Sim | Valor do pedágio |
| VlrBcr | Number(015,2) | Sim | Soma dos valores base do Cofins  à Recuperar |
| VlrCor | Number(015,2) | Sim | Soma dos valores do Cofins a recuperar |
| VlrBcl | Number(015,2) | Sim | Soma dos valores base do CSLL Retido |
| VlrCsl | Number(015,2) | Sim | Soma dos valores do CSLL  Retido |
| VlrBpt | Number(015,2) | Sim | Soma dos valores base do PIS Retido |
| VlrPit | Number(015,2) | Sim | Soma dos valores do PIS retido |
| VlrBct | Number(015,2) | Sim | Soma dos valores base do Cofins Retido |
| VlrCrt | Number(015,2) | Sim | Soma dos valores do Cofins Retido |
| VlrBor | Number(015,2) | Sim | Soma dos valores base de Outras Retenções |
| VlrOur | Number(015,2) | Sim | Soma dos valores de Outras Retenções |
| IntPat | String(001) | Sim | Indica se a nota fiscal de saída foi integrada com a gestão de patrimônio |
| VlrBii | Number(015,2) | Sim | Soma dos valores base do imposto de importação dos itens de produtos da nota fiscal de saída |
| VlrIim | Number(015,2) | Sim | Soma dos valores do imposto de importação dos itens de produtos da nota fiscal de saída |
| CodMar | String(010) | Sim | Código da Marca/Etiqueta vinculada à nota fiscal |
| CodSro | String(003) | Sim | Código da Sub Rota |
| CodLip | String(005) | Sim | Código da lista de preço utilizada na venda |
| VlrRis | Number(015,2) | Sim | Valor de retenção de ICMS Substituto |
| VlrOcl | Number(015,2) | Sim | Soma dos valores base originais de CSLL (anterior verificação limite retenção) |
| VlrOpt | Number(015,2) | Sim | Soma dos valores base originais de PIS (anterior verificação limite retenção) |
| VlrOct | Number(015,2) | Sim | Soma dos valores base originais de Cofins (anterior verificação limite retenção) |
| VlrOor | Number(015,2) | Sim | Soma dos valores base original de Outras Retenções (anterior a verificação do valor limite p/ retenção) |
| NumRde | String(020) | Sim | Número do Registro de Exportação |
| NumDde | String(020) | Sim | Número do Despacho de Exportação |
| IndCon | String(001) | Sim | Indicativo se o frete é pago pelo consignatário |
| CodTme | Number(004,0) | Sim | Código do tipo de mercadoria |
| CodTip | Number(004,0) | Sim | Código do tipo de veículo |
| TraMtr | Number(009,0) | Sim | Código da Transportadora do motorista |
| CodMtr | Number(006,0) | Sim | Código do Motorista |
| TraReb | Number(009,0) | Sim | Código da transportadora do reboque |
| PlaReb | String(010) | Sim | Placa do reboque |
| VolNfv | Number(014,5) | Sim | Volume Total da NF |
| CodEqu | Number(003,0) | Sim | Código do equipamento fiscal |
| NumCfi | Number(009,0) | Sim | Número do cupom fiscal de referência da redução Z |
| CroEcf | Number(006,0) | Sim | Cont. de Reinício de Operação do ECF |
| VlrFei | Number(015,2) | Sim | Valor de frete de importação |
| VlrSei | Number(015,2) | Sim | Valor de seguro de importação |
| VlrOui | Number(015,2) | Sim | Valor de outras despesas de importação |
| BcoImp | Number(015,2) | Sim | Valor base do cofins a recuperar na importação |
| CofImp | Number(015,2) | Sim | Valor do cofins a recuperar na importação |
| BpiImp | Number(015,2) | Sim | Valor base do pis a recuperar na importação |
| PisImp | Number(015,2) | Sim | Valor do pis a recuperar na importação |
| NumCpe | Number(009,0) | Sim | Número do carregamento para o qual foi gerada a nota fiscal |
| NumNsu | Number(010,0) | Sim | Número seqüencial único |
| DatNsu | Date | Sim | Data de geração do número seqüencial único |
| HorNsu | Number(005,0) | Sim | Hora de geração do número seqüencial único |
| DatImp | Date | Sim | Data da impressão da nota fiscal de saída |
| HorImp | Number(005,0) | Sim | Hora da impressão da nota fiscal de saída |
| DatAge | Date | Sim | Data do agendamento da entrega |
| DatCex | Date | Sim | Data do comprovante de exportação (Averbação) |
| VlrBpf | Number(015,2) | Sim | Soma dos valores base do PIS Faturamento dos itens da nota fiscal |
| VlrPif | Number(015,2) | Sim | Soma dos valores do PIS Faturamento dos itens da nota fiscal |
| VlrBcf | Number(015,2) | Sim | Soma dos valores base do COFINS Faturamento dos itens da nota fiscal |
| VlrCff | Number(015,2) | Sim | Soma dos valores do COFINS Faturamento dos itens da nota fiscal |
| DatVis | Date | Sim | Data de visualização da impressão da nota fiscal de saída |
| HorVis | Number(005,0) | Sim | Hora de visualização da impressão da nota fiscal de saída |
| DiaFix | Number(002,0) | Sim | Dia fixo de vencimento das parcelas geradas para o financeiro |
| VlrBsf | Number(015,2) | Sim | Soma dos valores base do ICMS Substituído dos produtos da nota fiscal de saída para entrega futura |
| VlrSif | Number(015,2) | Sim | Soma dos valores do ICMS Substituído dos produtos da nota fiscal de saída para entrega futura |
| SeqPco | Number(003,0) | Sim | Sequência do endereço do participante da coleta |
| SeqPen | Number(003,0) | Sim | Sequência do endereço do participante da entrega |
| SnfNcf | String(003) | Sim | Código da série da nota de cupom fiscal relacionada |
| NumNcf | Number(009,0) | Sim | Número da nota fiscal cupom relacionada |
| SomFre | String(001) | Sim | Indicativo se o frete deve ser somado ao valor líquido da nota fiscal |
| PerDs5 | Number(005,2) | Sim | Percentual de desconto - 5 do cliente |
| VlrDs5 | Number(015,2) | Sim | Valor do desconto - 5 do cliente |
| UfsEbq | String(002) | Sim | Sigla do estado do local de embarque das mercadorias (Exportação) |
| ProPre | String(060) | Sim | Produto predominante do conhecimento de transporte da carga |
| TotCid | Number(015,2) | Sim | Soma dos valores totais do Imposto CIDE dos itens da nota fiscal |
| NumPin | String(015) | Sim | Protocolo de Ingresso de Mercadoria Nacional |
| NumInt | String(020) | Sim | Número do Documento Externo (Integrado) |
| VlrMer | Number(015,2) | Sim | Valor estimado das mercadorias |
| SerImp | String(010) | Sim | Tipo de Serviço no contexto fiscal baseado na LC 116/2003 |
| FilFix | Number(005,0) | Sim | Código da filial |
| NumFix | Number(009,0) | Sim | Número da Fixação |
| IndRor | String(001) | Sim | Indica se o recibo que permite a geração da fatura automática foi recebido |
| QtdBpi | Number(015,3) | Sim | Quantidade da base do PIS a recuperar (Estorno devolução) |
| QtdBco | Number(015,3) | Sim | Quantidade da base do COFINS a recuperar  (Estorno devolução) |
| QtdBip | Number(015,3) | Sim | Quantidade da base do IPI |
| QtdBpf | Number(015,3) | Sim | Quantidade da base do PIS por faturamento |
| QtdBcf | Number(015,3) | Sim | Quantidade da base do COFINS por faturamento |
| BasOir | Number(015,2) | Sim | Soma dos valores originais de IRRF (anterior verificação do limite p/ retenção) |
| VlrOir | Number(015,2) | Sim | Soma dos valores base originais de IRRF (anterior verificação limite retenção) |
| VlrSub | Number(015,2) | Sim | Valor do subsídio na nota fiscal de saída |
| TemAva | String(001) | Sim | Tem Controle de Avalista |
| DatIzf | Date | Sim | Data efetiva do ingresso da mercadoria na zona franca de manaus. |
| NumCur | String(040) | Sim | Senha do serviço do tipo curso para ser utilizado no segmento varejo. |
| SeqRet | Number(004,0) | Sim | Sequência do endereço de retirada. |
| CodTab | String(004) | Sim | Código da tabela de preço frete |
| TraRe2 | Number(009,0) | Sim | Código da transportadora do reboque 2 |
| PlaRe2 | String(010) | Sim | Placa do reboque 2 |
| TraRe3 | Number(009,0) | Sim | Código da transportadora do reboque 3 |
| PlaRe3 | String(010) | Sim | Placa do reboque 3 |
| VlrBif | Number(015,2) | Sim | Base de cálculo do ICMS sobre o frete da nota fiscal de saída |
| HorEmi | Number(005,0) | Sim | Hora de emissão da nota no sistema terceiro |
| VlrDed | Number(015,2) | Sim | Valor de Deduções |
| DatInv | Date | Sim | Data base do inventário |
| VlrIcd | Number(015,2) | Sim | Valor do ICMS desonerado |
| IdeSac | String(050) | Sim | Identificador único alfanumérico |
| USU_CtrFin | String(001) | Sim | Controle do Financeiro |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv

---

## Índices

### E140NFVIndice2

**Tipo:** Não unico

Campos:
- CodCli
- SitNfv
- CodEmp
- CodFil

### E140NFVIndice3

**Tipo:** Não unico

Campos:
- DatEmi
- NumLot
- SitNfv
- CodFil
- CodEmp

### E140NFVIndice4

**Tipo:** Não unico

Campos:
- CodRep

### E140NFVIndice5

**Tipo:** Não unico

Campos:
- CodEmp
- CodCpg

### E140NFVIndice6

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf
- DatEmi
- CodEqu
- NumCfi
- NumNfv
- CroEcf

### USU_E140NFV3

**Tipo:** Não unico

Campos:
- NumNfv

### USU_E140NFV2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- SitNfv
- CodSnf
- NumNfv

### USU_E140NFV1

**Tipo:** Não unico

Campos:
- SitNfv
- CodFil
- CodEmp
- NumNfv
- DatEmi

---

## Relacionamentos

### IR_E140NFV_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140NFV_011

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E140NFV_017

**Tabela:** E090REP

| Origem | Destino |
|--------|---------|
| CodRep | CodRep |

### IR_E140NFV_018

**Tabela:** E028CPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCpg | CodCpg |

