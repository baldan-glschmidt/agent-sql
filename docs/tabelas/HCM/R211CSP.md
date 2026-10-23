# R211CSP

## Descrição

Pesquisa - Sequência de Pesquisas do Ciclo

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CicPes | Number(003,0) | Não | Código do ciclo de pesquisas |
| CodPsq | Number(006,0) | Não | Código da Pesquisa |
| SeqPsq | Number(002,0) | Não | Sequência da pesquisa |
| SeqCic | Number(002,0) | Sim | Sequência no Ciclo de Pesquisas |

---

## Chave Primária

- CicPes
- CodPsq
- SeqPsq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R211CSP_000

**Tabela:** R211CIC

| Origem | Destino |
|--------|---------|
| CicPes | CicPes |

### IR_R211CSP_001

**Tabela:** R211PSQ

| Origem | Destino |
|--------|---------|
| CodPsq | CodPsq |

### IR_R211CSP_002

**Tabela:** R211DEF

| Origem | Destino |
|--------|---------|
| CodPsq | CodPsq |
| SeqPsq | SeqPsq |

