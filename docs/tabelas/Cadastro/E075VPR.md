# E075VPR

## Descrição

Cadastros - Produtos - Alteração de Produtos

---

## Resumo

- Campos: 152
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| DatAtu | Date | Não | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Não | Hora/minuto da última atualização do cadastro |
| SeqAtu | Number(003,0) | Não | Sequência da atualização |
| DesPro | String(100) | Não | Descrição usual do produto |
| CplPro | String(050) | Sim | Descrição complementar do Produto |
| DesNfv | String(099) | Sim | Descrição do produto para impressão na nota fiscal |
| CodFam | String(006) | Não | Código da Família do Produto |
| UniMed | String(003) | Não | Código da Unidade de Medida do produto para Estoque |
| UniMe2 | String(003) | Sim | Código da 2ª unidade de medida (Quando / Produzido é utilizada na Ficha Técnica) |
| UniMe3 | String(003) | Sim | Código da  3ª unidade de medida |
| TipPro | String(001) | Não | Tipo do produto (C=Comprado, P=Produzido, M=Montagem, D=Passagem direta) |
| CodOri | String(003) | Não | Código de Origem do Produto |
| NumOri | Number(004,0) | Não | Número de Nível do Produto na Estrutura |
| CodMdp | String(008) | Sim | Código da Máscara de derivação que o produto pode utilizar |
| CodMod | String(014) | Sim | Código do Modelo para Produto Fabricado ou Montagem |
| CodRot | String(014) | Sim | Código do Roteiro de Produção para Produto Fabricado |
| CodAge | String(005) | Sim | Código de agrupamento de materiais/produtos para estoques |
| CodAgp | String(005) | Sim | Código de agrupamento de materiais/produtos para produção |
| CodAgu | String(005) | Sim | Código de agrupamento de materiais/produtos para custos |
| CodAgc | String(005) | Sim | Código de agrupamento de materiais/produtos para compras ou vendas |
| CodAgf | String(005) | Sim | Código de agrupamento de materiais/produtos para Impostos |
| CodClf | String(003) | Sim | Código interno da classificação fiscal do produto |
| CodStr | String(003) | Sim | Código da situação tributária do produto |
| PerIpi | Number(008,4) | Sim | Percentual de IPI válido para o produto |
| RecIpi | String(001) | Não | Indicativo se o Produto recupera ou não IPI |
| TemIcm | String(001) | Não | Indicativo se  o produto tem ou não ICMS |
| CodTic | String(003) | Sim | Código do ICMS Especial |
| CodTrd | String(003) | Sim | Código de redução de impostos |
| CodTst | String(003) | Sim | Código de ICMS Substituído |
| CodStp | String(003) | Sim | Código da substituição tributária do PIS |
| CodStc | String(003) | Sim | Código da substituição tributária do COFINS |
| RecIcm | String(001) | Não | Indicativo se o produto recupera ou não ICMS |
| CodRoy | Number(004,0) | Sim | Código de royalty |
| QtdMlt | Number(012,5) | Sim | Quantidade Múltipla para cálculo da geração de Ordem produção/compra |
| QtdMin | Number(012,5) | Sim | Quantidade Mínima para uma Ordem produção/compra |
| QtdMax | Number(012,5) | Sim | Quantidade Máxima para uma Ordem produção/compra |
| QtdGop | Number(012,5) | Sim | Quantidade Máxima para cada Guia de Produção (p/ não utilizar guias informe = 0) |
| BxaOrp | String(001) | Não | Se for componente de alguma OP, indica se o mesmo é baixado |
| CodPr2 | String(014) | Sim | Código do Produto associado para Entrada estoque 2ª qualidade |
| DerPr2 | String(007) | Sim | Código da Derivação  Produto p/ 2ª qualidade (se não informado assume 1ª qualidade) |
| CodPr3 | String(014) | Sim | Código do Produto associado para Entrada estoque 3ª qualidade |
| DerPr3 | String(007) | Sim | Código da Derivação Produto p/ 3ª qualidade (se não informado assume 1ª qualidade) |
| CodPr4 | String(014) | Sim | Código do Produto reaproveitado associado ao titular p/ entrada estoque sucatas/rebarbas/refugos na Produção |
| DerPr4 | String(007) | Sim | Código da Derivação do Produto reaproveitado (se não informado, então assume derivação do titular) |
| ProStq | String(001) | Sim | Produto é Utilizado para Estocar 2ª, 3ª Qualidade ou Reaproveitado (refugo) |
| SitPro | String(001) | Não | Situação do produto (Ativo ou Inativo) |
| RotPro | String(001) | Sim | Roteiro Informado é Utilizado p/ todas as Derivações do Produto (S=Sim, N=Não) |
| UsoCus | String(001) | Sim | Gerou Ficha de Custos (Produto Produzidos/Montagem) |
| IndMis | String(001) | Não | Indicativo que o produto é produzido mas também pode ser comprado (Misto) |
| IndVen | String(001) | Não | Indicativo se o produto pode ser vendido/faturado (item pedido e NF saída) |
| IndCpr | String(001) | Sim | Indicativo se o produto pode ser comprado. |
| IndReq | String(001) | Não | Indicativo se o produto pode ser requisitado (movimento estoque) |
| IndKit | String(001) | Não | Indicativo que o produto produzido é um "Kit" c/ vários produtos agregados p/ venda (não gera OP) |
| MatDir | String(001) | Não | Indicativo se o Material é Direto (produto comprado que é utilizado p/ fabricação de produtos produzidos) |
| ClaPro | Number(001,0) | Não | Classe do produto |
| IndPpc | String(001) | Não | Indicativo se o produto tem controle por cliente |
| IndFpr | String(001) | Não | Indicativo se a ligação de produto x fornecedor é usada p/ obter parâmetros fiscais |
| CodNtg | Number(004,0) | Sim | Código da natureza de gasto |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| CtaDcd | Number(007,0) | Sim | Conta contábil reduzida - 5 |
| CtaDci | Number(007,0) | Sim | Conta contábil reduzida - 6 |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pelo geração do registro |
| HorGer | Number(005,0) | Sim | Hora do cadastro do registro |
| DatGer | Date | Sim | Data do cadastro do registro |
| DepPad | String(010) | Sim | Depósito padrão para Produto |
| CtrVld | String(001) | Não | Indicativo da forma de controle da data de validade nos estoques |
| CtrLot | String(001) | Não | Controla Entrada/Saída no Estoque por  Lote |
| CtrSep | String(001) | Não | Controla Entrada/Saídas no Estoque  por Série |
| QtdMve | Number(012,5) | Sim | Quantidade Múltipla para Vendas |
| CodRef | String(030) | Sim | Código da Referência |
| CodPin | String(020) | Sim | Código do Plano de Inspeção |
| NotFor | Number(005,2) | Sim | Nota mínima necessária para a aprovação de um fornecedor. |
| ExgCcl | String(001) | Sim | Indicativo se o produto exige certificado de classificação |
| EmiGtr | String(001) | Sim | Indicativo se é emitida a guia de tráfego para o produto |
| UsuAlt | Number(010,0) | Sim | Código do usuário responsável pelo alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| SomIim | String(001) | Sim | Indicativo se calcula ICMS importação nas notas fiscais de importação e ordens de compra |
| RecPis | String(001) | Sim | Indicativo se o produto recupera ou não PIS |
| TriPis | String(001) | Sim | Indicativo se o produto tem tributação de PIS ou não |
| TriCof | String(001) | Sim | Indicativo se o produto tem tributação de COFINS ou não |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para integração |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| ExpWms | Number(001,0) | Sim | Indicativo se o produto foi exportado para o sistema WMS |
| TipInt | Number(001,0) | Sim | Tipo de Integração |
| CodFif | String(010) | Sim | Código fiscal federal do produto |
| CodFie | String(060) | Sim | Código Fiscal Estadual |
| CodFim | String(010) | Sim | Código fiscal municipal do produto |
| RecCof | String(001) | Sim | Indicativo se as notas fiscais poderão ter recuperação de Cofins |
| SomIil | String(001) | Sim | Indicativo se deve ser somado o valor do ICMS no valor líquido das notas fiscais de importação e ordens de compra |
| CalDzf | String(001) | Sim | Indicativo se deve ser calculado o desconto Suframa para o produto nas entradas |
| UniPad | String(003) | Sim | U.M. padrão para movimentação de estoque manual |
| CodMar | String(010) | Sim | Código da Marca/Etiqueta do produto |
| CodClc | String(010) | Sim | Código da coleção do produto |
| CodAgm | String(005) | Sim | Código de agrupamento de materiais/produtos para preço |
| FilPrd | Number(005,0) | Sim | Código da filial de produção do produto |
| TolQmx | Number(005,3) | Sim | Tolerância da quantidade máxima defininida no produto |
| GerOrp | String(001) | Não | Indica se o produto gera ordem de produção. |
| CodPdv | Number(010,0) | Sim | Código interno no PDV |
| PerIrf | Number(004,2) | Sim | Percentual do IRRF previsto para venda do produto |
| PerPis | Number(004,2) | Sim | Percentual de PIS retido válido para o produto |
| PerCof | Number(004,2) | Sim | Percentual de Cofins retido válido para o produto |
| PerCsl | Number(004,2) | Sim | Percentual de CSLL válido para o produto |
| PerOur | Number(004,2) | Sim | Percentual de Outras Retenções válido para o produto |
| ConMon | String(001) | Sim | Considerar o produto produzido como montagem na busca da estrutura |
| PerFun | Number(004,2) | Sim | Percentual de Funrural do Produto para Notas Fiscais de Saídas |
| CodAga | String(005) | Sim | Código da forma de agrupamento para aprovação multinível |
| SomIps | String(001) | Sim | Indicativo se calcula PIS importação nas notas fiscais de importação e ordens de compra |
| SomIco | String(001) | Sim | Indicativo se calcula COFINS importação nas notas fiscais de importação e ordens de compra |
| SomIpl | String(001) | Sim | Indicativo se deve ser somado o valor do PIS no valor líquido das notas fiscais de importação e ordens de compra |
| SomIcl | String(001) | Sim | Indicativo se deve ser somado o valor do COFINS no valor líquido das notas fiscais de importação e ordens de compra |
| IndOct | String(001) | Sim | Indica se os produtos/serviços podem ser orçados |
| CodEnd | String(020) | Sim | Código do endereçamento do produto |
| IndSpr | String(001) | Sim | Indicativo se Serviço é Produzido |
| PesBru | Number(011,5) | Sim | Peso bruto do produto |
| PesLiq | Number(011,5) | Sim | Peso líquido do produto |
| TolPes | Number(005,3) | Sim | Tolerância do peso líquido do produto |
| VolPro | Number(011,5) | Sim | Volume do produto |
| RotAnx | Number(002,0) | Sim | Código da rotina para controle de arquivos anexos |
| NumAnx | Number(010,0) | Sim | Número do controle de arquivos anexos gerado pelo sistema |
| ProImp | Number(002,0) | Sim | Indicativo do tipo de produto para impostos |
| DatFis | Date | Sim | Data da última atualização da data fiscal |
| DatFat | Date | Sim | Data da última alteração da data fiscal |
| UsuFat | Number(010,0) | Sim | Usuário da última alteração da data fiscal |
| HorFat | Number(005,0) | Sim | Hora da última alteração da data fiscal |
| CstIpi | String(002) | Sim | Código da situação tributária de IPI |
| CstPis | String(002) | Sim | Código da situação tributária de PIS |
| CstCof | String(002) | Sim | Código da situação tributária de COFINS |
| TprPis | String(004) | Sim | Código da tabela de tributação para o cálculo de PIS por unidade de medida |
| TprCof | String(004) | Sim | Código da tabela de tributação para o cálculo de Cofins por unidade de medida |
| TprIpi | String(004) | Sim | Código da tabela de tributação para o cálculo de IPI por unidade de medida |
| NatPis | Number(005,0) | Sim | Natureza da receita do PIS |
| NatCof | Number(005,0) | Sim | Natureza da receita do COFINS |
| BasCre | Number(002,0) | Sim | Código da base de cálculo do crédito |
| CodAgg | String(001) | Sim | Código de agrupamento de materiais/produtos para garantia estendida |
| IteFis | String(060) | Sim | Código fiscal do item |
| DesFis | String(255) | Sim | Descrição fiscal do item |
| PerPim | Number(008,4) | Sim | Percentual de PIS de importação diferenciado |
| PerCim | Number(008,4) | Sim | Percentual de Cofins de importação diferenciado |
| IndIcp | String(001) | Sim | Indicativo se OPs do produto permitem a incorporação de produtos |
| LimIcp | Number(004,0) | Sim | Percentual limite de incorporação de produtos na OP |
| CodBic | String(003) | Sim | Código da modalidade da base de cálculo do ICMS |
| PerSen | Number(004,2) | Sim | Percentual do SENAR/SENAT do produto para notas fiscais de saídas |
| PerIfp | Number(004,2) | Sim | Percentual do IRRF para Empresa Pública ou equiparada |
| PerGil | Number(004,2) | Sim | Percentual de GILRAT - Grau Incid. Incapac. Laborat. Decor. Riscos Amb. de Trab. |

---

## Chave Primária

- CodEmp
- CodPro
- DatAtu
- HorAtu
- SeqAtu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E075VPR_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E075VPR_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

