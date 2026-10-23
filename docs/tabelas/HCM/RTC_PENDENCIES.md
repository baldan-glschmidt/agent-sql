# RTC_PENDENCIES

## Descrição

Tabela de pendências de replicação

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ID | Number(010,0) | Não | Identificador único da pendência |
| TABLENAME | String(030) | Não | Nome da tabela replicada |
| OPERATIONTIME | Date | Não | Data e hora da operação |
| OPERATIONKIND | String(003) | Não | Tipo de operação. Inclusão, alteração ou exclusão |
| RECORDKEY | String(1499) | Sim | Chave do registro alterado |
| ALTEREDFIELDS | String(3999) | Sim | Campos alterados em atualização de registro |

---

## Chave Primária

- ID

---

## Índices

### RTC_PENDENCIESINDICE_1

**Tipo:** Não unico

Campos:
- TABLENAME
- OPERATIONTIME

---

## Relacionamentos

Nenhum relacionamento cadastrado.
