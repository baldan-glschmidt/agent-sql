# R304CAP

## Descrição

e-Sfinge Online - Concessão Aposentadoria

---

## Resumo

- Campos: 41
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumAto | String(016) | Não | Número do ato de pessoal |
| DatAto | Date | Não | Data do ato de pessoal |
| NumMat | String(016) | Não | Número da matrícula do servidor na unidade |
| NumCpf | Number(011,0) | Não | Código de identificação do contribuinte na receita federal |
| CodUni | Number(016,0) | Não | Código da unidade gestora do servidor |
| SeqReg | Number(009,0) | Não | Sequência |
| PubAto | Date | Sim | Data de publicação do ato de pessoal |
| TipAto | Number(002,0) | Sim | Tipo do ato de pessoal |
| VigAto | Date | Sim | Data em que o ato passa a viger |
| DatIca | Date | Sim | Data de ingresso no cargo atual |
| DatIsp | Date | Sim | Data de ingresso no serviço público |
| ModApo | Number(008,0) | Sim | Modalidade |
| FunLeg | String(4000) | Sim | Fundamento legal |
| EstCiv | Number(002,0) | Sim | Estado civil |
| DesCar | String(200) | Sim | Descrição do cargo |
| DesLot | String(100) | Sim | Descrição da lotação |
| GruCar | String(100) | Sim | Grupo nível referência do cargo |
| CarHor | Number(016,0) | Sim | Quantidade da carga horária |
| DatIcr | Date | Sim | Data de ingresso na carreira |
| IndPar | String(001) | Sim | Indicativo do parecer do controle interno |
| FatPro | Number(015,2) | Sim | Fator de proporcionalidade |
| MedSal | Number(015,2) | Sim | Média do salário de contribuição |
| DesCan | String(200) | Sim | Descrição do cargo anterior |
| DatTrc | Date | Sim | Data de transformação do cargo |
| FunLtc | String(1000) | Sim | Fundamento legal da transformação do cargo |
| IndAcu | String(001) | Sim | Indicativo acúmulo de cargo |
| TipAcu | Number(002,0) | Sim | Tipo de acumulação de cargo |
| CarHac | Number(016,0) | Sim | Carga horária acumulação |
| IndPro | String(001) | Sim | Indicativo processo judicial |
| DesCom | String(250) | Sim | Descrição da comarca do processo judicial |
| NumPro | String(100) | Sim | Número do processo judicial |
| TipPro | Number(003,0) | Sim | Tipo do processo judicial |
| NumPad | String(016) | Sim | Número do processo administrativo |
| DatReq | Date | Sim | Data de requerimento da aposentadoria |
| IndInc | String(001) | Sim | Indicativo Incapacidade para o trabalho |
| DatLau | Date | Sim | Data do laudo de inspeção de saúde |
| NumCid | String(050) | Sim | Número do CID |
| TipCau | Number(003,0) | Sim | Tipo de causa da invalidez |
| DisLeg | String(4000) | Sim | Dispositivo legal da doença |
| PidSta | String(030) | Sim | Pid status |

---

## Chave Primária

- NumEmp
- NumAto
- DatAto
- NumMat
- NumCpf
- CodUni
- SeqReg

---

## Índices

### R304CAPIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
