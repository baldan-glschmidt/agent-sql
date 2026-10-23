# RTC_REPLICATIONDEF

## Descrição

Definição das tabelas de replicação

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ID | Number(010,0) | Não | Identificador do registro |
| IDREPLICATOR | String(020) | Não | Identificador do replicador |
| TABLENAME | String(030) | Não | Tabela replicada |
| FILTER | String(3999) | Sim | Filtros das tabelas replicadas |

---

## Chave Primária

- ID

---

## Índices

### RTC_REPLICATIONDEFINDICE1

**Tipo:** Unico

Campos:
- IDREPLICATOR
- TABLENAME

---

## Relacionamentos

Nenhum relacionamento cadastrado.
