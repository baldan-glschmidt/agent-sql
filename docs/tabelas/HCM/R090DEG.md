# R090DEG

## Descrição

Distribuição Epi para Grupos de Visitante

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatEnt | Date | Não | Data da Entrega |
| HorEnt | Number(005,0) | Não | Hora de Entrada |
| SeqEnt | Number(002,0) | Não | Sequência do Registro |
| GruVis | Number(003,0) | Não | Código do Grupo de Visitantes |
| SeqVis | Number(003,0) | Não | Sequência do Visitante Segundo o Grupo |
| CodEpi | Number(008,0) | Não | Código do Epi |
| MedEpi | String(003) | Sim | Medida do Epi |
| QtdEnt | Number(003,0) | Sim | Quantidade da Entrega |
| DatDev | Date | Sim | Data da Devolução do Epi |
| HorDev | Number(005,0) | Sim | Hora da Devolução do Epi |
| QtdDev | Number(003,0) | Sim | Quantidade da Devolução |

---

## Chave Primária

- DatEnt
- HorEnt
- SeqEnt
- GruVis
- SeqVis
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090DEG_002

**Tabela:** R090MGV

| Origem | Destino |
|--------|---------|
| DatEnt | DatEnt |
| HorEnt | HorEnt |
| SeqEnt | SeqEnt |

### IR_R090DEG_003

**Tabela:** R090GRV

| Origem | Destino |
|--------|---------|
| GruVis | GruVis |

### IR_R090DEG_005

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

