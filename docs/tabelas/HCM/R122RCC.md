# R122RCC

## Descrição

Candidato - Resultado de Cálculo Cargo - Característica

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| DatSol | Date | Não | Data da solicitação do cálculo do cargo |
| EstCar | Number(004,0) | Não | Código da estrutura de cargos |
| CodCar | String(024) | Não | Código do cargo |
| NumCar | Number(001,0) | Não | Código da característica(1-8) |
| NotCal | Number(007,2) | Sim | Nota da característica |
| PerMin | Number(007,2) | Sim | Define uma nota mínima para esta característica |
| PerMax | Number(007,2) | Sim | Define uma nota máxima para esta característica |
| FatCar | Number(007,2) | Sim | Fator da característica |
| ObsCar | String(1000) | Sim | Observação sobre resultado da característica |

---

## Chave Primária

- NumCan
- DatSol
- EstCar
- CodCar
- NumCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122RCC_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122RCC_003

**Tabela:** R122RGC

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |
| DatSol | DatSol |
| EstCar | EstCar |
| CodCar | CodCar |

