# R124RCC

## Descrição

Colaborador - Resultado de Cálculo Cargo - Característica

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo de colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
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

- NumEmp
- TipCol
- NumCad
- DatSol
- EstCar
- CodCar
- NumCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124RCC_005

**Tabela:** R124RGC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatSol | DatSol |
| EstCar | EstCar |
| CodCar | CodCar |

