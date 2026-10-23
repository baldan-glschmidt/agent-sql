# R051REN

## Descrição

Rendimentos Informe/DIRF - Ficha Financeira

---

## Resumo

- Campos: 97
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRet | Number(004,0) | Não | Código de Retenção do IR |
| TipIrf | String(001) | Não | IR Normal ou Estrangeiro |
| CpfCgc | Number(015,0) | Não | Número do CPF/CNPJ |
| OriAnu | Number(001,0) | Não | Origem |
| CmpRen | Date | Não | Competência dos Rendimentos |
| BasIrf | Number(011,2) | Sim | Valor Base do IR |
| ConPre | Number(011,2) | Sim | Contribuição da Previdência |
| IpfNor | Number(011,2) | Sim | Valor do Ipmf |
| PenJud | Number(011,2) | Sim | Valor de Pensão Judicial |
| ValIrf | Number(011,2) | Sim | Valor do IR |
| ValDep | Number(011,2) | Sim | Valor de Dependentes |
| ValPis | Number(011,2) | Sim | Valor do PIS |
| AboVtr | Number(011,2) | Sim | Abono do Vtr |
| ValCpm | Number(011,2) | Sim | Valor do CPMF |
| BasFer | Number(011,2) | Sim | Base IR de Férias |
| IrfFer | Number(011,2) | Sim | Valor IR de Férias |
| DifFer | Number(011,2) | Sim | Diferença de Férias |
| Bas13s | Number(011,2) | Sim | Base de IR de 13° Salário |
| Irf13s | Number(011,2) | Sim | Valor do IR 13° Salário |
| Con13s | Number(011,2) | Sim | Contribuição Previdência 13° Salário |
| Pen13s | Number(011,2) | Sim | Pensão Judicial de 13° Salário |
| Dep13s | Number(011,2) | Sim | Valor Dependentes 13° Salário |
| DepLuc | Number(011,2) | Sim | Valor Dependentes Participação nos Lucros |
| DesMed | Number(011,2) | Sim | Valor de Despesas Médicas |
| SegVid | Number(011,2) | Sim | Valor do Seguro de Vida |
| SalFam | Number(011,2) | Sim | Valor do Salário Família |
| ApoRef | Number(011,2) | Sim | Valor de Aposentadoria Reforma |
| ApoIrf | Number(011,2) | Sim | Aposentadoria Reforma IR Normal |
| ApoFer | Number(011,2) | Sim | Aposentadoria Reforma Férias |
| Apo13s | Number(011,2) | Sim | Aposentadoria Reforma 13° Salário |
| ApoLuc | Number(011,2) | Sim | Aposentadoria Participação nos Lucros |
| ApoInv | Number(011,2) | Sim | Valor Aposentadoria Invalidez |
| DiaAju | Number(011,2) | Sim | Valor de Diárias / Ajuda de Custo |
| PrePri | Number(011,2) | Sim | Valor de Previdência Privada |
| Pri13s | Number(011,2) | Sim | Valor de Previdência Privada 13° Salário |
| AviPre | Number(011,2) | Sim | Valor do Aviso Prévio Indenizado |
| IndRcs | Number(011,2) | Sim | Valor de Indenizações de Rescisão |
| DisLuc | Number(011,2) | Sim | Valor de Distribuição de Lucros |
| RenTex | Number(011,2) | Sim | Valor dos Rendimentos de Tributação Exclusiva |
| LucArb | Number(011,2) | Sim | Valor do Lucro Arbitrado |
| IrfLre | Number(011,2) | Sim | IR Sobre o Lucro Real Distribuído |
| LucRea | Number(011,2) | Sim | Valor do Lucro Real Distribuído |
| RenIse | Number(011,2) | Sim | Valor de Rendimentos Isentos |
| ParLuc | Number(011,2) | Sim | Valor de Participação nos Lucros |
| IrfLuc | Number(011,2) | Sim | Valor de IR Sobre Participação nos Lucros |
| PenLuc | Number(011,2) | Sim | Valor de Pensão Judicial Participação nos Lucros |
| RenExt | Number(011,2) | Sim | Valor de Rendimentos Ausentes Exterior |
| Val13s | Number(011,2) | Sim | Valor 13° Salário |
| OriRen | String(001) | Sim | Origem dos Rendimentos |
| RedMes | Number(011,2) | Sim | Redutor de R$100,00 da Base de IR Mensal |
| RedFer | Number(011,2) | Sim | Redutor de R$100,00 da Base de IR de Férias |
| Red13s | Number(011,2) | Sim | Redutor de R$100,00 da Base de IR de 13° Salário |
| RedPar | Number(011,2) | Sim | Redutor de R$100,00 da Base de IR de Participação nos Lucros |
| ExBasI | Number(011,2) | Sim | Base Isenta IR - Exigibilidade Suspensa |
| ExDedI | Number(011,2) | Sim | Dedução Previdência Oficial IR Base - Exigibilidade Suspensa |
| ExDeDe | Number(011,2) | Sim | Dedução Dependente IR Base - Exigibilidade Suspensa |
| ExDePA | Number(011,2) | Sim | Dedução Pensão Alimentícia IR Base - Exigibilidade Suspensa |
| ExDePP | Number(011,2) | Sim | Dedução Previdência Privada IR Base - Exigibilidade Suspensa |
| ExDfTa | Number(011,2) | Sim | Diferença IR Outra Tabela - Exigibilidade Suspensa |
| ExDpJu | Number(011,2) | Sim | Depósito Judicial IR - Exigibilidade Suspensa |
| ExBa13 | Number(011,2) | Sim | Base Isenta IR 13° Salário - Exigibilidade Suspensa |
| ExDe13 | Number(011,2) | Sim | Dedução Previdência Oficial IR Base 13° Salário - Exigibilidade Suspensa |
| ExDD13 | Number(011,2) | Sim | Dedução Dependente IR Base 13° Salário - Exigibilidade Suspensa |
| ExPA13 | Number(011,2) | Sim | Dedução Pensão Alimentícia IR Base 13° Salário - Exigibilidade Suspensa |
| ExPP13 | Number(011,2) | Sim | Dedução Previdência Privada IR Base 13° Salário - Exigibilidade Suspensa |
| ExDf13 | Number(011,2) | Sim | Diferença IR 13° Salário Outra Tabela - Exigibilidade Suspensa |
| ExDp13 | Number(011,2) | Sim | Depósito Judicial IR 13° Salário - Exigibilidade Suspensa |
| AboPec | Number(011,2) | Sim | Valor do Abono Pecuniário de Férias |
| Api13s | Number(011,2) | Sim | 13° Indenizado Rescisão |
| IseFer | Number(011,2) | Sim | Rendimentos Isentos de Férias |
| BIDiRA | Number(011,2) | Sim | Valor Base do IR - Dissídio RRA |
| BIReRA | Number(011,2) | Sim | Valor Base do IR - Reclamatória RRA |
| BFDiRA | Number(011,2) | Sim | Base IR de Férias - Dissídio RRA |
| BFReRA | Number(011,2) | Sim | Base IR de Férias - Reclamatória RRA |
| B13DRA | Number(011,2) | Sim | Base de IR de 13° Salário - Dissídio RRA |
| B13RRA | Number(011,2) | Sim | Base de IR de 13° Salário - Reclamatória RRA |
| VIrfRA | Number(011,2) | Sim | Valor do IR - RRA |
| CPreRA | Number(011,2) | Sim | Contribuição da Previdência - RRA |
| PJudRA | Number(011,2) | Sim | Valor de Pensão Judicial - RRA |
| QMesRA | Number(004,1) | Sim | Quantidade de meses - RRA |
| IseRRA | Number(011,2) | Sim | Valor da Base Isenta RRA |
| AcaRRA | Number(011,2) | Sim | Valor da Despesa da Ação Judicial RRA |
| VolCop | Number(011,2) | Sim | Rendimentos Voluntário da Copa |
| MedRes | Number(011,2) | Sim | Bolsa de estudo recebida por Médico-Residente |
| BasAu1 | Number(011,2) | Sim | Uso Exclusivo da Senior |
| ValAu1 | Number(011,2) | Sim | Uso Exclusivo da Senior |
| BasAu2 | Number(011,2) | Sim | Uso Exclusivo da Senior |
| ValAu2 | Number(011,2) | Sim | Uso Exclusivo da Senior |
| TipAux | Number(005,0) | Sim | Uso Exclusivo da Senior |
| DedSim | Number(011,2) | Sim | Dedução simplificada mensal/férias |
| Ded13s | Number(011,2) | Sim | Dedução simplificada 13º salário |
| DeSiMs | Number(011,2) | Sim | Dedução simplificada mensal suspensa |
| DeSiDs | Number(011,2) | Sim | Dedução simplificada 13º salário suspensa |
| JurMor | Number(011,2) | Sim | Juros de mora |
| RiPrTr | Number(011,2) | Sim | Rendimentos isentos de processo trabalhista |

---

## Chave Primária

- NumEmp
- CodFil
- CodRet
- TipIrf
- CpfCgc
- OriAnu
- CmpRen

---

## Índices

### R051RENIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CpfCgc
- CmpRen
- OriAnu
- OriRen

---

## Relacionamentos

### IR_R051REN_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R051REN_005

**Tabela:** R051BEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodRet | CodRet |
| TipIrf | TipIrf |
| CpfCgc | CpfCgc |
| OriAnu | OriAnu |

