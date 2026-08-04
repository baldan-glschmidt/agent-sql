# E000AGE

## Descrição

Cadastros - Processos Automáticos

---

## Resumo

- Campos: 39
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPra | Number(004,0) | Não | Código do processo automático |
| DesPra | String(060) | Não | Descrição do processo automático |
| TipPra | Number(002,0) | Não | Tipo do processo automático |
| EstPra | String(001) | Sim | Estado do processo automático em relação ao controle do agendador |
| HoiVal | Number(005,0) | Sim | Hora inicial de validade para execução do processo automático |
| HofVal | Number(005,0) | Sim | Hora final de validade para execução do processo automático |
| DiaUti | String(001) | Não | Indica se o processo deve ser executado somente em dias úteis |
| ProSuc | Number(004,0) | Sim | Código do processo automático que será executado ao término deste |
| EmpExe | Number(004,0) | Sim | Código da empresa onde o processo automático será executado |
| FilExe | Number(005,0) | Sim | Código da filial onde o processo automático será executado |
| CodUsu | Number(010,0) | Sim | Código do usuário responsável pela execução do processo automático |
| SenUsu | String(030) | Sim | Senha do usuário responsável pela execução do processo automático |
| ArqMod | String(100) | Sim | Nome do arquivo do modelo |
| ArqEnt | String(100) | Sim | Nome do arquivo de entrada |
| ArqSai | String(100) | Sim | Nome do arquivo de saída |
| AcaArq | Number(001,0) | Sim | Indica a ação a ser tomada sobre o arquivo |
| AcaErr | Number(001,0) | Sim | Indica a ação a ser tomada sobre o arquivo quando importado com erros (tipos de processo: M) |
| NomImp | String(100) | Sim | Nome da impressora para impressão automática (tipos de processo: R) |
| RotSap | Number(003,0) | Sim | Rotina do Sapiens (tipos de processo: O) |
| ParRot | String(999) | Sim | Parâmetros para execução da rotina do Sapiens (tipos de processo: O) |
| CodReg | Number(003,0) | Sim | Código da regra (tipos de processo: G) |
| RmtMsg | String(100) | Sim | Endereço do remetente da mensagem (tipos de processo: I) |
| DstMsg | String(255) | Sim | Endereço dos destinatários da mensagem (tipos de processo: I) |
| CcpMsg | String(255) | Sim | Endereço dos destinatários de cópia da mensagem (tipos de processo: I) |
| AssMsg | String(255) | Sim | Descrição do assunto da mensagem (tipos de processo: I) |
| AnxMsg | String(999) | Sim | Caminho dos anexos da mensagem (tipos de processo: I) |
| TxtMs1 | String(999) | Sim | Texto da mensagem (tipos de processo: I) |
| CmdSql | String(999) | Sim | Comando SQL a ser executado (tipos de processo: Q) |
| StoPrc | String(050) | Sim | Nome da stored procedure a ser executada (tipos de processo: Q) |
| ArqXsl | String(200) | Sim | Arquivo de transformação XSLT utilizando XML |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| CamMov | String(250) | Sim | Caminho para mover o arquivo na ação de mover arquivo. |
| CamMoe | String(250) | Sim | Caminho para mover o arquivo na ação de mover arquivo em caso de erros. |
| CodIsg | Number(009,0) | Sim | Código do insight de processo automático |

---

## Chave Primária

- CodPra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
