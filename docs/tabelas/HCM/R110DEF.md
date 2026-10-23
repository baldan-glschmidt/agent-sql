# R110DEF

## Descrição

Definições do Medicina/Segurança

---

## Resumo

- Campos: 146
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| ModAte | String(011) | Sim | Modelo de relatório padrão para atestado |
| ModRec | String(011) | Sim | Modelo de relatório padrão para receita |
| ModSol | String(011) | Sim | Modelo de relatório padrão para solicitação |
| ModEnc | String(011) | Sim | Modelo de relatório padrão para encaminhamento |
| ModAud | String(011) | Sim | Modelo de relatório padrão para audiometria |
| ModAAu | String(011) | Sim | Modelo de relatório padrão para acompanhamento audiometria |
| ModAso | String(011) | Sim | Modelo de relatório padrão para ASO |
| GerAfa | String(001) | Sim | Gerar Solicitação de Exames Automaticamente no Afastamento |
| GerTrC | String(001) | Sim | Gerar Solicitação Exames Automaticamente na Transferência Cargo |
| GerTrL | String(001) | Sim | Gerar Solicitação Exames Automaticamente na Transferência Local |
| GerTrF | String(001) | Sim | Gerar Solicitação Exames Automaticamente na Transferência Função |
| CodExa | Number(004,0) | Sim | Código Exame de Audiometria |
| UltExa | String(001) | Sim | Usar o Último Resultado de Exame |
| UltAco | Number(002,0) | Sim | Últimos Resultados Exames para Acompanhamento Audiometria |
| AtuAut | String(001) | Sim | Atualização Automática da Agenda |
| IntAtu | Number(005,0) | Sim | Intervalo de Atualização da Agenda |
| FabAud | String(040) | Sim | Fabricante do Audiometro |
| MldAut | String(030) | Sim | Modelo do Audiometro |
| UltAfe | Date | Sim | Data da Última Aferição |
| TemAfe | Number(002,0) | Sim | Tempo para Aferição em Meses |
| UltCal | Date | Sim | Data da Última Calibragem |
| TemCal | Number(002,0) | Sim | Tempo para Calibragem em Meses |
| ModPro | String(011) | Sim | Modelo de relatório default para prontuário clínico |
| FicEmp | String(001) | Sim | Gerar Ficha Médica para Empregado |
| FicTer | String(001) | Sim | Gerar Ficha Médica para Terceiro |
| FicPar | String(001) | Sim | Gerar Ficha Médica para Parceiro |
| FicDep | String(001) | Sim | Gerar Ficha Médica para Dependente |
| FicCan | String(001) | Sim | Gerar Ficha Médica para Candidato |
| RegFic | Number(003,0) | Sim | Código da Regra para Gerar Ficha Médica |
| HorAte | String(001) | Sim | Horário dos Atendentes |
| NSgFic | Number(001,0) | Sim | Segurança dos Dados da Ficha Médica |
| NSgAte | Number(001,0) | Sim | Segurança dos Dados do Atendimento |
| NSgRes | Number(001,0) | Sim | Segurança dos Dados da Solicitação/Resultados de Exames |
| NSgEnc | Number(001,0) | Sim | Segurança dos Dados do Encaminhamento |
| NSgAtM | Number(001,0) | Sim | Segurança dos Dados do Atestado |
| NSgQue | Number(001,0) | Sim | Segurança dos Dados do Questionário |
| CodAud | Number(003,0) | Sim | Código do audiômetro mais utilizado |
| AudLim | Number(003,0) | Sim | Parecer dentro dos limites aceitáveis |
| AudPai | Number(003,0) | Sim | Parecer Sugestivo de PAINPSE(Perda Auditiva Induzida por Níveis de Pressão Sonora Elevados) |
| AudNpa | Number(003,0) | Sim | Parecer Não Sugestivo de PAINPSE(Perda Auditiva Induzida por Níveis de Pressão Sonora Elevados) |
| AudDes | Number(003,0) | Sim | Parecer Sugestivo desencadeamento PAINPSE(Perda Auditiva Induzida por Níveis de Pressão Sonora Elevados) |
| AudAgr | Number(003,0) | Sim | Parecer Sugestivo agravamento PAINPSE(Perda Auditiva Induzida por Níveis de Pressão Sonora Elevados) |
| NumGer | Number(009,0) | Sim | Último Nr. de solicitação de exame gerado |
| ModAgd | String(011) | Sim | Modelo de relatório default para agenda |
| UtiMeO | String(001) | Sim | Define se utiliza e a apresentação da Meatoscopia/Otoscopia |
| UtiLog | String(001) | Sim | Define se utiliza e a apresentação da Logoaudiometria |
| AudDDL | Number(003,0) | Sim | Parecer Sugestivo desencadeamento PAINPSE - Dentro dos Limites |
| ASOAge | String(001) | Sim | Define se permite emissão de ASO pelo Agendamento |
| TPeCon | Number(003,0) | Sim | Definição do tipo de perda Condutiva |
| TPeNeu | Number(003,0) | Sim | Definição do tipo de perda Neurosensorial |
| TPeMis | Number(003,0) | Sim | Definição do tipo de perda Mista |
| UtiCli | String(001) | Sim | Define se o Método Clínico é utilizado |
| UtiPer | String(001) | Sim | Define se o Método Pereira é utilizado |
| UtiINS | String(001) | Sim | Define se o Método INSS é utilizado |
| MCPNor | Number(003,0) | Sim | Método Clínico - Definição do parecer Grau 0 - Normal |
| MCPLev | Number(003,0) | Sim | Método Clínico - Definição do parecer de Grau 1 - Perda Leve |
| MCPMod | Number(003,0) | Sim | Método Clínico - Definição do parecer de Grau 2 - Perda Moderada |
| MCPMSe | Number(003,0) | Sim | Método Clínico - Definição do parecer de Grau 3 - Perda Moderada/Severa |
| MCPSev | Number(003,0) | Sim | Método Clínico - Definição do parecer de Grau 4 - Perda Severa |
| MCPPro | Number(003,0) | Sim | Método Clínico - Definição do parecer de Grau 5 - Perda Profunda |
| MCPAna | Number(003,0) | Sim | Método Clínico - Definição do parecer Anacusia |
| MPPNor | Number(003,0) | Sim | Método Pereira - Definição do parecer Grau 0 - Normal |
| MPPGot | Number(003,0) | Sim | Método Pereira - Definição do parecer Grau I - Gota Acústica |
| MPPPre | Number(003,0) | Sim | Método Pereira - Definição do parecer Grau II - Prejuízo Clínico |
| MPPSur | Number(003,0) | Sim | Método Pereira - Definição do parecer Grau III - Surdez Profissional |
| MPPMin | Number(003,0) | Sim | Método Pereira - Definição do parecer Grau IV - Redução em Grau Mínimo |
| MPPMed | Number(003,0) | Sim | Método Pereira - Definição do parecer Grau V - Redução em Grau Médio |
| MPPMax | Number(003,0) | Sim | Método Pereira - Definição do parecer Grau VI - Redução em Grau Máximo |
| MPPDan | Number(003,0) | Sim | Método Pereira - Definição do parecer D.A.N.O - Disacusia não-ocupacional |
| MIPNor | Number(003,0) | Sim | Método INSS - Definição do parecer Grau 0 - Normal |
| MIPMin | Number(003,0) | Sim | Método INSS - Definição do parecer Grau 1 - Redução em grau mínimo |
| MIPMed | Number(003,0) | Sim | Método INSS - Definição do parecer Grau 2 - Redução em grau médio |
| MIPMax | Number(003,0) | Sim | Método INSS - Definição do parecer Grau 3 - Redução em grau máximo |
| MIPPer | Number(003,0) | Sim | Método INSS - Definição do parecer Grau 4 - Perda de Audição |
| HisAfa | String(001) | Sim | Define se gera histórico de afastamento através do atendimento |
| AprAud | String(001) | Sim | Define como serão apresentados os dados da Audiometria |
| CodImp | Number(003,0) | Sim | Código do impedanciômetro mais utilizado |
| AprImi | String(001) | Sim | Define se apresenta a imitanciometria |
| AprRef | String(001) | Sim | Define se apresenta o reflexo estapediano |
| ConAUS | String(001) | Sim | Define se considera uma frequência ausente na média |
| ConRis | String(001) | Sim | No ASO apresenta todos os riscos ou os não controlados |
| CodGrq | Number(003,0) | Sim | Código do questionário que será utilizado na audiometria |
| PCMHis | String(001) | Sim | Define se utiliza PCMSO controlado por datas(Sim/Não) |
| ModQue | String(011) | Sim | Modelo de relatório default para questionário |
| EmiQue | String(001) | Sim | Quando emite audiometria,  emitir questionário(Sim/Não) |
| UtiTPe | String(001) | Sim | Define se o Tipo de Perda é utilizado |
| UtiMDS | String(001) | Sim | Define se o Método Davis & Silverman é utilizado |
| UtiFow | String(001) | Sim | Define se o Método Fowler é utilizado |
| MDSNor | Number(003,0) | Sim | Método D & S - Definição do parecer Grau 0 - Normal |
| MDSLev | Number(003,0) | Sim | Método D & S - Definição do parecer Grau 1 - Perda Leve |
| MDSMod | Number(003,0) | Sim | Método D & S - Definição do parecer Grau 2 - Perda Moderada |
| MDSSev | Number(003,0) | Sim | Método D & S - Definição do parecer Grau 3 - Perda Severa |
| MDSPro | Number(003,0) | Sim | Método D & S - Definição do parecer Grau 4 - Perda Profunda |
| MFONor | Number(003,0) | Sim | Método Fowler - Definição do parecer Normal |
| MFOMin | Number(003,0) | Sim | Método Fowler - Definição do parecer para perda em Grau Mínimo |
| MFOMed | Number(003,0) | Sim | Método Fowler - Definição do parecer para perda em Grau Médio |
| AprWeb | String(001) | Sim | Define se apresenta o Teste de Weber na Audiometria |
| NumVac | Number(009,0) | Sim | Último Nr. de solicitação de vacina gerado |
| AteDem | Number(001,0) | Sim | Alerta sobre registros de atendente demitido |
| AprCID | String(001) | Sim | Apresenta subgrupo da CID-10 |
| FicCex | Number(001,0) | Sim | Utilizado no processo de geração da ficha médica para candidato |
| RegCex | Number(003,0) | Sim | Código da regra para gerar ficha médica do candidato |
| AltCli | String(001) | Sim | Permite que o atendente/atendente complementar altere dados da pasta Dados Clínicos |
| OriPer | Number(003,0) | Sim | Origem de exame de periódico para uso na geração de exames |
| OriSub | Number(003,0) | Sim | Origem de exame de subnormalidade para uso na geração de exames |
| TolAco | Number(002,0) | Sim | Dias de tolerância para registrar acompanhamento médico do afastamento |
| LogExa | Number(001,0) | Sim | Funcionamento do log para solicitação de exames |
| OriAdm | Number(003,0) | Sim | Origem de exame admissional para uso na geração de exames |
| OriTCa | Number(003,0) | Sim | Origem de exame de transferência de cargo para uso na geração de exames |
| OriTLo | Number(003,0) | Sim | Origem de exame de transferência de local para uso na geração de exames |
| OriTFu | Number(003,0) | Sim | Origem de exame de transferência de função para uso na geração de exames |
| OriTAt | Number(003,0) | Sim | Origem de exame de transferência de atividade para uso na geração de exames |
| OriDem | Number(003,0) | Sim | Origem de exame demissional para uso na geração de exames |
| OriAco | Number(003,0) | Sim | Origem de exame de acompanhamento de demitidos para uso na geração de exames |
| NSgMed | Number(001,0) | Sim | Segurança dos dados da administração de medicamentos |
| LinTra | Number(003,0) | Sim | Valor da escala dB onde será traçada uma linha fixa no gráfico |
| AprFre | String(001) | Sim | Apresentação dos valores de frequência acima/abaixo do gráfico |
| RepAud | Number(002,0) | Sim | Horas em respouso padrão que será utilizada no resultado de exame na audiometria |
| AprLin | String(001) | Sim | Apresenta a linha fixa no gráfico |
| PacDem | Number(001,0) | Sim | Alerta ao criar um atendimento para um colaborador demitido |
| SemRes | Number(001,0) | Sim | Apresentação em relatórios de exames sem respostas |
| OssPio | String(001) | Sim | Aceita resultado da via óssea pior que da via aérea(S/N) |
| UtiPos | String(001) | Sim | Define se a empresa utiliza a rotina de Pós-Atendimento |
| LimInt | Number(003,0) | Sim | Limite de Intensidade da Logoaudiometria |
| ExaDep | String(001) | Sim | Define se realiza exames periódicos para dependentes |
| ExaCpl | Number(004,0) | Sim | Código do Exame para Atualizar a Ficha Complementar |
| ConFer | String(001) | Sim | Define se devem ser considerados os dias de feriado ao gerar solicitação de exames. |
| ResAud | Number(001,0) | Sim | Define se considera os resultados da audiometria por exame ou por orelha |
| NSgAge | Number(001,0) | Sim | Segurança dos dados da agenda médica |
| ModImi | String(011) | Sim | Modelo de relatório padrão para a imitanciometria |
| TabPri | Number(003,0) | Sim | Tabela de prioridade |
| UsaJer | String(001) | Sim | Indicar se utiliza o método Jerger (1970) na Imitânciometria. |
| RegAGF | Number(003,0) | Sim | Código da regra executado antes de gerar ficha médica dos candidatos |
| ResImi | String(001) | Sim | Resultado Imitanciometria |
| OriTPo | Number(003,0) | Sim | Origem exame de transferência de posto de trabalho para uso na geração de exames |
| OriTGH | Number(003,0) | Sim | Origem de exame de transferência de GHE para uso na geração de exames |
| ConExa | Number(001,0) | Sim | Considerar Data Exame |
| ExaDem | Number(003,0) | Sim | Prazo em dias que o exame realizado antes da demissão é considerado válido |
| IniNR7 | Date | Sim | Data de início de vigência da nova NR7 conforme Portaria SEPRT nº 6.734 |
| ExaTox | Number(002,0) | Sim | Prazo em meses da validade do exame toxicológico |
| AtdAbr | Number(001,0) | Sim | Define permissão de acesso aos atendimentos |
| NumRet | Number(002,0) | Sim | Quantidade de dias para que o registro de um atendimento seja considerado retroativo |
| InfJus | String(001) | Sim | Obriga o preenchimento de uma justificativa para realizar a impressão do prontuário clínico |
| ModCon | String(011) | Sim | Modelo de relatório default para o termo de consentimento |
| MonCon | String(001) | Sim | Monitorar assinatura do termo de consentimento pelo paciente |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110DEF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

