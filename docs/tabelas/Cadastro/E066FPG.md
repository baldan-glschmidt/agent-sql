# E066FPG

## Descrição

Tabelas - Formas de Pagamento

---

## Resumo

- Campos: 47
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFpg | Number(002,0) | Não | Código da forma de pagamento |
| DesFpg | String(030) | Não | Descrição da forma de pagamento |
| AbrFpg | String(010) | Não | Abreviatura da forma de pagamento |
| VenMfp | Number(015,2) | Sim | Valor mínimo de pedido de venda para a forma de pagamento |
| VenFpl | String(001) | Não | Indicativo se a forma de pagamento está liberada para qualquer cliente |
| TipFpg | Number(002,0) | Não | Tipo de Pagamento para controle do Acerto |
| FveFpg | String(010) | Sim | Hierarquia da Forma de Venda |
| FveDec | String(001) | Sim | Indicativo se pode liberar formas de venda inferiores |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| CodEcf | String(003) | Sim | Código da finalizadora para ECF |
| CodOpe | Number(004,0) | Sim | Código da operadora |
| TipCar | String(001) | Sim | Tipo do cartão utilizado pela operadora |
| ExiAcr | String(001) | Sim | Indicativo se a forma de pagamento exige análise de crédito do cliente |
| DatAtu | Date | Sim | Data da última atualização |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| SitFpg | String(001) | Não | Situação da forma de pagamento |
| AcrFin | Number(005,2) | Sim | Percentual de acréscimo financeiro para produtos com tabela de preço no módulo de vendas |
| VenDsc | Number(005,2) | Sim | Percentual a acrescentar ou diminuir para formação do preço de venda |
| CprDsc | Number(005,2) | Sim | Percentual a acrescentar ou diminuir para formação do preço de compra |
| PerDsc | Number(005,2) | Sim | Percentual a acrescentar ou diminuir aos descontos concedidos |
| PerCom | Number(005,2) | Sim | Percentual a acrescentar ou diminuir à comissão do representante |
| RedCom | Number(005,2) | Sim | Percentual redutor do valor base comissão |
| GerCtr | String(001) | Sim | Indicativo se a forma de pagamento deverá gerar contrato automaticamente |
| CodCli | Number(009,0) | Sim | Código do cliente para a geração do contrato financeiro e controle de comissão |
| CodBan | String(003) | Sim | Código do banco na Febraban |
| BndDeb | String(199) | Sim | Bandeiras aceitas para cartão de débito no PDV |
| BndCre | String(199) | Sim | Bandeiras aceitas para cartão de crédito no PDV |
| CodTpt | String(003) | Sim | Código do tipo de título a receber para vendas |
| TptTef | String(003) | Sim | Código do tipo de título a receber para operações com TEF |
| TptSub | String(003) | Não | Tipo de título substituto no contas a receber pelo varejo |
| CodFin | Number(004,0) | Sim | Código da financeira |
| TptCpr | String(003) | Sim | Código do tipo de título a pagar |
| ConInf | String(001) | Sim | Indica se inf. para forma de pagto serão validadas no pedido ou anál. crédito |
| IdeUni | Number(009,0) | Não | Identificador único da forma de pagamento |
| EndAut | String(001) | Sim | Indica na devolução de vendas no Retaguarda Senior o endosso deve ser gerado automaticamente |
| PorDev | String(004) | Sim | Indica o portador ao qual o título será atrelado quando a FPG não gerar endosso automático |
| ImpBol | String(001) | Sim | Indicativo se irá imprimir o documento de cobrança automaticamente |
| IntWmw | String(001) | Sim | Indicativo se registro deve integrar com o WMW |
| PorRem | String(004) | Sim | Indica o portador que será usado como sugestão na remessa de títulos |
| SitWmw | String(001) | Sim | Situação do registro no WMW |

---

## Chave Primária

- CodEmp
- CodFpg

---

## Índices

### E066FPGIndice1

**Tipo:** Unico

Campos:
- IdeUni

---

## Relacionamentos

### IR_E066FPG_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

