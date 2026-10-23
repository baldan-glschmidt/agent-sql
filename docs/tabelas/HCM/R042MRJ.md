# R042MRJ

## Descrição

Indenizações - Mestre

---

## Resumo

- Campos: 62
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| DatMrj | Date | Não | Data da Troca |
| TipMrj | Number(001,0) | Sim | Tipo Indenização |
| CauDem | Number(002,0) | Sim | Causa da Demissão |
| CodRmd | Number(003,0) | Sim | Código do Motivo da Demissão |
| DatAvi | Date | Sim | Data do Aviso Prévio |
| FinAvi | Date | Sim | Data Final do Aviso |
| DatPag | Date | Sim | Data Pagto da Rescisão |
| FimCtt | Date | Sim | Data Fim Contrato Trabalho |
| QtdInd | Number(005,2) | Sim | Dias Aviso Indenizado |
| QtdRea | Number(005,2) | Sim | Dias Aviso Reavido |
| QtdSsl | Number(003,0) | Sim | Dias de Saldo de Salários |
| QtdGra | Number(003,0) | Sim | Dias de Gratificação |
| QtdEst | Number(003,0) | Sim | Dias de Estabilidade |
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
| CodVin | Number(002,0) | Sim | Tipo de Vínculo |
| AviPre | Number(001,0) | Sim | Aviso Prévio |
| RepVag | String(001) | Sim | Reposição de Vaga |
| PenFGT | String(001) | Sim | Indica se existe pensão alimentícia sobre o saldo de FGTS |
| VlrPen | Number(011,2) | Sim | Valor Pensão FGTS |
| BinTot | Number(011,2) | Sim | Base INSS Não Limitado ao Teto |
| Bin13t | Number(011,2) | Sim | Base INSS 13° Salário Não Limitado ao Teto |
| StaPrg | String(001) | Sim | Indica se a programação está ou não efetivada |
| BipSld | Number(011,2) | Sim | Base IPE Saldos |
| Bip13s | Number(011,2) | Sim | Base IPE 13° Salário |
| JorSem | Number(001,0) | Sim | Cumpriu Jornada Semana |
| SabCom | Number(001,0) | Sim | Sábado Compensado Semana |
| BipTot | Number(011,2) | Sim | Base de IPE não Limitado ao Teto |
| Bip13t | Number(011,2) | Sim | Base de IPE 13° não Limitado ao Teto |
| QtdIAc | Number(005,2) | Sim | Dias Aviso Indenizado/Acréscimo |
| QtdRAc | Number(005,2) | Sim | Dias Aviso Reavido/Acréscimo |
| VlrERA | Number(011,2) | Sim | Estouro Rescisão Anterior |
| TerQui | Number(001,0) | Sim | Termo de Quitação do TRCT |
| BaApFg | Number(011,2) | Sim | Base do FGTS Indenizado |
| AfgInd | Number(011,2) | Sim | Abatimentos do FGTS Indenizado |
| BaApFd | Number(011,2) | Sim | Base do FGTS 13º Indenizado |
| AfgI13 | Number(011,2) | Sim | Abatimentos do FGTS 13º Indenizado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatMrj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042MRJ_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R042MRJ_005

**Tabela:** R042CAU

| Origem | Destino |
|--------|---------|
| CauDem | CauDem |

