# R082EPI

## Descrição

Perigo/Fator de Risco - EPI

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
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| CodEpi | Number(008,0) | Não | Código do Epi |

---

## Chave Primária

- CodAgt
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R082EPI_000

**Tabela:** R082AGT

| Origem | Destino |
|--------|---------|
| CodAgt | CodAgt |

### IR_R082EPI_001

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

