# E140IPV

## Descrição

Vendas - Notas Fiscais de Saída - Itens de Produtos

---

## Resumo

- Campos: 255
- Chave Primária: 5 campo(s)
- Índices: 6
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| TnsPro | String(005) | Sim | Transação do item de produto da nota |
| NopPro | String(005) | Sim | Código da natureza de operação |
| FilPed | Number(005,0) | Sim | Código da filial do pedido |
| NumPed | Number(008,0) | Sim | Número do pedido que gerou a  nota fiscal de saída |
| SeqIpd | Number(004,0) | Sim | Sequência do item no pedido da nota fiscal de saída |
| FilCtr | Number(005,0) | Sim | Código da filial do contrato de venda |
| NumCtr | Number(009,0) | Sim | Número do contrato que gerou a nota fiscal de saída |
| DatCpt | Date | Sim | Mês e ano de competência do item do contrato |
| SeqCvp | Number(003,0) | Sim | Sequência do item do contrato na competência |
| CodPro | String(014) | Sim | Código do produto da nota fiscal de saída |
| CodDer | String(007) | Sim | Código da derivação do produto da nota fiscal de saída |
| CplIpv | String(250) | Sim | Complemento da descrição do produto |
| CodFam | String(006) | Sim | Código da família do produto |
| CodClf | String(003) | Sim | Código da classificação fiscal do item da nota fiscal de saída |
| CodStr | String(003) | Sim | Situação tributária do I.C.M.S do item da nota fiscal de saída |
| CodTic | String(003) | Sim | Código do ICMS especial |
| CodTrd | String(003) | Sim | Código de redução de impostos |
| CodTst | String(003) | Sim | Código do ICMS substituído |
| CodStp | String(003) | Sim | Código de substituição do PIS |
| CodStc | String(003) | Sim | Código de substituição do COFINS |
| CodDep | String(010) | Sim | Código do depósito para baixa de estoque do produto da nota fiscal de saída |
| CodLot | String(050) | Sim | Código do lote de fabricação do produto |
| QtdFat | Number(014,5) | Sim | Quantidade faturada do item da nota fiscal de saída |
| QtdDev | Number(014,5) | Sim | Quantidade devolvida do item da nota fiscal de saída |
| UniMed | String(003) | Não | Unidade de medida do item da nota fiscal de saída |
| UniEmi | String(003) | Sim | Unidade de medida do item para a impressão da nota fiscal |
| VlrFum | Number(015,2) | Sim | Valor do frete por unidade de medida |
| QtdFre | Number(014,5) | Sim | Quantidade base na unidade do produto valida para o valor do frete |
| ForFre | Number(009,0) | Sim | Código do fornecedor para geração título de frete |
| PesBru | Number(014,5) | Sim | Peso bruto do item da nota fiscal de saída |
| PesLiq | Number(014,5) | Sim | Peso líquido do item da nota fiscal de saída |
| CodTpr | String(004) | Sim | Código da tabela de preço do item da nota fiscal de saída |
| PreUni | Number(021,10) | Sim | Preço unitário do item da nota fiscal de saída |
| PreBas | Number(021,10) | Sim | Preço unitário base para o movimento de estoque |
| PerDsc | Number(005,2) | Sim | Percentual de desconto do item da nota fiscal de saída |
| PerOfe | Number(010,5) | Sim | Percentual de oferta para o produto da nota fiscal de saída |
| PerAcr | Number(010,5) | Sim | Percentual de acréscimo para o produto da nota fiscal de saída |
| PerIpi | Number(008,4) | Sim | Percentual de IPI do item da nota fiscal de saída |
| PerIcm | Number(005,2) | Sim | Percentual do ICM do item da nota fiscal de saída |
| PerFun | Number(004,2) | Sim | Percentual do funrural |
| PerCom | Number(005,2) | Sim | Percentual de comissão do item da nota fiscal de saída |
| SalCan | String(001) | Sim | Indicativo se os saldos dos pedidos deverão ser cancelados |
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
| VlrBru | Number(015,2) | Sim | Valor bruto do item da nota fiscal de saída |
| VlrDsc | Number(015,2) | Sim | Valor do desconto do item da nota fiscal de saída |
| VlrDs1 | Number(015,2) | Sim | Valor do desconto - 1 do cliente |
| VlrDs2 | Number(015,2) | Sim | Valor do desconto - 2 do cliente |
| VlrDs3 | Number(015,2) | Sim | Valor do desconto - 3 do cliente |
| VlrDs4 | Number(015,2) | Sim | Valor do desconto - 4 do cliente |
| VlrOfe | Number(015,2) | Sim | Valor do desconto de Oferta |
| VlrDzf | Number(015,2) | Sim | Valor do desconto referente zona franca |
| VlrBfu | Number(015,2) | Sim | Valor base do funrural |
| VlrFun | Number(015,2) | Sim | Valor do funrural |
| VlrBip | Number(015,2) | Sim | Valor base IPI |
| VlrIpi | Number(015,2) | Sim | Valor do IPI do item da nota fiscal de saída |
| VlrBid | Number(015,2) | Sim | Valor base IPI presumido (50% compra no comércio) |
| VlrIpd | Number(015,2) | Sim | Valor do IPI presumido (50% compra no comércio) |
| VlrBic | Number(015,2) | Sim | Valor base ICMS |
| VlrIcm | Number(015,2) | Sim | Valor do ICMS do item da nota fiscal de saída |
| VlrDfa | Number(015,2) | Sim | Valor da diferença de alíquota inter-estadual |
| VlrBsi | Number(015,2) | Sim | Valor base ICMS substituído |
| VlrIcs | Number(015,2) | Sim | Valor do ICMS substituído do item da nota fiscal de saída |
| VlrBsd | Number(015,2) | Sim | Valor base ICMS substituído destacado |
| VlrIsd | Number(015,2) | Sim | Valor do ICMS substituído destacado |
| VlrBsp | Number(015,2) | Sim | Valor base da substituição tributária do PIS |
| VlrStp | Number(015,2) | Sim | Valor da substituição tributária do PIS |
| VlrBsc | Number(015,2) | Sim | Valor base da substituição tributária da COFINS |
| VlrStc | Number(015,2) | Sim | Valor da substituição tributária do COFINS |
| VlrBco | Number(015,2) | Sim | Valor base comissão |
| VlrCom | Number(015,2) | Sim | Valor comissão |
| VlrIip | Number(015,2) | Sim | Valor isento IPI |
| VlrIic | Number(015,2) | Sim | Valor isento ICMS |
| VlrOip | Number(015,2) | Sim | Valor outros IPI |
| VlrOic | Number(015,2) | Sim | Valor outros ICMS |
| VlrLpr | Number(015,2) | Sim | Valor do produto |
| VlrLou | Number(015,2) | Sim | Valor dos outros valores |
| VlrLiq | Number(015,2) | Sim | Valor líquido do item de produto da nota fiscal de saída |
| VlrFin | Number(015,2) | Sim | Valor do item válido para o financeiro |
| SeqNfi | Number(004,0) | Sim | Sequência do item na nota fiscal impressa |
| FilNfc | Number(005,0) | Sim | Código da filial da nota fiscal de entrada |
| CodFor | Number(009,0) | Sim | Fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Sim | Número da nota fiscal de entrada |
| SnfNfc | String(003) | Sim | Código da série da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Sim | Sequência do item da nota fiscal de entrada |
| NumFcc | Number(006,0) | Sim | Número do formulário do certificado de classificação impresso |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SerCcl | String(003) | Sim | Série do certificado de classificação |
| NumCcl | String(015) | Sim | Número do certificado de classificação |
| UniVen | String(003) | Sim | Unidade de medida de venda do item de produto |
| QtdVen | Number(014,5) | Sim | Quantidade do produto na unidade de medida de venda do item |
| PreVen | Number(021,10) | Sim | Preço unitário do produto na unidade de medida de venda do item |
| VlrBpi | Number(015,2) | Sim | Valor base do PIS (Estorno Devolução) |
| VlrPis | Number(015,2) | Sim | Valor do PIS a recuperar (Estorno Devolução) do item da nota fiscal de saída |
| PreBru | Number(021,10) | Sim | Preço unitário Bruto do produto da Nota Fiscal |
| VlrBcr | Number(015,2) | Sim | Valor base do Cofins à Recuperar (Estorno Devolução) |
| VlrCor | Number(015,2) | Sim | Valor do Cofins a recuperar (Estorno Devolução) |
| PerIim | Number(005,2) | Sim | Percentual de imposto de importação do item da nota fiscal de saída |
| VlrBii | Number(015,2) | Sim | Valor base imposto de importação |
| VlrIim | Number(015,2) | Sim | Valor do imposto de importação do item da nota fiscal de saída |
| CodMar | String(010) | Sim | Código da Marca/Etiqueta vinculada ao item da nota fiscal |
| PerDs1 | Number(005,2) | Sim | Percentual de desconto - 1 do cliente |
| PerDs2 | Number(005,2) | Sim | Percentual de desconto - 2 do cliente |
| PerDs3 | Number(005,2) | Sim | Percentual de desconto - 3 do cliente |
| PerDs4 | Number(005,2) | Sim | Percentual de desconto - 4 do cliente |
| VlrRis | Number(015,2) | Sim | Valor de retenção de ICMS Substituto |
| CodBem | String(020) | Sim | Código do Bem |
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
| DesImp | String(250) | Sim | Descrição do produto impressa na nota, para fins de relatórios fiscais (Sintegra) |
| CptFat | Date | Sim | Competência Faturada |
| VlrFei | Number(015,2) | Sim | Valor de frete de importação |
| VlrSei | Number(015,2) | Sim | Valor de seguro de importação |
| VlrOui | Number(015,2) | Sim | Valor de outras despesas de importação |
| BcoImp | Number(015,2) | Sim | Valor base do cofins a recuperar na importação |
| CofImp | Number(015,2) | Sim | Valor do cofins a recuperar na importação |
| BpiImp | Number(015,2) | Sim | Valor base do pis a recuperar na importação |
| PisImp | Number(015,2) | Sim | Valor do pis a recuperar na importação |
| PedCpe | Number(008,0) | Sim | Número do pedido do carregamento |
| IpdCpe | Number(004,0) | Sim | Sequência do item no pedido do carregamento |
| ObsIpv | String(999) | Sim | Observação do item de produto da Nota Fiscal de Saída |
| VlrBpf | Number(015,2) | Sim | Valor Base do PIS Faturamento |
| PerPif | Number(008,4) | Sim | Percentual do PIS Faturamento |
| VlrPif | Number(015,2) | Sim | Valor do PIS Faturamento |
| VlrBcf | Number(015,2) | Sim | Valor Base do COFINS Faturamento |
| PerCff | Number(008,4) | Sim | Percentual do COFINS Faturamento |
| VlrCff | Number(015,2) | Sim | Valor do COFINS Faturamento |
| VlrBsf | Number(015,2) | Sim | Valor base do ICMS Substituído para entrega futura |
| VlrSif | Number(015,2) | Sim | Valor do ICMS Substituído para entrega futura |
| CstIpi | String(002) | Sim | Código da situação tributária de IPI |
| CstPis | String(002) | Sim | Código da situação tributária de PIS |
| CstCof | String(002) | Sim | Código da situação tributária de COFINS |
| PerDs5 | Number(005,2) | Sim | Percentual de desconto - 5 do cliente |
| VlrDs5 | Number(015,2) | Sim | Valor do desconto - 5 do cliente |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| VlrAjs | Number(015,2) | Sim | Valor do ajuste do item referente ao dispositivo fiscal |
| PreRep | Number(014,5) | Sim | Valor de Repasse |
| VlrCid | Number(015,2) | Sim | Valor unitário do Imposto CIDE |
| TotCid | Number(015,2) | Sim | Valor total do Imposto CIDE |
| CodMs1 | Number(004,0) | Sim | Código da mensagem - 1 do item da nota fiscal de saída |
| CodMs2 | Number(004,0) | Sim | Código da mensagem - 2 do item da nota fiscal de saída |
| CodMs3 | Number(004,0) | Sim | Código da mensagem - 3 do item da nota fiscal de saída |
| CodMs4 | Number(004,0) | Sim | Código da mensagem - 4 do item da nota fiscal de saída |
| QtdBpi | Number(015,3) | Sim | Quantidade da base do PIS a recuperar (Estorno devolução) |
| AliPis | Number(015,4) | Sim | Alíquota por Valor do PIS a recuperar (Estorno devolução) |
| QtdBco | Number(015,3) | Sim | Quantidade da base do COFINS a recuperar (Estorno devolução) |
| AliCof | Number(015,4) | Sim | Alíquota por Valor do COFINS a recuperar (Estorno devolução) |
| QtdBip | Number(015,3) | Sim | Quantidade da base do IPI |
| AliIpi | Number(015,4) | Sim | Alíquota por Valor do IPI |
| QtdBpf | Number(015,3) | Sim | Quantidade da base do PIS por faturamento |
| AliPif | Number(015,4) | Sim | Alíquota por valor do PIS por faturamento |
| QtdBcf | Number(015,3) | Sim | Quantidade da base do COFINS por faturamento |
| AliCff | Number(015,4) | Sim | Alíquota por Valor do COFINS por faturamento |
| VlrSub | Number(015,2) | Sim | Valor do subsídio na nota fiscal de saída |
| NatPis | Number(005,0) | Sim | Natureza da receita do PIS |
| NatCof | Number(005,0) | Sim | Natureza da receita do COFINS |
| OriMer | String(001) | Sim | Origem fiscal da mercadoria |
| NumCur | String(040) | Sim | Senha do serviço do tipo curso para ser utilizado no segmento varejo. |
| CodRep | Number(009,0) | Sim | Código do representante do item de produto da nota fiscal de saída |
| ProMon | String(001) | Sim | Indicativo se o produto exige montagem |
| ProEnt | String(001) | Sim | Indicativo se o produto exige ser entregue |
| PerMgc | Number(014,5) | Sim | Percentual de Margem de Contribuição utilizada para a venda |
| VarSer | String(001) | Sim | Indica o tipo de serviço para o Varejo |
| RetMat | String(001) | Sim | Indicaivo se o produto será retirado no depósito da matriz pelo cliente |
| TipCur | Number(001,0) | Sim | Indicativo do tipo de curso online para varejo |
| EmpCto | Number(004,0) | Sim | Código da empresa do período de apuração da comissão |
| CodPco | Number(004,0) | Sim | Código período para o controle de comissionamento |
| FilCto | Number(005,0) | Sim | Código da filial do período de apuração da comissão |
| CptPco | Date | Sim | Mês e ano base do comissionamento |
| CodFin | Number(004,0) | Sim | Código da finalidade de venda |
| MotDes | Number(002,0) | Sim | Motivo desoneração ICMS |
| VlrIcd | Number(015,2) | Sim | Valor do ICMS desonerado |
| PerSen | Number(004,2) | Sim | Percentual do SENAR/SENAT |
| VlrBsn | Number(015,2) | Sim | Valor base do SENAR/SENAT |
| VlrSen | Number(015,2) | Sim | Valor do SENAR/SENAT |
| CodFci | String(036) | Sim | Código da ficha de conteúdo de importação (FCI) |
| CodBic | String(003) | Sim | Código da modalidade da base de cálculo do ICMS |
| VlrIbs | Number(015,2) | Sim | Valor base do ICMS Simples Nacional |
| VlrIsn | Number(015,2) | Sim | Valor do ICMS Simples Nacional |
| PerIsn | Number(005,2) | Sim | Percentual de aliquota de ICMS simples nacional |
| NroSev | String(040) | Sim | Número de Série vendido (quando produto não controla por série) |
| NumDrb | String(020) | Sim | Número do Drawback |
| NumRde | String(012) | Sim | Número do registro de exportação |
| NatExp | String(001) | Sim | Natureza da exportação |
| ChvNex | String(050) | Sim | Chave do documento eletrônico para exportação |
| DtiGar | Date | Sim | Data inicial de vigência da garantia |
| DtfGar | Date | Sim | Data final de vigência da garantia |
| VlrAip | Number(015,2) | Sim | Valor aproximado de impostos no item de produto no cupom |
| PerAip | Number(015,2) | Sim | Percentual aproximado de impostos no item de produto no cupom |
| NumLan | Number(009,0) | Sim | Número sequencial do lançamento destinado ao controle do crédito acumulado |
| VlrIdv | Number(015,2) | Sim | Valor do IPI devolvido |
| CodCnv | Number(004,0) | Sim | Código do convênio |
| VlrPmc | Number(011,2) | Sim | Valor do produto do convênio na tabela PMC |
| PerDcn | Number(005,2) | Sim | Percentual de desconto concedido pelo convênio |
| VlrDcn | Number(011,2) | Sim | Valor de desconto concedido pelo convênio |
| PerDif | Number(007,4) | Sim | Percentual de diferimento do item de produto |
| BasIdf | Number(015,2) | Sim | Valor base do ICMS diferido |
| PerIdf | Number(005,2) | Sim | Percentual do ICMS diferido do item da nota fiscal de saída |
| VlrIdf | Number(015,2) | Sim | Valor do ICMS diferido do item da nota fiscal de saída |
| TipGar | String(002) | Sim | Tipo de Garantia Estendida |
| AbtDes | String(001) | Sim | Indicativo se houve abatimento do valor do ICMS desonerado |
| SeqRem | Number(010,0) | Sim | Sequência da receita agronômica |
| NumRec | Number(009,0) | Sim | Número da receita |
| SeqRei | Number(010,0) | Sim | Sequência do item |
| CodEnq | Number(003,0) | Sim | Código de enquadramento legal do IPI |
| IcmAor | Number(005,2) | Sim | Alíquota de ICMS partilhado com o estado remetente |
| IcmVor | Number(015,2) | Sim | Valor de ICMS partilhado com o estado remetente |
| IcmAde | Number(005,2) | Sim | Alíquota de ICMS partilhado com o estado destinatário |
| IcmVde | Number(015,2) | Sim | Valor de ICMS partilhado com o estado destinatário |
| IcmBde | Number(015,2) | Sim | Valor Base ICMS partilha para estado de destino |
| IcmAfc | Number(007,4) | Sim | Alíquota do ICMS para fundo de combate à pobreza na UF de destino |
| IcmVfc | Number(015,2) | Sim | Valor do ICMS para fundo de combate à pobreza na UF de destino |
| CodCes | String(007) | Sim | Código especificador da substituição tributária |
| BasIef | Number(015,2) | Sim | Valor base do ICMS para entrega futura |
| PerIef | Number(005,2) | Sim | Percentual do ICMS para entrega futura |
| VlrIef | Number(015,2) | Sim | Valor do ICMS para entrega futura |
| CodBnf | String(010) | Sim | Código de Benefício Fiscal na UF aplicado ao produto |
| CptApu | Date | Sim | Competência de apuração da CBS/IBS |
| VlrCBS | Number(013,2) | Sim | Valor da CBS de origem |
| VlrIBU | Number(013,2) | Sim | Valor do IBS Estadual de origem |
| VlrIBM | Number(013,2) | Sim | Valor do IBS Municipal de origem |
| USU_bxamov | String(001) | Sim | Baixa Movimento |
| USU_recicm | String(001) | Sim | Recuperou ICMS |
| USU_NumLan | Number(009,0) | Sim | Numero Lancamento CAT83 |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv

---

## Índices

### E140IPVIndice2

**Tipo:** Não unico

Campos:
- CodPro
- CodDer
- CodEmp
- CodFil

### E140IPVIndice3

**Tipo:** Não unico

Campos:
- NumPed
- CodEmp
- FilPed
- SeqIpd

### E140IPVIndice4

**Tipo:** Não unico

Campos:
- SeqIpc
- SnfNfc
- FilNfc

### E140IPVIndice5

**Tipo:** Não unico

Campos:
- CodEmp
- FilCtr
- NumCtr
- SeqCvp
- DatCpt

### USU_E140IPV2

**Tipo:** Não unico

Campos:
- NumPed
- CodEmp
- CodFil
- NumNfv

### USU_E140IPV1

**Tipo:** Não unico

Campos:
- NumNfv
- CodEmp
- CodPro

---

## Relacionamentos

### IR_E140IPV_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

