# R190PRE

## Descrição

Preços Procedimentos Médicos (AMB)

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAmb | Number(008,0) | Não | Código do Procedimento Médico |
| DatAmb | Date | Não | Data de Referência dos Preços |
| HonMed | Number(011,4) | Sim | Honorários Médicos |
| CharUR | String(001) | Sim | UR |
| NroInc | Number(003,0) | Sim | Número de Incidentes |
| CusFil | Number(011,4) | Sim | Custo do Filme |
| CusOpe | Number(011,4) | Sim | Custo Operacional |
| TotCRR | Number(011,4) | Sim | Total C.R.R. |
| CusCir | Number(011,4) | Sim | Custo Cirurgião |
| NroAux | Number(003,0) | Sim | Número de Auxiliares |
| CusAne | Number(011,4) | Sim | Custo Anestesista |

---

## Chave Primária

- CodAmb
- DatAmb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R190PRE_000

**Tabela:** R190AMB

| Origem | Destino |
|--------|---------|
| CodAmb | CodAmb |

