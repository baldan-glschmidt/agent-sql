# R750SSR

## Descrição

Status de serviços escalonados

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
| ReqAgr | String(020) | Não | Identificador da requisição agrupadora |
| SeqReq | Number(003,0) | Não | Sequência da Requisição |
| ReqSrv | String(020) | Sim | Identificador da requisição |
| StaWSE | Number(001,0) | Sim | Status do processo escalonado na instância |

---

## Chave Primária

- SeqReq
- ReqAgr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
