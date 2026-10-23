# R126EQV

## Descrição

Requisições - Equivalência de Cargo

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código da Requisição |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| IndVal | String(001) | Sim | Define se o requisito deve ser considerado na triagem/seletiva |
| PtsEqv | Number(002,0) | Sim | Pontuação da Equivalência de Cargo |

---

## Chave Primária

- CodRqu
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126EQV_002

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

