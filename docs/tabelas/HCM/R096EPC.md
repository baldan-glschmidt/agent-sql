# R096EPC

## Descrição

Cursos para Epi

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
| CodEpi | Number(008,0) | Não | Código do EPI |
| CodCua | Number(009,0) | Não | Código do Curso Necessário p/ uso EPI |

---

## Chave Primária

- CodEpi
- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R096EPC_000

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

### IR_R096EPC_001

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

