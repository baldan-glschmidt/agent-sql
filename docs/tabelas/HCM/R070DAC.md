# R070DAC

## Descrição

Definições de Acesso

---

## Resumo

- Campos: 95
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDac | Number(003,0) | Não | Código da Definição de Acesso |
| DesDac | String(060) | Sim | Descrição do Acesso |
| PerDoc | String(001) | Sim | Permitir Cadastramento de Visitante sem Documento |
| PerAgv | String(001) | Sim | Permitir Entrada de Visitante sem Agendamento |
| LnkCon | String(030) | Sim | Link para Geração das Tabelas Telemática |
| ArmMar | Number(001,0) | Sim | Tipo de Armazenamento das Marcações do On-Line Telemática |
| UsuTel | String(030) | Sim | Nome do Usuário das Tabelas da Telemática |
| PerSAc | String(001) | Sim | Permitir a Saída do Acompanhante sem o Visitante |
| PerSig | String(001) | Sim | Permitir Saída de Um Integrante do Grupo Separadamente |
| GViGru | String(001) | Sim | Gravar Integrante do Grupo de Visitantes como Visitante |
| QtdViS | Number(002,0) | Sim | Quantidade Máxima de Visitas na Semana Para Cada Visitante |
| HorVis | Number(005,0) | Sim | Limite mínimo de horas para contador de visitas na semana |
| BloDia | Number(002,0) | Sim | Qtde de Dias de Falta Para Bloquear Acesso do Colaborador |
| MotBlo | Number(002,0) | Sim | Código do Motivo p/ Bloqueio do Acesso por Falta |
| AceNiv | String(001) | Sim | Controla até 99 Níveis de Acesso |
| LisVis | String(001) | Sim | Controla Lista de Visitantes p/ Acesso On-Line |
| PrmAen | Number(005,0) | Sim | Código da Permissão Padrão para Autorização de Entrada |
| SSeDoc | String(001) | Sim | Solicitar Segundo Documento do Visitante |
| ValPrv | String(001) | Sim | Sugere a Validade do Crachá Provisório |
| UsaBnf | String(001) | Sim | Utiliza Controle de Benefícios On-Line |
| UsaAla | String(001) | Sim | Monitora Tabela de Alarme dos Coletores |
| CriVis | String(001) | Sim | Critica na Entrada de Visitantes quando o Visitado está Ausente |
| VerDoc | Number(001,0) | Sim | Critica se Docto do Visitante for de Colaborador |
| TipDam | Number(001,0) | Sim | Tipo de Marcação |
| ConEpi | Number(001,0) | Sim | Controle de EPI para Visitantes |
| VisObr | String(001) | Sim | Cadastro do Visitado Obrigatório na Entrada de Visitantes |
| BloCra | Number(001,0) | Sim | Bloqueia Crachá pela Máscara do Crachá |
| GerCrc | String(001) | Sim | Gera Créditos de Acesso no Refeitório para Colaborador na Admissão |
| GerCrv | String(001) | Sim | Gera Créditos de Acesso no Refeitório para Visitantes na Entrada |
| VerPTe | Number(003,0) | Sim | Versão do Pacote de Acesso da Telemática |
| SitCol | String(001) | Sim | Monitoramento dos equipamentos pela tabela SitColetor |
| FncSob | Number(002,0) | Sim | Código da Função Padrão para Sobremesa na Coleta |
| VisLMa | Number(001,0) | Sim | Usar Letras Sempre Maiúsculas nas Telas de Visitantes |
| AgeAut | String(001) | Sim | Mostrar Somente Agendamentos com Autorizador na Entrada do Visitante |
| ConCre | Number(001,0) | Sim | Controla Créditos de Acesso para Visitantes |
| LimDam | String(001) | Sim | Efetuar a limpeza das tabelas temporárias Automaticamente. |
| PerAce | Number(001,0) | Sim | Permissão do Acesso na Saída do 3o. Turno |
| FotVis | Number(001,0) | Sim | Tipo de Armazenamento da Foto do Visitante |
| CreOcr | Number(001,0) | Sim | Controla Créditos de Acesso para Colaboradores de Outras Unidades |
| ObrAdb | String(001) | Sim | Obrigatório Autorizador de  Desbloqueio de Crachás e Colaboradores |
| PerCom | Number(003,0) | Sim | Percentual de Compressão da Foto |
| FotCol | Number(001,0) | Sim | Tipo de Armazenamento da Foto do Colaborador |
| UtiCam | String(001) | Sim | Utiliza Controle de Campus |
| CreAlu | Number(001,0) | Sim | Controla Créditos de Acesso para Alunos |
| FotAlu | Number(001,0) | Sim | Tipo de Armazenamento da Foto do Aluno / Responsável |
| OrgEmi | String(001) | Sim | Utiliza Orgão Emissor do Documento do Visitante |
| AlmTes | String(001) | Sim | Utiliza Alarme de Testes |
| MulQua | String(001) | Sim | Utiliza Múltiplo Monitoramento Quadro Sinótico |
| UtiHos | String(001) | Sim | Utiliza Controle de Hospitais |
| UtiWAV | String(001) | Sim | Utiliza WorkFlow Agendamento Visita Web |
| FotPac | Number(001,0) | Sim | Tipo de Armazenamento da Foto do Paciente |
| FaiOcr | Number(001,0) | Sim | Controla Faixa Horária de Acesso Colaborador Outra Unidade |
| VtdDfa | String(001) | Sim | Visitado afastado pode receber visita |
| CrePac | Number(001,0) | Sim | Controla Créditos de Acesso para Pacientes |
| ModBio | Number(001,0) | Sim | Modelo da Leitora Biométrica |
| AutMat | String(001) | Sim | Utiliza Autorização para Movimentação de Materiais |
| ChcAss | String(001) | Sim | Relacionamento de Crachás |
| ModSol | String(011) | Sim | Nome do Modelo para Impressão de Solicitação de Acesso por Local Físico |
| GerPen | String(001) | Sim | Gera Pendência Telemática |
| PenPer | String(001) | Sim | Gera Pendência telemática de permissão |
| PenCrc | String(001) | Sim | Gera Pendência Telemática de Créditos de Acesso |
| PenCon | String(001) | Sim | Gera Pendência Telemática para Condutores |
| PenFxh | String(001) | Sim | Gera Pendência Telemática de Faixa Horária |
| PenMsg | String(001) | Sim | Gera Pendência Telemática para Mensagens |
| PenDef | String(001) | Sim | Gera Pendência Telemática Def. Acesso |
| RejDup | String(001) | Sim | Rejeita marcações duplicadas |
| MulCon | String(001) | Sim | Utiliza multiconcentradora |
| UtiCcr | String(001) | Sim | Utiliza compra de crédito de acesso |
| UtiP73 | String(001) | Sim | Ativar o controle de integração de dados alfandegados (Portaria 73) |
| SelPor | String(001) | Sim | Selecionar agendamento de visitante por portaria |
| GerCMA | String(001) | Sim | Gera como matrícula armazenada |
| CreRes | Number(001,0) | Sim | Controla Créditos de Acesso para Responsável de Alunos |
| TemPra | Number(003,0) | Sim | Tempo Mínimo de Permanência no Acesso do Aluno |
| TemPrr | Number(003,0) | Sim | Tempo Mínimo de Permanência no Acesso do Responsável |
| ObrFmv | Number(001,0) | Sim | Obrigatório captura de foto na movimentação de visitantes |
| BaiAen | String(001) | Sim | Baixa automática de crachás de autorização de entrada |
| LeiDoc | Number(001,0) | Sim | Modelo da Leitora de Documentos |
| MonAlm | String(001) | Sim | Exibir rotina de monitoramento de alarmes |
| HchAlf | String(001) | Sim | Exibir rotina de crachás alfanuméricos |
| GrpVis | String(001) | Sim | Exibir rotina de grupo de visitantes |
| QtdPas | Number(003,0) | Sim | Quantidade de dias para rejeitar marcações passadas |
| QtdFut | Number(003,0) | Sim | Quantidade de dias para rejeitar marcações futuras |
| TipTbs | Number(002,0) | Sim | Tipo do arquivo TBS |
| AgeUti | String(001) | Sim | Exibir Agendamentos de Autorização de Entrada Já Utilizados |
| GerLpe | String(001) | Sim | Gera log de pendência da tabela R070ADM |
| ConFpl | String(001) | Sim | Controla fuso por planta |
| SeqAde | Number(001,0) | Sim | Sequenciamento Alfandegado |
| NotCol | Number(001,0) | Sim | Notificar Colaborador |
| MblVis | Number(002,0) | Sim | Código do motivo de bloqueio do colaborador por movimentação como visitante |
| UsaCpd | String(001) | Sim | Utiliza Controle de Provisórios não devolvidos |
| UtiAut | String(001) | Sim | Utiliza Carga de Inclusão e Exclusão Automática |
| TolAge | String(001) | Sim | Controla tolerância para busca de agendamentos |
| TolTem | Number(004,0) | Sim | Tempo tolerância (em minutos) |
| UtiNsc | String(001) | Sim | Utiliza nome social no cadastro de visitante |
| CstCol | Number(002,0) | Sim | Consentimento da LGPD para terceiros e parceiros |

---

## Chave Primária

- CodDac

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
