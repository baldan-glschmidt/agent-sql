# E140ISV

## Descrição

Vendas - Notas Fiscais de Saída - Itens de Serviços

---

## Resumo

- Campos: 253
- Chave Primária: 5 campo(s)
- Índices: 4
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIsv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| TnsSer | String(005) | Sim | Transação do item de serviço da nota |
| NopSer | String(005) | Sim | Código da natureza de operação |
| FilPed | Number(005,0) | Sim | Código da filial do pedido |
| NumPed | Number(008,0) | Sim | Número do pedido da nota fiscal de saída |
| SeqIsp | Number(003,0) | Sim | Sequência do pedido da nota fiscal de saída |
| FilCtr | Number(005,0) | Sim | Código da filial do contrato de venda |
| NumCtr | Number(009,0) | Sim | Número do contrato que gerou a nota fiscal de saída |
| DatCpt | Date | Sim | Mês e ano de competência do item do contrato |
| SeqCvs | Number(003,0) | Sim | Sequência do item do contrato na competência |
| CodSer | String(014) | Sim | Código do serviço da nota fiscal de saída |
| CodFam | String(006) | Sim | Código da família do serviço |
| CodTri | String(005) | Sim | Código de tributação para emissão da DARF |
| CplIsv | String(250) | Sim | Complemento da descrição do serviço |
| QtdFat | Number(014,5) | Sim | Quantidade faturada do serviço da nota fiscal de saída |
| QtdDev | Number(014,5) | Sim | Soma das quantidades devolvidas das NF de entrada |
| UniMed | String(003) | Não | Unidade de medida do serviço da nota fiscal de saída |
| CodTpr | String(004) | Sim | Código da tabela de preço do item da nota fiscal de saída |
| PreUni | Number(021,10) | Sim | Preço unitário do serviço da nota fiscal de saída |
| PerDsc | Number(005,2) | Sim | Percentual de desconto do serviço da nota fiscal de saída |
| PerIss | Number(006,4) | Sim | Percentual do ISS do serviço da nota fiscal de saída |
| PerIrf | Number(004,2) | Sim | Percentual do IRRF do serviço da nota fiscal de saída |
| PerIns | Number(004,2) | Sim | Percentual do INSS |
| PerCom | Number(005,2) | Sim | Percentual de comissão do serviço da nota fiscal de saída |
| SalCan | String(001) | Sim | Indicativo se o saldo do pedido deve ser cancelado |
| NumPrj | Number(008,0) | Sim | Número do projeto |
| CodFpj | Number(004,0) | Sim | Código da fase do projeto |
| CtaFin | Number(007,0) | Sim | Conta financeira reduzida |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| CodCcu | String(009) | Sim | Código do centro de custo |
| VlrEnc | Number(015,2) | Sim | Valor encargos financeiros |
| VlrOut | Number(015,2) | Sim | Valor outras despesas |
| VlrDar | Number(015,2) | Sim | Valor para arredondamento |
| VlrOud | Number(015,2) | Sim | Valor outras despesas destacado |
| VlrBru | Number(015,2) | Sim | Valor bruto do serviço da nota fiscal de saída |
| VlrDsc | Number(015,2) | Sim | Valor do desconto do serviço da nota fiscal de saída |
| VlrDs1 | Number(015,2) | Sim | Valor do desconto - 1 do cliente |
| VlrDs2 | Number(015,2) | Sim | Valor do desconto - 2 do cliente |
| VlrDs3 | Number(015,2) | Sim | Valor do desconto - 3 do cliente |
| VlrDs4 | Number(015,2) | Sim | Valor do desconto - 4 do cliente |
| VlrBis | Number(015,2) | Sim | Valor base ISS |
| VlrIss | Number(015,2) | Sim | Valor do ISS sobre o serviço da nota fiscal de saída |
| VlrBir | Number(015,2) | Sim | Valor base IRRF |
| VlrIrf | Number(015,2) | Sim | Valor do IRRF sobre o serviço da nota fiscal de saída |
| VlrBin | Number(015,2) | Sim | Valor base do INSS |
| VlrIns | Number(015,2) | Sim | Valor do INSS |
| VlrBco | Number(015,2) | Sim | Valor base comissão |
| VlrCom | Number(015,2) | Sim | Valor comissão |
| VlrLse | Number(015,2) | Sim | Valor do serviço |
| VlrLou | Number(015,2) | Sim | Valor dos outros valores |
| VlrLiq | Number(015,2) | Sim | Valor líquido do item de serviço da nota fiscal de saída |
| VlrFin | Number(015,2) | Sim | Valor do item válido para o financeiro |
| FilNfc | Number(005,0) | Sim | Código da filial da nota fiscal de entrada |
| CodFor | Number(009,0) | Sim | Código do Fornecedor |
| NumNfc | Number(009,0) | Sim | Número da nota fiscal de entrada |
| SnfNfc | String(003) | Sim | Código da série da nota fiscal de entrada |
| SeqIsc | Number(003,0) | Sim | Sequência do item de serviço da NF de entrada |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| ObsIsv | String(999) | Sim | Observação do item |
| CodClf | String(003) | Sim | Código da classificação fiscal do item da nota fiscal de saída |
| CodStr | String(003) | Sim | Situação tributária do I.C.M.S. do item da nota fiscal de saída |
| CodTic | String(003) | Sim | Código do ICMS especial |
| CodTrd | String(003) | Sim | Código de redução de Impostos |
| CodTst | String(003) | Sim | Código do ICMS substituído |
| PerIpi | Number(008,4) | Sim | Percentual de IPI do item da nota fiscal de saída |
| PerIcm | Number(005,2) | Sim | Percentual do ICM do item da nota fiscal de saída |
| VlrDzf | Number(015,2) | Sim | Valor do desconto referente zona franca |
| VlrBip | Number(015,2) | Sim | Valor base IPI |
| VlrIpi | Number(015,2) | Sim | Valor do IPI do item da nota fiscal de saída |
| VlrBic | Number(015,2) | Sim | Valor base ICMS |
| VlrIcm | Number(015,2) | Sim | Valor do ICMS do item da nota fiscal de saída |
| VlrDfa | Number(015,2) | Sim | Valor da diferença de alíquota inter-estadual |
| VlrBsi | Number(015,2) | Sim | Valor base ICMS substituído |
| VlrIcs | Number(015,2) | Sim | Valor do ICMS substituído do item da nota fiscal de saída |
| VlrBsd | Number(015,2) | Sim | Valor base ICMS substituído destacado |
| VlrIsd | Number(015,2) | Sim | Valor do ICMS substituído destacado |
| VlrIip | Number(015,2) | Sim | Valor isento IPI |
| VlrIic | Number(015,2) | Sim | Valor isento ICMS |
| VlrOip | Number(015,2) | Sim | Valor outros IPI |
| VlrOic | Number(015,2) | Sim | Valor outros ICMS |
| VlrBpi | Number(015,2) | Sim | Valor base do PIS (Estorno Devolução) |
| VlrPis | Number(015,2) | Sim | Valor do PIS a recuperar (Estorno Devolução) do item da nota fiscal de saída |
| VlrBcr | Number(015,2) | Sim | Valor base do Cofins à Recuperar (Estorno Devolução) |
| VlrCor | Number(015,2) | Sim | Valor do Cofins a recuperar (Estorno Devolução) |
| VlrBct | Number(015,2) | Sim | Valor base do Cofins Retido |
| VlrCrt | Number(015,2) | Sim | Valor do Cofins Retido |
| PerCrt | Number(004,2) | Sim | Percentual de Cofins Retido |
| VlrBpt | Number(015,2) | Sim | Valor base do PIS Retido |
| VlrPit | Number(015,2) | Sim | Soma dos valores do PIS retido |
| PerPit | Number(004,2) | Sim | Percentual de PIS Retido |
| VlrBcl | Number(015,2) | Sim | Valor base do CSLL Retido |
| VlrCsl | Number(015,2) | Sim | Valor do CSLL  Retido |
| PerCsl | Number(004,2) | Sim | Percentual de CSLL Retido |
| VlrBor | Number(015,2) | Sim | Valor base de Outras Retenções |
| VlrOur | Number(015,2) | Sim | Valor de Outras Retenções |
| PerOur | Number(004,2) | Sim | Percentual de Outras Retenções |
| SeqNfi | Number(004,0) | Sim | Sequência do item na nota fiscal impressa |
| PerDs1 | Number(005,2) | Sim | Percentual de desconto - 1 do cliente |
| PerDs2 | Number(005,2) | Sim | Percentual de desconto - 2 do cliente |
| PerDs3 | Number(005,2) | Sim | Percentual de desconto - 3 do cliente |
| PerDs4 | Number(005,2) | Sim | Percentual de desconto - 4 do cliente |
| VlrRis | Number(015,2) | Sim | Valor de retenção de ICMS Substituto |
| DesImp | String(250) | Sim | Descrição do produto impressa na nota, para fins de relatórios fiscais (Sintegra) |
| CptFat | Date | Sim | Competência Faturada |
| VlrOui | Number(015,2) | Sim | Valor de outras despesas de importação |
| BcoImp | Number(015,2) | Sim | Valor base do cofins a recuperar na importação |
| CofImp | Number(015,2) | Sim | Valor do cofins a recuperar na importação |
| BpiImp | Number(015,2) | Sim | Valor base do pis a recuperar na importação |
| PisImp | Number(015,2) | Sim | Valor do pis a recuperar na importação |
| VlrBpf | Number(015,2) | Sim | Valor Base do PIS Faturamento |
| PerPif | Number(008,4) | Sim | Percentual do PIS Faturamento |
| VlrPif | Number(015,2) | Sim | Valor do PIS Faturamento |
| VlrBcf | Number(015,2) | Sim | Valor Base do COFINS Faturamento |
| PerCff | Number(008,4) | Sim | Percentual do COFINS Faturamento |
| VlrCff | Number(015,2) | Sim | Valor do COFINS Faturamento |
| VlrBsf | Number(015,2) | Sim | Valor base do ICMS Substituído para entrega futura |
| VlrSif | Number(015,2) | Sim | Valores do ICMS Substituído para entrega futura |
| CstIpi | String(002) | Sim | Código da situação tributária de IPI |
| CstPis | String(002) | Sim | Código da situação tributária de PIS |
| CstCof | String(002) | Sim | Código da situação tributária de COFINS |
| PerDs5 | Number(005,2) | Sim | Percentual de desconto - 5 do cliente |
| VlrDs5 | Number(015,2) | Sim | Valor do desconto - 5 do cliente |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| VlrAjs | Number(015,2) | Sim | Valor do ajuste do item referente ao dispositivo fiscal |
| PreRep | Number(014,5) | Sim | Valor de Repasse |
| CodMs1 | Number(004,0) | Sim | Código da mensagem - 1 do item da nota fiscal de saída |
| CodMs2 | Number(004,0) | Sim | Código da mensagem - 2 do item da nota fiscal de saída |
| CodMs3 | Number(004,0) | Sim | Código da mensagem - 3 do item da nota fiscal de saída |
| CodMs4 | Number(004,0) | Sim | Código da mensagem - 4 do item da nota fiscal de saída |
| NumOpe | String(020) | Sim | Número da Operação para rastreamento TMS |
| QtdBpi | Number(015,3) | Sim | Quantidade da base do PIS a recuperar (Estorno devolução) |
| AliPis | Number(015,4) | Sim | Alíquota por Valor do PIS a recuperar (Estorno devolução) |
| QtdBco | Number(015,3) | Sim | Quantidade da base do COFINS a recuperar (Estorno devolução) |
| AliCof | Number(015,4) | Sim | Alíquota por Valor do COFINS a recuperar (Estorno devolução) |
| QtdBip | Number(015,3) | Sim | Quantidade da base do IPI |
| AliIpi | Number(015,4) | Sim | Alíquota por valor do IPI |
| QtdBpf | Number(015,3) | Sim | Quantidade da base do PIS por faturamento |
| AliPif | Number(015,4) | Sim | Alíquota por valor do PIS por faturamento |
| QtdBcf | Number(015,3) | Sim | Quantidade da base do COFINS por faturamento |
| AliCff | Number(015,4) | Sim | Alíquota por Valor do COFINS por faturamento |
| TraFat | Number(014,5) | Sim | Quantidade faturada do contrato via geração do CTRC |
| NatPis | Number(005,0) | Sim | Natureza da receita do PIS |
| NatCof | Number(005,0) | Sim | Natureza da receita do COFINS |
| CodRep | Number(009,0) | Sim | Código do representante do item de serviço da nota fiscal de saída |
| FilRef | Number(005,0) | Sim | Filial do pedido base referente a este serviço |
| PedRef | Number(008,0) | Sim | Número do pedido base referente a este serviço |
| SeqRef | Number(003,0) | Sim | Sequencia doítem do pedido base referente a este serviço |
| OriMer | String(001) | Sim | Origem fiscal da mercadoria |
| VlrPfm | Number(015,2) | Sim | Valor do frete a ser pago ao motorista que levará o produto |
| VarSer | String(001) | Sim | Indica o tipo de serviço para o Varejo |
| EmpFre | Number(004,0) | Sim | Código da empresa |
| TabFre | String(004) | Sim | Código da tabela de preço frete |
| DatIni | Date | Sim | Data início de validade da tabela de preço |
| LocEnt | Number(008,0) | Sim | Código da localização do local para entrega do frete |
| SeqFlc | Number(004,0) | Sim | Sequência da localização do frete |
| FilFre | Number(005,0) | Sim | Código da filial |
| EmpIpv | Number(004,0) | Sim | Empresa do ítem do cupom |
| FilIpv | Number(005,0) | Sim | Filial do ítem do cupom |
| SnfIpv | String(003) | Sim | Código da série do ítem do cupom |
| NfvIpv | Number(009,0) | Sim | Número da nota fiscal do ítem do cupom fiscal |
| SeqIpv | Number(003,0) | Sim | Sequência do item do cupom fiscal |
| EmpCto | Number(004,0) | Sim | Código da empresa do período de apuração da comissão |
| CodPco | Number(004,0) | Sim | Código período para o controle de comissionamento |
| FilCto | Number(005,0) | Sim | Código da filial do período de apuração da comissão |
| CptPco | Date | Sim | Mês e ano base do comissionamento |
| VlrDed | Number(015,2) | Sim | Valor de Deduções |
| IndInt | String(001) | Sim | Indicativo se este item de serviço foi vendido como intermediação |
| CodBic | String(003) | Sim | Código da modalidade da base de cálculo do ICMS |
| VlrIbs | Number(015,2) | Sim | Valor base do ICMS Simples Nacional |
| VlrIsn | Number(015,2) | Sim | Valor do ICMS Simples Nacional |
| PerIsn | Number(005,2) | Sim | Percentual de aliquota de ICMS simples nacional |
| DtiGar | Date | Sim | Data inicial de vigência da garantia |
| DtfGar | Date | Sim | Data final de vigência da garantia |
| VlrAis | Number(015,2) | Sim | Valor aproximado de imposto do item de serviço no cupom |
| PerAis | Number(005,2) | Sim | Percentual aproximado de imposto do item de serviço no cupom |
| NumLan | Number(009,0) | Sim | Número sequencial do lançamento destinado ao controle do crédito acumulado |
| VlrIdv | Number(015,2) | Sim | Valor do IPI devolvido |
| BilGar | String(050) | Sim | Número do Bilhete da garantia estendida |
| PerDif | Number(007,4) | Sim | Percentual de diferimento do item de serviço |
| BasIdf | Number(015,2) | Sim | Valor base do ICMS diferido |
| PerIdf | Number(007,4) | Sim | Percentual do ICMS diferido do item da nota fiscal de saída |
| VlrIdf | Number(015,2) | Sim | Valor do ICMS diferido do item da nota fiscal de saída |
| CstIss | String(010) | Sim | Situação tributária do ISS do serviço |
| CodFim | String(010) | Sim | Código fiscal municipal do serviço |
| CodAtv | String(016) | Sim | Código de atividade do item de serviço |
| PerMgc | Number(014,5) | Sim | Percentual de Margem de Contribuição utilizada para a venda |
| TipGar | String(002) | Sim | Tipo de Garantia Estendida |
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
| BasIef | Number(015,2) | Sim | Valor base do ICMS para entrega futura |
| PerIef | Number(005,2) | Sim | Percentual do ICMS para entrega futura |
| VlrIef | Number(015,2) | Sim | Valor do ICMS para entrega futura |
| CodCnm | String(050) | Sim | Código passível de ser consumido. |
| NumSer | String(050) | Sim | Número de série do código passível de ser consumido. |
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
| BasApe | Number(015,2) | Sim | Base de cálculo da aposentadoria especial |
| PerApe | Number(004,2) | Sim | Percentual da aposentadoria especial |
| VlrApe | Number(015,2) | Sim | Valor da aposentadoria especial |
| RedIss | Number(008,5) | Sim | Percentual de redução da base de cálculo do ISS |
| VicStd | Number(015,2) | Sim | Valor do ICMS-ST desonerado |
| MtdIst | Number(002,0) | Sim | Motivo desoneração ICMS-ST |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| VdiFcp | Number(015,2) | Sim | Valor diferido do ICMS relativo ao FCP |
| EfiFcp | Number(015,2) | Sim | Valor efetivo do ICMS relativo ao FCP |
| CbfRbc | String(010) | Sim | Código de Benefício Fiscal de redução de base de cálculo |
| AliFus | Number(005,2) | Sim | Percentual do FUST |
| BasFus | Number(015,2) | Sim | Base de Cálculo do FUST |
| VlrFus | Number(015,2) | Sim | Valor do FUST |
| AliFnt | Number(005,2) | Sim | Percentual do FUNTTEL |
| BasFnt | Number(015,2) | Sim | Base de Cálculo do FUNTTEL |
| VlrFnt | Number(015,2) | Sim | Valor do FUNTTEL |
| CnpjLD | Number(014,0) | Sim | Informar o CNPJ da operadora LD que irá lançar o item de cofaturamento em nota do tipo faturamento 2 |
| DocIdeLD | String(014) | Sim | Informar o CNPJ da operadora LD que irá lançar o item de cofaturamento em nota do tipo faturamento 2 |
| SnfNfr | String(003) | Sim | Série da nota fiscal de saída |
| NumNfr | Number(009,0) | Sim | Número da nota fiscal de saída |
| SeqIsr | Number(003,0) | Sim | Sequência do item da nota fiscal de saída |
| CodNfc | String(007) | Sim | Código item cClass |
| IdeNbs | Number(009,0) | Sim | Identificador NBS |
| VlrCBS | Number(013,2) | Sim | Valor da CBS de origem |
| VlrIBU | Number(013,2) | Sim | Valor do IBS Estadual de origem |
| VlrIBM | Number(013,2) | Sim | Valor do IBS Municipal de origem |
| VlrRee | Number(015,2) | Sim | Valor do reembolso |
| VlrDer | Number(015,2) | Sim | Valor de dedução/redução da base de cálculo do IBS/CBS |
| USU_NumLan | Number(009,0) | Sim | Numero Lancamento CAT83 |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIsv

---

## Índices

### E140ISVIndice2

**Tipo:** Não unico

Campos:
- CodSer
- CodEmp
- CodFil

### E140ISVIndice3

**Tipo:** Não unico

Campos:
- NumPed
- CodEmp
- FilPed
- SeqIsp

### E140ISVIndice4

**Tipo:** Não unico

Campos:
- CodEmp
- FilCtr
- NumCtr
- SeqCvs
- DatCpt

### E140ISVIndice5

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- SnfNfr
- NumNfr
- SeqIsr

---

## Relacionamentos

### IR_E140ISV_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

