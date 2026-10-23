# W000STP

## Descrição

Tabela de manutenção de passos executados pelo processo

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PRCIID | Number(010,0) | Não | Identificador da instância do processo de workflow |
| PRCSTP | Number(008,0) | Não | Passo do processo onde a atividade foi executada |
| ACTVID | Number(005,0) | Não | Identificador da atividade que gerou a pendência dona desta delegação |
| STATUS | Number(005,0) | Sim | Status do passo do processo |
| STPDAT | Image | Sim | Dados do passo do processo |

---

## Chave Primária

- PRCIID
- ACTVID
- PRCSTP

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
