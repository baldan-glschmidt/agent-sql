# R960PRV

## Descrição

Provedores de serviços

---

## Resumo

- Campos: 27
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PRVID | Number(004,0) | Não | Identificador seqüêncial do provedor de serviços. |
| PRVKND | Number(001,0) | Sim | Tipo do provedor (Enumeração TMCServiceProviderKind) |
| PRVPUB | Number(001,0) | Sim | Provedor publicado para todos os outros provedores de mesma base |
| PRVNAM | String(255) | Sim | Nome do provedor |
| PRVURL | String(255) | Sim | URL do servidor |
| PRVAPP | String(050) | Sim | Nome da aplicação onde estão os serviços |
| PRVDTO | Number(005,0) | Sim | Time out padrão |
| USRNAM | String(255) | Sim | Nome do usuário para execução de serviços |
| USRPWD | String(255) | Sim | Senha do usuário para execução de serviços |
| PRXSRV | String(255) | Sim | Definição do servidor de proxy |
| PRXPRT | Number(009,0) | Sim | Número da porta do proxy |
| PRXUSR | String(255) | Sim | Usuário do proxy |
| PRXPWD | String(100) | Sim | Senha do proxy |
| PRVCTX | String(255) | Sim | Contexto para execução de serviços |
| DISMOD | String(255) | Sim | Módulo(dll) de dispatch da chamada |
| PRVCSP | String(255) | Sim | Serviço e porta para obtenção do catálogo de serviços |
| TipAut | Number(003,0) | Sim | Tipo de Autenticação |
| AttUsr | String(255) | Sim | Atributo do nome do usuário |
| AttPwd | String(255) | Sim | Atributo da senha do usuário |
| NodNom | String(255) | Sim | Nome do nó |
| NamSpc | String(255) | Sim | NameSpace |
| ASNODE | String(001) | Sim | Atributo para definir a estrutura do Header(Node|Param). |
| CTXSEP | String(001) | Sim | Separador de Contexto da Url de serviço |
| ECDATA | String(001) | Sim | Encode CDATA |
| VerEnv | Number(004,0) | Sim | Versão do Envelope |
| TOKHEA | String(255) | Sim | Header referente ao TOKEN |
| TOKVAL | String(255) | Sim | Valor referente ao TOKEN |

---

## Chave Primária

- PRVID

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
