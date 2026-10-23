# R123EXP

## Descrição

Equivalência de Experiência nos Cargos - Temporária

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código da Requisição |
| GruEqe | Number(003,0) | Não | Grupo de Equivalência |
| SeqEqe | Number(002,0) | Não | Sequência |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| TpoMin | Number(003,0) | Sim | Tempo Mínimo de Experiência no Cargo (em meses) |
| TpoMax | Number(003,0) | Sim | Tempo Máximo de Experiência no Cargo (em meses) |
| IndVal | String(001) | Sim | Define se o requisito deve ser considerado na triagem/seletiva |
| PtsExp | Number(002,0) | Sim | Pontuação da Experiência |

---

## Chave Primária

- CodRqu
- GruEqe
- SeqEqe
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R123EXP_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

