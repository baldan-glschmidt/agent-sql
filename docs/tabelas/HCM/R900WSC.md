# R900WSC

## Descrição

Configurações de Webservice

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
| ENABLE | String(001) | Não | Webservice ativo |
| INSUSR | String(001) | Sim | Criar usuário automaticamente |
| GRPID | Number(010,0) | Sim | Grupo para criar novos usuários |
| ENUSRP | String(001) | Sim | Indica se a replicação de usuários está habilitada ou não |
| URSRID | Number(010,0) | Sim | Id do web service que será chamado para a replicação de usuários |

---

## Chave Primária

- ENABLE

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
