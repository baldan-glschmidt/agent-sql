# R195RLC

## Descrição

Cenário - Eventos Realizados por Local e Cargo

---

## Resumo

- Campos: 10
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CmpEve | Date | Não | Competência do Evento |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Novo Local |
| NumLoc | Number(009,0) | Não | Novo Local do Organograma |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| TipVag | Number(002,0) | Não | Código do tipo de vaga |
| IteOrc | Number(003,0) | Não | Item de orçamento |
| ValEve | Number(011,2) | Sim | Valor do Evento |

---

## Chave Primária

- NumEmp
- CodCen
- CmpEve
- TabOrg
- NumLoc
- EstCar
- CodCar
- TipVag
- IteOrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195RLC_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195RLC_003

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

### IR_R195RLC_004

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R195RLC_006

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R195RLC_008

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

