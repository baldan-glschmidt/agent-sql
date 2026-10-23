# R206QCA

## Descrição

PLR Paquetá - Quesitos p/ Cargo

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| CmpRef | Date | Não | Competência de Referência |
| CodQst | Number(004,0) | Não | Código do Quesito |
| PesQst | Number(005,2) | Sim | Peso do Quesito |

---

## Chave Primária

- NumEmp
- EstCar
- CodCar
- CmpRef
- CodQst

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R206QCA_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R206QCA_002

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R206QCA_004

**Tabela:** R206QST

| Origem | Destino |
|--------|---------|
| CodQst | CodQst |

