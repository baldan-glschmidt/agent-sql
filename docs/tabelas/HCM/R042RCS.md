# R042RCS

## Descrição

Rescisão Complementar

---

## Resumo

- Campos: 55
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatPag | Date | Não | Data de Pagamento |
| FinAvi | Date | Sim | Data Final do Aviso |
| FimCtt | Date | Sim | Data Fim Contrato Trabalho |
| QtdInd | Number(005,2) | Sim | Dias Aviso Indenizado |
| QtdRea | Number(005,2) | Sim | Dias Aviso Reavido |
| QtdSsl | Number(003,0) | Sim | Dias Saldo de Salários |
| QtdGra | Number(003,0) | Sim | Dias Gratificação |
| QtdEst | Number(004,0) | Sim | Dias Estabilidade |
| PerInd | Number(005,2) | Sim | Percentual de Indenização |
| QtdFca | Number(004,0) | Sim | Dias Fim Contrato Antecipado |
| DatCtb | Date | Sim | Data Contabilização |
| SalFav | Number(013,4) | Sim | Salário do Final do Aviso |
| SldFgt | Number(011,2) | Sim | Saldo Anterior FGTS |
| BinSld | Number(011,2) | Sim | Base INSS Saldos |
| Bin13s | Number(011,2) | Sim | Base INSS 13° Salário |
| BirSld | Number(011,2) | Sim | Base IR Saldos |
| AirSld | Number(011,2) | Sim | Abatimentos IR Saldos |
| Bir13s | Number(011,2) | Sim | Base IR 13° Salário |
| Air13s | Number(011,2) | Sim | Abatimentos IR 13° Salário |
| BirFer | Number(011,2) | Sim | Base IR Férias |
| AirFer | Number(011,2) | Sim | Abatimentos IR Férias |
| BasFgt | Number(011,2) | Sim | Base FGTS |
| AbaFgt | Number(011,2) | Sim | Abatimentos FGTS |
| BasFgd | Number(011,2) | Sim | Base FGTS 13° Salário |
| AbaFgd | Number(011,2) | Sim | Abatimentos FGTS 13° Salário |
| TotPro | Number(011,2) | Sim | Total de Proventos |
| TotDes | Number(011,2) | Sim | Total de Descontos |
| IntRcs | Number(001,0) | Sim | Código Cálculo Integração Rescisão |
| TotVan | Number(011,2) | Sim | Total de Vantagens |
| MaiRem | Number(013,4) | Sim | Guarda a Maior Remuneração |
| BirPar | Number(011,2) | Sim | Base IR Partic.Lucros |
| DisCol | Date | Sim | Homologação Dissídio Coletivo |
| TemDis | String(001) | Sim | Motivo Complementar |
| SalBas | Number(013,4) | Sim | Salário Base |
| CalRcs | Number(005,0) | Sim | Integrar Rescisão |
| AviPre | Number(001,0) | Sim | Aviso Prévio |
| BinTot | Number(011,2) | Sim | Base INSS Não Limitado ao Teto |
| Bin13t | Number(011,2) | Sim | Base INSS 13° Salário Não Limitado ao Teto |
| BipSld | Number(011,2) | Sim | Base IPE Saldos |
| Bip13s | Number(011,2) | Sim | Base IPE 13° Salário |
| QtdIAc | Number(005,2) | Sim | Dias Aviso Indenizado/Acréscimo |
| QtdRAc | Number(005,2) | Sim | Dias Aviso Reavido/Acréscimo |
| VlrERA | Number(011,2) | Sim | Estouro Rescisão Anterior |
| TerQui | Number(001,0) | Sim | Termo de Quitação do TRCT |
| BaIFgt | Number(011,2) | Sim | Base do FGTS Indenizado (cálculo antigo) |
| BaIFgd | Number(011,2) | Sim | Base do FGTS 13º Salário Indenizado (cálculo antigo) |
| ValIns | Number(011,2) | Sim | Valor INSS Rescisão |
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
- DatPag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042RCS_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

