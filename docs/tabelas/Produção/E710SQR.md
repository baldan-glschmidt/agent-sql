# E710SQR

## Descrição

Ficha - Roteiro - Seqüência Operacional

---

## Resumo

- Campos: 55
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodRot | String(014) | Não | Código do roteiro de produção associado ao produto |
| CodEtg | Number(004,0) | Não | Código do estágio de produção para execução da operação |
| SfxEtr | Number(003,0) | Não | Opção do estágio (1=Padrão, 2-999=Alternativas) |
| SeqRot | Number(004,0) | Não | Seqüência lógica da operação no roteiro de produção |
| SfxSeq | Number(002,0) | Não | Opção da seqüência (1=Padrão, 2-99=Alternativas) |
| CodOpr | String(006) | Não | Código da operação |
| UtiOpr | String(001) | Não | Tempo automático do cad. operações (tempo da operação vale p/ roteiros que utilizam tempo automático) |
| CplOpr | String(030) | Sim | Descrição complementar  da operação referente ao roteiro |
| CodCre | String(008) | Sim | Código do centro de recurso onde a operação é executada |
| OprCal | String(001) | Sim | Indica se os tempos da seqüência do roteiro são calculados ou digitados |
| TmpPrp | Number(010,4) | Sim | Tempo proporcional utilizado p/ execução da operação (unidade de tempo do C. Recurso) |
| TmpFix | Number(010,4) | Sim | Tempo de preparação, espera - setup - (Unidade de tempo C. Recurso) em função do lote técnico |
| TmpFrq | Number(012,3) | Sim | Tempo freqüencial em função da quantidade freqüencial |
| QtdFrq | Number(014,5) | Sim | Quantidade para dimensionar o tempo freqüencial |
| UniCre | String(001) | Não | Unidade de medida de tempo (M=Minuto, S=Segundo, D=Dia, H=Hora) |
| CodSer | String(014) | Sim | Código do serviço (Quando operação é realizada por Terceiros) |
| CodFor | Number(009,0) | Sim | Código fornecedor (Quando operação é realizado por Terceiros) |
| DatAlt | Date | Não | Data de geração/alteração da seqüência |
| CodCcu | String(009) | Sim | Código do Centro de Custos |
| CodUsu | Number(010,0) | Sim | Usuário que alterou |
| CodCel | String(004) | Sim | Código da Célula de Produção |
| TipPos | Number(001,0) | Não | Tipo Posicionamento (1=Inicia após fim do anterior, 2=inicia junto, 3=finaliza junto) |
| PerSbr | Number(003,0) | Sim | Percentual de sobreposição da operação em relação a operação precedente (quando tipo posicionamento = 2) |
| MovOrp | String(001) | Sim | Indica se é controlado através de movimento (apontamento) por Ordens de Produção |
| MaxCre | Number(008,2) | Não | Quantidade máxima de recursos que podem ser alocados p/ fabricação de cada unidade do produto |
| PerEfi | Number(005,2) | Sim | Percentual eficiência de produção na seqüência operação do roteiro |
| CapSmt | Number(014,5) | Sim | Capacidade produtiva simultânea (por unidade de produto) |
| LotTec | Number(010,3) | Sim | Lote Técnico ideal, de fabricação a nível de Operação |
| DtiVal | Date | Sim | Data de Validade inicial p/ utilização desta Operação (Opcional) |
| DtfVal | Date | Sim | Data de Validade final p/ utilização desta Operação (Opcional) |
| SelCus | String(001) | Não | Indica se o item será considerado para a área de custos (importação da ficha técnica). |
| QtdGop | Number(012,5) | Sim | Quantidade máxima para cada guia de produção da seqüência do roteiro do Estágio |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| QtdCre | Number(008,2) | Sim | Quantidade de recursos (máquinas/pessoas) que serão efetivamente utilizados |
| NecLig | String(001) | Sim | Seq. operacional será ligada ao Produto específico que o utiliza |
| IndIcp | String(001) | Sim | Indicativo se a sequência do roteiro permite a incorporação de produtos na OP |
| USU_numopr | Number(005,0) | Sim | Defasagem de Demanda( 0=D0, 1=D1, 2=D2, 3=D3...) |
| USU_IndAvu | String(001) | Sim | Indicativo se e avulso |
| USU_CodEqp | String(020) | Sim | Código do Equipamento |
| USU_TmpPcs | Number(010,4) | Sim | Tempo de preparação entre as peças do mesmo grupo |
| USU_codcel | Number(004,0) | Sim | Código Célula para Sequeciamento Produção |
| USU_GruCelPrd | String(020) | Sim | Grupo de Célula de Produção para sequenciamento produção |
| USU_SeqCelPrd | Number(007,0) | Sim | Sequência de célula de produção |
| USU_CelAlt | Number(004,0) | Sim | Código célula alternativa |
| USU_GruCelAlt | String(020) | Sim | Grupo de Célula de Produção Alternativo |
| USU_SeqCelAlt | Number(007,0) | Sim | Sequência de célula de produção Alternativa |
| USU_CodSup | String(250) | Sim | Codigo Suporte |
| USU_CodIns | String(250) | Sim | Codigo Inserto |
| USU_CodAgl | String(005) | Sim | Agrupamento para Logística |
| USU_TmpPas | Number(003,0) | Sim | Tempo de Passagem entre Processo atual e o sucessor |
| USU_InsMed | String(070) | Sim | Instrumento de Medição |
| USU_CorImp | Number(002,0) | Sim | Cor do Implemento |
| USU_GruMaq | String(005) | Sim | Grupo de Máquina |

---

## Chave Primária

- CodEmp
- CodRot
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq

---

## Índices

### E710SQRIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodOpr
- UtiOpr

---

## Relacionamentos

### IR_E710SQR_003

**Tabela:** E710ETR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |
| CodEtg | CodEtg |
| SfxEtr | SfxEtr |

### IR_E710SQR_006

**Tabela:** E720OPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOpr | CodOpr |

