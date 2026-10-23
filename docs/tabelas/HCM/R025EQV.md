# R025EQV

## Descrição

Equivalência de Cargos

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| EstEqv | Number(004,0) | Não | Código da Estrutura de Cargos Equivalente |
| CarEqv | String(024) | Não | Código do Cargo Equivalente |
| PtsEqv | Number(002,0) | Sim | Pontuação da Equivalência de Cargo |

---

## Chave Primária

- EstCar
- CodCar
- EstEqv
- CarEqv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R025EQV_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R025EQV_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstEqv | EstCar |
| CarEqv | CodCar |

