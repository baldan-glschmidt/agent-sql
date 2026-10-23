# R206PLR

## Descrição

PLR Paquetá - PLR Mensal p/ Colaborador

---

## Resumo

- Campos: 15
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colabolador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CmpPlr | Date | Não | Competência do PLR do Colaborador |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| NumCar | Number(004,0) | Sim | Nro de Colaboradores no Local e Cargo |
| NumCol | Number(004,0) | Sim | Nro de Colaboradores no Local |
| QtdAfa | Number(004,0) | Sim | Número de Pessoas Afastadas |
| SomPes | Number(005,2) | Sim | Soma dos Pesos dos Quesitos Atingidos pelo Colaborador |
| ValBas | Number(011,2) | Sim | Valor Base do PLR do Colaborador |
| ValPlr | Number(011,2) | Sim | Valor do PLR Proporcional aos Quesitos Atingidos |
| ValAju | Number(011,2) | Sim | Valor Ajustado do PLR (após proporcionalidade) |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpPlr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R206PLR_005

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R206PLR_007

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

