# W000TMR

## Descrição

Tabela para manutenção de temporizadores de processos

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PRCIID | Number(010,0) | Não | Identificador da instância do processo de workflow |
| PRCSTP | Number(008,0) | Não | Passo do processo onde a atividade foi executada |
| ELEMID | Number(005,0) | Não | Identificador da atividade que gerou a pendência dona desta delegação |
| TMRTYP | Number(003,0) | Não | Tipo de temporizador |
| EXPDAT | Date | Sim | Data de expiração do temporizador |
| EXPTIM | Number(005,0) | Sim | Tempo de expiração do temporizador |

---

## Chave Primária

- PRCIID
- ELEMID
- PRCSTP
- TMRTYP

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
