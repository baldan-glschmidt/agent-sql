# R090MVI

## Descrição

Entrada/Saída de Visitantes

---

## Resumo

- Campos: 55
- Chave Primária: 3 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatEnt | Date | Não | Data de Entrada |
| HorEnt | Number(005,0) | Não | Hora de Entrada |
| SeqEnt | Number(002,0) | Não | Sequência do Registro |
| NumCra | Number(012,0) | Sim | Código do Crachá |
| NumEmp | Number(004,0) | Sim | Empresa do Visitado |
| TipCol | Number(001,0) | Sim | Tipo do Visitado |
| NumCad | Number(009,0) | Sim | Cadastro do Visitado |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| CodPor | Number(003,0) | Sim | Código da Portaria da Entrada do Visitante |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| SegTDo | Number(001,0) | Sim | Segundo Tipo do Documento do Visitante |
| SegDoc | String(020) | Sim | Segundo Número do Documento do Visitante |
| PlaVee | String(010) | Sim | Placa do Veículo Entrada |
| CodPrm | Number(005,0) | Sim | Código Permissão de Acesso |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| TelCon | String(020) | Sim | Número do Telefone do Visitante para Contato |
| DatVal | Date | Sim | Data de Validade |
| HorVal | Number(005,0) | Sim | Hora da Validade do Visitante |
| TipVis | Number(003,0) | Sim | Tipo da Visita |
| ObsVis | String(160) | Sim | Observação do Visitante |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Entrada |
| DatSai | Date | Sim | Data da Saída da Empresa |
| HorSai | Number(005,0) | Sim | Hora da Saída da Empresa |
| DatSLo | Date | Sim | Data da Saída do Local Visitado na Empresa |
| HorSLo | Number(005,0) | Sim | Hora da Saída do Local Visitado na Empresa |
| PlaVes | String(010) | Sim | Placa do Veículo Saída |
| PlaCae | String(010) | Sim | Placa Reboque 1 - Entrada |
| PlaCas | String(010) | Sim | Placa Reboque 1 - Saída |
| AssVid | String(001) | Sim | Assistiu Vídeo de Segurança |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa |
| NumCon | String(015) | Sim | Número do Contrato de Serviço |
| EmpCCu | Number(004,0) | Sim | Empresa do Centro de Custo |
| CodCCu | String(018) | Sim | Código do Centro de Custo |
| NomOem | String(060) | Sim | Nome da Outra Empresa |
| CodLib | Number(002,0) | Sim | Código do motivo da liberação de acesso. |
| CodNac | Number(003,0) | Sim | Código da Nacionalidade |
| CodMot | Number(004,0) | Sim | Código Motivo Acesso |
| CraVei | Number(012,0) | Sim | Crachá Veículo |
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |
| PlaCE2 | String(010) | Sim | Placa Reboque 2 - Entrada |
| PlaCE3 | String(010) | Sim | Placa Reboque 3 - Entrada |
| PlaCS2 | String(010) | Sim | Placa Reboque 2 - Saída |
| PlaCS3 | String(010) | Sim | Placa Reboque 3 - Saída |
| EmaVis | String(100) | Sim | E-mail do Visitante |
| LocAgv | Number(009,0) | Sim | Código Localizador do Agendamento de Visita |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |
| ANDVIS | Number(003,0) | Sim | Andar da Visita |
| CPFRes | Number(011,0) | Sim | CPF da pessoa que coletou as info. em formulário papel durante a contingência |
| Repres | String(001) | Sim | Enviar como Representado para a API-Recintos, através do evento Representantes |
| RepTDo | Number(001,0) | Sim | Tipo do Documento do Representado |
| RepDoc | String(020) | Sim | Número do Documento do Representado |

---

## Chave Primária

- DatEnt
- HorEnt
- SeqEnt

---

## Índices

### R090MVIIndice2

**Tipo:** Não unico

Campos:
- NumCra
- TipDoc
- NumDoc
- DatSai

### R090MVIIndice3

**Tipo:** Não unico

Campos:
- TipDoc
- NumDoc
- NumCra

### R090MVIIndice4

**Tipo:** Não unico

Campos:
- DatSai

---

## Relacionamentos

Nenhum relacionamento cadastrado.
