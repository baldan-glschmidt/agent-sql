# R096GEP

## Descrição

Grupo EPI´s Equivalentes - EPI´s

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GruEpi | Number(004,0) | Não | Código do grupo de EPI´s equivalentes |
| CodEpi | Number(008,0) | Não | Código do EPI equivalente |

---

## Chave Primária

- GruEpi
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R096GEP_000

**Tabela:** R096GRU

| Origem | Destino |
|--------|---------|
| GruEpi | GruEpi |

### IR_R096GEP_001

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

