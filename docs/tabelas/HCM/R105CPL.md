# R105CPL

## Descrição

Cadastro de Avaliadores - Cargos Pares

---

## Resumo

- Campos: 10
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GruCar | Number(004,0) | Não | Código do Grupo de Cargos Pares |
| DatIni | Date | Não | Data de início do período do grupo de cargos pares |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da filial |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodTur | Number(001,0) | Não | Código do Turno |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do cargo |
| CodCic | Number(003,0) | Sim | Código do ciclo de avaliação |

---

## Chave Primária

- GruCar
- DatIni
- NumEmp
- CodFil
- TabOrg
- NumLoc
- CodTur
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R105CPL_001

**Tabela:** R105PGU

| Origem | Destino |
|--------|---------|
| GruCar | GruCar |
| DatIni | DatIni |

### IR_R105CPL_005

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R105CPL_008

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

