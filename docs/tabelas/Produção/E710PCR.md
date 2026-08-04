# E710PCR

## Descrição

Ficha - Roteiro - Seqüência Operações Exclusivas para fabricar Pedido/Item

---

## Resumo

- Campos: 38
- Chave Primária: 9 campo(s)
- Índices: 2
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial do pedido para uso exclusivo desse componente |
| NumPed | Number(008,0) | Não | Uso exclusivo para fabricação do pedido (componentes) |
| SeqIpd | Number(004,0) | Não | Componente para uso exclusivo para fabricação da seqüência de item do pedido |
| CodEtg | Number(004,0) | Não | Código do estágio de produção para execução da operação |
| SfxEtr | Number(003,0) | Não | Opção do estágio no roteiro do produto |
| SeqRot | Number(004,0) | Não | Seqüência lógica da operação no roteiro de produto |
| SfxSeq | Number(002,0) | Não | Opção da seqüência do roteiro do produto |
| SeqPcr | Number(004,0) | Não | Seqüência lógica que a operação é utilizada na fabricação do produto do pedido |
| CodRot | String(014) | Não | Código do roteiro de produção associado ao produto |
| CodOpr | String(006) | Não | Código da operação |
| UtiOpr | String(001) | Não | Tempo automático do cad. operações (tempo da operação vale p/ roteiros que utilizam tempo automático) |
| CplOpr | String(030) | Sim | Descrição complementar da operação referente ao roteiro |
| CodCre | String(008) | Sim | Código do centro de recurso onde a operação é executada |
| TmpPrp | Number(010,4) | Sim | Tempo proporcional utilizado p/ execução da operação (unidade de tempo do C. Recurso) |
| TmpFix | Number(010,4) | Sim | Tempo de preparação, espera - setup - (unidade de tempo C. Recurso) em função do lote técnico |
| TmpFrq | Number(012,3) | Sim | Tempo freqüencial em função da quantidade freqüencial |
| QtdFrq | Number(014,5) | Sim | Quantidade para dimensionar o tempo freqüencial |
| UniCre | String(001) | Não | Unidade de medida de tempo (M=Minuto, S=Segundo, D=Dia, H=Hora) |
| CodSer | String(014) | Sim | Código do serviço (quando operação é realizada por terceiros) |
| CodFor | Number(009,0) | Sim | Código fornecedor (quando operação é realizado por terceiros) |
| DatAlt | Date | Não | Data de geração/alteração da seqüência |
| CodCcu | String(009) | Sim | Código do centro de custos |
| CodUsu | Number(010,0) | Sim | Usuário que alterou |
| CodCel | String(004) | Sim | Código da célula de produção |
| TipPos | Number(001,0) | Não | Posicionamento (1=inicia após fim do anterior, 2=inicia junto, 3=finaliza junto) |
| PerSbr | Number(003,0) | Sim | Percentual de sobreposição da operação em relação a operação precedente (quando tipo posicionameto = 2) |
| MovOrp | String(001) | Sim | Indica se é controlado através de movimento (apontamento) por Ordens de Produção |
| MaxCre | Number(008,2) | Não | Quantidade máxima de recursos que podem ser alocados p/ fabricação de cada unidade do produto |
| PerEfi | Number(005,2) | Sim | Percentual de eficiência de produção na seqüência operação do roteiro |
| CapSmt | Number(014,5) | Sim | Capacidade produtiva simultânea (por unidade de produto) |
| LotTec | Number(010,3) | Sim | Lote técnico ideal, de fabricação a nível de operação |
| DtiVal | Date | Sim | Data de validade inicial p/ utilização desta operação (opcional) |
| DtfVal | Date | Sim | Data de validade final p/ utilização desta operação (opcional) |
| IndIae | String(001) | Não | Indicativo se o registro altera/inclui/exclui a seqüência do roteiro do produto |
| SelCus | String(001) | Não | Indica se o item será considerado para a área de custos (importação da ficha técnica) |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIpd
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq
- SeqPcr

---

## Índices

### E710PCRIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodRot
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq

### E710PCRIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodOpr
- UtiOpr

---

## Relacionamentos

### IR_E710PCR_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

### IR_E710PCR_003

**Tabela:** E120IPD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| SeqIpd | SeqIpd |

### IR_E710PCR_005

**Tabela:** E710ETR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |
| CodEtg | CodEtg |
| SfxEtr | SfxEtr |

### IR_E710PCR_010

**Tabela:** E720OPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOpr | CodOpr |

