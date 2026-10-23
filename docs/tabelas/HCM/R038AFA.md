# R038AFA

## Descrição

Afastamentos

---

## Resumo

- Campos: 66
- Chave Primária: 5 campo(s)
- Índices: 5
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAfa | Date | Não | Data do Afastamento |
| HorAfa | Number(005,0) | Não | Hora do Afastamento |
| DatTer | Date | Sim | Data do Término do Afastamento |
| HorTer | Number(005,0) | Sim | Hora do Término do Afastamento |
| PrvTer | Date | Sim | Data Término Previsto |
| SitAfa | Number(003,0) | Sim | Situação de Afastamento |
| CauDem | Number(002,0) | Sim | Causa Demissão do Colaborador |
| DiaJus | Number(002,0) | Sim | Dias Justificados |
| IndRem | Number(001,0) | Sim | Indicativo de situação de remuneração após o desligamento/término |
| FimQua | Date | Sim | Data fim remuneração após o desligamento/término |
| QhrAfa | Number(005,0) | Sim | Qtde de Horas Faltas no Afastamento |
| OriAfa | Number(001,0) | Sim | 0=Afast, 1=Perda Férias, 2=Medicina, 3=Aut. Saída, 4=Treinamento, 5=Troca Filial, 6=Benefício - Entes Públicos |
| ExmRet | String(001) | Sim | Exame de Retorno |
| ConTov | String(001) | Sim | Considerar Demissão p/ Cálculo do Turn-Over |
| ObsAfa | String(255) | Sim | Observação do Afastamento |
| StaAtu | Number(001,0) | Sim | Status do Histórico |
| MotRai | Number(002,0) | Sim | Motivo do Afastamento para a Rais |
| NroAut | String(015) | Sim | Número de Autorização |
| CodOem | Number(008,0) | Sim | Adm. Seguridade |
| CodSub | String(003) | Sim | Identificação do subgrupo da CID-10 |
| DatPer | Date | Sim | Data da Decisão da Perícia do Nexo Epidemiológico |
| SitIni | Number(003,0) | Sim | Situação Inicial do Afastamento |
| RisNex | String(001) | Sim | Indica se há risco do afastamento ser convertido em acidente de trabalho (Nexo Epidemiológico) |
| DatNex | Date | Sim | Data de Início do Nexo Epidemiológico |
| DiaPrv | Number(004,0) | Sim | Dias Previsto Término |
| CodCua | Number(009,0) | Sim | Código do Curso que Originou o Afastamento |
| TmaCua | Number(006,0) | Sim | Código da Turma que Originou o Afastamento |
| DatPar | Date | Sim | Data do Parto |
| DiaBlq | Number(001,0) | Sim | Número de dias que o crachá será bloqueado |
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |
| HrTRcs | Number(005,0) | Sim | Hora do Término do Afastamento Antes da Rescisão |
| CodDoe | String(004) | Sim | Classificação Internacional de Doenças |
| CodCid | String(010) | Sim | Código da Classificação Internacional de Doenças |
| CodAte | Number(006,0) | Sim | Código do Atendente |
| AciTra | Number(001,0) | Sim | Tipo de Acidente de Trânsito |
| EfeRet | String(001) | Sim | Indica se a alteração de motivo tem efeito retroativo |
| EncAfa | Number(001,0) | Sim | Forma de encerramento do afastamento |
| TipSuc | Number(001,0) | Sim | Tipo de inscrição da empresa sucessora |
| CgcSuc | Number(015,0) | Sim | Número de inscrição da empresa sucessora |
| CFJSUC | String(014) | Sim | Número de inscrição da empresa sucessora |
| DatAlt | Date | Sim | Data de alteração da situação do afastamento |
| SitOri | Number(003,0) | Sim | Situação original do afastamento |
| MotAlt | String(001) | Sim | Indica se o afastamento atual é uma alteração de situação não retroativa |
| NomAte | String(070) | Sim | Nome do Atendente |
| OrgCla | Number(001,0) | Sim | Órgão de Classe |
| RegCon | String(014) | Sim | Registro no Conselho Profissional |
| EstCon | String(002) | Sim | UF do Conselho Profissional |
| CgcCes | Number(015,0) | Sim | CNPJ da entidade para o qual o colaborador foi cedido |
| CFJCES | String(014) | Sim | CNPJ da entidade para o qual o colaborador foi cedido |
| OnuCes | Number(001,0) | Sim | Tipo de ônus para o colaborador cedido |
| CgcSin | Number(015,0) | Sim | CNPJ do sindicato que o colaborador exercerá o mandato |
| CFJSIN | String(014) | Sim | CNPJ do sindicato que o colaborador exercerá o mandato |
| OnuSin | Number(001,0) | Sim | Tipo de ônus para o colaborador com mandato sindical |
| AciAnt | String(001) | Sim | Indica se este afastamento é decorrente de outro acidente de trabalho |
| OriMot | Number(001,0) | Sim | Origem do Motivo da Alteração |
| NumPro | Number(009,0) | Sim | Processo Judicial/Benefício referente ao motivo da alteração |
| MsmMot | String(001) | Sim | Afastamento decorre de mesmo motivo de afastamento anterior dentro de 60 dias |
| CmpAu1 | Number(001,0) | Sim | Campo Auxiliar 1 |
| ManCgc | Number(015,0) | Sim | CNPJ do órgão no qual o trabalhador exercerá o mandato eletivo |
| CFJMDT | String(014) | Sim | CNPJ do órgão no qual o trabalhador exercerá o mandato eletivo |
| ManRem | String(001) | Sim | Indicar se o servidor optou pela remuneração do cargo efetivo |
| AtePat | String(001) | Sim | Atestado Sem Incidência INSS |
| USU_DiaAfa | Number(004,0) | Sim | Dias Afastados |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAfa
- HorAfa

---

## Índices

### R038AFAIndice2

**Tipo:** Não unico

Campos:
- StaAtu
- DatAfa
- HorAfa
- DatTer
- HorTer

### R038AFAIndice3

**Tipo:** Não unico

Campos:
- StaAtu
- DatTer
- HorTer

### R038AFAIndice4

**Tipo:** Não unico

Campos:
- SitAfa

### R038AFAIndice5

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- SitAfa
- DatAfa

### R038AFAIndice6

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CauDem

---

## Relacionamentos

### IR_R038AFA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R038AFA_008

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| SitAfa | CodSit |

