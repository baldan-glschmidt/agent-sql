# W000EXP

## Descrição

Tabela para manutenção de expirações de pendências

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PRCIID | Number(010,0) | Não | Identificador da instância do processo de workflow |
| PRCSTP | Number(008,0) | Não | Passo do processo onde a atividade foi executada |
| ACTVID | Number(005,0) | Não | Identificador da atividade que gerou a pendência dona desta delegação |
| EXPSEQ | Number(005,0) | Não | Sequencia da expiração da pendência |
| USUEXP | Number(010,0) | Sim | Usuário da expiração da pendência |
| EXPDAT | Date | Sim | Data atual de expiração da pendência |
| EXPTIM | Number(005,0) | Sim | Tempo da expiração da pendência |
| OLDDAT | Date | Sim | Data anterior de expiração da pendência |
| OLDTIM | Number(005,0) | Sim | Tempo anterior da expiração da pendê |

---

## Chave Primária

- PRCIID
- PRCSTP
- ACTVID
- EXPSEQ

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
