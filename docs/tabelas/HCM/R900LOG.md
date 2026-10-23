# R900LOG

## Descrição

Log - Eventos Registrados

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EVTPOS | Number(010,0) | Não | Posição atual do log |
| EVTNBR | Number(010,0) | Não | Número de eventos registrados |
| EVTIDT | Number(010,0) | Não | Identificador do evento do log |
| EVTTIM | Number(014,6) | Não | Data do log |
| EVTUSR | Number(010,0) | Não | Identificador do usuário |
| EVTDA1 | String(254) | Sim | Objeto de dados 1 de registro de logs |
| EVTDA2 | String(254) | Sim | Objeto de dados 2 de registro de logs |

---

## Chave Primária

- EVTPOS

---

## Índices

### R900LOGINDICE3

**Tipo:** Não unico

Campos:
- EVTTIM
- EVTPOS

---

## Relacionamentos

Nenhum relacionamento cadastrado.
