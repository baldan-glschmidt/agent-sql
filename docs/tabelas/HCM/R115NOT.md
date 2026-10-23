# R115NOT

## Descrição

Pendências de Notificação

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodNot | Number(009,0) | Não | Código da pendência de notificação |
| TipNot | Number(002,0) | Sim | Tipo de pendência de notificação |
| StaNot | Number(001,0) | Sim | Status da pendência de notificação |
| DthNot | Number(014,6) | Sim | Data e hora de criação da pendência de notificação |
| DthLim | Number(014,6) | Sim | Data e hora limite de envio da pendência de notificação |
| DthEnv | Number(014,6) | Sim | Data e hora do último envio da pendência de notificação |
| QtdEnv | Number(002,0) | Sim | Quantidade de tentativas de envio da pendência de notificação |
| MsgErr | String(200) | Sim | Mensagem de erro resultante da falha no envio da notificação |
| CodOri | Number(009,0) | Sim | Código de Origem da Notificação |

---

## Chave Primária

- CodNot

---

## Índices

### R115NOTIndice2

**Tipo:** Não unico

Campos:
- CodOri

---

## Relacionamentos

Nenhum relacionamento cadastrado.
