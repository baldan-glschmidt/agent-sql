# E022CLF

## Descrição

Tabelas - Classificações Fiscais

---

## Resumo

- Campos: 35
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodClf | String(003) | Não | Código interno da classificação fiscal |
| DesClf | String(250) | Não | Descrição da classificação fiscal |
| ClaFis | String(010) | Não | Classificação fiscal |
| PerIpi | Number(008,4) | Sim | Percentual do IPI válido para as entradas de mercadorias |
| PerIps | Number(008,4) | Sim | Percentual de IPI válido para as saídas de mercadorias |
| ObsClf | String(499) | Sim | Observação para a classificação fiscal |
| RecPis | String(001) | Sim | Indicativo se os produtos/serviços desta classificação fiscal recuperam ou não PIS |
| TriPis | String(001) | Sim | Indicativo se os produtos/serviços desta classificação fiscal tem tributação de PIS ou não |
| PerPis | Number(008,4) | Sim | Percentual do PIS |
| TriCof | String(001) | Sim | Indicativo se os produtos/serviços desta classificação fiscal tem tributação de COFINS ou não |
| RecCof | String(001) | Sim | Indicativo se as notas fiscais poderão ter recuperação de Cofins |
| PerCof | Number(008,4) | Sim | Percentual do COFINS |
| PerIim | Number(004,2) | Sim | Percentual do imposto de importação |
| TtbIpi | Number(001,0) | Sim | Indicativo do tipo de tributação de IPI |
| ClfExc | String(001) | Sim | Indicativo se a classificação fiscal é exceção |
| CodExc | Number(003,0) | Sim | Código da exceção da classificação fiscal |
| RegTri | String(001) | Sim | Regime tributário de apuração da contribuição social |
| ConPre | Number(009,0) | Sim | Código da contribuição sobre a receita bruta (tabela 5.1.1 SPED Contribuições) |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SitClf | String(001) | Sim | Situação da classificação fiscal |
| VlrLim | Number(015,2) | Sim | Valor do limite para isenção de PIS e Cofins |
| CodEnq | Number(003,0) | Sim | Código de enquadramento legal do IPI |
| CodCes | String(007) | Sim | Código especificador da substituição tributária |
| UniMed | String(003) | Sim | Código da Unidade de Medida Fiscal |
| IndVma | String(001) | Sim | Indicativo se o valor do imposto deve ser calculado considerando a tabela de valor mínimo por unidade de medida |
| Art119 | String(001) | Sim | NCM enquadrada no art. 119 do RICMS/2017 do Paraná |
| USU_naladi | String(008) | Sim | Naladi exportacao |
| USU_Descla | String(250) | Sim | Descricao NCM NBM Inaladi |
| USU_codnbm | String(010) | Sim | Codido NCM exportacao |
| USU_codncm | String(010) | Sim | Codido NCM exportacao |
| USU_IdConv | String(001) | Não | Identificador se a Classificacao pertence ao Convenio p/ Desconto Regional |
| USU_historico | String(250) | Sim | Historico |
| USU_UniMedExp | String(008) | Sim | Unidade de Medida Exportação |

---

## Chave Primária

- CodClf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
