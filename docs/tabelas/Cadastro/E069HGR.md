# E069HGR

## Descrição

Cadastros - Grupos de Empresas - Históricos

---

## Resumo

- Campos: 46
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodGre | Number(009,0) | Não | Código do grupo de empresa |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SalDup | Number(015,2) | Sim | Saldo devedor de duplicatas dos grupos de empresas |
| SalOut | Number(015,2) | Sim | Saldo devedor de outros títulos dos grupos de empresas |
| SalCre | Number(015,2) | Sim | Saldo dos créditos dos grupos de empresas |
| DatLim | Date | Sim | Data da última atualização do limite de crédito do grupo |
| VlrLim | Number(015,2) | Sim | Valor do limite de crédito do grupo |
| LimApr | String(001) | Sim | Indicativo se o limite de crédito está ou não aprovado |
| DatMac | Date | Sim | Data do maior saldo devedor acumulado do grupo |
| VlrMac | Number(015,2) | Sim | Valor do maior saldo devedor acumulado do grupo |
| DatUpe | Date | Sim | Data do último pedido do grupo |
| VlrUpe | Number(015,2) | Sim | Valor do último pedido do grupo |
| DatUfa | Date | Sim | Data do último faturamento do grupo |
| VlrUfa | Number(015,2) | Sim | Valor do último faturamento do grupo |
| DatUpg | Date | Sim | Data do último pagamento do grupo |
| VlrUpg | Number(015,2) | Sim | Valor do último pagamento do grupo |
| QtdPgt | Number(009,0) | Sim | Quantidade de pagamento efetuados pelo grupo |
| DatUpc | Date | Sim | Data do último pagamento em cartório efetuado pelo grupo |
| VlrUpc | Number(015,2) | Sim | Valor do último pagamento em cartório efetuado pelo grupo |
| QtdTpc | Number(004,0) | Sim | Quantidade de pagamentos efetuados em cartório pelo grupo |
| DatMfa | Date | Sim | Data da maior fatura do grupo |
| VlrMfa | Number(015,2) | Sim | Valor da maior fatura do grupo |
| DatAtr | Date | Sim | Data do maior atraso de pagamento do grupo |
| VlrAtr | Number(015,2) | Sim | Valor do título de maior atraso pago pelo grupo |
| MaiAtr | Number(004,0) | Sim | Quantidade de dias de maior pago pelo grupo |
| MedAtr | Number(004,0) | Sim | Quantidade de dias de média de atraso nos pagamentos do grupo |
| ConCli | Number(009,0) | Sim | Contador do número de clientes que compõe o grupo |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data do cadastro do registro |
| HorGer | Number(005,0) | Sim | Hora do cadastro do registro |
| UsuAlt | Number(010,0) | Sim | Código do usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Data da última alteração do registro |
| AvaVlr | Number(015,2) | Sim | Valor total para avalizar |
| AvaVlu | Number(015,2) | Sim | Valor avalizado no atual momento |
| AvaVls | Number(015,2) | Sim | Valor disponível para avalizar |
| AvaAti | String(001) | Sim | Determina se o cliente pode ser usado como avalista |
| AvaMot | Number(006,0) | Sim | Código do motivo usado para justificar porque o avalista está inativo |
| AvaObs | String(250) | Sim | Observação do motivo da inativação do avalista |
| AvdAlt | Date | Sim | Data da última alteração das informações do avalista |
| AvhAlt | Number(005,0) | Sim | Hora da última alteração das informações do avalista |
| AvuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração das informações do avalista |
| AvdGer | Date | Sim | Data de geração das informações do avalista |
| AvhGer | Number(005,0) | Sim | Hora de geração das informações do avalista |
| AvuGer | Number(010,0) | Sim | Usuário responsável pela geração das informações do avalista |

---

## Chave Primária

- CodGre
- CodEmp
- CodFil

---

## Índices

### E069HGRIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

### IR_E069HGR_000

**Tabela:** E069GRE

| Origem | Destino |
|--------|---------|
| CodGre | CodGre |

### IR_E069HGR_002

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

