# E080SER

## Descrição

Cadastros - Serviços

---

## Resumo

- Campos: 154
- Chave Primária: 2 campo(s)
- Índices: 5
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodSer | String(014) | Não | Código do serviço |
| DesSer | String(070) | Não | Descrição do serviço |
| DesNfv | String(070) | Não | Descrição do serviço para impressão na nota fiscal |
| CplSer | String(250) | Sim | Complemento da descrição do serviço |
| CodFam | String(006) | Não | Código da família de produtos que o serviço pertence |
| QtdPad | Number(014,5) | Sim | Quantidade padrão conforme a unidade de medida do serviço |
| UniMed | String(003) | Não | Unidade de medida do serviço |
| PreCpr | Number(014,5) | Sim | Preço unitário do serviço para compras |
| PreVen | Number(014,5) | Sim | Preço unitário do serviço para vendas |
| PerDsc | Number(004,2) | Sim | Percentual de desconto previsto para venda do serviço |
| PerIss | Number(006,4) | Sim | Percentual do ISS previsto para venda do serviço |
| PerIns | Number(004,2) | Sim | Percentual total do INSS (INSS + Aposentadoria especial) |
| PerIrf | Number(004,2) | Sim | Percentual do IRRF previsto para venda do serviço |
| PerCom | Number(005,2) | Sim | Percentual de comissão previsto para venda do serviço |
| CodTri | String(005) | Sim | Código de tributação para emissão de DARF |
| CodNtg | Number(004,0) | Sim | Código da natureza de gasto |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| SitSer | String(001) | Não | Situação do serviço (Ativo ou Inativo) |
| NotFor | Number(005,2) | Sim | Nota mínima necessária para a aprovação de um fornecedor |
| ObsSer | String(999) | Sim | Observação do Serviço |
| CodCcu | String(009) | Sim | Código do Centro de Custo |
| CodClf | String(003) | Sim | Código interno da classificação fiscal para os serviços com IPI |
| OriMer | String(001) | Sim | Origem fiscal da mercadoria |
| CodStr | String(003) | Sim | Código da situação tributária do serviço com tributação de ICMS e IPI |
| PerIpi | Number(008,4) | Sim | Percentual de IPI válido para o serviço |
| RecIpi | String(001) | Sim | Indicativo se o serviço recupera ou não IPI |
| TemIcm | String(001) | Sim | Indicativo se  o serviço tem ou não tributação ICMS |
| CodTic | String(003) | Sim | Código do ICMS Especial |
| CodTrd | String(003) | Sim | Código de redução de impostos |
| CodTst | String(003) | Sim | Código de ICMS Substituído |
| RecIcm | String(001) | Sim | Indicativo se o serviço recupera ou não ICMS |
| RecPis | String(001) | Sim | Indicativo se o serviço recupera ou não PIS |
| TriPis | String(001) | Sim | Indicativo se o serviço tem tributação de PIS ou não |
| TriCof | String(001) | Sim | Indicativo se o serviço tem tributação de COFINS ou não |
| CodFif | String(010) | Sim | Código fiscal federal do serviço |
| CodFie | String(060) | Sim | Código Fiscal Estadual |
| CodFim | String(010) | Sim | Código fiscal municipal do serviço |
| RecCof | String(001) | Sim | Indicativo se as notas fiscais poderão ter recuperação de COFINS |
| PerCsl | Number(004,2) | Sim | Percentual de CSLL válido para o serviço |
| PerCof | Number(004,2) | Sim | Percentual de Cofins retido válido para o serviço |
| PerPis | Number(004,2) | Sim | Percentual de PIS retido válido para o serviço |
| PerOur | Number(004,2) | Sim | Percentual de Outras Retenções válido para o serviço |
| CodPin | String(020) | Sim | Código do Plano de Inspeção |
| CodPdv | Number(010,0) | Sim | Código interno no PDV |
| IndOct | String(001) | Sim | Indica se o serviço pode ser orçado |
| IndSpr | String(001) | Sim | Indicativo se Serviço é Produzido |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| CodAgt | String(005) | Sim | Código de agrupamento para cotas de venda |
| SerImp | String(010) | Sim | Tipo de Serviço no contexto fiscal baseado na LC 116/2003 |
| VarSer | String(001) | Sim | Indica o tipo de serviço para comércio |
| CodSeg | Number(009,0) | Sim | Código da Seguradora |
| SomIps | String(001) | Sim | Indicativo se calcula PIS importação nas notas fiscais de importação e ordens de compra |
| SomIco | String(001) | Sim | Indicativo se calcula COFINS importação nas notas fiscais de importação e ordens de compra |
| ConEne | Number(002,0) | Sim | Classe de consumo de energia elétrica ou gás |
| ConAgu | Number(002,0) | Sim | Classe de fornecimento de água |
| TipLig | Number(002,0) | Sim | Tipo de ligação |
| GruTen | Number(002,0) | Sim | Código do grupo de tensão |
| CstIpi | String(002) | Sim | Código da situação tributária de IPI |
| CstPis | String(002) | Sim | Código da situação tributária de PIS |
| CstCof | String(002) | Sim | Código da situação tributária de COFINS |
| TprPis | String(004) | Sim | Código da tabela de tributação para o cálculo de PIS por unidade de medida |
| TprCof | String(004) | Sim | Código da tabela de tributação para o cálculo de COFINS por unidade de medida |
| TprIpi | String(004) | Sim | Código da tabela de tributação para o cálculo de IPI por unidade de medida |
| RegTri | String(001) | Sim | Regime tributário de apuração da contribuição social |
| CstIpc | String(002) | Sim | Código da situação tributária de IPI nas operações de compra |
| CstPic | String(002) | Sim | Código da situação tributária de PIS nas operações de compra |
| CstCoc | String(002) | Sim | Código da situação tributária de COFINS nas operações de compra |
| QtdMlt | Number(012,5) | Sim | Quantidade múltipla para cálculo da geração de ordem de produção/compra |
| QtdMin | Number(012,5) | Sim | Quantidade mínima para uma ordem de produção/compra |
| QtdMax | Number(012,5) | Sim | Quantidade máxima para uma ordem de produção/compra |
| NatPis | Number(005,0) | Sim | Natureza da receita do PIS |
| NatCof | Number(005,0) | Sim | Natureza da receita do COFINS |
| TriNfs | String(020) | Sim | Código de tributação do serviço para nota fiscal de serviço eletrônica |
| PerCit | Number(005,2) | Sim | Percentual de imposto CIDE tecnologia |
| CatMnt | String(005) | Sim | Código da categoria de manutenção |
| BasCre | Number(002,0) | Sim | Código da base de cálculo do crédito |
| CodOte | Number(004,0) | Sim | Código da operadora de telefonia |
| CodFil | Number(005,0) | Sim | Filial onde o serviço será utilizado |
| CodTpr | String(004) | Sim | Código da tabela de preço padrão para serviços de varejo |
| DatIni | Date | Sim | Data validade inicial da tabela de preço |
| VlrIni | Number(015,2) | Sim | Valor incial do serviço para serviços financeiros |
| VlrFin | Number(015,2) | Sim | Valor final do serviço para serviços financeiros |
| CodAgg | String(005) | Sim | Código de agrupamento de materiais/produtos para garantia estendida |
| CodTge | Number(004,0) | Sim | Código da Garantia Estendida |
| PrzTge | Number(004,0) | Sim | Prazo de garantia estendida (em meses) |
| VlrSer | Number(015,2) | Sim | Valor do serviço representado para serviços financeiros |
| IteFis | String(060) | Sim | Código fiscal do item |
| DesFis | String(255) | Sim | Descrição fiscal do item |
| IdaMin | Number(004,0) | Sim | Idade mínima para adquirir o serviço parcela protegida |
| IdaMax | Number(004,0) | Sim | Idade máxima para adquirir o serviço parcela protegida |
| FinCrp | Number(007,0) | Sim | Conta financeira de receita(saída) padrão para efeito de rateio |
| FinCdp | Number(007,0) | Sim | Conta financeira de despesa(entrada) padrão para efeito de rateio |
| PerPim | Number(008,4) | Sim | Percentual de PIS de importação diferenciado |
| PerCim | Number(008,4) | Sim | Percentual de Cofins de importação diferenciado |
| CodTra | Number(009,0) | Sim | Código da Transportadora |
| TipTge | String(002) | Sim | Tipo de Garantia Estendida |
| ParCom | String(001) | Sim | Indicativo se o serviço é participante do processo de comissão |
| CodNbs | String(015) | Sim | Nomenclatura brasileira de serviços, intangíveis e outras operações |
| ImoSer | String(001) | Sim | Indica se o serviço poderá ser imobilizado ao patrimônio |
| CodBic | String(003) | Sim | Código da modalidade da base de cálculo do ICMS |
| CodExp | String(010) | Sim | Código que identifica o item na seguradora. |
| TipSer | Number(002,0) | Sim | Tipo do serviço para a EFD-Reinf |
| ApoEsp | Number(001,0) | Sim | Tipo de aposentadoria especial |
| PerDif | Number(007,4) | Sim | Percentual de diferimento do serviço |
| CstIss | String(010) | Sim | Situação tributária do ISS do serviço |
| CodAtv | String(016) | Sim | Código de atividade do item de serviço |
| PerSen | Number(004,2) | Sim | Percentual do imposto SENAR/SENAT do serviço para notas fiscais de saídas |
| CodPri | String(004) | Sim | Código da tabela de presunção IRPJ |
| CodPrc | String(004) | Sim | Código da tabela de presunção CSLL |
| CodCes | String(007) | Sim | Código especificador da substituição tributária |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| PerIfp | Number(004,2) | Sim | Percentual do IRRF para Empresa Pública ou equiparada do Serviço. |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |
| TipRen | Number(003,0) | Sim | Tipo de rendimentos |
| ForTri | Number(002,0) | Sim | Forma de tributação |
| NatAti | Number(002,0) | Sim | Natureza da Atividade |
| IndM21 | String(001) | Sim | Indicativo se é um serviço para gerar notas fiscais de saída no modelo 21 |
| NumCbo | Number(006,0) | Sim | Número da classificação brasileira de ocupações |
| ModPre | Number(001,0) | Sim | Indica o modo de prestação para o Siscoserv |
| ClaCni | Number(004,0) | Sim | Classificação Convênio ICMS 115/2013 |
| TipUti | Number(002,0) | Sim | Tipo de utilização |
| PerIne | Number(004,2) | Sim | Percentual do INSS da parte da empresa |
| PerApe | Number(004,2) | Sim | Percentual da aposentadoria especial |
| IdeRen | Number(009,0) | Sim | Identificador do Registro da Natureza de Rendimento |
| NatRen | String(009) | Sim | Natureza Rendimentos |
| ProImp | Number(002,0) | Sim | Indicativo do tipo de serviço para impostos |
| SerRel | String(001) | Sim | Indicativo se Serviço Disponível para Busca no Recebimento Eletrônico |
| TaxFix | String(001) | Sim | Indicativo se a taxa para IRRF será fixa e sem deduções no valor base do imposto |
| UniEco | String(001) | Sim | Serviço tomado em Unidade Econômica |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| CatFor | Number(003,0) | Sim | Categoria Recibo de Pagamento Autônomo |
| PgtCom | Number(001,0) | Sim | Forma de pagamento serviço comunicação |
| ConIss | String(001) | Sim | Considera % efetivo do ISS do Simples Nacional nas notas fiscais |
| CodTbn | String(006) | Sim | Código de Tributação Nacional |
| CodNfc | String(007) | Sim | Código item cClass |
| CalFus | String(001) | Sim | Calcula FUST |
| AliFus | Number(005,2) | Sim | Percentual FUST |
| CalFnt | String(001) | Sim | Calcula FUNTTEL |
| AliFnt | Number(005,2) | Sim | Percentual FUNTTEL |
| IdeNbs | Number(009,0) | Sim | Identificador NBS |
| FinCib | String(003) | Sim | Aplicação da CBS/IBS |
| IndUso | String(001) | Sim | Indica operação de uso ou consumo pessoal |
| IndMdi | Number(001,0) | Sim | Indicador se a NFS-e deverá ser disponibilizada ao MDIC |
| USU_UsuCpr | Number(010,0) | Sim | Usuário responsável pela compra do item solicitado |

---

## Chave Primária

- CodEmp
- CodSer

---

## Índices

### E080SERIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- IteFis

### E080SERIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodFam

### E080SERIndice4

**Tipo:** Não unico

Campos:
- UniMed

### E080SERIndice5

**Tipo:** Não unico

Campos:
- CodEmp
- SerImp

### E080SERIndice6

**Tipo:** Não unico

Campos:
- CodEmp
- TriNfs

---

## Relacionamentos

### IR_E080SER_005

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

### IR_E080SER_007

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

