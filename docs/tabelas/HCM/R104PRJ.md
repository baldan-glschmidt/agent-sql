# R104PRJ

## Descrição

JR - Ações

---

## Resumo

- Campos: 45
- Chave Primária: 2 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| NroPrc | String(025) | Sim | Número da Ação |
| CodSin | Number(004,0) | Sim | Código do sindicato da parte contrária |
| EmpARe | Number(004,0) | Sim | Empresa do advogado da parte contrária |
| TpACon | Number(001,0) | Sim | Tipo do advogado da parte contrária |
| AdvCon | Number(009,0) | Sim | Código do advogado da parte contrária |
| EmNAdv | Number(004,0) | Sim | Empresa do nosso advogado |
| TpNAdv | Number(001,0) | Sim | Tipo do nosso advogado |
| NosAdv | Number(009,0) | Sim | Código do nosso advogado |
| CodCom | Number(004,0) | Sim | Código da vara |
| IniPro | Date | Sim | Data Início da Ação |
| ValPro | Number(011,2) | Sim | Valor da Ação |
| ResSen | String(8001) | Sim | Resumo da Sentença |
| PrvPrc | String(8001) | Sim | Providências da Ação |
| ObsPrc | String(8001) | Sim | Observações da Ação |
| NomArq | String(250) | Sim | Arquivo |
| TerPro | Date | Sim | Data de término da ação |
| IndAut | String(001) | Sim | Identifica se a empresa é autor da ação |
| MotEnc | Number(003,0) | Sim | Código do motivo de encerramento |
| CodAss | Number(003,0) | Sim | Código do assunto da ação |
| CodTip | Number(003,0) | Sim | Código do tipo da ação |
| ChaExi | Number(003,0) | Sim | Percentual de chance de êxito na visão da empresa |
| CodFil | Number(006,0) | Sim | Código da Filial |
| NumPro | Number(011,0) | Sim | Número do processo para recolhimento do SEFIP |
| AnoPro | Number(004,0) | Sim | Ano do Processo |
| PerIni | Date | Sim | Período de início do direito |
| PerFim | Date | Sim | Período de fim de direito |
| QtdPar | Number(002,0) | Sim | Quantidade de parcelas para cumprimento da sentença |
| TipPer | Number(001,0) | Sim | Tipo de periodicidade(1-Dias, 2-Meses) |
| IntPer | Number(002,0) | Sim | Intervalo entre as parcelas(em meses ou dias) |
| IniPag | Date | Sim | Competência de início do pagamento |
| RitSum | String(001) | Sim | Identifica se a ação será julgada no Rito Sumaríssimo |
| ParINS | Number(001,0) | Sim | Parcelamento INSS |
| ConPre | String(001) | Sim | Identifica se a ação foi submetida à comissão de conciliação prévia. |
| EscAdv | Number(008,0) | Sim | Escritório Advocacia |
| InfRec | Number(001,0) | Sim | Informações do Recurso |
| TipDec | Number(002,0) | Sim | Suspensão da Exigibilidade |
| DatDes | Date | Sim | Data da Decisão |
| DepInt | String(001) | Sim | Depósito do Montante Integral |
| AutPro | Number(001,0) | Sim | Autoria |
| MatPro | Number(002,0) | Sim | Indicativo de matéria do processo ou alvará judicial |
| BasDes | Number(001,0) | Sim | Informar se o processo deve ser enviado ao eSocial por esta Empresa |
| CodPro | Number(009,0) | Sim | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| RepPro | Number(001,0) | Sim | Repercussão do processo trabalhista ou de demanda submetida à CCP ou ao NINTER |

---

## Chave Primária

- NumEmp
- CodPrc

---

## Índices

### R104PRJIndice2

**Tipo:** Não unico

Campos:
- NroPrc

### R104PRJIndice3

**Tipo:** Não unico

Campos:
- EmpARe
- TpACon
- AdvCon

### R104PRJIndice4

**Tipo:** Não unico

Campos:
- EmNAdv
- TpNAdv
- NosAdv

---

## Relacionamentos

### IR_R104PRJ_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

