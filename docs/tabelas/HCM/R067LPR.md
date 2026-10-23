# R067LPR

## Descrição

Log Processamentos

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipLPr | Number(003,0) | Não | Tipo do Processamento |
| DtHLog | Number(014,6) | Não | Data/Hora do Log do Processamento |
| CnxUsu | Number(005,0) | Não | Número da Conexão do Usuário |
| SeqLog | Number(003,0) | Não | Sequência do Log |
| CodUsu | Number(010,0) | Sim | Código do Usuário do Processamento |
| TipPat | Number(002,0) | Sim | Tipo do Processamento |
| CodPro | Number(003,0) | Sim | Código do Processo |
| MsgLog | String(300) | Sim | Mensagem do Log |
| CodReq | String(021) | Sim | Código da Requisição Multicamada |

---

## Chave Primária

- TipLPr
- DtHLog
- CnxUsu
- SeqLog

---

## Índices

### R067LPRLogConsole

**Tipo:** Não unico

Campos:
- CodUsu
- TipLPr
- CodReq

---

## Relacionamentos

Nenhum relacionamento cadastrado.
