# R101PTA

## Descrição

Ciclos - Tipo de Competência - Peso

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| CodTpC | Number(004,0) | Não | Indica o tipo de competência do peso por ciclo |
| PesTpC | Number(007,4) | Sim | Peso do tipo de competência em relação aos demais do ciclo |

---

## Chave Primária

- CodCic
- CodTpC

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R101PTA_000

**Tabela:** R101CIC

| Origem | Destino |
|--------|---------|
| CodCic | CodCic |

### IR_R101PTA_001

**Tabela:** R577TPC

| Origem | Destino |
|--------|---------|
| CodTpC | CodTpC |

