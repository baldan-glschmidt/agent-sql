# HCM_REQUEST

## Descrição

Tabelas de controle de pendências de replicação HCM -> G5

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ORDEM | Number(010,0) | Não | Identificador da pendência |
| TIPO | Number(003,0) | Sim | Identificador do registro |
| ID | String(032) | Sim | ID do RequestUpdate no HCM |
| STATUS | Number(003,0) | Sim | Status da pendência |
| OPERACAO | String(002) | Sim | Operação a executar na G5 |
| DATA_ALTERACAO | Date | Sim | Data e hora da alteração |
| TENTATIVAS | Number(005,0) | Sim | Quantidade de tentativas de integração |
| ULTIMA_TENTATIVA | Date | Sim | Data e hora da última tentativa |

---

## Chave Primária

- ORDEM

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
