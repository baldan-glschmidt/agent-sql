# SAM_PENDENCIES

## Descrição

Tabelas de controle de pendências de replicação G5 -> SAMSenior

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ID_PENDENCY | Number(009,0) | Não | Identificador do registro |
| ROTINE | Number(002,0) | Não | Operação |
| OPERATIONTIME | Date | Não | Data e hora da operação |
| OPERATIONKIND | Number(001,0) | Não | Tipo de Operação |
| STATUS | Number(001,0) | Não | Status da Pendência |
| EXECUTIONRETURN | String(2047) | Sim | Retorno execução |
| EXECUTATIONTIME | Date | Sim | Data e hora da execução |
| NUMBERTRIALS | Number(002,0) | Sim | Número de Tentativas |
| IDREGISTER | String(255) | Sim | Identificador do Registro |
| IDSAM | String(255) | Sim | Identificador do SAMSenior |

---

## Chave Primária

- ID_PENDENCY

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
