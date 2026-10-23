# W000TMP

## Descrição

Tabela para manutenção de dados temporários na execução de processos

---

## Resumo

- Campos: 5
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
| TMPTYP | Number(003,0) | Não | Tipo de dado temporário |
| TMPDAT | Image | Sim | Dado temporário |

---

## Chave Primária

- PRCIID
- ACTVID
- PRCSTP
- TMPTYP

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
