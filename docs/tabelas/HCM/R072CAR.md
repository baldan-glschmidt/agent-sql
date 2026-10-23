# R072CAR

## Descrição

Cargos da Pesquisa por Empresa

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
| CodOem | Number(008,0) | Não | Número da Empresa |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| TitRed | String(030) | Sim | Título Reduzido do Cargo |

---

## Chave Primária

- CodOem
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R072CAR_000

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

