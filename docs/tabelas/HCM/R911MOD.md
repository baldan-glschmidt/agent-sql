# R911MOD

## Descrição

Controle de usuário

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumSec | Number(014,0) | Não | Numero interno |
| ModNam | String(030) | Não | Nome do módulo |

---

## Chave Primária

- NumSec
- ModNam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R911MOD_000

**Tabela:** R911SEC

| Origem | Destino |
|--------|---------|
| NumSec | NumSec |

