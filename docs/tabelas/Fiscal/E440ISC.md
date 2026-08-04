# E440ISC

## Descrição

Compras - Notas Fiscais de Entrada - Itens de Serviço

---

## Resumo

- Campos: 238
- Chave Primária: 6 campo(s)
- Índices: 3
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqIsc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| FilOcp | Number(005,0) | Sim | Código da filial da ordem de compra |
| NumOcp | Number(008,0) | Sim | Número da ordem de compra da nota fiscal de entrada |
| SeqIso | Number(004,0) | Sim | Sequência da ordem de compra da nota fiscal de entrada |
| TnsSer | String(005) | Sim | Transação de serviço do item da nota |
| NopSer | String(005) | Sim | Código da natureza de operação |
| CodSer | String(014) | Sim | Código do serviço da nota fiscal de entrada |
| CodFam | String(006) | Sim | Código da família do serviço |
| CodTri | String(005) | Sim | Código de tributação para emissão da DARF |
| CplIsc | String(250) | Sim | Complemento da descrição do serviço |
| QtdRec | Number(014,5) | Sim | Quantidade recebida do serviço da nota fiscal de entrada |
| QtdDev | Number(014,5) | Sim | Soma das quantidades devolvidas pelas NF de saída |
| UniMed | String(003) | Não | Unidade de medida do serviço da nota fiscal de entrada |
| PreUni | Number(021,10) | Sim | Preço unitário do serviço da nota fiscal de saída |
| PerDsc | Number(005,2) | Sim | Percentual de desconto do serviço da nota fiscal de entrada |
| PerIss | Number(006,4) | Sim | Percentual do ISS do serviço da nota fiscal de entrada |
| PerIrf | Number(004,2) | Sim | Percentual do IRRF do serviço da nota fiscal de entrada |
| PerIns | Number(004,2) | Sim | Percentual do INSS |
| SalCan | String(001) | Sim | Indicativo se o saldo da ordem de compra deve ser cancelado |
| NumPrj | Number(008,0) | Sim | Número do projeto |
| CodFpj | Number(004,0) | Sim | Código da fase do projeto |
| CtaFin | Number(007,0) | Sim | Conta financeira reduzida |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| CodCcu | String(009) | Sim | Código do centro de custo |
| VlrEnc | Number(015,2) | Sim | Valor encargos financeiros |
| VlrOut | Number(015,2) | Sim | Valor outras despesas |
| VlrDar | Number(015,2) | Sim | Valor para arredondamento |
| VlrOud | Number(015,2) | Sim | Valor outras despesas destacado |
| VlrBru | Number(015,2) | Sim | Valor bruto do serviço da nota fiscal de entrada |
| VlrDsc | Number(015,2) | Sim | Valor do desconto do serviço da nota fiscal de entrada |
| VlrDs1 | Number(015,2) | Sim | Valor do desconto - 1 do fornecedor |
| VlrDs2 | Number(015,2) | Sim | Valor do desconto - 2 do fornecedor |
| VlrBis | Number(015,2) | Sim | Valor base ISS |
| VlrIss | Number(015,2) | Sim | Valor do ISS sobre o serviço da nota fiscal de entrada |
| VlrBir | Number(015,2) | Sim | Valor base IRRF |
| VlrIrf | Number(015,2) | Sim | Valor do IRRF sobre o serviço da nota fiscal de entrada |
| VlrBin | Number(015,2) | Sim | Valor base do INSS |
| VlrIns | Number(015,2) | Sim | Valor do INSS |
| VlrLse | Number(015,2) | Sim | Valor do serviço |
| VlrLou | Number(015,2) | Sim | Valor dos outros valores |
| VlrLiq | Number(015,2) | Sim | Valor líquido do item de  serviço da nota fiscal de entrada |
| VlrFin | Number(015,2) | Sim | Valor do item válido para o financeiro |
| AcrFin | Number(015,2) | Sim | Valor de Acréscimo Financeiro |
| EmpNfv | Number(004,0) | Sim | Código da empresa da nota fiscal de saída |
| FilNfv | Number(005,0) | Sim | Código da filial da nota fiscal de saída |
| SnfNfv | String(003) | Sim | Série da nota fiscal de saída |
| NumNfv | Number(009,0) | Sim | Número da nota fiscal de saída |
| SeqIsv | Number(003,0) | Sim | Sequência do item da nota fiscal de saída |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| NumEpi | Number(009,0) | Sim | Identificador da inspeção aberta para o item |
| CodClf | String(003) | Sim | Código da classificação fiscal do item da nota fiscal de entrada |
| OriMer | String(001) | Sim | Origem fiscal da mercadoria |
| CodStr | String(003) | Sim | Situação tributária do item da nota fiscal de entrada |
| CodTic | String(003) | Sim | Código do ICMS especial |
| CodTrd | String(003) | Sim | Código de redução de impostos |
| CodTst | String(003) | Sim | Código do ICMS substituído |
| PerIpi | Number(008,4) | Sim | Percentual de IPI do item da nota fiscal de entrada |
| PerIcm | Number(007,4) | Sim | Percentual do ICM do item da nota fiscal de entrada |
| VlrDzf | Number(015,2) | Sim | Valor do desconto referente zona franca |
| VlrBip | Number(015,2) | Sim | Valor base IPI |
| VlrIpi | Number(015,2) | Sim | Valor do IPI do item da nota fiscal de entrada |
| VlrBid | Number(015,2) | Sim | Valor base IPI presumido (50% compra no comércio) |
| VlrIpd | Number(015,2) | Sim | Valor do IPI presumido (50% compra no comércio) |
| VlrBic | Number(015,2) | Sim | Valor base do ICMS |
| VlrIcm | Number(015,2) | Sim | Valor do ICMS do item da nota fiscal de entrada |
| VlrDfa | Number(015,2) | Sim | Valor da diferença de alíquota inter-estadual |
| VlrBsi | Number(015,2) | Sim | Valor base ICMS substituído |
| VlrIcs | Number(015,2) | Sim | Valor do ICMS substituído do item da nota fiscal de entrada |
| VlrBsd | Number(015,2) | Sim | Valor base ICMS substituído destacado |
| VlrIsd | Number(015,2) | Sim | Valor ICMS substituído destacado |
| VlrIip | Number(015,2) | Sim | Valor isentas IPI |
| VlrIic | Number(015,2) | Sim | Valor isentas ICMS |
| VlrOip | Number(015,2) | Sim | Valor outras IPI |
| VlrOic | Number(015,2) | Sim | Valor outros ICMS |
| VlrBpi | Number(015,2) | Sim | Valor base do PIS a recuperar |
| VlrPis | Number(015,2) | Sim | Valor do PIS a recuperar do item da nota fiscal de entrada |
| FilCtr | Number(005,0) | Sim | Código da filial do contrato de compra |
| NumCtr | Number(006,0) | Sim | Número do contrato que gerou a nota fiscal de entrada |
| DatCpt | Date | Sim | Mês e ano de competência do item do contrato |
| SeqCcs | Number(003,0) | Sim | Sequência do item do contrato na competência |
| IntPat | String(001) | Sim | Indica se o item deve ser mostrado para integração com a gestão de patrimônio |
| NotFor | Number(005,2) | Sim | Nota do fornecimento deste item |
| NotSer | Number(005,2) | Sim | Nota do serviço |
| VlrBcr | Number(015,2) | Sim | Valor base do Cofins a recuperar |
| VlrCor | Number(015,2) | Sim | Valor do Cofins a recuperar |
| VlrBct | Number(015,2) | Sim | Valor base do Cofins Retido |
| VlrCrt | Number(015,2) | Sim | Valor do Cofins Retido |
| PerCrt | Number(007,4) | Sim | Percentual de Cofins Retido |
| VlrBpt | Number(015,2) | Sim | Valor base do PIS Retido |
| VlrPit | Number(015,2) | Sim | Soma dos valores do PIS retido |
| PerPit | Number(007,4) | Sim | Percentual de PIS Retido |
| VlrBcl | Number(015,2) | Sim | Valor base do CSLL Retido |
| VlrCsl | Number(015,2) | Sim | Valor do CSLL Retido |
| PerCsl | Number(004,2) | Sim | Percentual de CSLL Retido |
| VlrBor | Number(015,2) | Sim | Valor base de Outras Retenções |
| VlrOur | Number(015,2) | Sim | Valor de Outras Retenções |
| PerOur | Number(004,2) | Sim | Percentual de Outras Retenções |
| VlrRis | Number(015,2) | Sim | Valor de retenção de ICMS Substituto |
| CodTpr | String(004) | Sim | Código da tabela de preço do serviço |
| PerDs1 | Number(005,2) | Sim | Percentual de desconto 1 |
| PerDs2 | Number(005,2) | Sim | Percentual de desconto 2 |
| PerDs3 | Number(005,2) | Sim | Percentual de desconto 3 |
| PerDs4 | Number(005,2) | Sim | Percentual de desconto 4 |
| PerDs5 | Number(005,2) | Sim | Percentual de desconto 5 |
| VlrDs3 | Number(015,2) | Sim | Valor do desconto 3 |
| VlrDs4 | Number(015,2) | Sim | Valor de desconto 4 |
| VlrDs5 | Number(015,2) | Sim | Valor de desconto 5 |
| BecIpi | Number(015,2) | Sim | Valor base de IPI creditado efetivamente |
| VecIpi | Number(015,2) | Sim | Valor de IPI creditado efetivamente |
| BecIcm | Number(015,2) | Sim | Valor base de ICMS creditado efetivamente |
| VecIcm | Number(015,2) | Sim | Valor ICMS Cred. Efetivamente |
| VlrBie | Number(015,2) | Sim | Valor base do INSS parte empresa |
| VlrIem | Number(015,2) | Sim | Valor do INSS parte empresa |
| VlrOui | Number(015,2) | Sim | Valor de outras despesas de importação |
| BcoImp | Number(015,2) | Sim | Valor base do cofins a recuperar na importação |
| CofImp | Number(015,2) | Sim | Valor do cofins a recuperar na importação |
| BpiImp | Number(015,2) | Sim | Valor base do pis a recuperar na importação |
| PisImp | Number(015,2) | Sim | Valor do pis a recuperar na importação |
| FilPed | Number(005,0) | Sim | Código da filial do pedido de venda |
| NumPed | Number(008,0) | Sim | Número do pedido de venda |
| SeqIsp | Number(003,0) | Sim | Sequência do item de serviço no pedido de venda |
| VlrBpf | Number(015,2) | Sim | Valor Base do PIS Faturamento (Estorno devolução) |
| PerPif | Number(008,4) | Sim | Percentual do PIS Faturamento (Estorno devolução) |
| VlrPif | Number(015,2) | Sim | Valor do PIS Faturamento (Estorno devolução) |
| VlrBcf | Number(015,2) | Sim | Valor Base do COFINS Faturamento (Estorno devolução) |
| PerCff | Number(008,4) | Sim | Percentual do COFINS Faturamento (Estorno devolução) |
| VlrCff | Number(015,2) | Sim | Valor do COFINS Faturamento (Estorno devolução) |
| BemPri | String(020) | Sim | Código do bem principal |
| CstIpi | String(002) | Sim | Código da situação tributária de IPI |
| CstPis | String(002) | Sim | Código da situação tributária de PIS |
| CstCof | String(002) | Sim | Código da situação tributária de COFINS |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| VlrAjs | Number(015,2) | Sim | Valor do ajuste do item referente ao dispositivo fiscal |
| SeqEve | Number(003,0) | Sim | Sequência do evento |
| NumOpe | String(020) | Sim | Número da Operação para rastreamento TMS |
| QtdBpi | Number(015,3) | Sim | Quantidade da base do PIS a recuperar |
| AliPis | Number(015,4) | Sim | Alíquota por Valor do PIS a recuperar |
| QtdBco | Number(015,3) | Sim | Quantidade da base do COFINS a recuperar |
| AliCof | Number(015,4) | Sim | Alíquota por Valor do COFINS a recuperar |
| QtdBip | Number(015,3) | Sim | Quantidade da base do IPI |
| AliIpi | Number(015,4) | Sim | Alíquota por Valor do IPI |
| QtdBpf | Number(015,3) | Sim | Quantidade da base do PIS por faturamento (Estorno devolução) |
| AliPif | Number(015,4) | Sim | Alíquota por valor do PIS por faturamento (Estorno devolução) |
| QtdBcf | Number(015,3) | Sim | Quantidade da base do COFINS por faturamento (Estorno devolução) |
| AliCff | Number(015,4) | Sim | Alíquota por Valor do COFINS por faturamento (Estorno devolução) |
| IndVis | String(001) | Sim | Indicativo de vínculo entre itens de serviço da NFE e OC via tela F440REL |
| PerCit | Number(005,2) | Sim | Percentual do imposto CIDE-Tecnologia |
| VlrCit | Number(015,2) | Sim | Valor do imposto CIDE-Tecnologia do item da nota fiscal de entrada |
| BasCre | Number(002,0) | Sim | Código da base de cálculo do crédito |
| PecIcm | Number(007,4) | Sim | Percentual do ICMS creditado efetivamente |
| PecIpi | Number(008,4) | Sim | Percentual do IPI creditado efetivamente |
| EmpCto | Number(004,0) | Sim | Código da empresa do período de apuração da comissão |
| CodPco | Number(004,0) | Sim | Código período para o controle de comissionamento |
| FilCto | Number(005,0) | Sim | Código da filial do período de apuração da comissão |
| CptPco | Date | Sim | Mês e ano base do comissionamento |
| PerPir | Number(008,4) | Sim | Percentual de PIS a Recuperar |
| PerCor | Number(008,4) | Sim | Percentual de COFINS a Recuperar |
| PerPim | Number(008,4) | Sim | Percentual de PIS a Recuperar na Importação |
| PerCim | Number(008,4) | Sim | Percentual de COFINS a Recuperar na Importação |
| PerIci | Number(005,2) | Sim | Percentual de ICMS na importação |
| CodBic | String(003) | Sim | Código da modalidade da base de cálculo do ICMS |
| VlrIbs | Number(015,2) | Sim | Valor base do ICMS Simples Nacional |
| VlrIsn | Number(015,2) | Sim | Valor do ICMS Simples Nacional do item da nota fiscal de entrada |
| PerIsn | Number(007,4) | Sim | Percentual do ICMS Simples Nacional do item da nota fiscal de entrada |
| NumLan | Number(009,0) | Sim | Número sequencial do lançamento destinado ao controle do crédito acumulado |
| IndInt | String(001) | Sim | Indicativo se este item de serviço foi vendido como intermediação |
| VarSer | String(001) | Sim | Indica o tipo de serviço para o Varejo |
| PerDif | Number(007,4) | Sim | Percentual de diferimento do item de serviço |
| BasIdf | Number(015,2) | Sim | Valor base do ICMS diferido |
| PerIdf | Number(005,2) | Sim | Percentual do ICMS diferido do item da nota fiscal de entrada |
| VlrIdf | Number(015,2) | Sim | Valor do ICMS diferido do item da nota fiscal de entrada |
| PerSen | Number(004,2) | Sim | Percentual do SENAR/SENAT |
| VlrBsn | Number(015,2) | Sim | Valor base do SENAR/SENAT |
| VlrSen | Number(015,2) | Sim | Valor do SENAR/SENAT |
| MotDes | Number(002,0) | Sim | Motivo desoneração ICMS |
| VlrIcd | Number(015,2) | Sim | ICMS Desonerado |
| AbtDes | String(001) | Sim | Indicativo se houve abatimento do valor do ICMS desonerado |
| CodEnq | Number(003,0) | Sim | Código de enquadramento legal do IPI |
| IcmAor | Number(005,2) | Sim | Alíquota de ICMS partilhado com o estado remetente |
| IcmVor | Number(015,2) | Sim | Valor de ICMS partilhado com o estado remetente |
| IcmAde | Number(005,2) | Sim | Alíquota de ICMS partilhado com o estado destinatário |
| IcmVde | Number(015,2) | Sim | Valor de ICMS partilhado com o estado destinatário |
| IcmBde | Number(015,2) | Sim | Valor Base ICMS partilha para estado de destino |
| IcmAfc | Number(007,4) | Sim | Alíquota do ICMS para fundo de combate à pobreza na UF de destino |
| IcmVfc | Number(015,2) | Sim | Valor do ICMS para fundo de combate à pobreza na UF de destino |
| CodCes | String(007) | Sim | Código especificador da substituição tributária |
| QecIpi | Number(015,3) | Sim | Quantidade da Base de IPI Creditado Efetivamente |
| AecIpi | Number(015,4) | Sim | Alíquota por Valor de IPI Creditado Efetivamente |
| RedIss | Number(008,5) | Sim | Percentual de redução da base de cálculo do ISS de entrada |
| VlrDed | Number(015,2) | Sim | Valor de Dedução na Base dos Impostos |
| PerIef | Number(005,2) | Sim | Percentual do ICMS entrega futura do item da nota |
| BasIef | Number(015,2) | Sim | Valor base do ICMS para entrega futura |
| VlrIef | Number(015,2) | Sim | Valores do ICMS para entrega futura |
| IcmBfc | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza na UF de destino |
| BasFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza |
| AliFcp | Number(007,4) | Sim | Alíquota do ICMS para fundo de combate à pobreza |
| VlrFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza |
| BstFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza retido por substituição tributária |
| AstFcp | Number(007,4) | Sim | Alíquota do fundo de combate à pobreza retido por substituição tributária |
| VstFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza retido por substituição tributária |
| BreFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza retido ant. por subst. trib. |
| AreFcp | Number(007,4) | Sim | Alíquota do fundo de combate à pobreza retido anteriormente por subst. trib. |
| VreFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza retido anteriormente por subst. trib. |
| CodBnf | String(010) | Sim | Código de Benefício Fiscal na UF aplicado ao serviço |
| BirRpa | Number(015,2) | Sim | Base acumulada do IRRF do período para fins de cálculo do RPA |
| BasApe | Number(015,2) | Sim | Base de cálculo da aposentadoria especial |
| PerApe | Number(004,2) | Sim | Percentual da aposentadoria especial |
| VlrApe | Number(015,2) | Sim | Valor da aposentadoria especial |
| VicStd | Number(015,2) | Sim | Valor do ICMS-ST desonerado |
| MtdIst | Number(002,0) | Sim | Motivo desoneração ICMS-ST |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| VdiFcp | Number(015,2) | Sim | Valor diferido do ICMS relativo ao FCP |
| EfiFcp | Number(015,2) | Sim | Valor efetivo do ICMS relativo ao FCP |
| SeqNfi | Number(004,0) | Sim | Sequência do item na nota fiscal impressa |
| CbfRbc | String(010) | Sim | Código de Benefício Fiscal de redução de base de cálculo |
| StrOri | String(003) | Sim | Situação tributária Original do item da nota fiscal de entrada |
| AliFus | Number(005,2) | Sim | Percentual do FUST |
| BasFus | Number(015,2) | Sim | Base de Cálculo do FUST |
| VlrFus | Number(015,2) | Sim | Valor do FUST |
| AliFnt | Number(005,2) | Sim | Percentual do FUNTTEL |
| BasFnt | Number(015,2) | Sim | Base de Cálculo do FUNTTEL |
| VlrFnt | Number(015,2) | Sim | Valor do FUNTTEL |
| CodNfc | String(007) | Sim | Código item cClass |
| IdeNbs | Number(009,0) | Sim | Identificador NBS |
| IndDev | String(001) | Sim | Indicativo se o item é uma devolução |
| VlrBcb | Number(015,4) | Sim | Valor da Base de Cálculo CBS/IBS Externo |
| SnfNfr | String(003) | Sim | Série da nota fiscal de entrada Ligada |
| ForNfr | Number(009,0) | Sim | Fornecedor da nota fiscal de entrada Ligada |
| NumNfr | Number(009,0) | Sim | Número da nota fiscal de entrada Ligada |
| SeqIsr | Number(003,0) | Sim | Sequência do item da nota fiscal de Entrada Ligada |
| USU_NumLan | Number(009,0) | Sim | Numero Lancamento CAT83 |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIsc

---

## Índices

### E440ISCIndice2

**Tipo:** Não unico

Campos:
- CodSer
- CodEmp
- CodFil

### E440ISCIndice3

**Tipo:** Não unico

Campos:
- NumOcp
- CodEmp
- FilOcp
- SeqIso

### E440ISCIndice4

**Tipo:** Não unico

Campos:
- CodEmp
- FilPed
- NumPed

---

## Relacionamentos

### IR_E440ISC_004

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |

### IR_E440ISC_017

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

