# R024SAL

## Descrição

Cargos - Salários p/ Empresa / Filial

---

## Resumo

- Campos: 14
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| DatAlt | Date | Não | Data da alteração da estrutura salarial por filial |
| CodFil | Number(006,0) | Não | Código da Filial |
| SeqInf | Number(003,0) | Não | Sequência referente as abrangências |
| EstSal | Number(004,0) | Sim | Estrutura salarial |
| ClaIni | String(005) | Sim | Classe/Nível Inicial do Cargo |
| NivIni | String(005) | Sim | Nível inicial |
| ClaFim | String(005) | Sim | Classe/Nível Final do Cargo |
| NivFim | String(005) | Sim | Nível final |
| ClaIns | String(005) | Sim | Classe/Nível Instrução do Cargo |
| NivIns | String(005) | Sim | Nível Final Instrução |
| TipSal | Number(001,0) | Sim | Tipo de Salário |

---

## Chave Primária

- EstCar
- CodCar
- NumEmp
- DatAlt
- CodFil
- SeqInf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024SAL_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R024SAL_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R024SAL_002

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

