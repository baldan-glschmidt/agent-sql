# E028CPG

## Descrição

Tabelas - Condição de Pagamento

---

## Resumo

- Campos: 66
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCpg | String(006) | Não | Código da condição de pagamento |
| DesCpg | String(050) | Não | Descrição da condição de pagamento |
| AbrCpg | String(010) | Não | Abreviatura da condição de pagamento |
| AplCpg | String(001) | Não | Aplicação da condição de pagamento |
| PgtAnt | String(001) | Não | Indicativo se é condição com pagamento antecipado |
| DiaEsp | String(001) | Não | Indicativo do dia da semana para vencimento parcelas |
| DiaMe1 | Number(002,0) | Sim | Primeiro dia especial do mês para vencimento das parcelas |
| DiaMe2 | Number(002,0) | Sim | Segundo dia especial do mês para vencimento das parcelas |
| DiaMe3 | Number(002,0) | Sim | Terceiro dia especial do mês para vencimento das parcelas |
| DiaSem | String(007) | Sim | Controle dos dias da semana aceitos ou não para vencimento |
| DiaMes | String(031) | Sim | Controle dos dias do mês aceitos ou não para vencimento |
| PrzMed | Number(003,0) | Sim | Prazo médio da condição de pagamento |
| QtdPar | Number(003,0) | Não | Quantidade total de parcelas da condição de pagamento |
| IpiPar | String(001) | Não | Indicativo se o valor total do IPI deve estar na 1ª parcela |
| IcmPar | String(001) | Não | Indicativo se o valor total do ICMS deve estar na 1ª parcela |
| SubPar | String(001) | Não | Indicativo se o valor total do ICMS Substituído deve estar na 1ª parcela |
| FrePar | String(001) | Não | Indicativo se o valor total do frete deve estar na 1ª parcela |
| SegPar | String(001) | Não | Indicativo se o valor total do seguro deve estar na 1ª parcela |
| EncPar | String(001) | Não | Indicativo se o valor total dos encargos deve estar na 1ª parcela |
| EmbPar | String(001) | Não | Indicativo se o valor total das embalagens deve estar na 1ª parcela |
| OutPar | String(001) | Não | Indicativo se o valor total das outras despesas deve estar na 1ª parcela |
| DarPar | String(001) | Não | Indicativo se o valor total de arredondamento deve estar na 1ª parcela |
| AcrFin | Number(005,2) | Sim | Percentual de acréscimo financeiro para produtos com tabela de preço no módulo de vendas |
| VenDsc | Number(005,2) | Sim | Percentual a acrescentar ou diminuir para formação do preço de venda |
| CprDsc | Number(005,2) | Sim | Percentual a acrescentar ou diminuir para formação do preço de compra |
| PerDsc | Number(005,2) | Sim | Percentual a acrescentar ou diminuir aos descontos concedidos |
| PerCom | Number(005,2) | Sim | Percentual a acrescentar ou diminuir à comissão do representante |
| RedCom | Number(005,2) | Sim | Percentual redutor do valor base comissão |
| TipPar | Number(001,0) | Não | Tipo de parcelas |
| SitCpg | String(001) | Não | Situação da condição de pagamento |
| CodTpr | String(004) | Sim | Código da tabela de preço |
| FveCpg | String(010) | Sim | Hierarquia da Forma de Venda |
| FveDec | String(001) | Sim | Indicativo se pode liberar formas de venda inferiores |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| TipInt | Number(001,0) | Sim | Tipo de Integração |
| CodPdv | Number(004,0) | Sim | Código interno no PDV |
| IssPar | String(001) | Sim | Indicativo se o valor total do ISS deve estar na 1ª parcela |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatAtu | Date | Sim | Data da última atualização |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| PerEnc | Number(005,2) | Sim | Percentual de Encargos |
| ComTit | String(001) | Sim | Considerar base e valor de comissão também na primeira parcela do título |
| MesEs1 | Number(002,0) | Sim | Primeiro mês especial para vencimento das parcelas |
| MesEs2 | Number(002,0) | Sim | Segundo mês especial para vencimento das parcelas |
| MesEs3 | Number(002,0) | Sim | Terceiro mês especial para vencimento das parcelas |
| RetIss | String(001) | Sim | Indicativo se o valor total do ISS retido deve ser descontado da 1ª parcela |
| TxaJur | Number(005,2) | Sim | Percentual de juros conforme condição de pagamento escolhida. |
| TipCju | Number(001,0) | Sim | Tipo de cálculo que será aplicado sobre os juros |
| DscAnt | Number(004,2) | Sim | Percentual de desconto por antecipação para os títulos gerados |
| DscPon | Number(004,2) | Sim | Percentual de desconto por pontualidade para os títulos gerados |
| JurVen | String(001) | Sim | Indicativo se o sistema deve calcular juros/multa desde a data da venda |
| IrfPar | String(001) | Não | Indicativo se o valor total do IRRF deve estar na 1ª parcela |
| IdeUni | Number(009,0) | Não | Identificador único da condição de pagamento |
| IntWmw | String(001) | Sim | Indicativo se registro deve integrar com o WMW |
| SitWmw | String(001) | Sim | Situação do registro no WMW |
| GerTit | String(001) | Sim | Indicativo se título deverá ser gerado a partir do pedido |
| USU_acfweb | Number(005,2) | Sim | Acrescimo Financeiro WEB |
| USU_codgecex | Number(003,0) | Sim | Codigo Cond.Pagto Gecex |
| USU_IntSF | String(001) | Sim | Integra com Salesforce |
| USU_SitSF | String(001) | Sim | Situação no Salesforce |

---

## Chave Primária

- CodEmp
- CodCpg

---

## Índices

### E028CPGIndice1

**Tipo:** Unico

Campos:
- IdeUni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
