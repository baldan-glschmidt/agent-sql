# E012FAM

## Descrição

Cadastros - Famílias

---

## Resumo

- Campos: 160
- Chave Primária: 2 campo(s)
- Índices: 2
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFam | String(006) | Não | Código da família de produto |
| DesFam | String(050) | Não | Descrição da família de produto |
| TipPro | String(001) | Não | Tipo de produto (C=Comprado, P=Produzido, S=Serviço) |
| CodOri | String(003) | Não | Código de origem do produto |
| DepPad | String(010) | Sim | Depósito padrão p/ Produtos desta Família |
| CtrVld | String(001) | Não | Indicativo da forma de controle da data de validade nos estoques |
| CtrLot | String(001) | Não | Controla Entrada/Saída no Estoque por  Lote |
| CtrSep | String(001) | Não | Controla Entrada/Saídas no Estoque  por Série |
| PosPro | Number(002,0) | Não | Quantidade de posições para o código de produto |
| CodMdp | String(008) | Sim | Código da máscara de derivação |
| UniMed | String(003) | Não | Unidade de Medida dos Produtos associado a Família (Unidade Medida de Estocagem) |
| UniMe2 | String(003) | Sim | Código da segunda unidade de medida (Quando p/ Produzido é Unidade Medida da Ficha) |
| UniMe3 | String(003) | Sim | Código da terceira unidade de medida |
| UtiDec | String(001) | Não | Casas Decimais p/ Arredondamento de Quantidade é Determinada pela Família |
| QtdDec | Number(001,0) | Sim | Quantidade de Casas Decimais p/ Arredondamento em Cálculos (até 5 casas decimais p/ 1ª Unidade Medida) |
| CodEt1 | Number(004,0) | Sim | Código do 1º estágio de produção |
| CodEt2 | Number(004,0) | Sim | Código do 2º estágio de produção |
| CodEt3 | Number(004,0) | Sim | Código do 3º estágio de produção |
| CodEt4 | Number(004,0) | Sim | Código do 4º estágio de produção |
| CodEt5 | Number(004,0) | Sim | Código do 5º estágio de produção |
| CodEt6 | Number(004,0) | Sim | Código do 6º estágio de produção |
| CodEt7 | Number(004,0) | Sim | Código do 7º estágio de produção |
| CodEt8 | Number(004,0) | Sim | Código do 8º estágio de produção |
| CodEt9 | Number(004,0) | Sim | Código do 9º estágio de produção |
| TemCte | String(001) | Não | Indicativo se a família de produto tem ou não características |
| NumOri | Number(004,0) | Não | Número do nível da origem do produto |
| QtdMlt | Number(012,5) | Sim | Quantidade múltipla para cálculo da geração de ordem produção |
| QtdMin | Number(012,5) | Sim | Quantidade mínima para uma ordem de produção/compra |
| QtdMax | Number(012,5) | Sim | Quantidade máxima para uma ordem de produção/compra |
| QtdGop | Number(012,5) | Sim | Quantidade máxima para cada guia de produção |
| BxaOrp | String(001) | Não | Se for componente de alguma OP, indica se o mesmo é baixado |
| CodAge | String(005) | Sim | Código de agrupamento para estoques dos produtos da família |
| CodAgp | String(005) | Sim | Código de agrupamento para produção dos produtos da família |
| CodAgu | String(005) | Sim | Código de agrupamento para custos dos produtos da família |
| CodAgc | String(005) | Sim | Código de agrupamento comercial(compras ou vendas) dos produtos da família |
| CodAgt | String(005) | Sim | Código de agrupamento para cotas de venda |
| CodAgf | String(005) | Sim | Código de agrupamento para Impostos dos produtos da família |
| CodClf | String(003) | Sim | Código interno da classificação fiscal para os produtos da família |
| CodStr | String(003) | Sim | Código interno da situação tributária para os produtos da família |
| RecIpi | String(001) | Não | Indicativo se os produtos da família recuperam ou não IPI |
| RecCof | String(001) | Sim | Indicativo se as notas fiscais poderão ter recuperação de Cofins |
| TemIcm | String(001) | Não | Indicativo se os produtos da família tem ou não ICMS |
| CodTic | String(003) | Sim | Código do ICMS especial para os produtos da família |
| CodTrd | String(003) | Sim | Código de redução de impostos para os produtos da família |
| CodTst | String(003) | Sim | Código do ICMS substituído para os produtos da família |
| CodStp | String(003) | Sim | Código da substituição tributária do PIS |
| CodStc | String(003) | Sim | Código da substituição tributária do COFINS |
| RecIcm | String(001) | Não | Indicativo se os produtos da família recuperam ou não ICMS |
| GerEan | String(001) | Sim | Indicativo se gera código de barras EAN13 p/ o produto automaticamente |
| CodMp1 | String(008) | Sim | Código da Máscara para 1ª parte do código do produto |
| CodMp2 | String(008) | Sim | Código da Máscara para 2ª parte do código do produto |
| CodMp3 | String(008) | Sim | Código da Máscara para 3ª parte do código do produto |
| CodMp4 | String(008) | Sim | Código da Máscara para 4ª parte do código do produto |
| CodMp5 | String(008) | Sim | Código da Máscara para 5ª parte do código do produto |
| CodMp6 | String(008) | Sim | Código da Máscara para 6ª parte do código do produto |
| CodMp7 | String(008) | Sim | Código da Máscara para 7ª parte do código do produto |
| RotPro | String(001) | Não | Roteiro Informado é Utilizado p/ todas as Derivações do Produto (S=Sim, N=Não) |
| MatDir | String(001) | Não | Indicativo se o Material é Direto (produto comprado que é utilizado na fabricação de produtos produzidos) |
| CodReg | Number(004,0) | Sim | Código de Regra p/ cálculo de dígito verificador do código do produto |
| CodNtg | Number(004,0) | Sim | Código da natureza de gasto |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| CtaDcd | Number(007,0) | Sim | Conta contábil reduzida - 5 |
| CtaDci | Number(007,0) | Sim | Conta contábil reduzida - 6 |
| IndKit | String(001) | Não | Indicativo que os produtos produzidos desta família são "Kit" c/ vários produtos agregados p/ venda (não gera OP) |
| CodPin | String(020) | Sim | Código do Plano de Inspeção padrão para os produtos desta |
| NotFor | Number(005,2) | Sim | Nota mínima necessária para a aprovação de um fornecedor. |
| IndMis | String(001) | Não | Indicativo que o produto é produzido mas também pode ser comprado (Misto) |
| EmiGtr | String(001) | Sim | Indicativo se é emitida a guia de tráfego para o produto |
| SomIim | String(001) | Sim | Indicativo se calcula ICMS importação nas notas fiscais de importação e ordens de compra |
| RecPis | String(001) | Sim | Indicativo se o produto recupera ou não PIS |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para integração |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| TipInt | Number(001,0) | Sim | Tipo de Integração |
| SomIil | String(001) | Sim | Indicativo se deve ser somado o valor do ICMS no valor líquido das notas fiscais de importação e ordens de compra |
| CodMar | String(010) | Sim | Código da Marca/Etiqueta da família |
| CodClc | String(010) | Sim | Código da coleção da família |
| NivCbn | Number(004,0) | Sim | Utilizado p/ ordenar em ordem crescente as famílias na geração das combinações. |
| SitCal | String(001) | Sim | Situação do Cálculo Necessidades/Geração OPs (A=Ativo, I=Inativo) |
| GerOrp | String(001) | Não | Indica se o produto gera ordem de produção. |
| PerIrf | Number(004,2) | Sim | Percentual do IRRF previsto para venda do produto |
| PerPis | Number(008,4) | Sim | Percentual de PIS válido para o produto |
| PerCof | Number(008,4) | Sim | Percentual de Cofins válido para o produto |
| PerCsl | Number(004,2) | Sim | Percentual de CSLL válido para o produto |
| PerOur | Number(004,2) | Sim | Percentual de Outras Retenções válido para o produto |
| SomIps | String(001) | Sim | Indicativo se calcula PIS importação nas notas fiscais de importação e ordens de compra |
| SomIco | String(001) | Sim | Indicativo se calcula COFINS importação nas notas fiscais de importação e ordens de compra |
| SomIpl | String(001) | Sim | Indicativo se deve ser somado o valor do PIS no valor líquido das notas fiscais de importação e ordens de compra |
| SomIcl | String(001) | Sim | Indicativo se deve ser somado o valor do COFINS no valor líquido das notas fiscais de importação e ordens de compra |
| IndOct | String(001) | Sim | Indica se as famílias de produtos/serviços podem ser orçados |
| IndSpr | String(001) | Sim | Indicativo se Serviço é Produzido |
| PreCus | Number(015,6) | Sim | Preço de custo a ser sugerido pelo sistema no momento de inserir uma derivação |
| SitFam | String(001) | Sim | Situação da família do produto (Ativo ou Inativo) |
| ProImp | Number(002,0) | Sim | Indicativo do tipo de produto para impostos |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| IntAgr | String(001) | Sim | Indicativo se produtos desta família devem integrar com agronegócio |
| CtrVis | String(001) | Não | Controla valor individual da série |
| DatVis | Date | Sim | Data da última alteração do controle do valor individual da série |
| HorVis | Number(005,0) | Sim | Hora da última alteração do controle de valor individual da série |
| DiaRep | Number(004,0) | Sim | Quantidade de dias de reposição (comprado)/dias precedentes p/ paralelismo (produzido) |
| IndFrt | String(001) | Sim | Indicativo se a origem é de ferramentas |
| FrtEqp | String(001) | Sim | Indicativo se as Ferramentas serão usadas como equipamentos |
| GrpFrt | String(004) | Sim | Código do grupo padrão de ferramentas |
| CstIpi | String(002) | Sim | Código da situação tributária de IPI nas operações de venda |
| CstPis | String(002) | Sim | Código da situação tributária de PIS nas operações de venda |
| CstCof | String(002) | Sim | Código da situação tributária de COFINS nas operações de venda |
| CstIpc | String(002) | Sim | Código da situação tributária de IPI nas operações de compra |
| CstPic | String(002) | Sim | Código da situação tributária de PIS nas operações de compra |
| CstCoc | String(002) | Sim | Código da situação tributária de COFINS nas operações de compra |
| VarPro | String(001) | Sim | Indica o tipo de produto para o Varejo |
| ProMon | String(001) | Sim | Indicativo se o produto exige montagem |
| FinCrp | Number(007,0) | Sim | Conta financeira de receita(saída) padrão para efeito de rateio |
| FinCdp | Number(007,0) | Sim | Conta financeira de despesa(entrada) padrão para efeito de rateio |
| PerPim | Number(008,4) | Sim | Percentual de PIS de importação diferenciado |
| PerCim | Number(008,4) | Sim | Percentual de Cofins de importação diferenciado |
| AplAtx | String(004) | Sim | Código da aplicação do autotexto |
| CodAtx | Number(010,0) | Sim | Código do autotexto |
| IndIcp | String(001) | Sim | Indicativo se OPs da família permitem a incorporação de produtos |
| MgcMin | Number(015,6) | Sim | Percentual de margem de contribuição mínima |
| MgcLim | Number(015,6) | Sim | Percentual de margem de contribuição limite |
| PerVen | Number(024,12) | Sim | Percentual adicional do vendedor no cálculo da margem |
| PreRef | Number(024,12) | Sim | Preço de referência vinculada a margem de contribuição |
| CodBic | String(003) | Sim | Código da modalidade da base de cálculo do ICMS |
| IndVol | String(001) | Sim | Indicativo se é usado como volume (sugestão para os produtos) |
| CodMph | Number(004,0) | Sim | Código da melhoria de PH |
| ModFab | String(001) | Sim | Modelo de Fabricação do produto para ficha técnica |
| CodPri | String(004) | Sim | Código da tabela de presunção IRPJ |
| CodPrc | String(004) | Sim | Código da tabela de presunção CSLL |
| TipFte | String(001) | Sim | Tipo de ficha técnica utilizada na geração do SPED Fiscal EFD |
| IndEnc | String(001) | Sim | Indicativo se é um produto sob encomenda. |
| PerIfp | Number(004,2) | Sim | Percentual do IRRF para Empresa Pública ou equiparada da Família |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |
| IndAco | String(001) | Sim | Indicativo se é ato cooperado. |
| IndM21 | String(001) | Sim | Indicativo se é um produto para gerar notas fiscais de saída no modelo 21 |
| RegTri | String(001) | Sim | Regime tributário de apuração da contribuição social |
| OriGti | Number(001,0) | Sim | Forma de busca do código GTIN para gerar as tags cEAN e cEANTrib |
| IntWmw | String(001) | Sim | Indicativo se registro deve integrar com o WMW |
| TemRci | String(001) | Sim | Indicativo se registra entradas e saídas para controle de impostos |
| SerRel | String(001) | Sim | Indicativo se Serviço Disponível para Busca no Recebimento Eletrônico |
| DprFam | String(001) | Sim | Indicativo se duplica automaticamente os produtos da família para outras empresas |
| GeaD14 | String(001) | Sim | Indicativo se os produtos da família aceitam geração automática do código de barras DUN-14 |
| CulInd | Number(012,0) | Sim | Código da cultivar junto ao INDEA |
| DevPro | Number(002,0) | Sim | Tipo de produto no SisDev |
| IntPos | String(001) | Sim | Indicativo se o registro integra no Gestão Safra |
| InsSaf | String(001) | Sim | Indicativo se o registro é insumo Gestão Safra |
| SitWmw | String(001) | Sim | Situação do registro no WMW |
| USU_finame | Number(007,0) | Sim | Finame |
| USU_expcat | String(001) | Sim | Exportar catalogo |
| USU_AvaQmm | String(001) | Sim | Avalia Quantidade Minima, Maxima e Multipla do Produto |
| USU_EspLin | String(001) | Sim | Espaçamento entre uma linha da outra de um Produto |

---

## Chave Primária

- CodEmp
- CodFam

---

## Índices

### E012FAMIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodOri

### E012FAMIndice2

**Tipo:** Não unico

Campos:
- UniMed

---

## Relacionamentos

### IR_E012FAM_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E012FAM_004

**Tabela:** E083ORI

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |

### IR_E012FAM_011

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

