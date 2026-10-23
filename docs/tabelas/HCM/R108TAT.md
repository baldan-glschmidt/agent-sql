# R108TAT

## Descrição

Atendentes

---

## Resumo

- Campos: 123
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAte | Number(006,0) | Não | Código Atendente |
| OriAte | String(001) | Sim | Origem do Atendente |
| NumEmp | Number(004,0) | Sim | Código Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro Colaborador |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| PisAte | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| NomAte | String(070) | Sim | Nome do Atendente |
| AreAte | Number(004,0) | Sim | Área Médica |
| RegCon | String(020) | Sim | Registro no Conselho Profissional |
| CodPrf | Number(004,0) | Sim | Conselho Profissional |
| NumTel | String(020) | Sim | Número do Telefone |
| CodUsu | Number(010,0) | Sim | Código do usuário relacionado ao atendente |
| CodPos | Number(007,0) | Sim | Código do posto  de atendimento padrão |
| NomBo1 | String(020) | Sim | Nome do 1º Botão |
| NomBo2 | String(020) | Sim | Nome do 2º Botão |
| NomBo3 | String(020) | Sim | Nome do 3º Botão |
| NomBo4 | String(020) | Sim | Nome do 4º Botão |
| ModBo1 | String(011) | Sim | Modelo Gerador Relatórios do 1º Botão |
| ModBo2 | String(011) | Sim | Modelo Gerador Relatórios do 2º Botão |
| ModBo3 | String(011) | Sim | Modelo Gerador Relatórios do 3º Botão |
| ModBo4 | String(011) | Sim | Modelo Gerador Relatórios do 4º Botão |
| BtnPro | String(001) | Sim | Exibir Botão Consulta Prontuário Clínico |
| BtnPpr | String(001) | Sim | Exibir Botão Consulta PGR |
| BtnAnt | String(001) | Sim | Exibir Botão Cadastro Ficha Médica |
| BtnRec | String(001) | Sim | Exibir Botão Cadastro Receita |
| BtnAso | String(001) | Sim | Exibir Botão Cadastro ASO |
| BtnAte | String(001) | Sim | Exibir Botão Cadastro Atestado |
| BtnSol | String(001) | Sim | Exibir Botão Cadastro Solicitação |
| BtnRes | String(001) | Sim | Exibir Botão Cadastro Resultado |
| BtnQue | String(001) | Sim | Exibir Botão Cadastro Questionário |
| BtnEnc | String(001) | Sim | Exibir Botão Cadastro Encaminhamento |
| BtnAud | String(001) | Sim | Exibir Botão Relatório Audiometria |
| BtnAAu | String(001) | Sim | Exibir Botão Relatório Acompanhamento Audiometria |
| BtnMed | String(001) | Sim | Exibir Botão Medicamentos |
| BtnExa | String(001) | Sim | Exibir Botão Próximos Exames |
| BtnVac | String(001) | Sim | Exibir Botão Vacina |
| BtnAAf | String(001) | Sim | Exibir botão acompanhamento de afastamento |
| CfgPCl | String(350) | Sim | Configurações do Prontuário Clínico |
| QtdZom | Number(003,0) | Sim | Zoom de Imagens |
| ReaAte | String(001) | Sim | Tem permissão para reabrir atendimento |
| DatAgd | Date | Sim | Data limite para permitir agendamento |
| QtdMes | Number(002,0) | Sim | É o tempo que será retrocedido p/ considerar exames no Aso |
| IndPar | String(001) | Sim | Na emissão do ASO considera a situação Exame |
| IndSai | Number(001,0) | Sim | Ao concluir atendimento, permite informar horário saída |
| AbrFil | String(025) | Sim | Abrangência de filial |
| AbrTip | String(025) | Sim | Abrangência de tipo de atendido |
| AbrAte | String(025) | Sim | Abrangência de atendente |
| TrfAgd | String(001) | Sim | Transferência do horário do agendamento na data corrente |
| ConAso | String(001) | Sim | Define qual endereço de contato deve sair no ASO/Audiometria |
| EndRua | String(040) | Sim | Endereço para contato |
| EndNum | String(006) | Sim | Número do endereço de contato |
| EndCpl | String(025) | Sim | Complemento do endereço de contato |
| CodCid | Number(007,0) | Sim | Cidade |
| CodBai | Number(004,0) | Sim | Bairro |
| EndCep | Number(008,0) | Sim | CEP do endereço de contato |
| TelCon | String(020) | Sim | Número do telefone para contato |
| CplCon | String(200) | Sim | Contato para constar na emissão do ASO |
| SitReg | String(001) | Sim | Situação do registro no conselho profissional |
| TitAte | String(009) | Sim | Título utilizado na apresentação do atendente(Dr,Dra,Fda,etc.) |
| ReaExa | String(001) | Sim | Tem permissão para reabrir exame concluído |
| InfSit | String(001) | Sim | Informa situação do resultado do exame(Ocupacional/Não Ocupac.) |
| FecQue | String(001) | Sim | Define comportamento ao gravar as respostas do questionário |
| NomBo5 | String(020) | Sim | Nome do 5º Botão |
| NomBo6 | String(020) | Sim | Nome do 6º Botão |
| ModBo5 | String(011) | Sim | Modelo Gerador Relatórios do 5º Botão |
| ModBo6 | String(011) | Sim | Modelo Gerador Relatórios do 6º Botão |
| CodRg1 | Number(003,0) | Sim | Código da regra do 1º Botão |
| CodRg2 | Number(003,0) | Sim | Código da regra do 2º Botão |
| CodRg3 | Number(003,0) | Sim | Código da regra do 3º Botão |
| CodRg4 | Number(003,0) | Sim | Código da regra do 4º Botão |
| CodRg5 | Number(003,0) | Sim | Código da regra do 5º Botão |
| CodRg6 | Number(003,0) | Sim | Código da regra do 6º Botão |
| CodOco | Number(006,0) | Sim | Código da Ocorrência padrão sugerido no atendimento |
| UsaAno | String(001) | Sim | Define se abre a tela de atendimento na pasta Anotações |
| ConAte | Number(001,0) | Sim | Define o que deve fazer com atendimentos anteriores em aberto |
| AprCon | Number(001,0) | Sim | Define se deve pedir confirmação ao concluir um atendimento. |
| UltAgd | String(001) | Sim | Ao abrir a tela de agendamento, apresenta a agenda aberta |
| BotAS1 | String(020) | Sim | Nome do 1º Botão para acompanhamento de subnormalidade |
| BotAS2 | String(020) | Sim | Nome do 2º Botão para acompanhamento de subnormalidade |
| MBoAS1 | String(011) | Sim | Modelo gerador relatórios do 1º botão de acompanhamento subnormalidade |
| MBoAS2 | String(011) | Sim | Modelo gerador relatórios do 2º botão de acompanhamento subnormalidade |
| RBoAS1 | Number(003,0) | Sim | Código da regra do 1º botão de acompanhamento subnormalidade |
| RBoAS2 | Number(003,0) | Sim | Código da regra do 2º botão de acompanhamento subnormalidade |
| BotAg1 | String(020) | Sim | Nome do 1º Botão para uso no agendamento |
| BotAg2 | String(020) | Sim | Nome do 2º Botão para uso no agendamento |
| MBoAg1 | String(011) | Sim | Modelo gerador relatórios do 1º botão para uso no agendamento |
| MBoAg2 | String(011) | Sim | Modelo gerador relatórios do 2º botão para uso no agendamento |
| RBoAg1 | Number(003,0) | Sim | Código da regra do 1º botão para uso no agendamento |
| RBoAg2 | Number(003,0) | Sim | Código da regra do 2º botão para uso no agendamento |
| ReaPos | String(001) | Sim | Tem permissão para reabrir pós-atendimento |
| AprExa | String(001) | Sim | Apresenta solicitação de exames na rotina de pós-atendimento |
| AprEnc | String(001) | Sim | Apresenta encaminhamento na rotina de pós-atendimento |
| AprMed | String(001) | Sim | Apresenta medicamentos na rotina de pós-atendimento |
| AprPro | String(001) | Sim | Apresenta procedimentos na rotina de pós-atendimento |
| BotPA1 | String(020) | Sim | Nome do 1º Botão para uso no Pós-Atendimento |
| BotPA2 | String(020) | Sim | Nome do 2º Botão para uso no Pós-Atendimento |
| MBoPA1 | String(011) | Sim | Modelo gerador relatórios do 1º botão para uso do Pós-Atendimento |
| MBoPA2 | String(011) | Sim | Modelo gerador relatórios do 2º botão para uso do Pós-Atendimento |
| RBoPA1 | Number(003,0) | Sim | Código da regra do 1º botão para uso no Pós-Atendimento |
| RBoPA2 | Number(003,0) | Sim | Código da regra do 2º botão para uso no Pós-Atendimento |
| IndPos | String(001) | Sim | Indica se o atendente faz pós-atendimento |
| BtnCat | String(001) | Sim | Exibir Botão Cadastro CAT |
| AprCID | String(001) | Sim | Apresenta CID do atendimento na rotina de pós-atendimento |
| AtuAge | Number(001,0) | Sim | Atualiza a hora de término do agendamento |
| UsaPro | Number(001,0) | Sim | Define qual tabela será usada no cadastro de procedimentos (AMB ou CBHPM) |
| OriExa | Number(003,0) | Sim | Código de Origem do Exame padrão para novos Resultados de Exame |
| SitExa | String(001) | Sim | Código da Situação do Exame padrão para novos Resultados de Exame |
| UsoRec | Number(001,0) | Sim | Define como deve ser realizada a prescrição na receita médica. |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |
| DddCon | Number(003,0) | Sim | Código DDD do contato |
| DdiCon | Number(003,0) | Sim | Código DDI do contato |
| ConCID | Number(001,0) | Sim | Define como deve apresentar a tela de consulta da CID-10. |
| NSgAge | Number(001,0) | Sim | Segurança dos dados da agenda médica |
| TabPri | Number(003,0) | Sim | Tabela de prioridade |
| LimAgd | Number(002,0) | Sim | Quantidade limite de agendamentos gerados por dia para o atendente |
| guiAMB | Number(001,0) | Sim | Guia Procedimentos AMB disponível para atendentes na tela Pré-Atendimento |
| gCBHPM | Number(001,0) | Sim | Guia Procedimentos CBHPM disponível para atendentes na tela de Pré-Atendimento |
| gRecei | Number(001,0) | Sim | Guia Receitas disponível para atendentes na tela de Pré-Atendimento |
| gImage | Number(001,0) | Sim | Guia Anexos disponível para atendentes na tela de Pré-Atendimento |
| ArqCer | Image | Sim | Certificado digital do atendente |
| MsgAtd | String(001) | Sim | Monitorar atendimentos não concluídos ao entrar e sair do sistema |

---

## Chave Primária

- CodAte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
