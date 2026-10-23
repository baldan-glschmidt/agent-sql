# R901LOG

## Descrição

LGPD - Log de exclusão/anonimização

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatLog | Date | Não | Data de execução da operação de exclusão/anonimização |
| HorLog | Number(005,0) | Não | Hora de execução da operação de exclusão/anonimização |
| SeqLog | Number(006,0) | Não | Sequência do log do processamento |
| CodUsu | Number(010,0) | Sim | Código do usuário que executou processo de exclusão/anonimização |
| StaExe | Number(001,0) | Não | Status de execução do comando de exclusão/anonimização |
| MsgLog | String(300) | Sim | Mensagem do log da execução do comando de exclusão/anonimização |
| ComExe | String(500) | Sim | Comando executado no processo de exclusão/anonimização |
| InfLog | String(500) | Sim | Informações complementares |

---

## Chave Primária

- DatLog
- HorLog
- SeqLog

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
