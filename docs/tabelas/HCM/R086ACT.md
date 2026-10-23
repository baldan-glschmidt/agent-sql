# R086ACT

## Descrição

Acidentes de Trabalho

---

## Resumo

- Campos: 119
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAct | Date | Não | Data Acidente de Trabalho |
| HorAct | Number(005,0) | Não | Hora Acidente de Trabalho |
| TipCat | Number(001,0) | Sim | Tipo CAT |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Cargo Acidentado |
| QmeCar | Number(003,0) | Sim | Meses de Cargo |
| ExeCar | String(001) | Sim | Já Exerceu Cargo (S/N) |
| OutCar | String(001) | Sim | Usar outro Cargo (S/N) |
| DesLoc | String(250) | Sim | Especificação do Local do Acidente |
| DesAct | String(1000) | Sim | Descrição do Acidente |
| NomTeA | String(040) | Sim | Nome Testemunha A |
| EndTeA | String(040) | Sim | Endereço Testemunha A |
| CidTeA | Number(007,0) | Sim | Código da Cidade Testemunha A |
| BaiTeA | Number(004,0) | Sim | Código do Bairro Testemunha A |
| TelTeA | String(020) | Sim | Número do Telefone Testemunha A |
| NomTeB | String(040) | Sim | Nome Testemunha B |
| EndTeB | String(040) | Sim | Endereço Testemunha B |
| CidTeB | Number(007,0) | Sim | Código da Cidade Testemunha B |
| BaiTeB | Number(004,0) | Sim | Código do Bairro Testemunha B |
| TelTeB | String(020) | Sim | Número do Telefone Testemunha B |
| HorTrb | Number(010,0) | Sim | Horas Trabalhadas Acidente |
| DatAfa | Date | Sim | Data de Início do Afastamento |
| HorAfa | Number(005,0) | Sim | Hora do Início do Afastamento |
| HorAft | Number(010,0) | Sim | Horas Afastadas |
| HorPer | Number(010,0) | Sim | Horas Úteis Perdidas |
| SitAte | Number(003,0) | Sim | Situação do Atestado |
| DiaAte | Number(002,0) | Sim | Dias de Atestado |
| SitAfa | Number(003,0) | Sim | Situação de Afastamento |
| DiaAfa | Number(003,0) | Sim | Dias de Afastamento |
| FimAfa | Date | Sim | Data Final Afastamento |
| HorTer | Number(005,0) | Sim | Hora do Término do Afastamento |
| ExmRet | String(001) | Sim | Exame de Retorno |
| DiaDeb | Number(004,0) | Sim | Dias Debitados |
| CusAte | Number(011,2) | Sim | Custo Atendimento |
| CusMat | Number(011,2) | Sim | Custo dos Materiais |
| CusQpr | Number(011,2) | Sim | Custo Queda Produção |
| EspAct | Number(003,0) | Sim | Código Espécie |
| CodAte | Number(006,0) | Sim | Código do Atendente |
| AreAte | Number(004,0) | Sim | Código da área médica |
| CodOco | Number(006,0) | Sim | Código da Ocorrência |
| TipAct | Number(003,0) | Sim | Código Tipo Acidente Trabalho |
| CodTas | Number(009,0) | Sim | Código da situação geradora do acidente conforme tabela do eSocial |
| CauAct | Number(003,0) | Sim | Causa Acidente |
| AgeLes | Number(003,0) | Sim | Código do Agente Causador |
| LocLes | Number(003,0) | Sim | Código Local das Lesões |
| NatLes | Number(003,0) | Sim | Código Natureza das Lesões |
| CodDnl | Number(009,0) | Sim | Código da natureza de lesão conforme tabela do eSocial |
| GraAci | String(001) | Sim | Gravidade do Acidente |
| DatAte | Date | Sim | Data Atendimento Médico |
| HorAte | Number(005,0) | Sim | Hora Atendimento Médico |
| HorSai | Number(005,0) | Sim | Hora Saída Ambulatório |
| DiaAct | String(160) | Sim | Diagnóstico Acidente Trabalho |
| ObsAct | String(1000) | Sim | Anotações Acidente Trabalho |
| DatRet | Date | Sim | Data de Retorno Consulta |
| UsaEPI | String(001) | Sim | Usando E.P.I. |
| RegPol | String(001) | Sim | Registro Policial (S/N) |
| EmpRsp | Number(004,0) | Sim | Código da empresa do responsável |
| TipRsp | Number(001,0) | Sim | Tipo de Colaborador Responsável |
| CadRsp | Number(009,0) | Sim | Cadastro Responsável Informações |
| AprAct | String(040) | Sim | Unidade Atendimento do Acidentado |
| DscLes | String(160) | Sim | Descrição das Lesões |
| DurTra | Number(004,0) | Sim | Duração do Tratamento em dias |
| HouInt | String(001) | Sim | Houve Internação do Acidentado |
| DatInt | Date | Sim | Data da Internação |
| AfsTra | String(001) | Sim | Afastar do Trabalho |
| ObsLau | String(160) | Sim | Observações do Laudo |
| DatObi | Date | Sim | Data do Óbito |
| FilIns | Number(001,0) | Sim | Filiação INSS |
| TipLoc | Number(001,0) | Sim | Local do Acidente |
| CodOem | Number(008,0) | Sim | Outra Empresa onde ocorreu o acidente |
| CodDoe | String(004) | Sim | Classificação Internacional de Doenças |
| TemAtd | String(001) | Sim | Tem Atendimento para o Acidente |
| AteAfs | String(001) | Sim | Atendimento com Afastamento |
| DatPri | Date | Sim | Data do Primeiro Afastamento |
| CodPos | Number(007,0) | Sim | Código do posto de atendimento |
| CodCid | Number(007,0) | Sim | Cidade onde ocorreu o acidente |
| CodPst | String(012) | Sim | Código de Endereçamento Postal |
| CATPPP | String(015) | Sim | Número da CAT conforme INSS - para constar no PPP |
| CatEmi | String(001) | Sim | Identifica se a CAT foi emitida pela empresa |
| CepTeA | Number(008,0) | Sim | CEP Testemunha A |
| CepTeB | Number(008,0) | Sim | CEP Testemunha B |
| CusAfa | Number(011,2) | Sim | Custo com Afastamento até 15 dias |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| NumAci | Number(008,0) | Sim | Número de identificação do acidente |
| TipOco | Number(001,0) | Sim | Tipo da Ocorrência (Acidente/Incidente) |
| OcoAct | Number(006,0) | Sim | Código da Ocorrência |
| CodInv | Number(006,0) | Sim | Código da Investigação |
| DddTeA | Number(003,0) | Sim | Código DDD do telefone da testemunha A |
| DdiTeA | Number(003,0) | Sim | Código DDI do telefone da testemunha A |
| DddTeB | Number(003,0) | Sim | Código DDD do telefone da testemunha B |
| DdiTeB | Number(003,0) | Sim | Código DDI do telefone da testemunha B |
| TipLgr | String(005) | Sim | Tipo de Logradouro do endereço onde ocorreu o acidente |
| EndAct | String(100) | Sim | Descrição do logradouro onde ocorreu o acidente |
| EndNum | String(006) | Sim | Número do logradouro onde ocorreu o acidente |
| NumTeA | String(005) | Sim | Número do logradouro |
| NumTeB | String(005) | Sim | Número do logradouro |
| LatLes | Number(001,0) | Sim | Lateralidade da Lesão/Parte Atingida |
| EstExt | String(001) | Sim | Estabelecimento no Exterior |
| CodPai | Number(004,0) | Sim | Código do país onde ocorreu o acidente |
| CodEst | String(004) | Sim | Estado onde ocorreu o acidente |
| EndCpl | String(030) | Sim | Complemento do endereço onde ocorreu o acidente |
| CodBai | Number(004,0) | Sim | Bairro onde ocorreu o acidente |
| EndCep | Number(008,0) | Sim | Código de Endereçamento Postal (CEP) onde ocorreu o acidente |
| TipIns | Number(001,0) | Sim | Tipo de inscrição do estabelecimento onde ocorreu o acidente |
| NumIns | Number(015,0) | Sim | Número de inscrição do estabelecimento onde ocorreu o acidente - Obsoleto |
| CfjIns | String(014) | Sim | Número de inscrição do estabelecimento onde ocorreu o acidente |
| CodFil | Number(006,0) | Sim | Filial onde ocorreu o acidente |
| NumAmb | Number(007,0) | Sim | Código do Ambiente de Trabalho |
| TipAci | Number(001,0) | Sim | Código do tipo de acidente de trabalho |
| CodAca | Number(009,0) | Sim | Código do agente causador do acidente conforme tabela do eSocial |
| CodPar | Number(009,0) | Sim | Código da parte atingida no acidente conforme tabela do eSocial |
| USU_NomEnc | String(060) | Sim | Nome Encarregado |
| USU_SupGer | String(060) | Sim | Supervisor/Gerente |
| USU_TipJor | Number(001,0) | Sim | Jornada |
| USU_BemMat | String(1000) | Sim | Bem Patrimonial Máquina |
| USU_DesEpi | String(1000) | Sim | Descrição EPI |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAct
- HorAct

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
