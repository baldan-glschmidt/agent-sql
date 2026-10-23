# R206CAR

## Descrição

PLR Paquetá - Cargos p/ PLR

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| BasCar | String(001) | Sim | Base de Cálculo |
| QtdSal | Number(004,2) | Sim | Quantidade de Salários Anuais (Se Base for 'S') |

---

## Chave Primária

- NumEmp
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R206CAR_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R206CAR_002

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

