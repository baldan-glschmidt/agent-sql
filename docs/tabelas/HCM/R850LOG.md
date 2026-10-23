# R850LOG

## Descrição

Log dos Processos Off Line

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPro | Number(003,0) | Não | Código do Processo Automático |
| DtHLog | Number(014,6) | Sim | Data/Hora do Log do Processo Automático |
| TipLoR | String(001) | Sim | Tipo de Log do Processo Automático (Aviso ou Erro) |
| MsgLog | String(500) | Sim | Mensagem do Log do Processo Automático |

---

## Chave Primária

- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R850LOG_000

**Tabela:** R850POF

| Origem | Destino |
|--------|---------|
| CodPro | CodPoF |

