# E900EOP

## Descrição

OP/OS - Estágios de produção

---

## Resumo

- Campos: 37
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção da O.P./O.S. |
| SfxEtr | Number(004,0) | Sim | Opção do Estágio (1=Padrão, 2-999=Alternativo) |
| SitEop | String(001) | Não | Situação (E=Explodida, L=Liberada, S=Suspensa, F=Finalizada, A=Em Andamento, C=Cancelada, R=Reabilitada) |
| FilPro | Number(005,0) | Sim | Filial de Produção do Estágio |
| SitAnt | String(001) | Não | Situação anterior |
| DtpIni | Date | Não | Data limite inicial prevista p/ Estágio Produção (mais tardia p/ o início) |
| DtpFim | Date | Não | Data final prevista p/ Estágio Produção |
| DtrIni | Date | Sim | Data inicial real p/ Estágio Produção |
| DtrFim | Date | Sim | Data final real p/ Estágio Produção |
| DatIca | Date | Não | Data inicial calculada pelo escalonador p/ Estágio Produção |
| DatFca | Date | Não | Data final calculada pelo escalonador p/ Estágio Produção |
| QtdPrv | Number(014,5) | Não | Quantidade Prevista de produção p/ o Estágio |
| QtdRe1 | Number(014,5) | Sim | Quantidade real de 1ª qualidade no Estágio |
| QtdRe2 | Number(014,5) | Sim | Quantidade real de 2ª qualidade no Estágio |
| QtdRe3 | Number(014,5) | Sim | Quantidade real de 3ª qualidade no Estágio |
| QtdRfg | Number(014,5) | Sim | Quantidade realizada de Refugos |
| QtdIql | Number(014,5) | Sim | Quantidade retirada p/ Inspeção de Qualidade |
| TipPos | Number(001,0) | Não | Tipo Posicionamento (1=Inicia após fim do anterior, 2=inicia junto c/ anterior, 3=Finaliza junto) |
| TmpPrv | Number(009,3) | Sim | Tempo Previsto p/ produção no Estágio (em dias) |
| TmpFix | Number(008,2) | Sim | Quantidade de dias (p/ estabelecer o lead-time) gasto no Estágio  independente da quantidade a produzir |
| QtdHor | Number(011,2) | Sim | Quantidade de horas prevista p/ no Estágio |
| QtdHrr | Number(011,2) | Sim | Quantidade real de horas |
| HorIni | Number(005,0) | Sim | Hora de início real da O.P./O.S. no Estágio |
| HorFim | Number(005,0) | Sim | Hora de fim real da O.P./O.S. no Estágio |
| HorIpv | Number(005,0) | Sim | Hora de início prevista (informada manualmente) no Estágio de Produção |
| HorFpv | Number(005,0) | Sim | Hora de fim prevista (informada manualmente) no Estágio de Produção |
| HorIca | Number(005,0) | Sim | Hora de início calculada pelo escalonador no Estágio de Produção |
| HorFca | Number(005,0) | Sim | Hora de fim calculada pelo escalonador no Estágio de Produção |
| CodCel | String(004) | Sim | Código da Célula de Produção |
| NumPri | Number(004,0) | Sim | Número da Prioridade de execução da O.P./O.S. no estágio |
| ObsEop | String(240) | Sim | Observações complementares |
| NumEpi | Number(009,0) | Sim | Identificador da inspeção aberta para a liberação do item |
| QtdIcp | Number(014,5) | Sim | Quantidade de produto incorporada no estágio (inclusive anteriores) |
| IcpBxa | Number(014,5) | Sim | Quantidade incorporada no estágio já considerada para a baixa de componentes |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg

---

## Índices

### E900EOPIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodOri
- NumOrp
- CodEtg
- SitEop

---

## Relacionamentos

### IR_E900EOP_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900EOP_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

