# R067RLP

## Descrição

Resumo de log de processo

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodReq | String(021) | Não | Código da Requisição Multicamada |
| TipPrc | Number(003,0) | Não | Tipo do Processamento |
| MsgLog | String(300) | Sim | Mensagem do Log |
| DtHIni | Date | Não | Data hora inicial |
| DtHFim | Date | Não | Data hora término |
| QtdProc | Number(007,0) | Sim | Quantidade processado |
| QtdTot | Number(007,0) | Sim | Quantidade total de processado |
| QtdErr | Number(007,0) | Sim | Quantidade processados com erros |
| QtdOk | Number(007,0) | Sim | Quantidade processados com sucesso |
| PrDhTe | Date | Não | Previsão data hora término |
| DatMsg | Date | Sim | Data da última mensagem |
| CodUsu | Number(010,0) | Sim | Código do Usuário do Processamento |
| UndLog | String(040) | Sim | Unidade do Log |
| QtdNPr | Number(007,0) | Sim | Quantidade de não processados |
| UsuCan | Number(010,0) | Sim | Usuário que cancelou processo |
| DatCan | Date | Sim | Data do cancelamento |

---

## Chave Primária

- CodReq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
