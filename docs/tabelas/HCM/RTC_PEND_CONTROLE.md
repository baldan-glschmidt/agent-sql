# RTC_PEND_CONTROLE

## Descrição

Tabela controle pendências por integração

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NAME | String(010) | Não | Nome da integração |
| ID | Number(010,0) | Não | Identificador único da pendência |
| STATUS | String(001) | Sim | Status integração. C-Confirmado Sucesso, E-Confirmado Erro, P-Processada Sistema, D-Descartada Sistema |
| MSGRET | String(4000) | Sim | Mensagem de retorno da integração |

---

## Chave Primária

- NAME
- ID

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
