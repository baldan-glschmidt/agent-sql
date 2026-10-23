# R112IGQ

## Descrição

Grupos de Questionário - Itens

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodGrq | Number(003,0) | Não | Código Grupo Questionário |
| CodItq | Number(003,0) | Não | Código Item Questionário |
| SeqItq | Number(003,0) | Sim | Sequência da pergunta |

---

## Chave Primária

- CodGrq
- CodItq

---

## Índices

### R112IGQIndice2

**Tipo:** Não unico

Campos:
- CodGrq
- SeqItq
- CodItq

---

## Relacionamentos

### IR_R112IGQ_000

**Tabela:** R112GRQ

| Origem | Destino |
|--------|---------|
| CodGrq | CodGrq |

### IR_R112IGQ_001

**Tabela:** R112ITE

| Origem | Destino |
|--------|---------|
| CodItq | CodItq |

