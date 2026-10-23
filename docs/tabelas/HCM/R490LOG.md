# R490LOG

## Descrição

Log de conversão de base.

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatLog | Date | Não | Data e Hora do Log |
| SeqLog | Number(009,0) | Não | Sequência |
| LogCtx | String(050) | Não | Contexto |
| MsgLog | String(4000) | Sim | Mensagem de log na atualização de base |

---

## Chave Primária

- DatLog
- SeqLog

---

## Índices

### R490LOGIndice1

**Tipo:** Não unico

Campos:
- LogCtx

---

## Relacionamentos

Nenhum relacionamento cadastrado.
