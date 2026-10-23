# R195PCC

## Descrição

Cenário - Eventos Previstos por Centro de Custo e Cargo

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CmpEve | Date | Não | Competência do Evento |
| CodCcu | String(018) | Não | Código do Centro de Custo |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| TipVag | Number(002,0) | Não | Código do tipo de vaga |
| IteOrc | Number(003,0) | Não | Item de orçamento |
| ValEve | Number(011,2) | Sim | Valor do Evento |
| ValRat | Number(011,2) | Sim | Valor do evento rateado entre as vagas |

---

## Chave Primária

- NumEmp
- CodCen
- CmpEve
- CodCcu
- EstCar
- CodCar
- TipVag
- IteOrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195PCC_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195PCC_003

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R195PCC_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R195PCC_007

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

