# R400LOG

## Descrição

Log da Replicação

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DtHLog | Number(014,6) | Não | Data/Hora do Log da Replicação |
| TipLoR | String(001) | Sim | Tipo de Log da Replicação (Aviso ou Erro) |
| UsuBan | String(020) | Sim | Nome do Usuário do Banco Para o Qual Foi Gerado o Log |
| SerBan | String(020) | Sim | Serviço do Banco Para o Qual Foi Gerado o Log |
| MsgLog | String(500) | Sim | Mensagem do Log da Replicação |

---

## Chave Primária

- DtHLog

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
