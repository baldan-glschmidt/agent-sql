# E120ISP

## Descrição

Vendas - Pedidos - Itens de Serviço

---

## Resumo

- Campos: 186
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqIsp | Number(003,0) | Não | Sequência do item de serviço no pedido |
| TnsSer | String(005) | Sim | Transação do item de serviço do pedido |
| CodSer | String(014) | Sim | Código do serviço do pedido |
| CplIsp | String(250) | Sim | Complemento da descrição do serviço |
| CodFam | String(006) | Sim | Código da Família do Serviço |
| CodTri | String(005) | Sim | Código de tributação para emissão da DARF |
| NumCad | Number(009,0) | Sim | Número do cadastro do operador que executou o serviço |
| QtdPed | Number(014,5) | Não | Quantidade pedida conforme a unidade de medida do serviço |
| QtdRea | Number(014,5) | Sim | Quantidade real conforme a unidade de medida do serviço |
| QtdFat | Number(014,5) | Sim | Quantidade faturada do serviço do pedido |
| QtdCan | Number(014,5) | Sim | Quantidade cancelada do serviço do pedido |
| QtdAbe | Number(014,5) | Sim | Quantidade em aberto do serviço do pedido |
| UniMed | String(003) | Não | Unidade de medida do serviço do pedido |
| CodMcp | String(003) | Sim | Moeda ou índice para correção do preço unitário |
| DatMfp | Date | Sim | Data da cotação da moeda para o fechamento do pedido |
| CotMfp | Number(019,10) | Sim | Valor da cotação da moeda para o fechamento do pedido |
| DatMoe | Date | Sim | Data da cotação da moeda para o faturamento do serviço |
| CotMoe | Number(019,10) | Sim | Valor da cotação da moeda para o faturamento do serviço |
| FecMoe | String(001) | Sim | Indicativo se o valor da cotação para o faturamento do serviço é fechado |
| DatEnt | Date | Não | Data de previsão de entrega do serviço |
| CodTpr | String(004) | Sim | Código da tabela de preço do serviço do pedido |
| PreUni | Number(021,10) | Não | Preço unitário do serviço do pedido |
| CodMoe | String(003) | Sim | Código da moeda/índice que o preço unitário está representado |
| PerDsc | Number(005,2) | Sim | Percentual de desconto do serviço do pedido |
| PerIss | Number(006,4) | Sim | Percentual do ISS do serviço do pedido |
| PerIrf | Number(004,2) | Sim | Percentual do IRRF do serviço do pedido |
| PerIns | Number(004,2) | Sim | Percentual do INSS |
| PerCom | Number(005,2) | Sim | Percentual de comissão do serviço do pedido |
| NumPrj | Number(008,0) | Sim | Número do projeto |
| CodFpj | Number(004,0) | Sim | Código da fase do projeto |
| CtaFin | Number(007,0) | Sim | Conta financeira reduzida |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| CodCcu | String(009) | Sim | Código do centro de custo |
| VlrEnc | Number(015,2) | Sim | Valor encargos financeiros |
| VlrOut | Number(015,2) | Sim | Valor outras despesas |
| VlrDar | Number(015,2) | Sim | Valor para arredondamento |
| VlrBru | Number(015,2) | Sim | Valor bruto do serviço do pedido |
| VlrDsc | Number(015,2) | Sim | Valor do desconto do serviço do pedido |
| VlrDs1 | Number(015,2) | Sim | Valor do desconto - 1 do cliente |
| VlrDs2 | Number(015,2) | Sim | Valor do desconto - 2 do cliente |
| VlrDs3 | Number(015,2) | Sim | Valor do desconto - 3 do cliente |
| VlrDs4 | Number(015,2) | Sim | Valor do desconto - 4 do cliente |
| VlrBis | Number(015,2) | Sim | Valor base ISS |
| VlrIss | Number(015,2) | Sim | Valor do ISS do serviço do pedido |
| VlrBir | Number(015,2) | Sim | Valor base IRRF |
| VlrIrf | Number(015,2) | Sim | Valor do IRRF do serviço do pedido |
| VlrBin | Number(015,2) | Sim | Valor base do INSS |
| VlrIns | Number(015,2) | Sim | Valor do INSS |
| VlrBco | Number(015,2) | Sim | Valor base comissão |
| VlrCom | Number(015,2) | Sim | Valor comissão |
| VlrLse | Number(015,2) | Sim | Valor do serviço |
| VlrLou | Number(015,2) | Sim | Valor dos outros valores |
| VlrLiq | Number(015,2) | Sim | Valor líquido do item de serviço do pedido |
| VlrFin | Number(015,2) | Sim | Valor do item válido para o financeiro |
| SitIsp | Number(001,0) | Não | Situação do item de serviço do pedido |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do item de serviço |
| ObsMot | String(250) | Sim | Observação do motivo da situação do serviço |
| NumCtr | Number(006,0) | Sim | Número interno de controle |
| DatCpt | Date | Sim | Mês e ano de competência do controle |
| SeqCvs | Number(003,0) | Sim | Sequência de controle para itens de programação de faturamento |
| PedCli | String(020) | Sim | Número do pedido do cliente |
| SeqPcl | String(010) | Sim | Sequência do item no pedido do cliente |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| ObsIsp | String(999) | Sim | Observação do item |
| FilOcp | Number(005,0) | Sim | Código da filial da Ordem de Compra |
| NumOcp | Number(008,0) | Sim | Número da ordem de compra |
| SeqIso | Number(004,0) | Sim | Sequência do item de serviço na ordem de compra |
| CodTic | String(003) | Sim | Código do ICMS especial |
| CodTrd | String(003) | Sim | Código de redução de impostos |
| CodTst | String(003) | Sim | Código do ICMS substituído |
| PerIpi | Number(008,4) | Sim | Percentual de IPI do serviço do pedido |
| PerIcm | Number(005,2) | Sim | Percentual de ICMS do serviço do pedido |
| VlrDzf | Number(015,2) | Sim | Valor do desconto referente zona franca |
| VlrBip | Number(015,2) | Sim | Valor base IPI |
| VlrIpi | Number(015,2) | Sim | Valor do IPI para o serviço do pedido |
| VlrBic | Number(015,2) | Sim | Valor Base ICMS |
| VlrIcm | Number(015,2) | Sim | Valor do ICMS |
| VlrBsi | Number(015,2) | Sim | Valor base ICMS substituído |
| VlrIcs | Number(015,2) | Sim | Valor do ICMS Substituído para o serviço do pedido |
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
| PerDs1 | Number(005,2) | Sim | Percentual de desconto - 1 do cliente |
| PerDs2 | Number(005,2) | Sim | Percentual de desconto - 2 do cliente |
| PerDs3 | Number(005,2) | Sim | Percentual de desconto - 3 do cliente |
| PerDs4 | Number(005,2) | Sim | Percentual de desconto - 4 do cliente |
| VlrRis | Number(015,2) | Sim | Valor de retenção de ICMS Substituto |
| GerNec | Number(001,0) | Sim | Indicativo de geração de necessidades para efeito de produção |
| EmpOcp | Number(004,0) | Sim | Código da empresa da ordem de compra |
| VlrBpf | Number(015,2) | Sim | Valor Base do PIS Faturamento |
| PerPif | Number(008,4) | Sim | Percentual do PIS Faturamento |
| VlrPif | Number(015,2) | Sim | Valor do PIS Faturamento |
| VlrBcf | Number(015,2) | Sim | Valor Base do COFINS Faturamento |
| PerCff | Number(008,4) | Sim | Percentual do COFINS Faturamento do pedido |
| VlrCff | Number(015,2) | Sim | Valor do COFINS Faturamento |
| PerDs5 | Number(005,2) | Sim | Percentual de desconto - 5 do cliente |
| VlrDs5 | Number(015,2) | Sim | Valor do desconto - 5 do cliente |
| QtdBpf | Number(015,3) | Sim | Quantidade da base do PIS por faturamento |
| AliPif | Number(015,4) | Sim | Alíquota por valor do PIS por faturamento |
| QtdBcf | Number(015,3) | Sim | Quantidade da base do COFINS por faturamento |
| AliCff | Number(015,4) | Sim | Alíquota por valor do COFINS por faturamento |
| QtdBip | Number(015,3) | Sim | Quantidade da base do IPI |
| AliIpi | Number(015,4) | Sim | Alíquota por valor do IPI |
| FilCtr | Number(005,0) | Sim | Código da filial do contrato de venda |
| CtrCvs | Number(009,0) | Sim | Número do contrato de serviço que gerou o item de serviço |
| SeqCtr | Number(003,0) | Sim | Sequência do item de serviço do contrato que gerou o item do pedido |
| CptCvs | Date | Sim | Mês e ano de competência do item de serviço que gerou o item de produto |
| FilRef | Number(005,0) | Sim | Filial do pedido base referente a este serviço |
| PedRef | Number(008,0) | Sim | Número do pedido base referente a este serviço |
| SeqRef | Number(003,0) | Sim | Sequencia doítem do pedido base referente a este serviço |
| VlrPfm | Number(015,2) | Sim | Valor do frete a ser pago ao motorista que levará o produto |
| VarSer | String(001) | Sim | Indica o tipo de serviço para o Varejo |
| SenApr | String(050) | Sim | Senha para liberação da pendência de aprovação |
| EmpFre | Number(004,0) | Sim | Código da empresa |
| TabFre | String(004) | Sim | Código da tabela de preço frete |
| DatIni | Date | Sim | Data início de validade da tabela de preço |
| LocEnt | Number(008,0) | Sim | Código da localização do local para entrega do frete |
| SeqFlc | Number(004,0) | Sim | Sequência da localização do frete |
| FilFre | Number(005,0) | Sim | Código da filial |
| CodRep | Number(009,0) | Sim | Código do representante |
| PerMgc | Number(014,5) | Sim | Percentual de Margem de Contribuição utilizada para a venda |
| PerJur | Number(005,2) | Sim | Percentual de juros aplicado ao item para a geração das parcelas |
| VlrOud | Number(015,2) | Sim | Valor outras despesas destacado |
| PerDif | Number(007,4) | Sim | Percentual de diferimento do item de serviço |
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
| IcmAor | Number(005,2) | Sim | Alíquota de ICMS partilhado com o estado remetente |
| IcmVor | Number(015,2) | Sim | Valor de ICMS partilhado com o estado remetente |
| IcmAde | Number(005,2) | Sim | Alíquota de ICMS partilhado com o estado destinatário |
| IcmVde | Number(015,2) | Sim | Valor de ICMS partilhado com o estado destinatário |
| IcmBde | Number(015,2) | Sim | Valor Base ICMS partilha para estado de destino |
| IcmAfc | Number(007,4) | Sim | Alíquota do ICMS para fundo de combate à pobreza na UF de destino |
| IcmVfc | Number(015,2) | Sim | Valor do ICMS para fundo de combate à pobreza na UF de destino |
| FilNfv | Number(005,0) | Sim | Código da filial |
| SnfNfv | String(003) | Sim | Código da série da nota fiscal |
| NumNfv | Number(009,0) | Sim | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Sim | Sequência do item da nota fiscal de saída |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| VlrTot | Number(015,2) | Sim | Valor total antes de liquidar. Usado no Varejo Terceiros |
| IteCan | String(001) | Sim | Indicativo se o item foi cancelado antes do faturamento (Varejo Terceiros) |
| DscVar | Number(015,2) | Sim | Valor do desconto para o serviço do pedido. Usado no Varejo Terceiros |
| PdsVar | Number(005,2) | Sim | Percentual de desconto para o serviço do pedido. Usado no Varejo Terceiros |
| NumInt | String(020) | Sim | Número do Documento Externo (Integrado) |
| IcmBfc | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza na UF de destino |
| BasFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza |
| AliFcp | Number(007,4) | Sim | Alíquota do ICMS para fundo de combate à pobreza |
| VlrFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza |
| BstFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza retido por substituição tributária |
| AstFcp | Number(007,4) | Sim | Alíquota do fundo de combate à pobreza retido por substituição tributária |
| VstFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza retido por substituição tributária |
| VicStd | Number(015,2) | Sim | Valor do ICMS-ST desonerado |
| MtdIst | Number(002,0) | Sim | Motivo desoneração ICMS-ST |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| VdiFcp | Number(015,2) | Sim | Valor diferido do ICMS relativo ao FCP |
| EfiFcp | Number(015,2) | Sim | Valor efetivo do ICMS relativo ao FCP |
| IdeNbs | Number(009,0) | Sim | Identificador NBS |
| VlrCBS | Number(015,2) | Sim | Valor da CBS de origem |
| VlrIBU | Number(015,2) | Sim | Valor do IBS Estadual de origem |
| VlrIBM | Number(015,2) | Sim | Valor do IBS Municipal de origem |
| VlrRee | Number(015,2) | Sim | Valor do reembolso |
| VlrDer | Number(015,2) | Sim | Valor de dedução/redução da base de cálculo do IBS/CBS |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIsp

---

## Índices

### E120ISPIndice2

**Tipo:** Não unico

Campos:
- CodSer
- DatEnt
- CodEmp
- CodFil

### E120ISPIndice3

**Tipo:** Não unico

Campos:
- DatEnt
- CodSer
- CodEmp
- CodFil

---

## Relacionamentos

### IR_E120ISP_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

