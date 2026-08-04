# E140CTE

## Descrição

Vendas - Nota Fiscal de Saída - Dados do Conhecimento de Transporte

---

## Resumo

- Campos: 65
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| TipMod | String(003) | Sim | Informação do tipo do modal do CT-e a ser emitido |
| TipFmt | Number(001,0) | Sim | Informação do tipo de formato da impressão do CT-e |
| TipEmi | Number(001,0) | Sim | Informação da forma de emissão do CT-e |
| TipCte | Number(001,0) | Sim | Informação do tipo do CT-e |
| TipSer | Number(001,0) | Sim | Informação do tipo de serviço do CT-e |
| CodCl3 | Number(009,0) | Sim | Código do cliente (Expedidor) |
| CodCl4 | Number(009,0) | Sim | Código do cliente (Recebedor) |
| IndRet | String(001) | Sim | Informação do indicativo se o recebedor retira a mercadoria |
| DetRet | String(299) | Sim | Informação de detalhamento se o recebedor retira a mercadoria |
| DatCtg | Date | Sim | Informação da data da entrada em contingência |
| HorCtg | Number(005,0) | Sim | Informação da hora da entrada em contingência |
| JusCtg | String(499) | Sim | Informação da justificativa da entrada em contingência |
| InfCtr | String(050) | Sim | Informação da característica adicional do transporte |
| InfCse | String(090) | Sim | Informação da característica adicional do serviço |
| OriMun | String(100) | Sim | Informação do nome do município de origem para efeito de cálculo do frete |
| DstMun | String(100) | Sim | Informação do nome do município de destino para efeito de cálculo do frete |
| VlrOup | Number(015,2) | Sim | Informação do valor do crédito outorgado/presumido |
| VlrTri | Number(015,2) | Sim | Informação do valor total de tributos |
| InfOca | String(090) | Sim | Informação de outras características da carga |
| IndLot | String(001) | Sim | Informação se o CT-e é lotação |
| NumCio | String(030) | Sim | Informação do código identificador da operação de transporte (CIOT) |
| NumMin | String(020) | Sim | Número da minuta |
| NumOca | String(020) | Sim | Número operacional do Conhecimento Aéreo |
| TipTar | String(001) | Sim | Informação da classe da tarifa no modal aéreo |
| CodTar | String(010) | Sim | Informação do código da tarifa no modal aéreo |
| VlrTar | Number(015,2) | Sim | Informação do valor da tarifa no modal aéreo |
| DimCar | String(030) | Sim | Informação pertinente as dimensões da carga |
| CodImp | String(010) | Sim | Informação do código Interline Message Procedure (IMP) |
| CodRot | String(030) | Sim | Código da rota de entrega |
| CodOri | String(060) | Sim | Código interno da filial/porto/estação/aeroporto de origem |
| CodDst | String(060) | Sim | Código interno da filial/porto/estação/aeroporto de destino |
| TipDat | Number(001,0) | Sim | Tipo de data/período programado para a entrega |
| DatIpr | Date | Sim | Data prevista para o inicio da entrega |
| DatFpr | Date | Sim | Data prevista para o fim da entrega |
| TipHor | Number(001,0) | Sim | Tipo de horário programado para a entrega |
| HorIpr | Number(005,0) | Sim | Horário previsto para o inicio da entrega |
| HorFpr | Number(005,0) | Sim | Horário previsto para o final da entrega |
| SnfCto | String(003) | Sim | Série fiscal do CT-e original anulado/substituído |
| NumCto | Number(009,0) | Sim | Número do CT-e original anulado/substituído |
| DatDec | Date | Sim | Data de emissão da declaração de anulação |
| SnfCta | String(003) | Sim | Série fiscal do CT-e de anulação |
| NumCta | Number(009,0) | Sim | Número do CT-e de anulação |
| SnfAnu | String(003) | Sim | Série fiscal do documento de anulação gerado pelo tomador do serviço |
| NumAnu | Number(009,0) | Sim | Número do documento fiscal de anulação gerado pelo tomador do serviço |
| TipDan | Number(001,0) | Sim | Tipo do documento de anulação emitido pelo tomador contribuinte |
| DanChv | String(050) | Sim | Chave do CT-e emitido pelo tomador contribuinte de ICMS |
| DanCli | String(001) | Não | Tipo do cliente do documento de anulação emitido pelo tomador contribuinte |
| DanCgc | Number(014,0) | Sim | Nro. do CNPJ/CPF do documento de anulação emitido pelo tomador contribuinte |
| DocIdeDan | String(014) | Sim | Nro. do CNPJ/CPF do documento de anulação emitido pelo tomador contribuinte |
| DanMod | String(002) | Sim | Modelo do documento fiscal de anulação emitido pelo tomador contribuinte |
| DanSel | String(003) | Sim | Código da Série Legal do documento de anulação emitido pelo tomador contribuinte |
| DanSsl | String(002) | Sim | Código da Subsérie do documento de anulação emitido pelo tomador contribuinte |
| DanNro | Number(006,0) | Sim | Número do documento fiscal de anulação emitido pelo tomador contribuinte |
| DanEmi | Date | Não | Data de emissão do documento de anulação emitido pelo tomador contribuinte |
| DanVlr | Number(015,2) | Sim | Valor do documento de anulação emitido pelo tomador contribuinte |
| IndNeg | Number(001,0) | Sim | Indicador negociável |
| VlrCav | Number(015,2) | Sim | Informação do valor da carga para efeito de averbação |
| DesSrv | String(030) | Sim | Descrição do serviço que está prestando para o CT-e OS. |
| QtdCar | Number(013,4) | Sim | Informação da quantidade da carga do CT-e OS |
| TipFre | Number(001,0) | Sim | Tipo de fretamento |
| CteGlo | String(001) | Sim | Indicativo se o CT-e é Globalizado |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140CTE_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140CTE_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

