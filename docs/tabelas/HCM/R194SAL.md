# R194SAL

## Descrição

BS - Salários

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| CmpSal | Date | Não | Competência |
| VlrSal | Number(011,4) | Sim | Valor Salário |

---

## Chave Primária

- EstCar
- CodCar
- CmpSal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R194SAL_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

