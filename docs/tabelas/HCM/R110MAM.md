# R110MAM

## Descrição

Atestados Médicos

---

## Resumo

- Campos: 42
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodAte | Number(006,0) | Não | Código do Atendente |
| NumAte | Number(009,0) | Não | Número do Atestado Médico |
| CodFic | Number(009,0) | Sim | Código da Ficha Médica |
| DatAte | Date | Sim | Data de emissão do atestado |
| TipAte | Number(001,0) | Sim | Tipo de Atendimento que está gerando o Atestado/ASO |
| TipMam | Number(001,0) | Sim | Tipo Duração |
| DiaAte | Number(004,0) | Sim | Tempo de Atestado  em Dias |
| CodOco | Number(006,0) | Sim | Código da Ocorrência |
| CodPar | Number(003,0) | Sim | Código do Parecer |
| CodPos | Number(007,0) | Sim | Código do posto  de atendimento |
| DesAte | String(500) | Sim | Procedimento |
| CodDoe | String(004) | Sim | Classificação Internacional de Doenças |
| CodCid | String(010) | Sim | Código da Classificação Internacional de Doenças |
| TipAso | Number(001,0) | Sim | Tipo do ASO |
| OriAte | String(001) | Sim | Origem do Atestado |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| DatAfa | Date | Sim | Data do afastamento |
| SitAte | Number(003,0) | Sim | Situação do atestado |
| HorAfa | Number(005,0) | Sim | Hora do afastamento |
| HorTer | Number(005,0) | Sim | Hora término do afastamento |
| ObsAte | String(2000) | Sim | Observação do Atestado |
| FimAte | Date | Sim | Data de término do atestado |
| HorAte | Number(005,0) | Sim | Tempo de Atestado em Horas |
| CodSub | String(003) | Sim | Identificação do subgrupo da CID-10 |
| DatInc | Number(014,6) | Sim | Data da inclusão do atestado |
| UltAlt | Number(014,6) | Sim | Data da última alteração do atestado |
| AciTra | Number(001,0) | Sim | Tipo de Acidente de Trânsito |
| MsmMot | String(001) | Sim | Afastamento decorre de mesmo motivo de afastamento anterior dentro de 60 dias |
| NomAte | String(070) | Sim | Nome do médico que emitiu o atestado |
| CodPrf | Number(004,0) | Sim | Código do conselho profissional do médico que emitiu o atestado |
| RegCon | String(014) | Sim | Número de inscrição do médico no conselho profissional |
| CpfAte | Number(011,0) | Sim | Número do CPF do médico que emitiu o atestado |
| PisAte | Number(011,0) | Sim | Número do PIS, PASEP ou NIT do médico que emitiu o atestado |
| OrgCla | Number(001,0) | Sim | Código do órgão de classe no eSocial |
| EstOrg | String(002) | Sim | Sigla da UF do órgão de classe |
| EnvEso | String(001) | Sim | Informar se deseja que o ASO seja enviado ao eSocial através do evento S-2220 |
| DocuId | String(050) | Sim | DocumentId do arquivo no GED |
| EnveId | String(050) | Sim | EnvelopeId do arquivo no GED |
| SitAss | Number(001,0) | Sim | Status da assinatura do documento no GED |
| FusHor | Number(002,0) | Sim | Fuso Horário |
| USU_Ocupa | String(001) | Sim | Classificação |

---

## Chave Primária

- NumEmp
- CodAte
- NumAte

---

## Índices

### R110MAMIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodDoe
- CodPar
- TipAso
- DatAte

---

## Relacionamentos

### IR_R110MAM_001

**Tabela:** R108TAT

| Origem | Destino |
|--------|---------|
| CodAte | CodAte |

### IR_R110MAM_003

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

