# R112GRI

## Descrição

Grupos de Questionário - Itens - Obsoleta

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número Empresa |
| CodGrq | Number(003,0) | Não | Código Grupo Questionário |
| CodItq | Number(003,0) | Não | Código Item Questionário |
| SeqItq | Number(003,0) | Sim | Sequência da pergunta |

---

## Chave Primária

- NumEmp
- CodGrq
- CodItq

---

## Índices

### R112GRIIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodGrq
- SeqItq
- CodItq

---

## Relacionamentos

### IR_R112GRI_001

**Tabela:** R112GRU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodGrq | CodGrq |

### IR_R112GRI_002

**Tabela:** R112ITE

| Origem | Destino |
|--------|---------|
| CodItq | CodItq |

