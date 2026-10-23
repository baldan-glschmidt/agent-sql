# W000DEL

## Descrição

Tabela para manutenção de delegações de pendências de um processo de workflow

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
| DELSEQ | Number(005,0) | Não | Sequencia de delegação |
| USUDEL | Number(010,0) | Sim | Usuário que efetuou a delegação |
| DELDAT | Date | Sim | Data e hora que ocorreu a delegação |
| DELTIM | Number(005,0) | Sim | Tempo em que ocorreu a delegação |
| USUOLD | Number(010,0) | Sim | Usuário anterior a delegação |
| USUNEW | Number(010,0) | Sim | Usuário responsável pela pendência após a delegação |

---

## Chave Primária

- PRCIID
- PRCSTP
- ACTVID
- DELSEQ

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
