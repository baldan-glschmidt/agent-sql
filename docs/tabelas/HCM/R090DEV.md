# R090DEV

## Descrição

Distribuição Epi para Visitantes

---

## Resumo

- Campos: 10
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
| TipDoc | Number(001,0) | Não | Tipo do Documento do Visitante |
| NumDoc | String(020) | Não | Número do Documento do Visitante |
| CodEpi | Number(008,0) | Não | Código do Epi |
| MedEpi | String(003) | Sim | Medida do Epi |
| DatDev | Date | Sim | Data da Devolução do Epi |
| HorDev | Number(005,0) | Sim | Hora da Devolução do Epi |
| UtiEpi | String(001) | Sim | Utilizou EPI |

---

## Chave Primária

- DatEnt
- HorEnt
- SeqEnt
- TipDoc
- NumDoc
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090DEV_002

**Tabela:** R090MVI

| Origem | Destino |
|--------|---------|
| DatEnt | DatEnt |
| HorEnt | HorEnt |
| SeqEnt | SeqEnt |

### IR_R090DEV_004

**Tabela:** R090VIS

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

### IR_R090DEV_005

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

