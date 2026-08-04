# E440PAR

## Descrição

Compras - Notas Fiscais de Entrada - Parcelas

---

## Resumo

- Campos: 42
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| CodPar | Number(003,0) | Não | Sequência de parcelas da nota fiscal de entrada |
| CodCrp | String(003) | Sim | Código do grupo a pagar |
| NumTit | String(015) | Não | Número do título a ser gerado no contas a pagar |
| CodTpt | String(003) | Sim | Código do tipo de título a ser gerado no contas a pagar |
| CodFcr | String(003) | Sim | Código da moeda ou índice como fator de correção (financeiro) |
| DatFcr | Date | Sim | Data da cotação da moeda ou índice para o fator de correção (financeiro) |
| VctPar | Date | Não | Data de vencimento da parcela da nota fiscal de entrada |
| VlrPar | Number(015,2) | Não | Valor da parcela da nota fiscal de entrada |
| PerDdp | Number(005,2) | Sim | Percentual de desconto da parcela da nota fiscal de entrada |
| QtdDdd | Number(003,0) | Sim | Quantidade de dias de tolerância para o desconto da parcela |
| CodPor | String(004) | Não | Código do portador a ser lançado o título no contas a pagar |
| CodCrt | String(002) | Não | Código da carteira a ser lançado o título no contas a pagar |
| CodNtg | Number(004,0) | Sim | Código da natureza de gasto |
| ObsPar | String(250) | Sim | Texto da observação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| VlrDsc | Number(015,2) | Sim | Valor do desconto negociado a ser concedido ao título a pagar |
| JrsNeg | Number(015,2) | Sim | Valor dos juros negociados |
| MulNeg | Number(015,2) | Sim | Valor da multa negociada |
| OutNeg | Number(015,2) | Sim | Valor de outros valores negociados |
| DatNeg | Date | Sim | Data base dos valores negociados (data até) |
| CodBan | String(003) | Sim | Número do banco na FEBRABAN |
| TipTcc | Number(002,0) | Sim | Tipo de conta |
| CodAge | String(007) | Sim | Número da agência do banco |
| CcbFor | String(014) | Sim | Número da conta corrente do fornecedor no banco |
| CodFav | Number(014,0) | Sim | Número do CNPJ ou CPF do favorecido |
| DocIdeFav | String(014) | Sim | Número do CNPJ ou CPF do favorecido |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| NumCpr | String(020) | Sim | Número do cartão presente |
| CodRep | Number(009,0) | Sim | Código do representante |
| NumCoo | Number(009,0) | Sim | Contador da ordem de operação que emitiu o recebimento na ECF |
| CroEcf | Number(006,0) | Sim | Cont. de Reinício de Operação do ECF |
| CodEqu | Number(003,0) | Sim | Código do equipamento fiscal |
| VlrInt | Number(015,2) | Sim | Valor de intermediação de serviços da parcela |
| IndPag | String(001) | Sim | Indicativo da forma de pagamento |
| IdeFav | String(050) | Sim | Identificador único alfanumérico |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- CodPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440PAR_004

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |

### IR_E440PAR_015

**Tabela:** E039POR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPor | CodPor |

### IR_E440PAR_016

**Tabela:** E033CRT

| Origem | Destino |
|--------|---------|
| CodCrt | CodCrt |

