# R020RLC

## Descrição

Rateio Mão de Obra por Local e Cargo

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Tabela de Organograma |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| EstCar | Number(004,0) | Não | Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| CmpRef | Date | Não | Competência do Rateio |
| RatRmo | Number(009,0) | Não | Código Rateio M.O. |
| ConRat | Number(001,0) | Sim | Considera Rateio |
| PerRmo | Number(005,2) | Sim | % Rateio M.O. |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- EstCar
- CodCar
- CmpRef
- RatRmo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R020RLC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R020RLC_001

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

### IR_R020RLC_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R020RLC_003

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R020RLC_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

