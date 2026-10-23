# R145COL

## Descrição

LNT - Colaboradores

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatLnt | Date | Não | Data do levantamento de necessidades de treinamento (LNT) |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos considerada no LNT |
| PosTra | String(024) | Sim | Código do posto de trabalho considerado no LNT |
| EstCar | Number(004,0) | Sim | Código da estrutura de cargos considerada no LNT |
| CodCar | String(024) | Sim | Código do cargo considerado no LNT |
| CarLNT | Number(001,0) | Sim | Cargo considerado no levantamento de necessidades de treinamento |
| PosLNT | Number(001,0) | Sim | Posto considerado no levantamento de necessidades de treinamento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatLnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R145COL_006

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R145COL_007

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

