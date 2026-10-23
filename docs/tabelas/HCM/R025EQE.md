# R025EQE

## Descrição

Equivalência de Experiência nos Cargos

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| GruEqe | Number(003,0) | Não | Grupo de Equivalência |
| SeqEqe | Number(002,0) | Não | Sequência |
| EstEqe | Number(004,0) | Sim | Código da Estrutura de Cargos Equivalente |
| CarEqe | String(024) | Sim | Código do Cargo Equivalente |
| TpoMin | Number(003,0) | Sim | Tempo Mínimo de Experiência no Cargo (em meses) |
| TpoMax | Number(003,0) | Sim | Tempo Máximo de Experiência no Cargo (em meses) |
| PtsExp | Number(002,0) | Sim | Pontuação da Experiência |

---

## Chave Primária

- EstCar
- CodCar
- GruEqe
- SeqEqe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R025EQE_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R025EQE_004

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstEqe | EstCar |

### IR_R025EQE_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstEqe | EstCar |
| CarEqe | CodCar |

