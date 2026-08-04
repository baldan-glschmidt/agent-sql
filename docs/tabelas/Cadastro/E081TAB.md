# E081TAB

## Descrição

Tabelas - Tabelas de Preços de Venda - Dados Gerais

---

## Resumo

- Campos: 41
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço |
| DesTpr | String(250) | Não | Descrição da tabela de preço |
| AbrTpr | String(010) | Não | Abreviatura da tabela de preço |
| CodMoe | String(003) | Não | Código da moeda que os preço dos produtos/serviços estão representados |
| EspCli | String(001) | Não | Indicativo se a tabela é especial para cliente |
| AplTpv | Number(001,0) | Não | Aplicação da tabela de preço de venda |
| SitReg | String(001) | Não | Situação do registro |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| UtiPme | String(001) | Sim | Indicativo se utiliza preço médio como preço base dos itens da tabela de preço |
| CodPdv | Number(010,0) | Sim | Código interno no PDV |
| CodCli | Number(009,0) | Sim | Código do cliente que poderá utilizar a tabela de preço |
| CodTpb | String(004) | Sim | Código da tabela de preço base |
| VenEcf | String(001) | Sim | Indicativo se a tabela será utilizada para venda com ECF |
| TabBld | String(001) | Sim | Indicativo se a tabela de preço é um tablóide |
| TabPrm | String(001) | Sim | Indicativo se a tabela de preço é uma promoção interna |
| TipTge | String(002) | Sim | Tipo de Garantia Estendida |
| CodSeg | Number(009,0) | Sim | Código da Seguradora |
| CodFab | String(010) | Sim | Código do Fabricante |
| CodAgg | String(001) | Sim | Código de agrupamento de materiais/produtos para garantia estendida |
| IdaMin | Number(004,0) | Sim | Idade mínima para adquirir o serviço parcela protegida |
| IdaMax | Number(004,0) | Sim | Idade máxima para adquirir o serviço parcela protegida |
| CodApc | Number(009,0) | Sim | Código da análise |
| TipFpr | Number(001,0) | Sim | Tipo informado para formação do preço final (venda,margem ou referência) |
| FilApc | Number(005,0) | Sim | Código da filial da Análise |
| TabCam | String(001) | Sim | Indicativo se a tabela de preço é uma campanha de triangulação |
| CodFam | String(006) | Sim | Código da família de produto |
| UniMed | String(003) | Sim | Unidade de Medida dos Produtos associado a Família (Unidade Medida de Estocagem) |
| TprBas | String(004) | Sim | Código da tabela de preço base (formação de preços para comércio) |
| TabDev | String(001) | Sim | Indicativo se a tabela de preço aceita que os produtos sejam devolvidos |
| VenFci | String(001) | Sim | Indicativo se a tabela de preço é utilizada no cálculo do FCI |
| IntWmw | String(001) | Sim | Indicativo se registro deve integrar com o WMW |
| SitWmw | String(001) | Sim | Situação do registro no WMW |
| ObsTab | String(100) | Sim | Dados Gerais - Observação |
| USU_TPSEMG | String(001) | Sim | Segmento do Cliente Site Tabela Preço |
| USU_IntSF | String(001) | Sim | Integra com Salesforce |
| USU_CodTns | String(005) | Sim | Transação Padrão |
| USU_ApeSF | String(999) | Sim | Apelido para Salesforce |
| USU_SitSF | String(001) | Sim | Situação no Salesforce |

---

## Chave Primária

- CodEmp
- CodTpr

---

## Índices

### E081TABIndice1

**Tipo:** Não unico

Campos:
- CodMoe

---

## Relacionamentos

### IR_E081TAB_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E081TAB_004

**Tabela:** E031MOE

| Origem | Destino |
|--------|---------|
| CodMoe | CodMoe |

