# R092DFG

## Descrição

Definições por grupo de usuários - Controle do quadro

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodGrp | Number(010,0) | Não | Código do grupo de usuários |
| VerAdm | Number(001,0) | Sim | Ver Quadro Admissão |
| VerQua | Number(001,0) | Sim | Ver Quadro Transferências |
| UniTem | Number(001,0) | Sim | Indica a unidade de tempo usada para delimitar quando deve-se buscar o saldo |
| IntAnt | Number(003,0) | Sim | Indica quanto tempo antes da data de referência o saldo deve ser exibido |
| IntApo | Number(003,0) | Sim | Indica quanto tempo após a data de referência o saldo deve ser exibido |
| AutQua | String(001) | Sim | Indica se os usuários autorizam movimentações quando não há vagas no quadro |
| CodUsu | Number(009,0) | Sim | Usuário que realizou a última alteração no plano de vagas |
| DthAlt | Number(014,6) | Sim | Data/Hora da última alteração do plano de vagas |
| MsgApr | String(200) | Sim | Mensagem do comunicado aos aprovadores que ainda não trataram as propostas |

---

## Chave Primária

- CodGrp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
