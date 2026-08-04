# E000IPC

## Descrição

Tabelas - Recebimento de Documentos Eletrônicos - Notas Fiscais de Entrada - Itens de Produto

---

## Resumo

- Campos: 257
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CgcFil | Number(015,0) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| DocIdeFil | String(014) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| CgcFor | Number(014,0) | Sim | Número do CNPJ ou CPF do fornecedor |
| DocIdeFor | String(014) | Sim | Número do CNPJ ou CPF do fornecedor |
| ChvNel | String(050) | Não | Chave de acesso da nota fiscal eletrônica |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| NumNfc | Number(009,0) | Sim | Número da nota fiscal de entrada |
| CodSnf | String(003) | Sim | Código da série da nota fiscal de entrada |
| TnsPro | String(005) | Sim | Transação de produto do item da nota |
| NopPro | String(005) | Sim | Código da natureza de operação |
| NumOcp | Number(008,0) | Sim | Número da ordem de compra da nota fiscal de entrada |
| SeqIpo | Number(004,0) | Sim | Sequência do item na ordem de compra da nota fiscal de entrada |
| CodPro | String(014) | Sim | Código do produto da nota fiscal de entrada |
| CodDer | String(007) | Sim | Código da derivação do produto da nota fiscal de entrada |
| CplIpc | String(250) | Sim | Complemento da descrição do produto |
| CodFam | String(006) | Sim | Código da família do produto |
| CodClf | String(003) | Sim | Código da classificação fiscal do item da nota fiscal de entrada |
| CodStr | String(003) | Sim | Situação tributária do item da nota fiscal de entrada |
| CodTic | String(003) | Sim | Código do ICMS especial |
| CodTrd | String(003) | Sim | Código de redução de impostos |
| CodTst | String(003) | Sim | Código do ICMS substituído |
| CodStp | String(003) | Sim | Código de substituição do PIS |
| CodStc | String(003) | Sim | Código de substituição do COFINS |
| LauTec | String(250) | Sim | Laudo Técnico do Produto |
| UsuLau | Number(009,0) | Sim | Código do usuário que informou o laudo técnico |
| DatLau | Date | Sim | Data da informação do laudo técnico |
| HorLau | Number(005,0) | Sim | Hora da informação do laudo técnico |
| CodDep | String(010) | Sim | Código do depósito para entrada de estoque do produto |
| CodLot | String(050) | Sim | Código do lote de fabricação do produto |
| QtdRec | Number(014,5) | Sim | Quantidade recebida do item da nota fiscal de entrada |
| UniNfc | String(006) | Sim | Código da unidade de medida da nota fiscal de entrada |
| QtdAjb | Number(014,5) | Sim | Quantidade de Ajuste de Balança para Efeito de Estoque |
| QtdDev | Number(014,5) | Sim | Quantidade devolvida do item da nota fiscal de entrada |
| UniMed | String(006) | Não | Unidade de medida de estoque do item da nota fiscal de entrada |
| QtdEst | Number(014,5) | Sim | Quantidade de entrada conforme unidade de medida de estoque |
| VlrFum | Number(015,2) | Sim | Valor do frete por unidade de medida quando CIF |
| QtdFre | Number(014,5) | Sim | Quantidade base na unidade do produto valida para o valor do frete |
| ForFre | Number(009,0) | Sim | Código do fornecedor para geração título de frete |
| PesBru | Number(021,10) | Sim | Peso bruto do item da nota fiscal de entrada |
| PesLiq | Number(021,10) | Sim | Peso líquido do item da nota fiscal de entrada |
| CodTpr | String(004) | Sim | Código da tabela de preço do produto |
| PreUni | Number(021,10) | Sim | Preço unitário do item da nota fiscal de entrada |
| PreEst | Number(021,10) | Sim | Preço do item conforme unidade de medida de estoque |
| PreBas | Number(021,10) | Sim | Preço unitário base para o movimento de estoque |
| PerDsc | Number(005,2) | Sim | Percentual de desconto do item da nota fiscal de entrada |
| PerDs3 | Number(005,2) | Sim | Percentual de desconto 3 |
| PerDs4 | Number(005,2) | Sim | Percentual de desconto 4 |
| PerDs5 | Number(005,2) | Sim | Percentual de desconto 5 |
| PerIpi | Number(008,4) | Sim | Percentual de IPI do item da nota fiscal de entrada |
| PerIcm | Number(007,4) | Sim | Percentual do ICM do item da nota fiscal de entrada |
| PerFun | Number(004,2) | Sim | Percentual do Funrural ou INSS |
| SalCan | String(001) | Sim | Indicativo se o saldo do item da O.C. deverá ser cancelado |
| NumPrj | Number(008,0) | Sim | Número do projeto |
| CodFpj | Number(004,0) | Sim | Código da fase do projeto |
| CtaFin | Number(007,0) | Sim | Conta financeira reduzida |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| CodCcu | String(009) | Sim | Código do centro de custo |
| VlrFre | Number(015,2) | Sim | Valor frete |
| VlrSeg | Number(015,2) | Sim | Valor do seguro |
| VlrEmb | Number(015,2) | Sim | Valor embalagem |
| VlrEnc | Number(015,2) | Sim | Valor encargos financeiros |
| VlrOut | Number(015,2) | Sim | Valor outras despesas |
| VlrDar | Number(015,2) | Sim | Valor para arredondamento |
| VlrFrd | Number(015,2) | Sim | Valor frete destacado |
| VlrOud | Number(015,2) | Sim | Valor outras despesas destacado |
| VlrBru | Number(015,2) | Sim | Valor bruto do item da nota fiscal de entrada |
| VlrDsc | Number(015,2) | Sim | Valor do desconto do item da nota fiscal de entrada |
| VlrDs1 | Number(015,2) | Sim | Valor do desconto 1 |
| VlrDs2 | Number(015,2) | Sim | Valor do desconto 2 |
| VlrDs3 | Number(015,2) | Sim | Valor de desconto 3 |
| VlrDs4 | Number(015,2) | Sim | Valor de desconto 4 |
| VlrDs5 | Number(015,2) | Sim | Valor de desconto 5 |
| VlrDzf | Number(015,2) | Sim | Valor do desconto referente zona franca |
| VlrBfu | Number(015,2) | Sim | Valor base do Funrural ou INSS |
| VlrFun | Number(015,2) | Sim | Valor do Funrural ou INSS |
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
| VlrBsp | Number(015,2) | Sim | Valor base da substituição tributário do PIS |
| VlrStp | Number(015,2) | Sim | Valor da substituição tributária do PIS |
| VlrBsc | Number(015,2) | Sim | Valor base da substituição tributário da COFINS |
| VlrStc | Number(015,2) | Sim | Valor da substituição tributária do COFINS |
| VlrIip | Number(015,2) | Sim | Valor isentas IPI |
| VlrIic | Number(015,2) | Sim | Valor isentas ICMS |
| VlrOip | Number(015,2) | Sim | Valor outras IPI |
| VlrOic | Number(015,2) | Sim | Valor outros ICMS |
| VlrLpr | Number(015,2) | Sim | Valor do produto |
| VlrLou | Number(015,2) | Sim | Valor dos outros valores |
| VlrLiq | Number(015,2) | Sim | Valor líquido do item da nota fiscal de entrada |
| VlrFin | Number(015,2) | Sim | Valor do item válido para o financeiro |
| AcrFin | Number(015,2) | Sim | Valor de Acréscimo Financeiro |
| EmpNfv | Number(004,0) | Sim | Código da empresa da nota fiscal de saída |
| SnfNfv | String(003) | Sim | Série da nota fiscal de saída |
| NumNfv | Number(009,0) | Sim | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Sim | Sequência do item da nota fiscal de saída |
| CgcFab | Number(014,0) | Sim | Código do Fabricante |
| DocIdeFab | String(014) | Sim | Código do Fabricante |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| NumEpi | Number(009,0) | Sim | Identificador da inspeção aberta para a liberação do item |
| DatVlt | Date | Sim | Data de validade do lote |
| VlrBpi | Number(015,2) | Sim | Valor base do PIS a recuperar |
| VlrPis | Number(015,2) | Sim | Valor do PIS a recuperar do item da nota fiscal de entrada |
| FilCtr | Number(005,0) | Sim | Código da filial do contrato de compra |
| NumCtr | Number(006,0) | Sim | Número do contrato que gerou a nota fiscal de entrada |
| DatCpt | Date | Sim | Mês e ano de competência do item do contrato |
| SeqCcp | Number(003,0) | Sim | Sequência do item do contrato na competência |
| IntPat | String(001) | Sim | Indica se o item será mostrado para integração com a gestão de patrimônio |
| NotFor | Number(005,2) | Sim | Nota do fornecimento deste item |
| NotPro | Number(005,2) | Sim | Nota do produto |
| ProFab | String(021) | Sim | Código do produto no Fabricante |
| SeqIsc | Number(003,0) | Sim | Sequência do item na nota fiscal de entrada relacionado ao item de produto. |
| VlrBcr | Number(015,2) | Sim | Valor base do Cofins a recuperar |
| VlrCor | Number(015,2) | Sim | Valor do Cofins a recuperar |
| PerIim | Number(005,2) | Sim | Percentual de imposto de importação do item da nota fiscal de entrada |
| VlrBii | Number(015,2) | Sim | Valor base imposto de importação |
| VlrIim | Number(015,2) | Sim | Valor do imposto de importação do item da nota fiscal de entrada |
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
| PerDs1 | Number(005,2) | Sim | Percentual de desconto 1 |
| PerDs2 | Number(005,2) | Sim | Percentual de desconto 2 |
| BecIpi | Number(015,2) | Sim | Valor base de IPI creditado efetivamente |
| VecIpi | Number(015,2) | Sim | Valor de IPI creditado efetivamente |
| BecIcm | Number(015,2) | Sim | Valor base de ICMS creditado efetivamente |
| VecIcm | Number(015,2) | Sim | Valor ICMS Cred. Efetivamente |
| ProFor | String(060) | Sim | Código do produto no fornecedor |
| VlrFei | Number(015,2) | Sim | Valor de frete de importação |
| VlrSei | Number(015,2) | Sim | Valor de seguro de importação |
| VlrOui | Number(015,2) | Sim | Valor de outras despesas de importação |
| BcoImp | Number(015,2) | Sim | Valor base do cofins a recuperar na importação |
| CofImp | Number(015,2) | Sim | Valor do cofins a recuperar na importação |
| BpiImp | Number(015,2) | Sim | Valor base do pis a recuperar na importação |
| PisImp | Number(015,2) | Sim | Valor do pis a recuperar na importação |
| FilPed | Number(005,0) | Sim | Código da filial do pedido de venda |
| NumPed | Number(008,0) | Sim | Número do pedido de venda |
| SeqIpd | Number(004,0) | Sim | Sequência do item de produto no pedido de venda |
| VlrDm1 | Number(014,5) | Sim | Valor Dimensão 1 |
| VlrDm2 | Number(014,5) | Sim | Valor Dimensão 2 |
| VlrDm3 | Number(014,5) | Sim | Valor Dimensão 3 |
| VlrDm4 | Number(014,5) | Sim | Valor Dimensão 4 |
| VlrDm5 | Number(014,5) | Sim | Valor Dimensão 5 |
| VlrDm6 | Number(014,5) | Sim | Valor Dimensão 6 |
| BemPri | String(020) | Sim | Código do bem principal |
| VlrBpf | Number(015,2) | Sim | Valor Base do PIS Faturamento (Estorno devolução) |
| PerPif | Number(008,4) | Sim | Percentual do PIS Faturamento (Estorno devolução) |
| VlrPif | Number(015,2) | Sim | Valor do PIS Faturamento (Estorno devolução) |
| VlrBcf | Number(015,2) | Sim | Valor Base do COFINS Faturamento (Estorno devolução) |
| PerCff | Number(008,4) | Sim | Percentual do COFINS Faturamento (Estorno devolução) |
| VlrCff | Number(015,2) | Sim | Valor do COFINS Faturamento (Estorno devolução) |
| CstIpi | String(002) | Sim | Código da situação tributária de IPI |
| CstPis | String(002) | Sim | Código da situação tributária de PIS |
| CstCof | String(002) | Sim | Código da situação tributária de COFINS |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| VlrAjs | Number(015,2) | Sim | Valor do ajuste do item referente ao dispositivo fiscal |
| SeqEve | Number(003,0) | Sim | Sequência do evento |
| NumAdi | Number(003,0) | Sim | Número da adição |
| SeqAdi | Number(005,0) | Sim | Número sequencial do item dentro da adição |
| DscAdi | Number(015,2) | Sim | Valor do desconto do item da DI - adição |
| FabEst | String(010) | Sim | Código do fabricante estrangeiro |
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
| VlrSub | Number(015,2) | Sim | Valor do subsídio na nota fiscal de compra |
| IndVip | String(001) | Sim | Indicativo de vínculo entre itens de produto da NFE e OC via tela F440REL |
| OriMer | String(001) | Sim | Origem fiscal da mercadoria |
| PerCit | Number(005,2) | Sim | Percentual do imposto CIDE-Tecnologia |
| VlrCit | Number(015,2) | Sim | Valor do imposto CIDE-Tecnologia do item da nota fiscal de entrada |
| BasCre | Number(002,0) | Sim | Código da base de cálculo do crédito |
| CgcOcp | Number(015,0) | Sim | CNPJ Filial OC |
| DocIdeOcp | String(014) | Sim | CNPJ Filial OC |
| CgcNfv | Number(015,0) | Sim | CNPJ Filial NF |
| DocIdeNfv | String(014) | Sim | CNPJ Filial NF |
| CodBar | String(030) | Sim | Código de barras livre |
| CodFci | String(036) | Sim | Código da ficha de conteúdo de importação (FCI) |
| VlrIbs | Number(015,2) | Sim | Valor base do ICMS Simples Nacional |
| VlrIsn | Number(015,2) | Sim | Valor do ICMS Simples Nacional do item da nota fiscal de entrada |
| PerIsn | Number(007,4) | Sim | Percentual do ICMS Simples Nacional do item da nota fiscal de entrada |
| NumDrb | String(020) | Sim | Número do ato concessório de Drawback |
| PerDif | Number(007,4) | Sim | Percentual de diferimento do item |
| BasIdf | Number(015,2) | Sim | Valor base do ICMS diferido |
| PerIdf | Number(005,2) | Sim | Percentual do ICMS diferido do item |
| VlrIdf | Number(015,2) | Sim | Valor do ICMS diferido do item |
| PerPir | Number(008,4) | Sim | Percentual de PIS a Recuperar |
| PerCor | Number(008,4) | Sim | Percentual de COFINS a Recuperar |
| PecIcm | Number(007,4) | Sim | Percentual do ICMS creditado efetivamente |
| PecIpi | Number(008,4) | Sim | Percentual do IPI creditado efetivamente |
| PerPim | Number(008,4) | Sim | Percentual de PIS a Recuperar na Importação |
| PerCim | Number(008,4) | Sim | Percentual de COFINS a Recuperar na Importação |
| VlrImp | Number(015,2) | Sim | Valor da parcela importada do exterior |
| CoeFci | Number(005,2) | Sim | Coeficiente do conteúdo de importação calculado |
| PerIci | Number(005,2) | Sim | Percentual de ICMS na importação |
| PerSen | Number(004,2) | Sim | Percentual do Senar |
| VlrBsn | Number(015,2) | Sim | Valor base do Senar |
| VlrSen | Number(015,2) | Sim | Valor do Senar |
| CodBic | String(003) | Sim | Código da modalidade da base de cálculo do ICMS |
| VlrAfm | Number(015,2) | Sim | Valor adicional ao frete para renovação da marinha mercante |
| GenA01 | String(080) | Sim | Tratamentos externos ao ERP no item de Produto - A1 |
| GenA02 | String(080) | Sim | Tratamentos externos ao ERP no item de Produto - A2 |
| GenA03 | String(080) | Sim | Tratamentos externos ao ERP no item de Produto - A3 |
| GenA04 | String(080) | Sim | Tratamentos externos ao ERP no item de Produto - A4 |
| GenN01 | Number(015,2) | Sim | Tratamentos externos ao ERP no item de Produto - N1 |
| GenN02 | Number(015,2) | Sim | Tratamentos externos ao ERP no item de Produto - N2 |
| GenN03 | Number(015,2) | Sim | Tratamentos externos ao ERP no item de Produto - N3 |
| GenN04 | Number(015,2) | Sim | Tratamentos externos ao ERP no item de Produto - N4 |
| MotDes | Number(002,0) | Sim | Motivo desoneração ICMS |
| VlrIcd | Number(015,2) | Sim | ICMS Desonerado |
| CodEnq | Number(003,0) | Sim | Código de enquadramento legal do IPI |
| IcmAor | Number(005,2) | Sim | Alíquota de ICMS partilhado com o estado remetente |
| IcmVor | Number(015,2) | Sim | Valor de ICMS partilhado com o estado remetente |
| IcmAde | Number(005,2) | Sim | Alíquota de ICMS partilhado com o estado destinatário |
| IcmVde | Number(015,2) | Sim | Valor de ICMS partilhado com o estado destinatário |
| IcmBde | Number(015,2) | Sim | Valor Base ICMS partilha para estado de destino |
| IcmAfc | Number(007,4) | Sim | Alíquota do ICMS para fundo de combate à pobreza na UF de destino |
| IcmVfc | Number(015,2) | Sim | Valor do ICMS para fundo de combate à pobreza na UF de destino |
| CodCes | String(007) | Sim | Código especificador da substituição tributária |
| GenA05 | String(080) | Sim | Tratamentos externos ao ERP no item de Produto - A5 |
| GenA06 | String(080) | Sim | Tratamentos externos ao ERP no item de Produto - A6 |
| GenN05 | Number(013,2) | Sim | Tratamentos externos ao ERP no item de Produto - N5 |
| GenN06 | Number(013,2) | Sim | Tratamentos externos ao ERP no item de Produto - N6 |
| QecIpi | Number(015,3) | Sim | Quantidade da Base de IPI Creditado Efetivamente |
| AecIpi | Number(015,4) | Sim | Alíquota por Valor de IPI Creditado Efetivamente |
| PerIef | Number(005,2) | Sim | Percentual do ICMS entrega futura do item da nota |
| BasIef | Number(015,2) | Sim | Valor base do ICMS para entrega futura |
| VlrIef | Number(015,2) | Sim | Valores do ICMS para entrega futura |
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| IdeNfc | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

### E000IPCIndice1

**Tipo:** Não unico

Campos:
- DocIdeFil
- DocIdeFor
- ChvNel
- SeqIpc

### E000IPCIndice2

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel
- SeqIpc

### E000IPCIndice3

**Tipo:** Não unico

Campos:
- IdeNfc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
