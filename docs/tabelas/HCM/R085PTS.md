# R085PTS

## Descrição

Param Orç-Salários não tabelados por C.Custo e Cargo

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CmpPer | Date | Não | Competência |
| CodCcu | String(018) | Não | Código do Centro de Custo |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| ValSal | Number(011,2) | Sim | Salário a ser considerado no aumento e redução quadro |
| ValSim | Number(011,2) | Sim | Sal.simulado a ser considerado no aumento/redução quadro |

---

## Chave Primária

- NumEmp
- CodCen
- CmpPer
- CodCcu
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085PTS_003

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R085PTS_004

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R085PTS_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

