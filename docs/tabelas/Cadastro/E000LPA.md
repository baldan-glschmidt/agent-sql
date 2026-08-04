# E000LPA

## Descrição

Cadastros - Processos Automáticos - Logs

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPra | Number(004,0) | Não | Código do processo automático |
| SeqLog | Number(007,0) | Não | Sequência do log do processo automático |
| TipLor | String(001) | Sim | Tipo do log do processo automático |
| DatIni | Date | Sim | Data inicial da execução do processo automático |
| HorIni | Number(005,0) | Sim | Hora inicial da execução do processo automático |
| DatFim | Date | Sim | Data final da execução do processo automático |
| HorFim | Number(005,0) | Sim | Hora final da execução do processo automático |
| MsgLg1 | String(4999) | Sim | Mensagem do log do processo automático |

---

## Chave Primária

- CodPra
- SeqLog

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E000LPA_000

**Tabela:** E000AGE

| Origem | Destino |
|--------|---------|
| CodPra | CodPra |

