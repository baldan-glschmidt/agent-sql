# R024HDE

## Descrição

Cargos - Revisão descrição

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Cargo que será descrito |
| DatHis | Date | Não | Data da revisão da descrição do Cargo |

---

## Chave Primária

- EstCar
- CodCar
- DatHis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024HDE_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

