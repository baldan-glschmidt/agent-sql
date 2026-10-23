# R124HCA

## Descrição

Colaborador - Cargos Pretendidos

---

## Resumo

- Campos: 7
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Candidato |
| NumCad | Number(009,0) | Não | Cadastro do Candidato |
| DatSol | Date | Não | Data da Solicitação |
| CodSol | Number(003,0) | Não | Tipo da Solicitação |
| EstCar | Number(004,0) | Não | Código da Estrutura do Cargo |
| CodCar | String(024) | Não | Código do Cargo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatSol
- CodSol
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124HCA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R124HCA_004

**Tabela:** R114SLC

| Origem | Destino |
|--------|---------|
| CodSol | CodSlc |

### IR_R124HCA_006

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

