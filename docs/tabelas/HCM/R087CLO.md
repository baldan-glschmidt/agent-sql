# R087CLO

## Descrição

Cargos x Centro de Custo

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código do Centro de Custo |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| NatDes | Number(003,0) | Sim | Código da Natureza de Despesa |
| IndCon | String(001) | Sim | Quando  possui mais de uma natureza de despesa por CC. |

---

## Chave Primária

- NumEmp
- CodCcu
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R087CLO_001

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R087CLO_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

