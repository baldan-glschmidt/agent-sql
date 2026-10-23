# R024BHP

## Descrição

Cargos - Blocos de Habilidades Pessoais

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| DatHab | Date | Não | Data da Última Revisão das Habilidades do Cargo |
| BloHpe | String(004) | Não | Bloco de Habilidades Pessoais do Cargo |

---

## Chave Primária

- EstCar
- CodCar
- DatHab
- BloHpe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024BHP_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R024BHP_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R024BHP_003

**Tabela:** R079BLO

| Origem | Destino |
|--------|---------|
| BloHpe | BloHpe |

