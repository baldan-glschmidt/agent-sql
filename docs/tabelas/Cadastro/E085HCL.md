# E085HCL

## Descrição

Cadastros - Clientes - Históricos

---

## Resumo

- Campos: 162
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SalDup | Number(015,2) | Sim | Saldo devedor de duplicatas dos clientes |
| SalOut | Number(015,2) | Sim | Saldo devedor de outros títulos dos clientes |
| SalCre | Number(015,2) | Sim | Saldo dos créditos dos clientes |
| DatLim | Date | Sim | Data da última atualização do limite de crédito do cliente |
| VlrLim | Number(015,2) | Sim | Valor do limite de crédito do cliente |
| LimApr | String(001) | Sim | Indicativo se o limite de crédito do cliente está ou não aprovado |
| VlrPfa | Number(015,2) | Sim | Soma das pré-faturas |
| DatMac | Date | Sim | Data da ocorrência do maior acúmulo de saldo devedor do cliente |
| VlrMac | Number(015,2) | Sim | Valor do maior acúmulo de saldo devedor do cliente |
| DatUpe | Date | Sim | Data do último pedido do cliente |
| VlrUpe | Number(015,2) | Sim | Valor do último pedido do cliente |
| DatUfa | Date | Sim | Data do último faturamento do cliente |
| VlrUfa | Number(015,2) | Sim | Valor do último faturamento do cliente |
| DatUpg | Date | Sim | Data do último pagamento do cliente |
| VlrUpg | Number(015,2) | Sim | Valor do último pagamento do cliente |
| QtdPgt | Number(009,0) | Sim | Quantidade total de pagamentos efetuados pelo cliente |
| DatUpc | Date | Sim | Data do último pagamento em cartório do cliente |
| VlrUpc | Number(015,2) | Sim | Valor do último pagamento em cartório do cliente |
| QtdTpc | Number(004,0) | Sim | Quantidade total de pagamentos em cartório do cliente |
| DatMfa | Date | Sim | Data da ocorrência da maior fatura do cliente |
| VlrMfa | Number(015,2) | Sim | Valor da maior fatura do cliente |
| DatAtr | Date | Sim | Data da ocorrência do maior atraso do cliente |
| VlrAtr | Number(015,2) | Sim | Valor de pagamento do maior atraso do cliente |
| MaiAtr | Number(004,0) | Sim | Quantidade de dias do maior atraso do cliente |
| MedAtr | Number(004,0) | Sim | Quantidade de dias de média de atraso do cliente |
| DatPmr | Date | Sim | Data de ínicio de contagem para cálculo do prazo médio de recebimento dos títulos |
| PrzMrt | Number(005,0) | Sim | Prazo médio de recebimento dos títulos do cliente |
| QtdRpm | Number(009,0) | Sim | Quantidade de títulos recebidos após data para prazo médio |
| QtdChs | Number(004,0) | Sim | Quantidade de cheques sem fundo do cliente |
| CatCli | Number(003,0) | Não | Categoria do cliente (prioridade para faturamento) |
| CodCca | String(003) | Sim | Código da categoria do cliente para a análise de crédito |
| AcePar | String(001) | Sim | Indicativo se o cliente aceita faturamento parcial de pedidos |
| QtdMfp | Number(003,0) | Sim | Quantidade máxima de faturas por pedido aceito pelo cliente |
| PerAqa | Number(005,2) | Sim | Percentual acima da quantidade do pedido aceito no faturamento pelo cliente |
| IndAgr | String(001) | Sim | Indicativo se o cliente só aceita grade completa (agrupamento derivação) |
| JunPed | String(001) | Sim | Indicativo se o cliente aceita juntar pedidos numa mesma nota |
| PerDs1 | Number(005,2) | Sim | Percentual de desconto - 1 para o cliente |
| PerDs2 | Number(005,2) | Sim | Percentual de desconto - 2 para o cliente |
| PerCom | Number(005,2) | Sim | Percentual de comissão nas vendas para o cliente (+ ou -) |
| CodCrp | String(003) | Sim | Código de grupo do contas a receber |
| CodRep | Number(009,0) | Sim | Código do representante padrão para o cliente |
| CodRve | String(003) | Sim | Código da região de venda do cliente |
| CodTpr | String(004) | Sim | Código da tabela de preço padrão para o cliente |
| CodCpg | String(006) | Sim | Código da condição de pagamento padrão para o cliente |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| QtdDcv | Number(003,0) | Sim | Quantidade de dias para cálculo de vencimento |
| CriEdv | String(001) | Sim | Critério para escolha do dia de vencimento das parcelas e títulos |
| CodTra | Number(009,0) | Sim | Código da transportadora padrão para o cliente |
| CodRed | Number(009,0) | Sim | Código da transportadora de redespacho padrão para o cliente |
| RecJmm | Number(005,2) | Sim | Percentual de juros de mora mês para o contas a receber |
| RecTjr | String(001) | Sim | Tipo de juros para contas a receber |
| RecDtj | Number(004,0) | Sim | Dias de tolerância para cálculo de juros de mora |
| RecMul | Number(005,2) | Sim | Percentual de multa para atraso contas a receber |
| RecDtm | Number(004,0) | Sim | Dias de tolerância para multa do contas a receber |
| PerDsc | Number(004,2) | Sim | Percentual padrão de desconto para os títulos gerados |
| TolDsc | Number(004,0) | Sim | Quantidade padrão de dias de tolerância para desconto |
| PrdDsc | String(001) | Sim | Indicativo do período para cálculo do desconto antecipado |
| AntDsc | String(001) | Sim | Indicativo se calcula desconto por antecipação de recebimento |
| PorSi1 | String(004) | Sim | Código do primeiro portador aceito pelo cliente |
| PorSi2 | String(004) | Sim | Código do segundo portador aceito pelo cliente |
| CodCrt | String(002) | Sim | Código da carteira padrão para o cliente |
| PorNa1 | String(004) | Sim | Código do primeiro portador não aceito pelo cliente |
| PorNa2 | String(004) | Sim | Código do segundo portador não aceito pelo cliente |
| CodIn1 | String(003) | Sim | Código da primeira instrução bancária |
| CodIn2 | String(003) | Sim | Código da segunda instrução bancária |
| CodBan | String(003) | Sim | Código do banco onde o cliente mantém conta corrente |
| TipTcc | Number(002,0) | Sim | Tipo de conta |
| CodAge | String(007) | Sim | Código da agência bancária onde o cliente mantém conta corrente |
| CcbCli | String(014) | Sim | Número da conta corrente bancária do cliente |
| CodFrj | String(003) | Sim | Código da fórmula de reajuste do título a receber |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| CtaAux | Number(009,0) | Sim | Número reduzido da conta de composição auxiliar - 1 |
| CtaAad | Number(009,0) | Sim | Número reduzido da conta de composição auxiliar - 2 |
| UsuAge | Number(010,0) | Sim | Código do usuário agente de turismo do cliente |
| ExiLcp | String(001) | Não | Indicativo se o cliente exige ligação de cliente X produto/derivação |
| PerFre | Number(005,2) | Sim | Percentual de Frete |
| PerSeg | Number(005,2) | Sim | Percentual de Seguro |
| PerEmb | Number(005,2) | Sim | Percentual de Embalagens |
| PerEnc | Number(005,2) | Sim | Percentual de Encargos |
| PerOut | Number(005,2) | Sim | Percentual de Outras Despesas |
| FveTns | String(010) | Sim | Hierarquia da Forma de Venda |
| FveFpg | String(010) | Sim | Hierarquia da Forma de Venda |
| FveCpg | String(010) | Sim | Hierarquia da Forma de Venda |
| PerIss | Number(006,4) | Sim | Percentual do ISS para os serviços prestados ao cliente |
| CodVen | Number(009,0) | Sim | Código do Vendedor do Cliente |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| CifFob | String(001) | Sim | Indicativo se o frete para o cliente é CIF ou FOB |
| CodTab | String(004) | Sim | Código da tabela de preço frete |
| PerDs3 | Number(005,2) | Sim | Percentual de desconto - 3 para o cliente |
| PerDs4 | Number(005,2) | Sim | Percentual de desconto - 4 para o cliente |
| PerOf1 | Number(005,2) | Sim | Percentual de oferta 1 para o cliente |
| PerOf2 | Number(005,2) | Sim | Percentual de oferta 2 para o cliente |
| CodMar | String(010) | Sim | Código da Marca/Etiqueta padrão do cliente |
| DiaEsp | String(001) | Sim | Indicativo do dia da semana para vencimento parcelas para o cliente |
| DiaMe1 | Number(002,0) | Sim | Primeiro dia especial do mês para vencimento das parcelas do cliente |
| DiaMe2 | Number(002,0) | Sim | Segundo dia especial do mês para vencimento das parcelas do cliente |
| DiaMe3 | Number(002,0) | Sim | Terceiro dia especial do mês para vencimento das parcelas do cliente |
| GerTcc | String(001) | Sim | Indicativo se, no momento do faturamento de um contrato, gera título para o cliente do contrato, e não do faturamento |
| ApmDen | String(001) | Sim | Aceita pedido com a mesma data de entrega |
| CtrPad | Number(009,0) | Sim | Número do contrato padrão |
| EpcPed | String(001) | Sim | Exige número do pedido do cliente no pedido |
| EcpCnp | String(001) | Sim | Exige código do produto do cliente no pedido |
| QdiPrt | Number(003,0) | Sim | Indicativo da quantidade de dias para protesto ("0" - não protesta) |
| QtdPrt | Number(004,0) | Sim | Quantidade de protestos do cliente |
| VlrPrt | Number(015,2) | Sim | Valor total de protestos do cliente |
| AcrDia | Number(005,2) | Sim | Percentual de acréscimo na diária paga ao motorista |
| ExiAge | String(001) | Sim | Indicativo se o cliente exige o agendamento da entrega |
| UltNfv | Number(009,0) | Sim | Último número de nota fiscal de saída faturada |
| UltSnf | String(003) | Sim | Código da série da última nota fiscal de saída |
| CodFcr | String(003) | Sim | Código da moeda ou índice como fator de correção dos contratos |
| CodPdv | Number(009,0) | Sim | Código interno no PDV |
| VlrAcr | Number(015,2) | Sim | Valor de acréscimo na diária paga ao motorista |
| PerDs5 | Number(005,2) | Sim | Percentual de desconto - 5 para o cliente |
| SeqCob | Number(005,0) | Sim | Sequência do endereço de cobrança padrão do cliente |
| SeqEnt | Number(005,0) | Sim | Sequência do endereço de entrega padrão do cliente |
| IndOrf | String(001) | Sim | Indica se o cliente obriga o recebimento do recibo para cobrança via fatura automática |
| CodTic | String(003) | Sim | Código do ICMS especial |
| CodTrd | String(003) | Sim | Código de redução de impostos |
| PerCcr | String(001) | Sim | Origem do percentual de comissão |
| DscPrd | String(001) | Sim | Desconsidera percentual de perda do componente utilizado para industrialização |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| AvaVlr | Number(015,2) | Sim | Valor total para avalizar |
| AvaVlu | Number(015,2) | Sim | Valor avalizado no atual momento |
| AvaVls | Number(015,2) | Sim | Valor disponível para avalizar |
| AvaAti | String(001) | Sim | Determina se o cliente pode ser usado como avalista |
| AvaMot | Number(006,0) | Sim | Código do motivo usado para justificar porque o avalista está inativo |
| AvaObs | String(250) | Sim | Observação do motivo da inativação do avalista |
| AvdAlt | Date | Sim | Data da última alteração das informações do avalista |
| AvhAlt | Number(005,0) | Sim | Hora da última alteração das informações do avalista |
| AvuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração das informações do avalista |
| AvdGer | Date | Sim | Data de geração das informações do avalista |
| AvhGer | Number(005,0) | Sim | Hora de geração das informações do avalista |
| AvuGer | Number(010,0) | Sim | Usuário responsável pela geração das informações do avalista |
| CodFin | Number(004,0) | Sim | Código da finalidade de venda |
| DscAnt | Number(004,2) | Sim | Percentual de desconto por antecipação para os títulos gerados |
| DscPon | Number(004,2) | Sim | Percentual de desconto por pontualidade para os títulos gerados |
| MotDes | Number(002,0) | Sim | Motivo desoneração ICMS |
| CodStr | String(003) | Sim | Código da situação tributária do cliente |
| VolSep | String(001) | Sim | Indicativo se deve separar os componentes/volumes ao gerar o pedido |
| ConFin | String(001) | Sim | Consumidor Final |
| IndPre | String(001) | Sim | Indicativo presencial do consumidor |
| PerDif | Number(007,4) | Sim | Percentual de diferimento configurado para o cliente |
| PerIsr | Number(006,4) | Sim | Percentual do ISS retido para DF, exclusivo para construção civil |
| ZerDif | String(001) | Sim | Indicativo se deve zerar o cálculo do Difal na nota fiscal de saída |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| CodDes | Number(009,0) | Sim | Código do Destinatário do serviço prestado |
| USU_LimTer | Number(015,2) | Sim | Limite de Crédito Terceiro |
| USU_PorLim | String(004) | Sim | Portador do Limite |

---

## Chave Primária

- CodCli
- CodEmp
- CodFil

---

## Índices

### E085HCLIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

### IR_E085HCL_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E085HCL_002

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

