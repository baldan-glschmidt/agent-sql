# E075DER

## Descrição

Cadastros - Produtos - Derivações

---

## Resumo

- Campos: 160
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| DesDer | String(050) | Sim | Descrição da Derivação no Componente da Máscara |
| DesCpl | String(090) | Sim | Descrição Complementar |
| CodBar | Number(014,0) | Sim | Código de barras |
| CodAgr | Number(004,0) | Sim | Código de agrupamento para derivação - Controle de Grade |
| CodAgt | String(005) | Sim | Código de agrupamento para cotas de venda |
| SeqCmd | Number(007,0) | Não | Sequência do Componente da Derivação |
| DatVal | Date | Sim | Data máxima de Validade do Produto |
| DiaVlt | Number(006,0) | Sim | Quantidade de dias para cálculo da validade do lote de fabricação |
| TipCn2 | String(001) | Sim | Tipo conversão Unidade Estoque p/ 2ª Unidade Medida produto/derivação |
| VlrCn2 | Number(013,6) | Sim | Valor conversão Unidade Estoque p/ 2ª Unidade Medida produto/derivação |
| TipCn3 | String(001) | Sim | Tipo conversão Unidade Estoque p/ 3ª Unidade Medida produto/derivação |
| VlrCn3 | Number(013,6) | Sim | Valor conversão Unidade Estoque p/ 3ª Unidade Medida produto/derivação |
| PreCus | Number(021,10) | Sim | Preço de custo |
| DatCus | Date | Sim | Data base do preço de custo |
| PreMed | Number(021,10) | Sim | Preço Médio Orientativo (preço médio real é calculado através do Processo de Fechamento) |
| DatMed | Date | Sim | Data base do preço médio |
| PreUen | Number(021,10) | Sim | Preço da última entrada |
| DatUen | Date | Sim | Data base da última entrada |
| PreRep | Number(021,10) | Sim | Preço de reposição |
| DatRep | Date | Sim | Data base do preço de reposição |
| DiaRep | Number(004,0) | Sim | Quantidade de dias de reposição (comprado)/dias precedentes p/ paralelismo (produzido) |
| PesBru | Number(011,5) | Sim | Peso bruto do produto |
| PesLiq | Number(011,5) | Sim | Peso líquido do produto |
| TolPes | Number(005,3) | Sim | Tolerância do peso líquido do produto/derivação |
| VolDer | Number(011,5) | Sim | Volume do Produto |
| PerPrd | Number(004,2) | Sim | Percentual de perda do produto (estocagem, defeituosos, imperfeitos) |
| QtdIql | Number(014,5) | Sim | Quantidade padrão p/ inspecionar pela Qualidade quando da Movimentação de OPs |
| QtdCic | Number(014,5) | Sim | Quantidade cíclica (de quando e quando) p/ inspecionar pela Qualidade quando da Movimentação de OPs |
| QtdPrd | Number(014,5) | Sim | Quantidade de perda fixa do produto para considerar na explosão de Necessidade e Geração de OPs. |
| PreUis | Number(017,8) | Sim | Preço unitário base para o ICMS substituído da última entrada |
| PerIcs | Number(005,2) | Sim | Percentual do ICMS substituído da última entrada por compra |
| CodEmb | Number(004,0) | Sim | Código da embalagem padrão do produto/derivação |
| QtdEmb | Number(012,5) | Sim | Quantidade padrão do produto por embalagem |
| CodRot | String(014) | Sim | Código do Roteiro (quando a Derivação do produto tem processo de fabricação específico) |
| CodRoy | Number(004,0) | Sim | Código do Royalty |
| BxaOrp | String(001) | Não | Se for componente de alguma OP, indica se o mesmo é baixado |
| SerCcl | String(003) | Sim | Série do certificado de classificação do produto |
| NumCcl | String(015) | Sim | Número do certificado de classificação do produto |
| CurAbc | String(001) | Sim | Curva ABC (informar A, B ou C) através da classificação pela curva de quantidades em estoque |
| CurAb2 | String(001) | Sim | Curva ABC através da classificação pela curva de custos (valor do Produto) |
| CurAb3 | String(001) | Sim | Curva ABC através da classificação pela curva de quantidade consumida por período |
| CurAb4 | String(001) | Sim | Curva ABC através da classificação pela curva de valores monetários consumidos por período |
| CodReg | Number(004,0) | Sim | Código da regra usado p/ cálculo de consumo do Modelo (Eng.Ind.) |
| SitDer | String(001) | Não | Situação do produto |
| CodMot | Number(006,0) | Sim | Código do motivo da situação |
| CtrLot | String(001) | Não | Controla Entrada/Saída no Estoque por Lote |
| CtrSep | String(001) | Não | Controla Entrada/Saídas no Estoque por Série |
| CtrVld | String(001) | Não | Indicativo da forma de controle da data de validade nos estoques |
| DepPad | String(010) | Sim | Depósito padrão p/ Derivação do Produto |
| DepPaa | String(010) | Sim | Depósito padrão "ATÉ" p/ Derivação do Produto |
| IndPce | String(001) | Não | Indicativo de controle, se usa Estrutura de Pedido com componentes configurados |
| IndPcr | String(001) | Não | Indicativo de controle, se usa Roteiro Produção p/ Pedido com operações configuradas |
| IndKan | String(001) | Não | Indicativo se usa controle de Critério Kanban na geração de OPs (Analisa Estoque) |
| CodRef | String(040) | Sim | Código da Referência |
| CodPin | String(020) | Sim | Código do Plano de Inspeção |
| NotFor | Number(005,2) | Sim | Nota mínima necessária para a aprovação de um fornecedor. |
| OriCus | String(001) | Sim | Origem do Preço de Custo |
| InfCus | String(001) | Sim | Indicativo se o valor foi calculado pelo sistema, ou informado |
| HorCus | Number(005,0) | Sim | Hora de atualização do Custo |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pelo geração do registro |
| HorGer | Number(005,0) | Sim | Hora do cadastro do registro |
| DatGer | Date | Sim | Data do cadastro do registro |
| UsuAlt | Number(010,0) | Sim | Código do usuário responsável pelo alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| CodAge | String(010) | Sim | Não Utilizar - Será excluído |
| CodBa2 | String(030) | Sim | Código de barras livre |
| GtiUtr | Number(014,0) | Sim | Deprecado |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para integração |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| ExpWms | Number(001,0) | Sim | Indicativo se a derivação foi exportada para o sistema WMS |
| SerMvp | String(014) | Sim | Código do serviço ligado ao produto para geração de nota fiscal de serviços que necessitem de movimentação de estoques |
| AprDft | String(001) | Sim | Indicativo se o produto pode ou não ser aprovado com defeitos ou não conformidades |
| CodAem | String(010) | Sim | Código do agrupamento para embalagens |
| CodPdv | Number(009,0) | Sim | Código interno no pdv |
| IndGen | String(001) | Sim | Indicativo se a derivação é a derivação genérica do produto para o comercial |
| QtdMlt | Number(012,5) | Sim | Quantidade múltipla para cálculo da geração de ordem de produção |
| QtdMin | Number(012,5) | Sim | Quantidade mínima para uma ordem de produção |
| QtdMax | Number(012,5) | Sim | Quantidade máxima para uma ordem de produção |
| RotAnx | Number(002,0) | Sim | Código da rotina para controle de arquivos anexos |
| CodEnd | String(020) | Sim | Código do endereçamento do produto |
| NumAnx | Number(010,0) | Sim | Número do controle de arquivos anexos gerado pelo sistema |
| IndPcq | String(001) | Sim | Indicativo se necessita de conferência de quantidades na carga |
| VlrCid | Number(015,2) | Sim | Valor unitário do Imposto CIDE |
| QtdCus | Number(012,5) | Sim | Quantidade utilizada no cálculo do custo padrão do produto |
| VlrUis | Number(017,8) | Sim | Valor unitário de ICMS substituído da última entrada |
| QtdMcf | Number(006,0) | Sim | Qtde máxima diária do produto para subdivisão do item de pedido para MRP |
| DsdDer | Number(011,5) | Sim | Densidade da derivação |
| IndCnv | String(001) | Sim | Indicativo se a derivação pode ser utilizada em convênios |
| LarDer | Number(011,5) | Sim | Largura da derivação |
| AltDer | Number(011,5) | Sim | Altura da derivação |
| ComDer | Number(011,5) | Sim | Comprimento da derivação |
| PerCit | Number(005,2) | Sim | Percentual de imposto CIDE tecnologia |
| VarPro | String(001) | Sim | Indica o tipo de produto para o Varejo |
| VlrVar | Number(015,2) | Sim | Valor do produto para ser usado no varejo |
| ProFol | String(001) | Sim | Indicativo se a derivação está fora de linha e não pode sofrer reposição externa |
| ProVes | String(001) | Sim | Indicativo se o produto pode ser vendido separadamente |
| IteFis | String(060) | Sim | Código fiscal do item |
| DesFis | String(255) | Sim | Descrição fiscal do item |
| TipCur | Number(001,0) | Sim | Indicativo do tipo de curso online para varejo |
| PreFix | Number(015,6) | Sim | Custo médio fixo |
| IcmFix | Number(019,6) | Sim | Valor do ICMS médio fixo dos produtos acabados |
| DatPfx | Date | Sim | Data base do custo médio fixo |
| HorPfx | Number(005,0) | Sim | Hora de atualização do custo médio fixo |
| IndVol | String(001) | Sim | Indicativo se é usado como volume |
| CodCor | Number(004,0) | Sim | Código da Cor |
| VltDer | Number(001,0) | Sim | Voltagem da derivação do produto |
| QtdBcp | Number(014,5) | Sim | Quantidade base para cálculo de preço por unidade de medida |
| CodFif | String(010) | Sim | Código fiscal federal do produto |
| CodFie | String(060) | Sim | Código Fiscal Estadual |
| CodFim | String(010) | Sim | Código fiscal municipal do produto |
| GruSml | Number(009,0) | Sim | Número do grupo similar da derivação do produto |
| ConKwh | Number(014,7) | Sim | Consumo de energia elétrica em Kwh |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |
| CusSal | Number(015,2) | Sim | Despesas com salários e ordenados para a fabricação de uma unidade do produto |
| CusEnc | Number(015,2) | Sim | Despesas com encargos sociais/trabalhistas para fabricação de uma unid. do prod. |
| NumDcr | Number(010,0) | Sim | Número do registro DCR-e |
| CodSku | String(022) | Sim | Código SKU, para manter a referência do produto com a plataforma G7 |
| RegAnv | String(020) | Sim | Número do registro Anvisa |
| MotAnv | String(255) | Sim | Motivo de isenção do registro Anvisa |
| IndEsc | String(001) | Sim | Indicador de Produção em Escala Relevante |
| TemRci | String(001) | Sim | Indicativo se registra entradas e saídas para controle de impostos |
| FilIcs | Number(005,0) | Sim | Filial da última entrada com ICMS ST para o produto/derivação |
| BstUfc | Number(015,2) | Sim | Valor base unitário do FCP retido por ST da última entrada |
| AstFcp | Number(007,4) | Sim | Alíquota do FCP retido por ST da última entrada |
| VstUfc | Number(015,2) | Sim | Valor unitário do FCP retido por ST da última entrada |
| CodGtn | String(014) | Sim | GTIN Unidade Tributável |
| CodCes | String(007) | Sim | Código especificador da substituição tributária |
| CodPat | String(040) | Sim | Código do princípio ativo |
| CulInd | Number(012,0) | Sim | Código cultivar/agrotóxico junto ao INDEA |
| DevPro | Number(002,0) | Sim | Tipo de produto no SisDev |
| CodCcs | String(010) | Sim | Código da categoria da semente |
| IndBmu | Number(001,0) | Sim | Indicativo de fornecimento de bem móvel usado |
| USU_dersub | String(007) | Sim | Der. Subst. ICMS |
| USU_datfli | Date | Sim | Data do Produto Fora de Linha |
| USU_clacom | String(030) | Sim | Classificacao dos produto para Comercial |
| USU_qtdweb | Number(005,0) | Sim | Ordem Heijunka |
| USU_promoc | String(030) | Sim | Produto Em Promocao |
| USU_proconf | String(001) | Sim | Derivacao pode ser Vendida |
| USU_codfot | String(020) | Sim | USU_codfot |
| USU_PreFix | Number(015,6) | Sim | Preço Custo Média Ponderada Fixa |
| USU_DatPfx | Date | Sim | Data Preço de Custo Fixo |
| USU_HorPfx | Number(005,0) | Sim | Hora de atualização do Custo Fixo |
| USU_ICMFIX | Number(015,6) | Sim | Valor do ICMS médio fixo |
| USU_IndIng | String(001) | Sim | Manual Inglês Comprado/Produzido? |
| USU_IndFra | String(001) | Sim | Manual Francês Comprado/Produzido? |
| USU_IndEsp | String(001) | Sim | Manual Espanhol Comprado/Produzido? |
| USU_IndPor | String(001) | Sim | Manual Português Comprado/Produzido? |
| USU_CapDer | String(020) | Sim | Capacidade da Derivacao |
| USU_observ | String(200) | Sim | Observacao Nao Pode ser Vendido |
| USU_CODSCA | Number(004,0) | Sim | Código Categoria de Classificação Comercial |
| USU_CODOPE | Number(004,0) | Sim | Código da Operação Comercial |
| USU_CODSEG | Number(004,0) | Sim | Código da Segmentação Comercial |
| USU_DESCOM | String(120) | Sim | Título para Sites |
| USU_INTEGR | String(001) | Sim | Integra com sistemas Externos |
| USU_PrdDes | String(001) | Sim | B2B - Produto Destaque |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer

---

## Índices

### E075DERIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- IteFis

---

## Relacionamentos

### IR_E075DER_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

