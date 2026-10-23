# R024RIS

## Descrição

Cargos - Revisão descrição - Atividades de risco

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| DatHis | Date | Não | Data da revisão da descrição do Cargo |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodAtv | Number(007,0) | Não | Código da Atividade |

---

## Chave Primária

- EstCar
- CodCar
- DatHis
- NumEmp
- CodAtv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024RIS_002

**Tabela:** R024HDE

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |
| DatHis | DatHis |

