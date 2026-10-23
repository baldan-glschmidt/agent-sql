# R090AGV

## Descrição

Agendamento de Visitantes

---

## Resumo

- Campos: 63
- Chave Primária: 6 campo(s)
- Índices: 5
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatPrv | Date | Não | Data Prevista da Visita |
| HorPrv | Number(005,0) | Não | Hora Prevista da Visita |
| NumEmp | Number(004,0) | Não | Código da Empresa do Visitado |
| TipCol | Number(001,0) | Não | Tipo do Colaborador Visitado |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador Visitado |
| SeqAgv | Number(002,0) | Não | Sequência do Agendamento |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| NomVis | String(040) | Sim | Nome do Visitante |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa |
| NomOem | String(060) | Sim | Empresa do Visitante |
| AutVei | String(001) | Sim | Autorizar Entrada do Visitante com Veículo |
| PlaVei | String(010) | Sim | Placa do Veículo do Visitante |
| TipVis | Number(003,0) | Sim | Tipo de Visita |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso do Visitante |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| TelCon | String(020) | Sim | Número do Telefone do Visitante para Contato |
| DatVal | Date | Sim | Data da Validade da Visita |
| HorVal | Number(005,0) | Sim | Hora da Validade da Visita |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador do Agendamento |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador do Agendamento |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador do Agendamento |
| ObsVis | String(160) | Sim | Observação da Visita |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou o Agendamento |
| VisEfe | String(001) | Sim | Indica que a Visita foi Efetuada (Agendamento Executado) |
| StaPng | Number(001,0) | Sim | Status do Agendamento |
| UsuLib | Number(010,0) | Sim | Código do Usuário que Liberou o Agendamento |
| DatLib | Date | Sim | Data da Liberação do Agendamento |
| HorLib | Number(005,0) | Sim | Hora da Liberação do Agendamento |
| MotLib | String(080) | Sim | Motivo da Liberação do Agendamento |
| EmiCid | String(020) | Sim | Orgão Emissor da Carteira de Identidade |
| EstCid | String(002) | Sim | Estado do Orgão Emissor da Carteira de Identidade |
| DexCid | Date | Sim | Data de Expedição da Carteira de Identidade |
| EmpSol | Number(004,0) | Sim | Empresa do Colaborador Solicitante |
| TclSol | Number(001,0) | Sim | Tipo do Colaborador Solicitante |
| CadSol | Number(009,0) | Sim | Cadastro do Colaborador Solicitante |
| EmpCCu | Number(004,0) | Sim | Empresa do Centro de Custo |
| CodCCu | String(018) | Sim | Código do Centro de Custo |
| StaWAV | Number(001,0) | Sim | Status do Workflow de Agendamento de Visita |
| CodLib | Number(002,0) | Sim | Código do motivo da liberação de acesso. |
| CodNac | Number(003,0) | Sim | Código da Nacionalidade |
| SegTDo | Number(001,0) | Sim | Segundo Tipo do Documento do Visitante |
| SegDoc | String(020) | Sim | Segundo Número do Documento do Visitante |
| CodPor | Number(003,0) | Sim | Código da Portaria do Agendamento de Visitante |
| CodMot | Number(004,0) | Sim | Código Motivo Acesso |
| EmaVis | String(100) | Sim | E-mail do Visitante |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |
| DatSAg | Date | Sim | Data de Solicitação do Agendamento |
| HorSAg | Number(005,0) | Sim | Hora de Solicitação do Agendamento |
| DatPSA | Date | Sim | Data de Processamento da Solicitação de Agendamento |
| HorPSA | Number(005,0) | Sim | Hora de Processamento da Solicitação de Agendamento |
| CodUPS | Number(010,0) | Sim | Código do Usuário que Processou a Solicitação de Agendamento |
| ObsRep | String(160) | Sim | Observação de Reprovação do Agendamento |
| LocAgv | Number(009,0) | Sim | Código Localizador do Agendamento de Visita |
| NomDoc | String(040) | Sim | Nome do visitante no documento |
| DatNas | Date | Sim | Data de Nascimento |
| FunVis | String(060) | Sim | Função do visitante na empresa representada |
| QuaVis | String(060) | Sim | Qualificação do visitante na empresa representada |
| DvaDoc | Date | Sim | Data de Validade (Documento) |
| PaiDoc | Number(004,0) | Sim | País de Emissão (Documento) |
| TipSex | String(001) | Sim | Sexo do Visitante |

---

## Chave Primária

- DatPrv
- HorPrv
- NumEmp
- TipCol
- NumCad
- SeqAgv

---

## Índices

### R090AGVIndice2

**Tipo:** Não unico

Campos:
- TipDoc
- NumDoc
- DatPrv
- HorPrv

### R090AGVIndice3

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

### R090AGVIndice4

**Tipo:** Não unico

Campos:
- NomVis

### R090AGVIndice5

**Tipo:** Não unico

Campos:
- DatVal

### R090AGVIndice6

**Tipo:** Não unico

Campos:
- LocAgv

---

## Relacionamentos

Nenhum relacionamento cadastrado.
