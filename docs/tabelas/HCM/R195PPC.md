# R195PPC

## Descrição

Cenário - Eventos Previstos por Posto de Trabalho

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Posto de Trabalho |
| CmpEve | Date | Não | Competência do evento |
| IteOrc | Number(003,0) | Não | Item de orçamento |
| ValEve | Number(011,2) | Sim | Valor do evento |
| ValRat | Number(011,2) | Sim | Valor do evento rateado entre as vagas |

---

## Chave Primária

- NumEmp
- CodCen
- EstPos
- PosTra
- CmpEve
- IteOrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195PPC_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195PPC_003

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

### IR_R195PPC_005

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

