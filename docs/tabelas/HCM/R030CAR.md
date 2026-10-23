# R030CAR

## Descrição

Empresa - Histórico de Estruturas de Cargo

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| DatAlt | Date | Não | Data da Alteração da Estrutura de Cargo |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |

---

## Chave Primária

- NumEmp
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030CAR_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R030CAR_002

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

