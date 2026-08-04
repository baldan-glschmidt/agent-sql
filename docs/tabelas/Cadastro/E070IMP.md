# E070IMP

## Descrição

Cadastros - Filiais - Parâmetros Tributos

---

## Resumo

- Campos: 127
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da Filial |
| EfiDac | String(001) | Não | Indicativo se deve adicionar o valor do diferencial de alíquotas ao CIAP |
| EfiDfi | Date | Sim | Data de cálculo do PIS a recuperar - Financeiro |
| EfiDpa | Date | Sim | Data de cálculo do PIS a recuperar - Patrimônio |
| EfiDcf | Date | Sim | Data de cálculo do COFINS a recuperar - Financeiro |
| EfiDcp | Date | Sim | Data de cálculo do COFINS a recuperar - Patrimônio |
| ConSer | String(001) | Sim | Indicativo se considera notas fiscais de entrada de serviço nas apurações e nos livros fiscais |
| EfiCcc | String(001) | Sim | Indicativo se o sistema efetua o crédito do CIAP na apuração do ICMS |
| EfiCip | String(001) | Sim | Indicativo se o sistema efetua o crédito do CIAP no imposto Outros (Base Faturamento) |
| DatTar | Date | Sim | Data em que foi efetuada a última exportação da TARE (DF) |
| HorTar | Number(005,0) | Sim | Hora em que foi efetuada a última exportação da TARE (DF) |
| ConNum | String(001) | Sim | Indicativo se deve controlar a numeração das notas fiscais de saídas digitadas em impostos |
| InfIte | String(001) | Sim | Indicativo se informa o detalhamento dos itens das notas fiscais |
| FilTot | String(001) | Sim | Indicativo se a filial é totalizadora de cálculos e apurações de impostos de todas as filiais |
| VlmRcs | Number(015,2) | Sim | Valor mínimo para retenção da CSLL |
| MoeCip | String(003) | Sim | Código da moeda ou índice usado para correção do CIAP |
| BasPis | String(001) | Sim | Base de cálculo do bem para crédito do PIS |
| BasCof | String(001) | Sim | Base de cálculo do bem para crédito do COFINS |
| BasCsl | String(001) | Sim | Base de cálculo do bem para crédito do CSLL |
| VlmRpi | Number(015,2) | Sim | Valor mínimo para retenção do PIS |
| VlmRcf | Number(015,2) | Sim | Valor mínimo para retenção do COFINS |
| VlmRor | Number(015,2) | Sim | Valor mínimo para retenção de Outras Retenções |
| DifAli | String(001) | Sim | Indicativo se no cálculo do ICMS considera diferencial de alíquota |
| DaiDev | Number(001,0) | Sim | Forma de lançamento da devolução do diferencial de alíquotas na apuração do ICMS |
| RatImp | String(001) | Sim | Rateio para nota fiscal de impostos |
| ImeCta | String(005) | Sim | Critério de rateio para as contas e centros de custos na nota fiscal de entrada |
| ImeRed | Number(007,0) | Sim | Conta contábil a classificar para nota fiscal de entrada |
| ImeCcu | String(009) | Sim | Centro de custo a classificar para nota fiscal de entrada |
| ImsCta | String(005) | Sim | Critério de rateio para as contas e centros de custos na nota fiscal de saída |
| ImsRed | Number(007,0) | Sim | Conta contábil a classificar para nota fiscal de saída |
| ImsCcu | String(009) | Sim | Centro de custo a classificar para nota fiscal de saída |
| ImzCta | String(005) | Sim | Critério de rateio para as contas e centros de custos na redução Z |
| ImzRed | Number(007,0) | Sim | Conta contábil a classificar para redução Z |
| ImzCcu | String(009) | Sim | Centro de custo a classificar para redução Z |
| TnsInv | String(001) | Sim | Indicativo se considera nos movimentos de saída e entrada a possibilidade de utilização de transações inversas a natureza do movimento |
| DatIns | Date | Sim | Data da inscrição estadual |
| CodCrt | Number(001,0) | Sim | Código do Regime Tributário |
| IncCul | String(001) | Sim | Incentivador Cultural |
| RegEst | Number(002,0) | Sim | Regime Especial de Tributação (Meramente Informativo para NF-e) |
| GerSpc | String(001) | Sim | Filial gera informações para o SPED Contribuições |
| GerSpe | String(001) | Sim | Filial gera informações para o SPED Contábil Fiscal (ECF) |
| ConRir | String(001) | Sim | Indica se existe controle diário de retenção de IRRF |
| VlmRir | Number(015,2) | Sim | Valor mínimo para retenção de IRRF |
| OriRet | String(001) | Sim | Exibir origens das retenções na apuração de IRPJ/CSLL |
| RegRex | String(015) | Sim | Número do Regime Especial do Redex |
| ComCip | String(001) | Sim | Crédito do ICMS (CIAP) de componentes somente na conclusão do bem principal |
| UtiCre | String(001) | Sim | Utiliza primeiramente o crédito fiscal do período da apuração do PIS/COFINS |
| CalFin | Number(001,0) | Sim | Indicador da rotina responsável para calcular Pis/Cofins/IRPJ/CSLL no financeiro |
| UtiRet | String(001) | Sim | Utiliza primeiramente a retenção do período da apuração do PIS/Cofins |
| CtrDif | String(001) | Sim | Filial Controla Diferido |
| CpfScp | Number(014,0) | Sim | Número do CNPJ/CPF da sociedade em conta de participação (deprecado) |
| ConNfs | String(001) | Sim | Considera data de autorização do NFS-e como data de emissão do documento |
| CodPft | Number(004,0) | Sim | Código sequencial do perfil tributário |
| RetRec | String(001) | Sim | Retenção da nota fiscal ocorrer pela data da baixa do título |
| OpeFil | Number(002,0) | Sim | Tipo de operação realizada pela filial |
| IpiCip | String(001) | Sim | Subtrair IPI do valor contábil na composição do índice do CIAP |
| AgrLme | Number(003,0) | Sim | Quantidade de meses limite para utilização do crédito do ICMS no agronegócio |
| AgrVti | Number(004,0) | Sim | Quantidade de dias para vencimento do título de pagamento do crédito do ICMS |
| AgrCdf | Number(006,0) | Sim | Código do dispositivo fiscal do crédito do ICMS no agronegócio |
| AgrTns | String(005) | Sim | Código da transação da nota fiscal de crédito do ICMS no agronegócio |
| AgrSnf | String(003) | Sim | Código da série da nota fiscal de crédito do ICMS |
| PrfTrb | String(001) | Sim | Perfil tributário enquadrado para emissão do SPED conforme determinação do fisco |
| ClaTri | Number(002,0) | Sim | Código da classificação tributária para o Reinf |
| TipSoc | Number(002,0) | Sim | Tipo de Sociedade Cooperativa para o SPED Contribuições |
| TrfCip | String(001) | Sim | Manter CIAP na transferência entre filiais |
| IstCip | String(001) | Sim | Subtrair ICMS ST do valor contábil na composição do índice do CIAP |
| CodPri | String(004) | Sim | Código da tabela de presunção IRPJ |
| CodPrc | String(004) | Sim | Código da tabela de presunção CSLL |
| TipPam | String(001) | Sim | Período para Apuração das Movimentações de Estoque e Produção do SPED Fiscal |
| LucExp | String(001) | Sim | Lucro de Exploração |
| IndFin | String(001) | Sim | Indicativo de existência de FINOR/FINAM/FUNRES |
| CalCip | String(001) | Sim | Modalidade Cálculo CIAP |
| ConRco | String(001) | Sim | Controle diário de retenção das contribuições sociais (PIS, Cofins e CSLL) |
| VlmRco | Number(015,2) | Sim | Valor mínimo para retenção das contribuições sociais (PIS, Cofins e CSLL) |
| SnlPrp | String(001) | Sim | Lançar crédito do ICMS do Simples Nacional nos campos de ICMS |
| AtiRur | String(001) | Sim | Atividade Rural |
| TipJur | Number(002,0) | Sim | Tipo Pessoa Juridica Imunes ou Isentas |
| TipCst | String(001) | Sim | Tipo de crédito de ST que deverá ser utilizado no cálculo do imposto do ICMS. |
| FciInt | String(001) | Sim | Calcular FCI das Operações Internas (ART 352 publicado no decreto 1757/2013) |
| FilCon | Number(005,0) | Sim | Código da filial consolidadora |
| TipCmp | String(001) | Sim | Forma de Compensação/Restituição de impostos indevidos ou a maior |
| TipReg | Number(001,0) | Sim | Forma de Tributação Simples Nacional |
| DetRis | String(001) | Sim | Forma de utilização do valor de ISS dos RPA na apuração do ISS |
| DetRic | String(001) | Sim | Forma de utilização do valor de ICMS dos RPA na apuração do ICMS |
| UsuQui | String(255) | Sim | Usuário para auditoria da Quirius |
| SenQui | String(255) | Sim | Senha para auditoria da Quirius |
| UrlQui | String(255) | Sim | URL para auditoria da Quirius |
| OriRpc | String(001) | Não | Gerar Origem da Retenção do PIS e COFINS |
| GorPco | String(001) | Sim | Indica se deverá gravar as origens de pis/cofins na apuração dos impostos |
| DesDve | String(001) | Sim | Descontar as devoluções de venda no cálculo do índice do CIAP |
| VlfSnl | Number(015,2) | Sim | Valor limite do faturamento do Simples Nacional |
| NfePro | String(001) | Sim | Tipos de notas fiscais de produtor rural que serão escrituradas com valor |
| FcpPro | String(001) | Sim | Indica se o FCP Próprio deve ser somado ao ICMS na integração de notas fiscais |
| FcpSit | String(001) | Sim | Indica se o FCP ST deve ser somado ao ICMS ST na integração de notas fiscais |
| ConIcp | String(001) | Sim | Contribuinte com isenção de contribuição previdenciaria de acordo com a lei nº 13.606/2018 |
| ConDes | String(001) | Sim | Considerar data de execução do serviço prestado como data de emissão |
| TrfDat | String(001) | Sim | Considerar transferência de crédito/débito de ICMS conforme data de saída da nota fiscal |
| ArrCip | Number(001,0) | Sim | Forma de arredondamento na geração de parcelas do CIAP |
| FilCos | Number(005,0) | Sim | Código da filial consolidadora das notas fiscais de serviço |
| TipRin | Number(001,0) | Sim | Forma de Retenção de IRRF Nota de Entrada |
| CtrInd | String(001) | Sim | Indica se o controle de retenção das contribuições sociais (PIS, Cofins e CSLL) será individual (por imposto) ou agrupado |
| PrdTek | String(001) | Sim | Considerar itens de serviço nas operações de terceirizações do bloco K |
| TipDep | Number(002,0) | Sim | Tipo de Dependência Desif (anexo 8) |
| TipTit | String(002) | Sim | Tipo de Instituição Desif (anexo 2) |
| IncRai | String(001) | Sim | Incentivo fiscal por redução de alíquota (DES-IF) |
| CptRci | Date | Sim | Comp. de início do fat. da filial (retomar CIAP par. em transf. entre filiais) |
| QtdPii | Number(004,0) | Sim | Quantidade de parcelas para parcelamento do Imposto Importação na apuração do ICMS |
| IndNfc | String(001) | Sim | Indicativo se considera notas fiscais de produtos rural a fixar na integração do registro R-2055 do REINF |
| QtdPid | Number(004,0) | Sim | Quantidade de parcelas para parcelamento do ICMS Diferido das operações internas na apuração do ICMS. |
| EstDpc | String(001) | Sim | Considerar estorno por devolução de bem na apuração do PIS e Cofins |
| FilOst | Number(005,0) | Sim | Código da filial sócio ostensiva |
| PerPar | Number(004,2) | Sim | % participação da filial sócio ostensiva na SCP |
| PrgIna | Number(001,0) | Sim | Programa de Incentivo ao Algodão |
| CalFaf | String(001) | Sim | Indicativo se deve ser calculado o fator de ajuste de fruição |
| CstRtm | String(001) | Sim | Indicativo se as CST de Pis/Cofins 04 e 05 são consideradas receitas tributadas na matriz de crédito |
| ImpGst | String(003) | Sim | Código imposto ST para integrar guia paga pelo remetente |
| LocIcm | String(001) | Sim | Local para lançamento do crédito do ICMS monofásico destacado |
| IcmsNR | String(001) | Sim | Lançar ICMS ST Solidário não recuperado no campo ICMS ST Não recuperado |
| UtiRcc | String(001) | Sim | Utiliza rateio do consumo de créditos entre os diferentes tipos de crédito |
| IndDat | Number(001,0) | Sim | Indicativo do tipo de data a ser considerada na integração das notas do REINF - Bloco 4000. |
| CalCIb | String(001) | Sim | Calcula CBS/IBS nos documentos fiscais |
| DatIre | Date | Sim | Data inicial para recolhimento da CBS/IBS |
| DatIca | Date | Sim | Data inicial para cálculo da CBS/IBS |
| DifEnd | String(001) | Sim | Apurar DIFAL e FCP para endereço do cliente PJ |
| RegApu | Number(001,0) | Sim | Regime de Apuração Tributária pelo Simples Nacional |
| DatIec | Date | Sim | Data inicial para estorno de crédito da CBS/IBS |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070IMP_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

