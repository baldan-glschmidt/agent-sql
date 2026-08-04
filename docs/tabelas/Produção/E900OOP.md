# E900OOP

## Descrição

OP/OS - Sequência Operacional

---

## Resumo

- Campos: 53
- Chave Primária: 7 campo(s)
- Índices: 2
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção para execução da Operação |
| SfxEtr | Number(003,0) | Não | Opção do Estágio (1=Padrão, 2-999=Alternativas) |
| SeqRot | Number(004,0) | Não | Sequência lógica da Operação no Roteiro de Produção |
| SfxSeq | Number(002,0) | Não | Opção da sequência (1=Padrão, 2-99=Alternativas) |
| CodOpr | String(006) | Não | Código da operação |
| UtiOpr | String(001) | Não | Tempo automático do cadastro operações (tempo da operação vale p/ roteiros que utilizam tempo automático) |
| CodCre | String(008) | Não | Código do Centro de Recurso onde a operação é executada |
| TmpPrp | Number(010,4) | Sim | Tempo Proporcional utilizado p/ execução da operação (Unidade de tempo do C. Recurso) |
| TmpFix | Number(013,4) | Sim | Tempo fixo do Set-Up na operação (Unidade de Tempo do C. Recurso) |
| TmpFrq | Number(012,3) | Sim | Tempo Freqüencial em função da Quantidade Freqüencial |
| UniCre | String(001) | Não | Unidade de Medida de Tempo (M=Minuto, S=Segundo, D=Dia, H=Hora) |
| TipCre | String(001) | Sim | Tipo de Centro de Recursos se Interno ou Externo (terceiros) |
| TmpTpr | Number(013,4) | Sim | Tempo total previsto para a sequência operacional (na UM do centro de recursos) |
| TmpCal | Number(013,4) | Sim | Tempo total previsto para a sequência operacional (em dias) |
| QtdFrq | Number(014,5) | Sim | Quantidade em função do tempo freqüencial |
| CodSer | String(014) | Sim | Código do serviço (Quando operação é realizada por Terceiros) |
| CodFor | Number(009,0) | Sim | Código Fornecedor (Quando operação é realizado por Terceiros) |
| QtdPrv | Number(014,5) | Sim | Quantidade Prevista por operação |
| QtdRe1 | Number(014,5) | Sim | Quantidade Realizada de 1ª Qualidade |
| QtdRe2 | Number(014,5) | Sim | Quantidade Realizada de 2ª Qualidade |
| QtdRe3 | Number(014,5) | Sim | Quantidade Realizada de 3ª Qualidade |
| QtdRfg | Number(014,5) | Sim | Quantidade realizada de Refugos |
| QtdIql | Number(014,5) | Sim | Quantidade Retirada p/ Inspeção Qualidade |
| DtrIni | Date | Sim | Data de início real da Operação na O.P./O.S. |
| DtrFim | Date | Sim | Data de fim real da Operação na O.P./O.S. |
| DtpIni | Date | Sim | Data inicial  prevista (informada manualmente) da Operação na O.P./O.S. |
| DtpFim | Date | Sim | Data final prevista (informada manualmente) da Operação na O.P./O.S. |
| DatIca | Date | Sim | Data inicial calculada pelo escalonador da Operação na O.P./O.S. |
| DatFca | Date | Sim | Data final calculada pelo escalonador da Operação na O.P./O.S. |
| HorIni | Number(005,0) | Sim | Hora de início real da Operação na O.P./O.S. |
| HorFim | Number(005,0) | Sim | Hora de fim real da Operação na O.P./O.S. |
| HorIpv | Number(005,0) | Sim | Hora de início prevista (informada manualmente) da Operação na O.P./O.S. |
| HorFpv | Number(005,0) | Sim | Hora de fim prevista (informada manualmente) da Operação na O.P./O.S. |
| HorIca | Number(005,0) | Sim | Hora de início calculada pelo escalonador da Operação na O.P./O.S. |
| HorFca | Number(005,0) | Sim | Hora de fim calculada pelo escalonador da Operação na O.P./O.S. |
| CodCel | String(004) | Sim | Código da Célula de Produção |
| ObsOop | String(1999) | Sim | Observações complementares |
| TipPos | Number(001,0) | Não | Tipo Posicionamento (1=Inicia após fim do anterior, 2=inicia junto, 3=finaliza junto) |
| NumPri | Number(004,0) | Sim | Número da Prioridade de execução da O.P./O.S. na operação |
| CreLoc | String(008) | Sim | Recurso Locado pelo escalonador da Operação na O.P./O.S. |
| SeqCre | Number(004,0) | Sim | Sequência do Recurso Locado pelo escalonador da Operação na O.P./O.S. |
| QtdPrc | Number(014,5) | Sim | Qtde Produto Processada na TheScheduller |
| IndFrt | String(001) | Sim | Indicativo que a operação utiliza ferramentas |
| MovOrp | String(001) | Sim | Indica se é controlado através de movimento (apontamento) por Ordens de Produção |
| IndIcp | String(001) | Sim | Indicativo se a operação permite a incorporação de produtos na OP |
| QtdIcp | Number(014,5) | Sim | Quantidade de produto incorporada na operação (inclusive anteriores) |
| IndSmz | String(001) | Sim | Indica se a operação é subordinada a uma OP de sumarização |
| USU_CodCcu | String(009) | Sim | Código do Centro de Custos |
| USU_DatPrd | Date | Sim | Data de Produção para sequenciamento de célula na operação |
| USU_CodMaq | String(020) | Sim | Código da Máquina Utilizada |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq

---

## Índices

### E900OOPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodOri
- NumOrp
- TipCre

### E900OOPIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqRot
- MovOrp

---

## Relacionamentos

### IR_E900OOP_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900OOP_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

### IR_E900OOP_007

**Tabela:** E720OPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOpr | CodOpr |

### IR_E900OOP_009

**Tabela:** E725CRE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCre | CodCre |

