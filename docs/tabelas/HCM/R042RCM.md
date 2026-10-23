# R042RCM

## Descrição

Rescisão - Mestre

---

## Resumo

- Campos: 81
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| DatDem | Date | Sim | Data da Demissão |
| CauDem | Number(002,0) | Sim | Causa da Demissão |
| CodRmd | Number(003,0) | Sim | Código do Motivo da Demissão |
| DatAvi | Date | Sim | Data do Aviso Prévio |
| FinAvi | Date | Sim | Data Final do Aviso |
| DatPag | Date | Sim | Data Pagto da Rescisão |
| FimCtt | Date | Sim | Data Fim Contrato Trabalho |
| IndRem | Number(001,0) | Sim | Indicativo de situação de remuneração após o desligamento/término |
| FimQua | Date | Sim | Data fim remuneração após o desligamento/término |
| QtdInd | Number(005,2) | Sim | Dias Aviso Indenizado |
| QtdRea | Number(005,2) | Sim | Dias Aviso Reavido |
| QtdSsl | Number(003,0) | Sim | Dias de Saldo de Salários |
| QtdGra | Number(003,0) | Sim | Dias de Gratificação |
| QtdEst | Number(004,0) | Sim | Dias de Estabilidade |
| DiMuQp | Number(003,0) | Sim | Dias Multa Qualificação Profissional |
| PerInd | Number(005,2) | Sim | Percentual de Indenização |
| QtdFca | Number(004,0) | Sim | Dias Fim Contrato Antecipado |
| DatCtb | Date | Sim | Data Contabilização |
| SalFav | Number(013,4) | Sim | Salário do Final do Aviso |
| SldFgt | Number(011,2) | Sim | Saldo Anterior do FGTS |
| FgtAnt | Number(001,0) | Sim | Fgts Mês Anterior |
| CodSaq | String(003) | Sim | Código do Saque |
| ComRes | String(050) | Sim | Comentário da Rescisão |
| BinSld | Number(011,2) | Sim | Base INSS Saldos |
| Bin13s | Number(011,2) | Sim | Base INSS 13° Salário |
| BirSld | Number(011,2) | Sim | Base IR Saldos |
| AirSld | Number(011,2) | Sim | Abatimentos IR Saldos |
| Bir13s | Number(011,2) | Sim | Base IR 13° Salário |
| Air13s | Number(011,2) | Sim | Abatimentos IR 13° Salário |
| BirFer | Number(011,2) | Sim | Base IR Férias |
| AirFer | Number(011,2) | Sim | Abatimentos IR Férias |
| BirPar | Number(011,2) | Sim | Base IR Partic.Lucros |
| BasFgt | Number(011,2) | Sim | Base do FGTS |
| AbaFgt | Number(011,2) | Sim | Abatimentos do FGTS |
| BasFgd | Number(011,2) | Sim | Base FGTS 13° Salário |
| AbaFgd | Number(011,2) | Sim | Abatimentos FGTS 13° Salário |
| TotPro | Number(011,2) | Sim | Total de Proventos |
| TotDes | Number(011,2) | Sim | Total de Descontos |
| IntRcs | Number(001,0) | Sim | Código Cálculo Integração Rescisão |
| QtdDsr | Number(003,0) | Sim | Dias Descanso Indenizado |
| TotVan | Number(011,2) | Sim | Total de Vantagens |
| MaiRem | Number(013,4) | Sim | Guarda a Maior Remuneração |
| RepVag | String(001) | Sim | Reposição de Vaga |
| PenFGT | String(001) | Sim | Indica se existe pensão alimentícia sobre o saldo de FGTS |
| VlrPen | Number(011,2) | Sim | Valor Pensão FGTS |
| SalBas | Number(013,4) | Sim | Salário Base |
| AviPre | Number(001,0) | Sim | Aviso Prévio |
| BinTot | Number(011,2) | Sim | Base INSS Não Limitado ao Teto |
| Bin13t | Number(011,2) | Sim | Base INSS 13° Salário Não Limitado ao Teto |
| StaPrg | String(001) | Sim | Indica se a programação está ou não efetivada |
| BipSld | Number(011,2) | Sim | Base IPE Saldos |
| Bip13s | Number(011,2) | Sim | Base IPE 13° Salário |
| JorSem | Number(001,0) | Sim | Cumpriu Jornada Semana |
| SabCom | Number(001,0) | Sim | Sábado Compensado Semana Rescisão |
| BipTot | Number(011,2) | Sim | Base de IPE não Limitado ao Teto |
| Bip13t | Number(011,2) | Sim | Base de IPE 13° não Limitado ao Teto |
| QtdIAc | Number(005,2) | Sim | Dias Aviso Indenizado/Acréscimo |
| QtdRAc | Number(005,2) | Sim | Dias Aviso Reavido/Acréscimo |
| VlrERA | Number(011,2) | Sim | Estouro Rescisão Anterior |
| TerQui | Number(001,0) | Sim | Termo de Quitação do TRCT |
| AteObi | String(032) | Sim | Atestado Óbito |
| ProTra | String(020) | Sim | Processo Trabalhista |
| BFgtAn | Number(011,2) | Sim | Base FGTS - Mês Anterior |
| BFgDAn | Number(011,2) | Sim | Base FGTS 13º Salário - Mês Anterior |
| BaIFgt | Number(011,2) | Sim | Base do FGTS Indenizado (cálculo antigo) |
| BaIFgd | Number(011,2) | Sim | Base do FGTS 13º Salário Indenizado (cálculo antigo) |
| ValIns | Number(011,2) | Sim | Valor INSS Rescisão |
| ApoEsp | Number(002,0) | Sim | Número Anos p/ Aposentadoria Especial |
| EmpCon | String(001) | Sim | Empréstimo Consignado Garantia FGTS (Obsoleto) |
| MatCon | String(005) | Sim | Matrícula Instituição Consignatária (Obsoleto) |
| NroCon | Number(015,0) | Sim | Número Contrato Empréstimo Consignado (Obsoleto) |
| PagCLT | Date | Sim | Data Pagamento CLT |
| ObsDes | String(255) | Sim | Observação Sobre o Desligamento do Trabalhador |
| BaApFg | Number(011,2) | Sim | Base do FGTS Indenizado |
| AfgInd | Number(011,2) | Sim | Abatimentos do FGTS Indenizado |
| BaApFd | Number(011,2) | Sim | Base do FGTS 13º Indenizado |
| AfgI13 | Number(011,2) | Sim | Abatimentos do FGTS 13º Indenizado |
| PagObt | Number(001,0) | Sim | Informar para quem foi efetuado o pagamento em casos de óbito do colaborador |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042RCM_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R042RCM_004

**Tabela:** R042CAU

| Origem | Destino |
|--------|---------|
| CauDem | CauDem |

