# R300LOG

## Descrição

Log dos Processos Automáticos

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DtHLog | Number(014,6) | Não | Data/Hora do Log do Processo Automático |
| TipPat | Number(002,0) | Sim | Tipo do Processo Automático |
| CodPro | Number(003,0) | Sim | Código do Processo Automático |
| TipLoR | String(001) | Sim | Tipo de Log do Processo Automático (Aviso ou Erro) |
| MsgLog | String(4000) | Sim | Mensagem do Log do Processo Automático |

---

## Chave Primária

- DtHLog

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R300LOG_002

**Tabela:** R300PRO

| Origem | Destino |
|--------|---------|
| TipPat | TipPat |
| CodPro | CodPro |

