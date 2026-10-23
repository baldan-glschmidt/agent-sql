# R304CPE

## Descrição

e-Sfinge Online - Concessão Pensão

---

## Resumo

- Campos: 29
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
| DatVig | Date | Sim | Data em que o ato passa a viger |
| DatObt | Date | Sim | Data de óbito |
| VlrPen | Number(015,2) | Sim | Valor total da pensão |
| DesLot | String(100) | Sim | Descrição da lotação |
| DesCar | String(200) | Sim | Descrição do cargo |
| GruCar | String(100) | Sim | Grupo nível referência do cargo |
| FunLeg | String(4000) | Sim | Fundamento legal |
| IndPro | String(001) | Sim | Indicativo processo judicial |
| TipPro | Number(003,0) | Sim | Tipo do processo judicial |
| NumPro | String(100) | Sim | Número do processo judicial |
| DesCom | String(250) | Sim | Descrição da comarca do processo judicial |
| IndAcu | String(001) | Sim | Indicativo acúmulo de cargo |
| TipAcu | Number(002,0) | Sim | Tipo de acumulação de cargo |
| IndPar | String(001) | Sim | Indicativo do parecer do controle interno |
| IndSva | String(001) | Sim | Indicativo servidor ativo |
| NumApo | String(100) | Sim | Número aposentadoria no TCE |
| DatCer | Date | Sim | Data da certidão de óbito |
| NumCer | String(050) | Sim | Número da certidão de óbito |
| EstCiv | Number(002,0) | Sim | Estado civil |
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

### R304CPEIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
