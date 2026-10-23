# R320TAB

## Descrição

Cadastro de Integrações via Consulta de Pendências - Tabelas Monitoradas

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ID | String(010) | Não | Identificador único da integração |
| TABELA | String(023) | Não | Tabela monitorada |
| CAMPOSEXC | String(1500) | Sim | Campos exceção |
| FILTRO | String(3999) | Sim | Filtros das tabelas replicadas |

---

## Chave Primária

- ID
- TABELA

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R320TAB_000

**Tabela:** R320INT

| Origem | Destino |
|--------|---------|
| ID | ID |

