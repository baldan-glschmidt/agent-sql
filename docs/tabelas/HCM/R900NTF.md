# R900NTF

## Descrição

Notificações

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| Ntf_ID | Number(010,0) | Não | ID |
| DatTim | Date | Sim | Data e hora em que a notificação ocorreu |
| NtfSrc | String(025) | Sim | Nome do sistema/programa que gerou a notificação |
| NtfPid | Number(007,0) | Sim | Identificador do processo que gerou a notificação |
| SysUsr | String(100) | Sim | Nome do usuário conectado ao sistema Senior que gerou a notificação |
| AccTyp | String(100) | Sim | Tipo de acesso ao sistema que gerou a notificação |
| Ntf_PC | String(100) | Sim | Nome do computador de onde foi gerada a notificação |
| SOUser | String(100) | Sim | Nome do usuário logado no sistema operacional onde foi gerada a notificação |
| Srv_Id | String(100) | Sim | Id do serviço para notificações |
| Evt_Id | String(100) | Sim | Id do evento que gerou a notificação |
| NtfMsg | String(19999) | Sim | Mensagem destinada ao usuário final que irá ler a notificação |
| NtfDet | String(19999) | Sim | Mensagem técnica atribuída a notificação, mais comum na ocorrência de algum erro |
| NtfTyp | String(100) | Sim | Tipo da notificação |

---

## Chave Primária

- Ntf_ID

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
