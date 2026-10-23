# R024HDI

## Descrição

Cargos - Revisão descrição - Itens descritos

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código Cargo |
| DatHis | Date | Não | Data da revisão da descrição do Cargo |
| SeqIdc | Number(005,0) | Não | Item de descrição de cargo |
| TexIte | String(5000) | Sim | Descrição detalhada do item do Cargo |

---

## Chave Primária

- EstCar
- CodCar
- DatHis
- SeqIdc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024HDI_002

**Tabela:** R024HDE

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |
| DatHis | DatHis |

### IR_R024HDI_003

**Tabela:** R024IDC

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| SeqIdc | SeqIdc |

