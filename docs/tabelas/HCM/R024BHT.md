# R024BHT

## Descrição

Cargos - Blocos de Habilidades Técnicas

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
| BloHte | String(004) | Não | Bloco de Habilidades Técnicas do Cargo |

---

## Chave Primária

- EstCar
- CodCar
- DatHab
- BloHte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024BHT_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R024BHT_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R024BHT_003

**Tabela:** R077BLO

| Origem | Destino |
|--------|---------|
| BloHte | BloHte |

