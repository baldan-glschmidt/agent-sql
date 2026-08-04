# E120PAR

## Descrição

Vendas - Pedidos - Parcelas

---

## Resumo

- Campos: 47
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqPar | Number(003,0) | Não | Sequência da parcela |
| CodCrp | String(003) | Sim | Código do grupo a receber |
| CodFcr | String(003) | Sim | Código da moeda ou índice como fator de correção (financeiro) |
| DatFcr | Date | Sim | Data da cotação da moeda ou índice para o fator de correção (financeiro) |
| DiaPar | Number(004,0) | Sim | Quantidade de dias para a parcela |
| VctPar | Date | Sim | Data de vencimento da parcela |
| PerPar | Number(007,4) | Sim | Percentual do valor da parcela |
| VlrPar | Number(015,2) | Sim | Valor da parcela |
| DscPar | Number(005,2) | Sim | Percentual de desconto previsto para a parcela |
| ObsPar | String(250) | Sim | Texto da observação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| CodTpt | String(003) | Sim | Código do tipo de título a ser gerado no contas a receber |
| CodPor | String(004) | Sim | Código do portador a ser lançado o título no contas a receber |
| DatNeg | Date | Sim | Data base dos valores negociados (data até) |
| DscNeg | Number(015,2) | Sim | Valor do desconto negociado a ser concedido ao título a receber |
| CodSac | Number(014,0) | Sim | Código do sacado |
| DocIdeSac | String(014) | Sim | Código do sacado |
| CheBan | String(003) | Sim | Número do banco na FEBRABAN do cheque |
| CheAge | String(007) | Sim | Número da agência do banco do cheque |
| CheCta | String(014) | Sim | Número da conta no banco do cheque |
| CheNum | String(010) | Sim | Número do cheque no banco |
| CodBar | String(050) | Sim | Código de barras do título |
| CatTef | String(128) | Sim | Código de Autorização da Transação para Pagamentos Eletrônicos |
| NsuTef | String(100) | Sim | Número Seqüencial Único da Transação TEF (Host - Operadora) |
| CatExt | String(100) | Sim | Código de autorização externo |
| VlrRps | Number(015,2) | Sim | Valor de repasse a operado do cartão Débito/Crédito. |
| CodOpe | Number(004,0) | Sim | Código da operadora |
| CarCov | String(100) | Sim | Número do cartão convênio |
| CarPre | String(050) | Sim | Código do Cartão Presente |
| CodCnv | Number(004,0) | Sim | Código do convênio |
| VlrTro | Number(015,2) | Sim | Valor do troco dado ao cliente da venda. |
| FpgTro | Number(002,0) | Sim | Código da forma de pagamento |
| DscAnt | Number(004,2) | Sim | Percentual de desconto por antecipação para os títulos gerados |
| DscPon | Number(004,2) | Sim | Percentual de desconto por pontualidade para os títulos gerados |
| JurVen | String(001) | Sim | Indicativo se o sistema deve calcular juros/multa desde a data da venda |
| DatPpt | Date | Sim | Data do provável pagamento do título |
| EntPar | String(001) | Sim | Parcela é uma entrada |
| IndPag | String(001) | Sim | Indicativo da forma de pagamento |
| TipInt | String(001) | Sim | Tipo Integração do processo de pagamento com o sistema de automação da empresa |
| BanOpe | String(002) | Sim | Bandeira da operadora de cartão de crédito e/ou débito |
| IdeSac | String(050) | Sim | Identificador único alfanumérico |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120PAR_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

