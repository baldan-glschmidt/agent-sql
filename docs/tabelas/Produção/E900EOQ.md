# E900EOQ

## Descrição

O.P./O.S. - Movimentação OP/OS

---

## Resumo

- Campos: 65
- Chave Primária: 5 campo(s)
- Índices: 3
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da OP/OS |
| CodEtg | Number(004,0) | Não | Código do estágio de produção |
| SeqEoq | Number(005,0) | Não | Sequência da movimentação da produção |
| NumGop | Number(004,0) | Sim | Número da guia associada a quantidade informada |
| CodPro | String(014) | Não | Código do Produto/Serviço |
| CodDer | String(007) | Não | Código da derivação |
| SeqRot | Number(004,0) | Sim | Sequência lógica da Operação no Roteiro de Produção |
| CodOpr | String(006) | Sim | Código da operação |
| CodCel | String(004) | Sim | Célula de Produção |
| TurTrb | Number(001,0) | Sim | Turno de Trabalho |
| CodLot | String(050) | Sim | Código Lote de Produção |
| QtdRe1 | Number(014,5) | Sim | Quantidade real de 1ª qualidade no Estágio |
| QtdRe2 | Number(014,5) | Sim | Quantidade real de 2ª qualidade no Estágio |
| QtdRe3 | Number(014,5) | Sim | Quantidade real de 3ª qualidade no Estágio |
| QtdRfg | Number(014,5) | Sim | Quantidade de Refugo |
| QtdIql | Number(014,5) | Sim | Quantidade Retirada p/ Inspeção de Qualidade |
| DatRea | Date | Não | Data da efetivação (data fim do processo de fabricação) |
| HorRea | Number(005,0) | Sim | Hora da efetivação (hora fim do processo de fabricação) |
| NumCad | Number(009,0) | Sim | Número do Cadastro do Operador |
| QtdHrr | Number(011,2) | Sim | Tempo líquido gasto no movimento (em minutos) |
| CodUsu | Number(010,0) | Sim | Código do Usuário  que deu a entrada no Estoque (Último Estágio) |
| DatIni | Date | Sim | Data Inicial do Processo de fabricação |
| HorIni | Number(005,0) | Sim | Hora Inicial do Processo de fabricação |
| FimOrp | String(001) | Sim | Indicador de fim da Ordem de Produção/Serviço (última Operação/Estágio) c/ entrada no Estoque |
| NumSep | String(050) | Sim | Série do Produto fabricado nesta OP |
| CodDep | String(010) | Sim | Código do depósito |
| CodCcu | String(009) | Sim | Código do centro de custos |
| CodTns | String(005) | Sim | Código da transação |
| CodCre | String(008) | Sim | Código do Centro de Recurso da movimentação |
| CodAc1 | String(008) | Sim | Código do acessório utilizado na operação |
| CodAc2 | String(008) | Sim | Código do acessório utilizado na operação |
| CodAc3 | String(008) | Sim | Código do acessório utilizado na operação |
| CodCte | String(003) | Sim | Código da característica de produto associada ao movimento |
| SeqCcp | Number(004,0) | Sim | Sequência do componente da característica de produto p/ o movimento |
| IdeBem | String(020) | Sim | Código do equipamento utilizado para coletagem de dados |
| TipObs | String(001) | Não | Tipo da Observação |
| ObsEoq | String(240) | Sim | Observações complementares (sobre o Movimento/Ação corretiva/Inspeção) |
| NumEpi | Number(009,0) | Sim | Identificador da inspeção aberta para a liberação do item |
| IndRtm | Number(001,0) | Sim | [Deprecado na 5.7.5.1] Indicativo se recalcula tempo do movimento da OP/OS |
| CodRef | String(030) | Sim | Código da Referência para Controles Diversos |
| QtdTr1 | Number(014,5) | Sim | Quantidade transferida de 1ª qualidade no Movimento |
| VlrDm1 | Number(014,5) | Sim | Valor Dimensão 1 |
| VlrDm2 | Number(014,5) | Sim | Valor Dimensão 2 |
| VlrDm3 | Number(014,5) | Sim | Valor Dimensão 3 |
| VlrDm4 | Number(014,5) | Sim | Valor Dimensão 4 |
| VlrDm5 | Number(014,5) | Sim | Valor Dimensão 5 |
| VlrDm6 | Number(014,5) | Sim | Valor Dimensão 6 |
| CnvTmp | String(001) | Sim | Tipo de conversão de tempo |
| BasCal | Number(008,5) | Sim | Quantidade base para cálculo do tempo do movimento da O.P./O.S. |
| BasCa2 | Number(008,5) | Sim | Quantidade base para cálculo do tempo do movimento da O.P./O.S. 2. |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| FilNfc | Number(005,0) | Sim | Filial da Nota Fiscal de Entrada |
| CodNfc | String(003) | Sim | Código da Série da Nota Fiscal de Entrada |
| NumNfc | Number(009,0) | Sim | Número da Nota Fiscal de Retorno de Serviços para Terceiros |
| SeqSet | Number(004,0) | Sim | Sequência da Remessa |
| EoqFrt | String(001) | Sim | Indicativo se o movimento possui ferramentas ligadas |
| UsuRev | Number(009,0) | Sim | Usuário responsável por revisar a quantidade do movimento da OP |
| CodEqp | String(020) | Sim | Código do equipamento utilizado para o movimento |
| TmpBru | Number(011,2) | Sim | Tempo bruto gasto no movimento (em minutos) |
| IndPsz | Number(006,3) | Sim | Proporção da quantidade apontada em relação ao apontado na OP de sumarização |
| IdeApt | Number(009,0) | Sim | Identificador único do apontamento |
| USU_SeqIpc | Number(003,0) | Sim | Sequência do item na nota fiscal de entrada |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqEoq

---

## Índices

### E900EOQIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- NumCad
- DatRea
- DatIni

### E900EOQIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqEoq
- SeqRot

### E900EOQIndLigacaoMov

**Tipo:** Não unico

Campos:
- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqRot
- NumGop
- NumCad
- CodPro
- CodDer
- DatRea
- SeqEoq

---

## Relacionamentos

### IR_E900EOQ_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900EOQ_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

### IR_E900EOQ_007

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

