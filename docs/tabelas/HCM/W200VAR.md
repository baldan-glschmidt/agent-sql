# W200VAR

## Descrição

Tabela para manutenção de histórico de variáveis públicas relacionadas ao processo

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PRCIID | Number(010,0) | Não | Identificador da instância do processo de workflow |
| VARGRP | String(255) | Não | Grupo da variável |
| VARCOD | Number(008,0) | Não | Código da variável |
| VARNAM | String(255) | Sim | Nome da variável |
| VARTYP | Number(003,0) | Sim | Tipo da variável |
| VARVAL | String(1024) | Sim | Valor da variável |

---

## Chave Primária

- PRCIID
- VARCOD

---

## Índices

### W200VARVARNAM

**Tipo:** Não unico

Campos:
- VARNAM

---

## Relacionamentos

Nenhum relacionamento cadastrado.
