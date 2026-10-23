# R578AVA

## Descrição

Avaliação de Competências - Cadastro

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do Colaborador avaliado |
| TipCol | Number(001,0) | Não | Tipo do Colaborador avaliado |
| NumCad | Number(009,0) | Não | Colaborador avaliado |
| CodCic | Number(003,0) | Não | Indica a qual Ciclo esta Avaliação pertence |
| IdeAva | Number(005,0) | Não | Identificador da avaliação de competências |
| DatRef | Date | Sim | Data de referência da avaliação |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Sim | Posto de Trabalho em que o Colaborador será avaliado |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Cargo em que o Colaborador será avaliado |
| ObsAva | String(8001) | Sim | Observação da avaliação |
| NotAva | Number(008,4) | Sim | Nota da avaliação do colaborador |
| PerAva | Number(007,4) | Sim | Percentual de atingimento da avaliação |
| NumLot | Number(009,0) | Sim | Nr. do lote em que foi gerada a avaliação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- IdeAva

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R578AVA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R578AVA_003

**Tabela:** R101CIC

| Origem | Destino |
|--------|---------|
| CodCic | CodCic |

### IR_R578AVA_009

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

