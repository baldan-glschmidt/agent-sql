# E075VDR

## Descrição

Cadastros - Produtos - Alteração de Derivações

---

## Resumo

- Campos: 98
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do Produto (tamanho, cor, etc.) |
| DatAtu | Date | Não | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Não | Hora/minuto da última atualização do cadastro |
| SeqAtu | Number(003,0) | Não | Sequência da atualização |
| DesDer | String(050) | Sim | Descrição da Derivação no Componente da Máscara |
| DesCpl | String(090) | Sim | Descrição Complementar |
| CodBar | Number(014,0) | Sim | Código de barras EAN13 |
| CodAgr | Number(004,0) | Sim | Código de agrupamento para derivação - Controle de Grade |
| CodAgt | String(005) | Sim | Código de agrupamento para cotas de venda |
| SeqCmd | Number(007,0) | Não | Sequência do Componente da Derivação |
| DatVal | Date | Sim | Data máxima de Validade do Produto |
| DiaVlt | Number(006,0) | Sim | Quantidade de dias para cálculo da validade do lote de fabricação |
| TipCn2 | String(001) | Sim | Tipo conversão Unidade Estoque para 2ª Unidade Medida produto/derivação |
| VlrCn2 | Number(013,6) | Sim | Valor conversão Unidade Estoque para 2ª Unidade Medida produto/derivação |
| TipCn3 | String(001) | Sim | Tipo conversão Unidade Estoque para 3ª Unidade Medida produto/derivação |
| VlrCn3 | Number(013,6) | Sim | Valor conversão Unidade Estoque para 3ª Unidade Medida produto/derivação |
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
| QtdIql | Number(014,5) | Sim | Quantidade padrão para inspecionar pela Qualidade quando da Movimentação de OPs |
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
| CodReg | Number(004,0) | Sim | Código da regra usado para cálculo de consumo do Modelo (Eng.Ind.) |
| SitDer | String(001) | Não | Situação do produto |
| CodMot | Number(006,0) | Sim | Código do motivo da situação |
| CtrLot | String(001) | Não | Controla Entrada/Saída no Estoque por Lote |
| CtrSep | String(001) | Não | Controla Entrada/Saídas no Estoque por Série |
| CtrVld | String(001) | Não | Indicativo da forma de controle da data de validade nos estoques |
| DepPad | String(010) | Sim | Depósito padrão para Derivação do Produto |
| DepPaa | String(010) | Sim | Depósito padrão "até" p/ derivação do produto |
| IndPce | String(001) | Não | Indicativo de controle, se usa Estrutura de Pedido com componentes configurados |
| IndPcr | String(001) | Não | Indicativo de controle, se usa Roteiro Produção p/ Pedido com operações configuradas |
| IndKan | String(001) | Não | Indicativo se usa controle de Critério Kanban na geração de OPs (Analisa Estoque) |
| CodRef | String(030) | Sim | Código da Referência |
| CodPin | String(020) | Sim | Código do Plano de Inspeção |
| NotFor | Number(005,2) | Sim | Nota mínima necessária para a aprovação de um fornecedor. |
| OriCus | String(001) | Sim | Origem do Preço de Custo |
| InfCus | String(001) | Sim | Indicativo se o valor foi calculado pelo sistema, ou informado |
| HorCus | Number(005,0) | Sim | Hora de atualização do Custo |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| CodAge | String(010) | Sim | Não Utilizar - Será excluído |
| CodBa2 | String(030) | Sim | Código de barras livre |
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
| CodEnd | String(020) | Sim | Código do endereçamento do produto |
| RotAnx | Number(002,0) | Sim | Código da rotina para controle de arquivos anexos |
| NumAnx | Number(010,0) | Sim | Número do controle de arquivos anexos gerado pelo sistema |
| IndPcq | String(001) | Sim | Indicativo se necessita de conferência de quantidades na carga |
| IteFis | String(060) | Sim | Código fiscal do item |
| DesFis | String(255) | Sim | Descrição fiscal do item |
| DatFis | Date | Sim | Data da última atualização da data fiscal |
| DatFat | Date | Sim | Data da última alteração da data fiscal |
| UsuFat | Number(010,0) | Sim | Usuário da última alteração da data fiscal |
| HorFat | Number(005,0) | Sim | Hora da última alteração da data fiscal |
| CusSal | Number(015,2) | Sim | Despesas com salários e ordenados para a fabricação de uma unidade do produto |
| CusEnc | Number(015,2) | Sim | Despesas com encargos sociais/trabalhistas para fabricação de uma unid. do prod. |
| NumDcr | Number(010,0) | Sim | Número do registro DCR-e |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- DatAtu
- HorAtu
- SeqAtu

---

## Índices

### E075VDRIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- IteFis

---

## Relacionamentos

### IR_E075VDR_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

