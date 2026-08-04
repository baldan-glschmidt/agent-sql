# E095HFO

## Descrição

Cadastros - Fornecedores - Históricos

---

## Resumo

- Campos: 114
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SalDup | Number(015,2) | Sim | Saldo devedor de duplicatas aos fornecedores |
| SalOut | Number(015,2) | Sim | Saldo devedor de outros títulos aos fornecedores |
| SalCre | Number(015,2) | Sim | Saldo créditos a fornecedores |
| DatUpe | Date | Sim | Data do último pedido |
| VlrUpe | Number(015,2) | Sim | Valor do último pedido |
| DatUcp | Date | Sim | Data da última nota fiscal de entrada |
| VlrUcp | Number(015,2) | Sim | Valor da última nota fiscal de entrada |
| DatMcp | Date | Sim | Data da maior nota fiscal de entrada (maior compra) |
| VlrMcp | Number(015,2) | Sim | Valor da maior nota fiscal de entrada (maior compra) |
| DatUpg | Date | Sim | Data último pagamento |
| VlrUpg | Number(015,2) | Sim | Valor do último pagamento |
| QtdPgt | Number(009,0) | Sim | Quantidade de títulos pagos ao fornecedor |
| DatAtr | Date | Sim | Data do maior atraso |
| VlrAtr | Number(015,2) | Sim | Valor do maior atraso |
| MaiAtr | Number(004,0) | Sim | Quantidade de dias do maior atraso |
| MedAtr | Number(004,0) | Sim | Quantidade de dias de atraso médio |
| PrzEnt | Number(003,0) | Sim | Quantidade de dias de prazo de entrega do fornecedor |
| CprCql | Number(002,0) | Sim | Conceito do fornecedor para o quesito qualidade (0 a 99) |
| CprCpe | Number(002,0) | Sim | Conceito do fornecedor para o quesito pontualidade na entrega (0 a 99) |
| CprCat | Number(002,0) | Sim | Conceito do fornecedor para o quesito atendimento (0 a 99) |
| CodTpr | String(004) | Sim | Código da tabela de preço padrão |
| CodCpg | String(006) | Sim | Código da condição de pagamento padrão |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| QtdDcv | Number(003,0) | Sim | Quantidade de dias para cálculo de vencimento |
| CriEdv | String(001) | Sim | Critério para escolha do dia de vencimento |
| CodTra | Number(009,0) | Sim | Código da transportadora padrão |
| CodPor | String(004) | Sim | Código do portador padrão |
| CodCrt | String(002) | Sim | Código da carteira padrão |
| CodBan | String(003) | Sim | Código do banco da conta corrente do fornecedor |
| TipTcc | Number(002,0) | Sim | Tipo de conta |
| CodAge | String(007) | Sim | Código da agência do banco da conta corrente do fornecedor |
| CcbFor | String(014) | Sim | Número da conta corrente do fornecedor no banco |
| CodCrp | String(003) | Sim | Código do grupo de contas a pagar |
| UltDup | Number(010,0) | Sim | Número da última duplicata gerada para o fornecedor |
| PagJmm | Number(005,2) | Sim | Percentual de juros de mora mês para o contas a pagar |
| PagTir | String(001) | Sim | Tipo de juros para o contas a pagar |
| PagDtj | Number(004,0) | Sim | Dias de tolerância para cálculo de juros de mora do contas a pagar |
| PagMul | Number(005,2) | Sim | Percentual de multa para atraso do contas a pagar |
| PagDtm | Number(004,0) | Sim | Dias de tolerância para multa do conta a pagar |
| PerDsc | Number(004,2) | Sim | Percentual padrão de desconto para os títulos gerados no financeiro |
| TolDsc | Number(004,0) | Sim | Quantidade padrão de dias de tolerância para desconto |
| AntDsc | String(001) | Sim | Indicativo se calcula desconto por antecipação de pagamento |
| PagEev | Number(003,0) | Sim | Quantidade mínima de dias aceito entre a data de entrada e o vencimento de um título |
| PerDs1 | Number(005,2) | Sim | Percentual de desconto - 1 para fornecedor |
| PerDs2 | Number(005,2) | Sim | Percentual de desconto - 2 para fornecedor |
| PerDs3 | Number(005,2) | Sim | Percentual de desconto 3 para fornecedor |
| PerDs4 | Number(005,2) | Sim | Percentual de desconto 4 para fornecedor |
| PerDs5 | Number(005,2) | Sim | Percentual de desconto 5 para fornecedor |
| PerFun | Number(004,2) | Sim | Percentual do Funrural ou INSS do Produto para Notas Fiscas de Entrada |
| PerIns | Number(004,2) | Sim | Percentual do INSS para o Serviço |
| IndInd | String(001) | Não | Indicativo se o fornecedor é indústria ou equiparado a industrial para IPI presumido |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| CtaAux | Number(009,0) | Sim | Número reduzido da conta de composição auxiliar - 1 |
| CtaAad | Number(009,0) | Sim | Número reduzido da conta de composição auxiliar - 2 |
| ConEst | String(001) | Não | Indicativo se o representante deve contar estoque do cliente |
| PerFre | Number(005,2) | Sim | Percentual de Frete |
| PerSeg | Number(005,2) | Sim | Percentual de Seguro |
| PerEmb | Number(005,2) | Sim | Percentual de Embalagens |
| PerEnc | Number(005,2) | Sim | Percentual de Encargos |
| PerOut | Number(005,2) | Sim | Percentual de Outras Despesas |
| PerIss | Number(006,4) | Sim | Percentual do ISS para os serviços do fornecedor |
| PerIrf | Number(004,2) | Sim | Percentual do IRRF para os serviços do fornecedor |
| SeqOrm | Number(005,0) | Sim | Sequência do endereço de origem da mercadoria |
| CifFob | String(001) | Sim | Indicativo se o frete para o fornecedor é CIF ou FOB |
| CodFav | Number(014,0) | Sim | Número do CNPJ ou CPF do favorecido |
| DocIdeFav | String(014) | Sim | Número do CNPJ ou CPF do favorecido |
| PerIne | Number(004,2) | Sim | Percentual do INSS da parte da empresa |
| RvlCfr | String(001) | Sim | Tipo de rateio do valor do conhecimento de frete para efetuar movimento de estoque(acerto) |
| RvlFre | String(001) | Sim | Tipo de rateio do valor de frete para os itens de produto. |
| RvlSeg | String(001) | Sim | Tipo de rateio do valor de seguro para os itens de produto. |
| RvlEmb | String(001) | Sim | Tipo de rateio do valor de embalagens para os itens de produto. |
| RvlEnc | String(001) | Sim | Tipo de rateio do valor de encargos para os itens de produto e serviço. |
| RvlOut | String(001) | Sim | Tipo de rateio do valor de outros para os itens de produto e serviço. |
| RvlDar | String(001) | Sim | Tipo de rateio do valor de arredondamento para os itens de produto e serviço. |
| RvlFei | String(001) | Sim | Tipo de rateio do valor de frete de importação para os itens de produtos |
| RvlSei | String(001) | Sim | Tipo de rateio do valor de seguro de importação para os itens de produtos |
| RvlOui | String(001) | Sim | Tipo de rateio do valor de outras despesas de importação para os itens de produto e serviço |
| CodDep | String(010) | Sim | Código do depósito padrão para armazenagem no sistema de WMS |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| ForMon | String(001) | Sim | Indicativo para informar ao sistema se fornecedor realiza montagem de produtos |
| SerCur | String(030) | Sim | Número de série para serviço de curso online para o segmento varejo. |
| PgtMon | String(002) | Sim | Tipo de pagamento a ser feito para os montadores |
| PgtFre | String(002) | Sim | Tipo de pagamento a ser feito para os motoristas |
| TnsPro | String(005) | Sim | Transação de sugestão da nota fiscal de entrada para produtos |
| TnsSer | String(005) | Sim | Transação de sugestão da nota fiscal de entrada para serviços |
| CodEdc | String(003) | Sim | Espécie de documento para fins fiscais |
| CqdCvn | String(001) | Sim | Considerar quantidades devolvidas no cálculo de valorização nas NFE do tipo 8 |
| DscPon | Number(004,2) | Sim | Percentual de desconto por pontualidade para os títulos gerados |
| DscAnt | Number(004,2) | Sim | Percentual de desconto por antecipação para os títulos gerados |
| CodFin | Number(004,0) | Sim | Código da finalidade de compra |
| PerSen | Number(004,2) | Sim | Percentual do imposto SENAR/SENAT para notas fiscais de entrada |
| PerDif | Number(007,4) | Sim | Percentual de diferimento |
| TnsRcp | String(005) | Sim | Transação de recebimento para o produto da nota fiscal de entrada |
| TnsPgp | String(005) | Sim | Transação de pagamento para o produto da nota fiscal de entrada |
| TnsRcs | String(005) | Sim | Transação de recebimento para o serviço da nota fiscal de entrada |
| TnsPgs | String(005) | Sim | Transação de pagamento para o serviço da nota fiscal de entrada |
| PerGil | Number(004,2) | Sim | Percentual de GILRAT - Grau Incid. Incapac. Laborat. Decor. Riscos Amb. de Trab. |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| EcoIid | String(001) | Sim | Emitir Contra Nota |
| IndFcf | String(001) | Sim | Indicativo se o fornecedor calcula fundeinfra |
| IdeFav | String(050) | Sim | Identificador único alfanumérico |
| USU_CodIde | String(040) | Sim | Alguns Fornecedores informa o codigo de identificacao para o pagto.ou deposito |

---

## Chave Primária

- CodFor
- CodEmp
- CodFil

---

## Índices

### E095HFOIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

### USU_E095HFO1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodFor
- CtaRed

---

## Relacionamentos

### IR_E095HFO_000

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E095HFO_002

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

