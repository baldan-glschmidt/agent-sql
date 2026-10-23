# R085ICA

## Descrição

Orçamento - Base Cálculo - Itens

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IteOrc | Number(003,0) | Não | Código do Item |
| SeqIte | Number(002,0) | Não | Sequência Item |
| CodIte | Number(003,0) | Sim | Código do Item |
| SinBas | String(001) | Sim | Sinal Base |

---

## Chave Primária

- IteOrc
- SeqIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085ICA_000

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

### IR_R085ICA_002

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| CodIte | IteOrc |

