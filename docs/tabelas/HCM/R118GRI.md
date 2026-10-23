# R118GRI

## Descrição

Grupos de Questionário - Itens

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodGrq | Number(003,0) | Não | Código Grupo Questionário |
| CodItq | Number(003,0) | Não | Código Item Questionário |
| ResItq | String(050) | Sim | Resposta Item Questionário |
| SeqItq | Number(003,0) | Sim | Sequência da pergunta |

---

## Chave Primária

- EstCar
- CodGrq
- CodItq

---

## Índices

### R118GRIIndice2

**Tipo:** Não unico

Campos:
- EstCar
- CodGrq
- SeqItq
- CodItq

---

## Relacionamentos

### IR_R118GRI_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R118GRI_001

**Tabela:** R118GRQ

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodGrq | CodGrq |

### IR_R118GRI_002

**Tabela:** R118ITQ

| Origem | Destino |
|--------|---------|
| CodItq | CodItq |

