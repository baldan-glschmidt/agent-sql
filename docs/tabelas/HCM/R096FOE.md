# R096FOE

## Descrição

Epi - Fornecedores

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
| CodEpi | Number(008,0) | Não | Código do Epi |
| CodOem | Number(008,0) | Não | Código do Fornecedor |

---

## Chave Primária

- CodEpi
- CodOem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R096FOE_000

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

### IR_R096FOE_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

