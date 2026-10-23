# R024ITC

## Descrição

Descrição do Cargo

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| SeqIdc | Number(005,0) | Não | Código do Item |
| TexIte | String(5000) | Sim | Texto do Item |

---

## Chave Primária

- EstCar
- CodCar
- SeqIdc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024ITC_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R024ITC_002

**Tabela:** R024IDC

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| SeqIdc | SeqIdc |

