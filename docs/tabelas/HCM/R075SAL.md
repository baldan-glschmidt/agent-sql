# R075SAL

## Descrição

Carreira - Salários p/ Empresa / Filial

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCrr | Number(003,0) | Não | Código da Carreira |
| CodCar | String(024) | Não | Código do Cargo |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| EstSal | Number(004,0) | Sim | Código da Estrutura Salarial |
| ClaIni | String(005) | Sim | Classe Salarial |
| NivIni | String(005) | Sim | Nível Salarial |
| ClaFim | String(005) | Sim | Classe Final do Cargo |
| NivFim | String(005) | Sim | Nível Final do Cargo |

---

## Chave Primária

- EstCar
- CodCrr
- CodCar
- NumEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R075SAL_001

**Tabela:** R075CRR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCrr | CodCrr |

### IR_R075SAL_002

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R075SAL_004

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R075SAL_005

**Tabela:** R076DES

| Origem | Destino |
|--------|---------|
| EstSal | CodEst |

