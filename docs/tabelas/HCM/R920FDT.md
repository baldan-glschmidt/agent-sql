# R920FDT

## Descrição

Formulários X-Window (dados).

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
| XWFID | Number(009,0) | Não | Identificador dos formulários |
| DATSEQ | Number(004,0) | Não | Seqüência de dados dos formulários |
| DAT1 | String(254) | Sim | Objeto de dados 1 de dados dos formulários |
| DAT2 | String(254) | Sim | Objeto de dados 2 dos formulários |

---

## Chave Primária

- XWFID
- DATSEQ

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R920FDT_000

**Tabela:** R920XWF

| Origem | Destino |
|--------|---------|
| XWFID | XWFID |

