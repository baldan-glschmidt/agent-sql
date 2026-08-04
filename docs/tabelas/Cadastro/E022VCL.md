# E022VCL

## Descrição

Tabelas - Alterações de Classificações Fiscais

---

## Resumo

- Campos: 30
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodClf | String(003) | Não | Código interno da classificação fiscal |
| DatAtu | Date | Não | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Não | Hora/minuto da última atualização do cadastro |
| SeqAtu | Number(003,0) | Não | Sequência da atualização |
| DesClf | String(250) | Não | Descrição da classificação fiscal |
| ClaFis | String(010) | Não | Classificação fiscal |
| PerIpi | Number(005,2) | Sim | Percentual do IPI válido para as entradas de mercadorias |
| PerIps | Number(004,2) | Sim | Percentual de IPI válido para as saídas de mercadorias |
| ObsClf | String(250) | Sim | Observação para a classificação fiscal |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| RecPis | String(001) | Sim | Indicativo se os produtos/serviços desta classificação fiscal recuperam ou não PIS |
| TriPis | String(001) | Sim | Indicativo se os produtos/serviços desta classificação fiscal tem tributação de PIS ou não |
| TriCof | String(001) | Sim | Indicativo se os produtos/serviços desta classificação fiscal tem tributação de COFINS ou não |
| RecCof | String(001) | Sim | Indicativo se as notas fiscais poderão ter recuperação de Cofins |
| PerIim | Number(004,2) | Sim | Percentual do imposto de importação |
| TtbIpi | Number(001,0) | Sim | Indicativo do tipo de tributação de IPI |
| ClfExc | String(001) | Sim | Indicativo se a classificação fiscal é exceção |
| CodExc | Number(003,0) | Sim | Código da exceção da classificação fiscal |
| SitClf | String(001) | Sim | Situação da classificação fiscal |
| PerPis | Number(007,4) | Sim | Percentual do PIS |
| PerCof | Number(007,4) | Sim | Percentual do COFINS |
| RegTri | String(001) | Sim | Regime tributário de apuração da contribuição social |
| ConPre | Number(009,0) | Sim | Código da contribuição sobre a receita bruta (tabela 5.1.1 SPED Contribuições) |
| DatFis | Date | Sim | Data da última atualização da data fiscal |
| DatFat | Date | Sim | Data da última alteração da data fiscal |
| HorFat | Number(005,0) | Sim | Hora da última alteração da data fiscal |
| UsuFat | Number(010,0) | Sim | Usuário da última alteração da data fiscal |
| VlrLim | Number(015,2) | Sim | Valor do limite para isenção de PIS e Cofins |

---

## Chave Primária

- CodClf
- DatAtu
- HorAtu
- SeqAtu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
