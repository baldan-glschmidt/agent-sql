# E090HRP

## Descrição

Cadastros - Representantes - Históricos

---

## Resumo

- Campos: 71
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRep | Number(009,0) | Não | Código do representante |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodRve | String(003) | Não | Código da região de venda do representante |
| PerCom | Number(005,2) | Sim | Percentual de comissão padrão para produtos do representante |
| PerCos | Number(005,2) | Sim | Percentual de comissão padrão para serviços do representante |
| ComFat | Number(005,2) | Sim | Percentual da comissão pago ao representante no faturamento |
| ComRec | Number(005,2) | Sim | Percentual da comissão pago ao representante no recebimento dos títulos |
| PerIrf | Number(004,2) | Sim | Percentual do IRRF para o cálculo das comissões |
| PerIss | Number(006,4) | Sim | Percentual do ISS para o cálculo das comissões |
| PerIns | Number(004,2) | Sim | Percentual do INSS para o cálculo das comissões |
| IpiCom | String(001) | Não | Indicativo se o IPI está ou não na base de comissão |
| IcmCom | String(001) | Não | Indicativo se o ICMS está ou não na base de comissão |
| SubCom | String(001) | Não | Indicativo se o ICMS substituído está ou não na base de comissão |
| FreCom | String(001) | Não | Indicativo se o frete está ou não na base de comissão |
| SegCom | String(001) | Não | Indicativo se o seguro está ou não na base de comissão |
| EmbCom | String(001) | Não | Indicativo se o valor das embalagens está ou não na base de comissão |
| EncCom | String(001) | Não | Indicativo se o valor dos encargos está ou não na base de comissão |
| OutCom | String(001) | Não | Indicativo se o valor das outras despesas está ou não na base de comissão |
| DarCom | String(001) | Não | Indicativo se o valor do arredondamento está ou não na base de comissão |
| RecAdc | String(001) | Sim | Indicativo se abate os descontos concedidos da comissão |
| RecAoc | String(001) | Sim | Indicativo se abate os outros descontos da comissão |
| RecPcj | String(001) | Sim | Indicativo se recebe comissão sobre juros cobrados |
| RecPcm | String(001) | Sim | Indicativo se recebe comissão sobre multas cobradas |
| RecPcc | String(001) | Sim | Indicativo se recebe comissão sobre a correção monetária |
| RecPce | String(001) | Sim | Indicativo se recebe comissão sobre os encargos financeiros |
| RecPco | String(001) | Sim | Indicativo se recebe comissão sobre outros acréscimos |
| ComPri | String(001) | Não | Indicativo se a comissão é paga totalmente na primeira parcela |
| RepSup | Number(009,0) | Sim | Código do representante superior do representante |
| CatRep | String(003) | Sim | Categoria do Representante |
| ComSup | Number(004,2) | Sim | Percentual da comissão pago ao representante superior |
| CodBan | String(003) | Sim | Código do banco da conta corrente do representante |
| CodAge | String(007) | Sim | Código da agência do banco da conta corrente do representante |
| CcbRep | String(014) | Sim | Número da conta corrente do representante |
| TipCol | Number(001,0) | Sim | Tipo de Colaborador |
| NumCad | Number(009,0) | Sim | Número do Cadastro do Representante como Colaborador |
| VenVmp | Number(015,2) | Sim | Valor mínimo aceito para pedidos |
| RecVmt | Number(015,2) | Sim | Valor mínimo aceito para títulos do contas a receber |
| PerCqt | Number(007,4) | Sim | Percentual das cotas sobre as quantidades de venda |
| PerCvl | Number(007,4) | Sim | Percentual das cotas sobre os valores de venda |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| ConEst | String(001) | Não | Indicativo se o representante deve contar estoque do cliente |
| InsCom | String(001) | Sim | Indicativo se o INSS está ou não na base de comissão dos pedidos, pré-faturas e notas fiscais |
| IssCom | String(001) | Sim | Indicativo se o ISS está ou não na base de comissão dos pedidos, pré-faturas e notas fiscais |
| CofCom | String(001) | Sim | Indicativo se o COFINS Retido está ou não na base de comissão dos pedidos, pré-faturas e notas fiscais |
| PisCom | String(001) | Sim | Indicativo se o PIS Retido está ou não na base de comissão dos pedidos, pré-faturas e notas fiscais |
| IrfCom | String(001) | Sim | Indicativo se o IRRF está ou não na base de comissão dos pedidos, pré-faturas e notas fiscais |
| CslCom | String(001) | Sim | Indicativo se a CSLL Retido está ou não na base de comissão dos pedidos, pré-faturas e notas fiscais |
| OurCom | String(001) | Sim | Indicativo se as outras retenções está ou não na base de comissão dos pedidos, pré-faturas e notas fiscais |
| PifCom | String(001) | Sim | Indicativo se o PIS Faturamento está ou não na base de comissão dos pedidos, pré-faturas e notas fiscais |
| CffCom | String(001) | Sim | Indicativo se o COFINS Faturamento está ou não na base de comissão dos pedidos, pré-faturas e notas fiscais |
| AvaVlr | Number(015,2) | Sim | Valor total para avalizar |
| AvaVlu | Number(015,2) | Sim | Valor avalizado no atual momento |
| AvaVls | Number(015,2) | Sim | Valor disponível para avalizar |
| AvaAti | String(001) | Sim | Determina se o representante pode ser usado como avalista |
| AvaMot | Number(006,0) | Sim | Código do motivo usado para justificar porque o avalista está inativo |
| AvaObs | String(250) | Sim | Observação do motivo da inativação do avalista |
| AvdAlt | Date | Sim | Data da última alteração das informações do avalista |
| AvhAlt | Number(005,0) | Sim | Hora da última alteração das informações do avalista |
| AvuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração das informações do avalista |
| AvdGer | Date | Sim | Data de geração das informações do avalista |
| AvhGer | Number(005,0) | Sim | Hora de geração das informações do avalista |
| AvuGer | Number(010,0) | Sim | Usuário responsável pela geração das informações do avalista |
| RepAud | String(001) | Sim | Indicativo se o representante pode realizar auditorias |
| ComAss | Number(005,2) | Sim | Percentual de comissão padrão para as ocorrências de assistência técnica |
| PerFix | Number(005,2) | Sim | Percentual de comissão pago ao representante na fixação |
| USU_RepSupImp | Number(009,0) | Sim | Código do representante superior de implementos do representante |
| USU_RepSupPec | Number(009,0) | Sim | Código do representante superior de peças do representante |

---

## Chave Primária

- CodRep
- CodEmp

---

## Índices

### E090HRPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodRve

---

## Relacionamentos

### IR_E090HRP_000

**Tabela:** E090REP

| Origem | Destino |
|--------|---------|
| CodRep | CodRep |

### IR_E090HRP_002

**Tabela:** E017RVE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRve | CodRve |

