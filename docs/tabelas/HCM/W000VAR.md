# W000VAR

## Descrição

Tabela para a manutenção de variáveis publicas relacionadas a pendências

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PRCIID | Number(010,0) | Não | Identificador da instância do processo de workflow |
| PRCSTP | Number(008,0) | Não | Passo do processo onde a atividade foi executada |
| ACTVID | Number(005,0) | Não | Identificador da atividade que gerou a pendência dona desta delegação |
| VARGRP | String(255) | Não | Grupo da variável |
| VARCOD | Number(008,0) | Não | Código da variável |
| VARVAL | String(1024) | Sim | Valor da variável |
| VARNAM | String(255) | Sim | Nome da variável |
| VARTYP | Number(003,0) | Sim | Tipo da variável |

---

## Chave Primária

- PRCIID
- ACTVID
- PRCSTP
- VARCOD

---

## Índices

### W000VARVARNAM

**Tipo:** Não unico

Campos:
- VARNAM

---

## Relacionamentos

Nenhum relacionamento cadastrado.
