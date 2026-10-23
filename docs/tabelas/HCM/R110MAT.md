# R110MAT

## Descrição

Atendimentos

---

## Resumo

- Campos: 85
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| DatAte | Date | Não | Data do Atendimento |
| HorAte | Number(005,0) | Não | Hora do Atendimento |
| TipAte | Number(001,0) | Sim | Tipo de Atendimento |
| CodAte | Number(006,0) | Sim | Código do atendente interno responsável pelo atendimento |
| AreAte | Number(004,0) | Sim | Código da área médica |
| CodOco | Number(006,0) | Sim | Código da Ocorrência |
| ValCus | Number(011,2) | Sim | Valor do Custo |
| DatRet | Date | Sim | Data para o próximo Retorno |
| HorEnt | Number(005,0) | Sim | Hora de Entrada |
| HorSai | Number(005,0) | Sim | Hora Saída |
| ObsAte | String(8000) | Sim | Anotações do Atendimento |
| DatAfa | Date | Sim | Data do Afastamento |
| HorAfa | Number(005,0) | Sim | Hora do Afastamento |
| SitAte | Number(003,0) | Sim | Situação Atestado |
| DiaAte | Number(004,0) | Sim | Dias de Atestado |
| SitAfa | Number(003,0) | Sim | Situação de Afastamento |
| DiaAfa | Number(004,0) | Sim | Dias de Afastamento |
| FimAfa | Date | Sim | Data Final Afastamento |
| HorTer | Number(005,0) | Sim | Hora Término do Afastamento Atestado |
| ExmRet | String(001) | Sim | Exame no Retorno |
| PreAlt | Number(003,0) | Sim | Pressão Alta (Sistólica) |
| PreBai | Number(003,0) | Sim | Pressão Baixa (Diastólica) |
| PlsAte | Number(003,0) | Sim | Batimentos Cardíaco |
| TmpAte | Number(003,1) | Sim | Temperatura |
| PesAte | Number(006,3) | Sim | Peso |
| NumRec | Number(006,0) | Sim | Número da Receita Médica |
| NumAte | Number(009,0) | Sim | Número do Atestado |
| CodDoe | String(004) | Sim | Classificação Internacional de Doenças |
| CodCid | String(010) | Sim | Código da Classificação Internacional de Doenças |
| DatAct | Date | Sim | Data Acidente de Trabalho |
| HorAct | Number(005,0) | Sim | Hora Acidente de Trabalho |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| AltAtn | Number(005,2) | Sim | Altura do Atendido |
| AteCpl | Number(006,0) | Sim | Código do atendente que complementou o atendimento |
| AreCpl | Number(004,0) | Sim | Código da área do atendente complementar |
| RecCpl | Number(006,0) | Sim | Número da receita médica complementar |
| NAtCpl | Number(009,0) | Sim | Número do atestado complementar |
| ObsCpl | String(8000) | Sim | Anotações do atendimento complementar |
| AtePre | Number(006,0) | Sim | Código do atendente do Pré-atendimento |
| SitAtd | Number(001,0) | Sim | Situação do atendimento |
| AteFim | Number(006,0) | Sim | Código do atendente final |
| DatFim | Date | Sim | Data da finalização do atendimento |
| HorFim | Number(005,0) | Sim | Hora da finalização do atendimento |
| CodPos | Number(007,0) | Sim | Código do posto  de atendimento |
| IndAlt | String(001) | Sim | Indicador de atendimento alterado |
| ObsPre | String(5000) | Sim | Anotações do pré-atendimento |
| IndAge | String(001) | Sim | Houve Agendamento |
| HorRet | Number(005,0) | Sim | Hora para próximo retorno |
| RaiAte | Number(002,0) | Sim | Motivo para a Rais relacionado ao atestado |
| RaiAfa | Number(002,0) | Sim | Motivo para a Rais relacionado ao afastamento |
| FimAte | Date | Sim | Data de término do atestado |
| PreAfa | String(001) | Sim | Define se a data de término é somente uma previsão |
| AteAss | String(001) | Sim | Define se o atendimento é assistencial/ocupacional |
| CodSub | String(003) | Sim | Identificação do subgrupo da CID-10 |
| DurTra | Number(004,0) | Sim | Duração do Tratamento em dias |
| PerCef | Number(006,3) | Sim | Perímetro Cefálico (cm) |
| PerAbd | Number(006,3) | Sim | Perímetro Abdominal (cm) |
| RisNex | String(001) | Sim | Indica se há risco do afastamento ser convertido em acidente de trabalho (Nexo Epidemiológico) |
| DiaJus | Number(002,0) | Sim | Dias Justificados |
| TabPri | Number(003,0) | Sim | Tabela de prioridade |
| CodPri | Number(003,0) | Sim | Código da prioridade do atendimento |
| AciTra | Number(001,0) | Sim | Tipo de Acidente de Trânsito |
| MsmMot | String(001) | Sim | Afastamento decorre de mesmo motivo de afastamento anterior dentro de 60 dias |
| AteExt | Number(006,0) | Sim | Código do Atendente (Externo) |
| NatExt | Number(009,0) | Sim | Número do Atestado (Externo) |
| RegRet | String(001) | Sim | Registro de atendimento retroativo |
| JusRet | String(300) | Sim | Justificativa para registro retroativo |
| ModAtd | Number(001,0) | Sim | Modalidade do atendimento |
| FreRes | Number(003,0) | Sim | Frequência Respiratória (rpm) |
| SatOxi | Number(005,2) | Sim | Saturação de oxigênio (%) |
| GliCap | Number(006,1) | Sim | Glicemia capilar (mg/dL) |
| IntDor | Number(001,0) | Sim | Intensidade da dor |
| ObsCli | String(2000) | Sim | Observações de clínicas livres |
| SupCor | Number(005,2) | Sim | Superfície corpórea (m²) |
| CodCia | String(010) | Sim | Código único do CIAP-2 |
| SoaSub | String(8000) | Sim | SOAP - Subjetivo |
| SoaObj | String(8000) | Sim | SOAP - Objetivo |
| SoaAva | String(8000) | Sim | SOAP - Avaliação |
| SoaPla | String(8000) | Sim | SOAP - Plano |
| JusRea | String(8000) | Sim | Justificativa Reabertura |
| FusHor | Number(002,0) | Sim | Fuso Horário |
| USU_TipOco | Number(001,0) | Sim | Tipo da Ocorrência (Acidente/Incidente) |
| USU_CodOco | Number(006,0) | Sim | Código da Ocorrência / Acidente |

---

## Chave Primária

- NumEmp
- CodFic
- DatAte
- HorAte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110MAT_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R110MAT_006

**Tabela:** R108ARE

| Origem | Destino |
|--------|---------|
| AreAte | AreAte |

### IR_R110MAT_007

**Tabela:** R108TOC

| Origem | Destino |
|--------|---------|
| CodOco | CodOco |

