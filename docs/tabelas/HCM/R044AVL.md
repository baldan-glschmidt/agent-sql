# R044AVL

## Descrição

Pedido Avulso de Vales

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpPed | Date | Não | Competência |
| LocEnt | Number(004,0) | Não | Local de Entrega |
| TabEve | Number(003,0) | Não | Tabela de Eventos |
| TipVal | Number(004,0) | Não | Tipo de Vale |
| QtdVal | Number(003,0) | Sim | Quantidade de Vales por Bloco |
| VlrVal | Number(011,2) | Sim | Valor Facial |
| QtdBlo | Number(003,0) | Sim | Quantidade de Blocos |

---

## Chave Primária

- NumEmp
- CmpPed
- LocEnt
- TabEve
- TipVal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044AVL_003

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

