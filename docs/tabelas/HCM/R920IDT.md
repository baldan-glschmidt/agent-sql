# R920IDT

## Descrição

Interfaces (dados).

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ITFID | Number(010,0) | Não | Identificador das interfaces |
| DATSEQ | Number(004,0) | Não | Seqüência das interfaces |
| DAT1 | String(254) | Sim | Objeto de dados 1 das interfaces |
| DAT2 | String(254) | Sim | Objeto de dados 2 das interfaces |

---

## Chave Primária

- ITFID
- DATSEQ

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R920IDT_000

**Tabela:** R920ITF

| Origem | Destino |
|--------|---------|
| ITFID | ITFID |

