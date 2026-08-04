# E000PRA

## Descrição

Cadastros - Processos Automáticos

---

## Resumo

- Campos: 36
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPra | Number(004,0) | Não | Código do processo automático |
| TipPra | Number(002,0) | Não | Tipo do processo automático |
| TipPrc | Number(003,0) | Sim | Tipo de Processo |
| DesPra | String(060) | Não | Descrição do processo |
| DatIni | Date | Não | Data inicial de execução do processo |
| HorIni | Number(005,0) | Sim | Hora inicial de execução do processo |
| DatVal | Date | Sim | Data de validade ou até quando é para executar |
| HoiVal | Number(005,0) | Sim | Hora validade inicial de execução do processo |
| HofVal | Number(005,0) | Sim | Hora validade final de execução do processo |
| DatExe | Date | Sim | Data da última execução |
| HorExe | Number(005,0) | Sim | Hora da última execução |
| PerExe | Number(001,0) | Não | Periodicidade de execução |
| IntGer | Number(004,0) | Sim | Intervalo de execução |
| EmpExe | Number(004,0) | Sim | Código da empresa onde o processo será executado |
| FilExe | Number(005,0) | Sim | Código da filial onde o processo será executado |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| SenUsu | String(030) | Sim | Senha do usuário para execução do processo |
| DiaUti | String(001) | Não | Indica se é para executar somente em dias úteis |
| ProPre | Number(004,0) | Sim | Código do processo sucessor a este |
| RenArq | Number(001,0) | Sim | Indica a ação a ser tomada sobre o arquivo |
| ArqEnt | String(100) | Sim | Nome do arquivo de entrada |
| ArqSai | String(100) | Sim | Nome do arquivo de saída |
| ArqMod | String(100) | Sim | Nome do arquivo do modelo |
| DirSai | String(100) | Sim | Nome do diretório de saída |
| ImpFax | String(255) | Sim | Nome da impressora ou fax |
| CodReg | Number(003,0) | Sim | Código da regra |
| RmtMsg | String(255) | Sim | Nome do remetente para a mensagem |
| DstMsg | String(255) | Sim | Nome do destinatário para a mensagem |
| CcpMsg | String(255) | Sim | Nome do destinatário para a cópia da mensagem |
| AssMsg | String(255) | Sim | Descrição do assunto para a mensagem |
| AnxMsg | String(255) | Sim | Anexos da mensagem |
| TxtMs1 | String(999) | Sim | Texto para a mensagem |
| CmdSql | String(999) | Sim | Comandos SQL |
| StoPrc | String(050) | Sim | Nome da stored procedure a ser executada |
| StsPro | String(001) | Não | Status do Processo |
| SitExe | Number(001,0) | Sim | Situação da execução do processo |

---

## Chave Primária

- CodPra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
