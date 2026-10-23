# R078TCA

## Descrição

Times - Cargos - OBSOLETA

---

## Resumo

- Campos: 15
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTim | String(008) | Não | Código do Time |
| DatCar | Date | Não | Data da Última Revisão das Carreira de Cargos |
| SeqCar | Number(003,0) | Não | Sequência do Cargo |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| PerPft | Number(005,2) | Sim | % Performance do Time |
| PerPfc | Number(005,2) | Sim | % Performance da Carreira |
| PerExt | Number(005,2) | Sim | % Excelência do Time |
| PerExc | Number(005,2) | Sim | % Excelência da Carreira |
| PerApt | Number(005,2) | Sim | % Aperfeiçoamento do Time |
| PerApc | Number(005,2) | Sim | % Aperfeiçoamento da Carreira |
| PerFot | Number(005,2) | Sim | % Formação do Time |
| PerFoc | Number(005,2) | Sim | % Formação da Carreira |
| PerDot | Number(005,2) | Sim | % Domínio do Time |
| PerDoc | Number(005,2) | Sim | % Domínio da Carreira |

---

## Chave Primária

- CodTim
- DatCar
- SeqCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R078TCA_000

**Tabela:** R078TIM

| Origem | Destino |
|--------|---------|
| CodTim | CodTim |

### IR_R078TCA_003

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R078TCA_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

