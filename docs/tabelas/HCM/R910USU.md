# R910USU

## Descrição

Usuários (só para consultas)

---

## Resumo

- Campos: 21
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEnt | Number(010,0) | Não | Código da entidade. |
| NomCom | String(127) | Não | Nome completo do usuário. |
| DesUsu | String(127) | Sim | Descrição do usuário. |
| AltSen | Number(001,0) | Não | 0=Usuário não precisa alterar senha. 1=Usuário precisa alterar senha no próximo logon. |
| ConHab | Number(001,0) | Não | 0=Conta desabilitada. 1=Conta habilitada. |
| ConBlo | Number(001,0) | Não | 0=Conta desbloqueada. 1=Conta bloqueada. |
| DatBlo | Date | Sim | Data em que o usuário foi bloqueado pelo sistema. |
| HorBlo | Number(005,0) | Sim | Hora em que o usuário foi bloqueado pelo sistema. |
| DatSen | Date | Sim | Data em que o usuário definiu a senha atual. |
| HorSen | Number(005,0) | Sim | Hora em que o usuário definiu a senha atual. |
| PolDSe | Number(010,0) | Não | Código da política duração de senhas. |
| PolSAn | Number(010,0) | Não | Código da política de senhas antigas. |
| PolBlq | Number(010,0) | Não | Código da política de bloqueio de conta |
| DatCre | Date | Sim | Data de criação do usuário |
| DatLog | Date | Sim | Data em que o usuário fez o último logon |
| HorLog | Number(005,0) | Sim | Hora em que o usuário fez o último logon |
| DatAlt | Date | Sim | Data da última alteração no usuário |
| HorAlt | Number(005,0) | Sim | Hora da última alteração no usuário |
| DatDes | Date | Sim | Data em que o usuário foi desabilitado |
| HorDes | Number(005,0) | Sim | Hora em que o usuário foi desabilitado |
| SEQREG | Number(015,0) | Sim | Sequência do Registro |

---

## Chave Primária

- CodEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
