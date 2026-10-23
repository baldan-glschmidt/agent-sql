# R300PRO

## Descrição

Processos Automáticos

---

## Resumo

- Campos: 107
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPat | Number(002,0) | Não | Tipo do Processo Automático |
| CodPro | Number(003,0) | Não | Código do Processo |
| DesPro | String(040) | Sim | Descrição do Processo |
| DatIni | Date | Sim | Data de Início do Processo |
| HorIni | Number(005,0) | Sim | Hora de Início do Processo |
| PerExe | Number(001,0) | Sim | Periodicidade de Execução do Processo |
| IntGer | Number(004,0) | Sim | Intervalo de Execução |
| CodLcl | Number(003,0) | Sim | Código da Localidade |
| RenArq | Number(001,0) | Sim | Renomear Arquivo Anterior |
| DatVal | Date | Sim | Data da Validade do Processo Automático |
| DatExe | Date | Sim | Data da Próxima Execução do Processo |
| HorExe | Number(005,0) | Sim | Hora da Próxima Execução do Processo |
| DiaUti | String(001) | Sim | Executar o Processo Somente em Dias Úteis |
| PrePat | Number(002,0) | Sim | Tipo do Processo Predecessor |
| PreCod | Number(003,0) | Sim | Código do Processo Predecessor |
| ArqEnt | String(100) | Sim | Nome do Arquivo de Entrada |
| ArqSai | String(100) | Sim | Nome do Arquivo de Saída |
| ArqApe | String(100) | Sim | Concatenar Arquivo |
| ArqMod | String(100) | Sim | Nome do Modelo Gerador Relatórios/Importação/Exportação |
| GerAut | String(001) | Sim | Executa rotina padrão de atualização de históricos |
| ProCal | Number(001,0) | Sim | Tipo do Cálculo |
| IncCal | String(001) | Sim | Gerar Cálculo Automaticamente ao Processar Novo Período |
| LerArq | String(001) | Sim | Ler Arquivos de Marcações Coletados no Off-Line |
| ArqExe | String(100) | Sim | Nome do Programa a Ser Executado |
| AceBlo | Number(001,0) | Sim | Tipo de Operação |
| AceLis | Number(002,0) | Sim | Tipo de Lista |
| AceCol | Number(001,0) | Sim | Coletas do Coletor |
| ProAOn | Number(002,0) | Sim | Tipo de Processo On-Line |
| ProAOf | Number(001,0) | Sim | Tipo de Processo Off-Line |
| NivPri | Number(001,0) | Sim | Nível de Prioridade do Processo |
| DirSai | Number(001,0) | Sim | Direção da Saída do Resultado da Execução do Processo |
| NomImp | String(255) | Sim | Nome da Impressora |
| CodReg | Number(003,0) | Sim | Código da Regra a ser Executada |
| DInExe | Date | Sim | Data do Início da Execução do Processo |
| HInExe | Number(005,0) | Sim | Hora do Início da Execução do Processo |
| StaPro | Number(001,0) | Sim | Status do Processo |
| LisOff | Number(002,0) | Sim | Lista do Off-Line |
| ColOff | Number(001,0) | Sim | Tipo de Coleta Off-Line |
| RmtEma | String(250) | Sim | Endereco Eletrônico do Remetente |
| DstEma | String(250) | Sim | Destinatários do E-mail |
| CcPEma | String(250) | Sim | Destinatários da Cópia do E-mail |
| CcOEma | String(250) | Sim | Destinatários da Cópia Oculta do E-mail |
| AssEma | String(250) | Sim | Assunto do E-mail |
| AnxEma | String(250) | Sim | Caminho dos Arquivos Anexos do E-mail (Arquivos Atachados) |
| TxtEma | String(1500) | Sim | Texto do E-mail |
| CmdSql | String(254) | Sim | Comandos SQL do Banco |
| StoPrc | String(030) | Sim | Nome da Stored Procedure a ser Disparada |
| StaPat | String(001) | Sim | Status do Registro  (I/A/E) |
| SigSis | String(003) | Sim | Sigla do Sistema Proprietário do Processo |
| QtdCre | Number(001,0) | Sim | Qtde Créditos Padrão para Geração da Lista Contadora |
| GerLog | String(001) | Sim | Gera Mensagem de Aviso |
| DesPat | String(001) | Sim | Processo pode ser Desativado pelo Sistema |
| EmaRes | String(050) | Sim | E-mail do Responsável pelo Processo |
| CfgReg | Number(005,0) | Sim | Configuração Regional do Processo |
| AceArq | String(100) | Sim | Arquivo que Contém a Lista |
| LisOnl | Number(002,0) | Sim | Codigo da Lista On-Line para Gerar |
| QtdRec | Number(001,0) | Sim | Qtde Dias Para Recalcular Antes do Último dia Processado |
| QtdDes | Number(001,0) | Sim | Qtde de Dias Desconsiderar antes do Dia Atual. |
| EmaRlv | String(001) | Sim | Envia e-mail aos destinatários mesmo que o relatório não tenha informações a listar |
| TipLog | Number(001,0) | Sim | Tipo Geração Log |
| LimBak | Number(003,0) | Sim | Manter Últimos x Dias Informações dos Comandos de Acesso |
| AssCsc | Number(002,0) | Sim | Assuntos agrupados dos campos de pendêcncias smart card |
| AgrCmd | String(001) | Sim |  |
| TimOut | Number(002,0) | Sim | Time Out Comando |
| NotUsu | String(001) | Sim | Notificar por e-mail em caso de erro do comando |
| CodAge | Number(009,0) | Sim | Código Processo Agendador |
| TipPrv | String(001) | Sim | Tipo de Provisão |
| RegAju | Number(003,0) | Sim | Regra Ajuste |
| TipCal | Number(002,0) | Sim | Tipo de Cálculo |
| ConTab | Number(001,0) | Sim | Tipo de Contabilização |
| NumDoc | String(015) | Sim | Número do Documento |
| ConSol | String(001) | Sim | Consolidar |
| NivTot | Number(001,0) | Sim | Nível de Totais |
| TotClc | String(001) | Sim | Totalizar CLC´s |
| CodTcl | Number(004,0) | Sim | Tipo de CLC |
| CodIdm | Number(003,0) | Sim | Código da Tabela de Índices |
| DiaCnv | Number(002,0) | Sim | Dia da Conversão |
| DirTxt | String(050) | Sim | Diretório do Arquivo Texto |
| NomMod | String(030) | Sim | Modelo |
| NomTxt | String(035) | Sim | Nome Arquivo Texto |
| LisCfi | String(001) | Sim | Listar Conta Financeira |
| CtbCal | Number(002,0) | Sim | Tipo do Cálculo |
| TipPav | Number(001,0) | Sim | Tipo de Pessoa |
| DiAnPg | Number(002,0) | Sim | Dias de antecedência para a verificação da programação de férias |
| DiAnEf | Number(002,0) | Sim | Dias de antecedência para a efetivação da programação de férias |
| Pag13s | String(001) | Sim | Paga 13° Salário |
| DiaAbo | Number(002,0) | Sim | Dias de abono na programação de férias |
| NomUsu | String(255) | Sim | Nome Usuário |
| SenUsu | String(255) | Sim | Senha Usuário |
| TipImp | String(001) | Sim | Tipo Importação |
| TabImp | String(020) | Sim | Tabela Importação |
| LmpHis | String(001) | Sim | Efetuar limpeza por histórico |
| LngCod | String(005) | Sim | Código do Idioma |
| ExeGpo | String(001) | Sim | Executado pelo Módulo Gestão de Ponto |
| DiaAlt | String(001) | Sim | Somente dias alterados após apuração |
| ReaMar | String(001) | Sim | Realocar Marcações |
| DesAce | String(001) | Sim | Desfazer Acertos |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| NumSec | Number(014,0) | Sim | Número interno |
| TipMob | Number(001,0) | Sim | Tipo de Ação da Mobilidade |
| LeiAut | String(001) | Sim | Leitura Automática das Marcações |
| STRGE1 | String(255) | Sim | Informação Genérica |
| ConDeM | String(001) | Sim | Considerar colaboradores demitidos no mês |
| IntPla | String(001) | Sim | Mobilidade integrado com plataforma Senior X |
| FusApu | String(001) | Sim | Utilizar fusos do Histórico de Apuração |
| FusCpo | String(001) | Sim | Integrar fuso horário |
| RotSis | Number(001,0) | Sim | Rotina a ser executada quando o tipo do processo for 'Rotinas do Sistema'. |

---

## Chave Primária

- TipPat
- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
