# E085HIN

## Descrição

Cadastros - Clientes - Históricos nos Informantes

---

## Resumo

- Campos: 30
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodInf | Number(006,0) | Não | Código da referência comercial ou bancária |
| CodCei | String(001) | Não | Conceito do cliente na referência comercial ou bancária |
| SalDup | Number(015,2) | Sim | Saldo devedor do cliente |
| DatLim | Date | Sim | Data da última atualização do limite de crédito do cliente |
| VlrLim | Number(015,2) | Sim | Valor do limite de crédito do cliente |
| DatMac | Date | Sim | Data da ocorrência do maior acúmulo do cliente |
| VlrMac | Number(015,2) | Sim | Valor do maior acúmulo do cliente |
| DatUpe | Date | Sim | Data do último pedido do cliente |
| VlrUpe | Number(015,2) | Sim | Valor do último pedido do cliente |
| DatUfa | Date | Sim | Data do último faturamento do cliente |
| VlrUfa | Number(015,2) | Sim | Valor do último faturamento do cliente |
| DatUpg | Date | Sim | Data do último pagamento do cliente |
| VlrUpg | Number(015,2) | Sim | Valor do último pagamento do cliente |
| QtdPgt | Number(009,0) | Sim | Quantidade total de pagamentos efetuados pelo cliente |
| DatUpc | Date | Sim | Data do último pagamento em cartório do cliente |
| VlrUpc | Number(015,2) | Sim | Valor do último pagamento em cartório do cliente |
| QtdTpc | Number(004,0) | Sim | Quantidade total de pagamentos em cartório do cliente |
| DatMfa | Date | Sim | Data da ocorrência da maior fatura do cliente |
| VlrMfa | Number(015,2) | Sim | Valor da maior fatura do cliente |
| DatAtr | Date | Sim | Data da ocorrência do maior atraso do cliente |
| VlrAtr | Number(015,2) | Sim | Valor de pagamento do maior atraso do cliente |
| MaiAtr | Number(004,0) | Sim | Quantidade de dias do maior atraso do cliente |
| MedAtr | Number(004,0) | Sim | Quantidade de dias de média de atraso do cliente |
| DatRef | Date | Sim | Data da consulta a instituição bancária ou comericial |
| DatCdd | Date | Sim | Mês e Ano desde que o cliente possui conta na instituição bancária |
| CodBan | String(003) | Sim | Código do banco da conta corrente |
| TipTcc | Number(002,0) | Sim | Tipo de conta |
| CodAge | String(007) | Sim | Código da agência do banco da conta corrente |
| CcbHin | String(014) | Sim | Número da conta corrente no banco |

---

## Chave Primária

- CodCli
- CodInf

---

## Índices

### E085HINIndice1

**Tipo:** Não unico

Campos:
- CodInf

---

## Relacionamentos

### IR_E085HIN_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E085HIN_001

**Tabela:** E087INF

| Origem | Destino |
|--------|---------|
| CodInf | CodInf |

