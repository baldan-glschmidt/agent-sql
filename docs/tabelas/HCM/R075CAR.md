# R075CAR

## Descrição

Carreira - Sequência de Cargos

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCrr | Number(003,0) | Não | Código da Carreira |
| SeqCrr | Number(003,0) | Não | Sequência do Cargo na Carreira |
| CodCar | String(024) | Sim | Código do Cargo |
| MesPmn | Number(003,0) | Sim | Meses de Permanência no Cargo |
| PerCnc | Number(005,2) | Sim | Mínimo de % de Conhecimento para o cargo |
| PerPer | Number(005,2) | Sim | Mínimo de % de Performance para o cargo |
| PerFor | Number(005,2) | Sim | Mínimo de % de Formação para o cargo |
| PerApf | Number(005,2) | Sim | Mínimo de % de Aperfeiçoamento para o cargo |
| PerExc | Number(005,2) | Sim | Mínimo de % de Excelência para o cargo |
| PerDom | Number(005,2) | Sim | % Domínio |
| PerFin | Number(005,2) | Sim | Mínimo de % Final para o cargo |

---

## Chave Primária

- EstCar
- CodCrr
- SeqCrr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R075CAR_001

**Tabela:** R075CRR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCrr | CodCrr |

### IR_R075CAR_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

