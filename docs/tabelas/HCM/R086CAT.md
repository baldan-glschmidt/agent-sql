# R086CAT

## Descrição

Acidentes de Trabalho - Ocorrências CAT

---

## Resumo

- Campos: 63
- Chave Primária: 7 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAct | Date | Não | Data Acidente de Trabalho |
| HorAct | Number(005,0) | Não | Hora Acidente de Trabalho |
| DatCat | Date | Não | Data de registro da CAT |
| TipCat | Number(001,0) | Não | Tipo CAT |
| DatObi | Date | Sim | Data do Óbito |
| CodAte | Number(006,0) | Sim | Código do Atendente |
| AreAte | Number(004,0) | Sim | Código da Área |
| CodOco | Number(006,0) | Sim | Código da Ocorrência |
| DatAte | Date | Sim | Data Atendimento Médico |
| HorAte | Number(005,0) | Sim | Hora Atendimento Médico |
| HorSai | Number(005,0) | Sim | Hora Saída Ambulatório |
| DiaAct | String(300) | Sim | Diagnóstico Acidente Trabalho |
| DatRet | Date | Sim | Data de Retorno Consulta |
| AprAct | String(040) | Sim | Unidade Atendimento do Acidentado |
| DurTra | Number(004,0) | Sim | Duração do Tratamento em dias |
| DscLes | String(300) | Sim | Descrição das Lesões |
| HouInt | String(001) | Sim | Houve Internação do Acidentado |
| DatInt | Date | Sim | Data da Internação |
| AfsTra | String(001) | Sim | Afastar do Trabalho |
| ObsLau | String(300) | Sim | Observações do Laudo |
| CodDoe | String(004) | Sim | Classificação Internacional de Doenças |
| CodCid | String(010) | Sim | Código da Classificação Internacional de Doenças |
| CodDoa | String(004) | Sim | Código de Doença conforme CID-9 |
| CodSub | String(003) | Sim | Identificação do subgrupo da CID-10 |
| ObsCat | String(999) | Sim | Observações da CAT |
| CodEsp | Number(003,0) | Sim | Código da espécie do acidente |
| AnoBas | Number(004,0) | Sim | Ano para controle de identificação da CAT |
| NumCat | Number(004,0) | Sim | Número de Controle da CAT |
| DatUlt | Date | Sim | Data do Último Dia Trabalhado |
| CodPos | Number(007,0) | Sim | Código do posto  de atendimento |
| CATPPP | String(015) | Sim | Número da CAT conforme INSS - para constar no PPP |
| CatEmi | String(001) | Sim | Identifica se a CAT foi emitida pela empresa |
| DatAfa | Date | Sim | Data de Início do Afastamento |
| HorAfa | Number(005,0) | Sim | Hora do Início do Afastamento |
| SitAte | Number(003,0) | Sim | Situação do Atestado |
| DiaAte | Number(004,0) | Sim | Dias de Atestado |
| HorTer | Number(005,0) | Sim | Hora do Término do Afastamento |
| SitAfa | Number(003,0) | Sim | Situação de Afastamento |
| DiaAfa | Number(004,0) | Sim | Dias de Afastamento |
| ExmRet | String(001) | Sim | Exame de Retorno |
| FimAfa | Date | Sim | Data final ou previsão de término do Afastamento |
| DatEmi | Date | Sim | Data da emissão da CAT |
| FimAte | Date | Sim | Data de término do atestado |
| PreAfa | String(001) | Sim | Define se a data de término é somente uma previsão |
| RaiAte | Number(002,0) | Sim | Motivo para a Rais relacionado ao atestado |
| RaiAfa | Number(002,0) | Sim | Motivo para a Rais relacionado ao afastamento |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| DiaJus | Number(002,0) | Sim | Dias Justificados |
| DatOri | Date | Sim | Informar a data da CAT de origem |
| CatOri | String(015) | Sim | Informar o número da CAT de origem |
| AciTra | Number(001,0) | Sim | Tipo de Acidente de Trânsito |
| IniCat | Number(001,0) | Sim | Iniciativa |
| CodAct | String(006) | Sim | Codificação Acidente (Obsoleto) |
| MsmMot | String(001) | Sim | Afastamento decorre de mesmo motivo de afastamento anterior dentro de 60 dias |
| RegCon | String(014) | Sim | Registro no Conselho Profissional |
| NomMed | String(070) | Sim | Nome do Médico |
| SigOrg | String(002) | Sim | Sigla da UF do Órgão de Classe |
| OrgCla | Number(001,0) | Sim | Órgão de Classe |
| TipAci | Number(001,0) | Sim | Código do tipo de acidente de trabalho |
| FusHor | Number(002,0) | Sim | Fuso Horário |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAct
- HorAct
- DatCat
- TipCat

---

## Índices

### R086CATIndice2

**Tipo:** Não unico

Campos:
- AnoBas
- NumCat

### R086CATindice3

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- DatAte
- HorAte

---

## Relacionamentos

### IR_R086CAT_028

**Tabela:** R086ESP

| Origem | Destino |
|--------|---------|
| CodEsp | CodEsp |

