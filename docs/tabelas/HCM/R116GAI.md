# R116GAI

## Descrição

Grupos de Avaliação - Itens de avaliação

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
| CodGav | Number(003,0) | Não | Código do Grupo de Avaliação |
| CodIta | Number(006,0) | Não | Código Item Avaliação |
| ResIta | String(050) | Sim | Resposta Item Avaliação |

---

## Chave Primária

- EstCar
- CodGav
- CodIta

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R116GAI_001

**Tabela:** R116GAV

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodGav | CodGav |

### IR_R116GAI_002

**Tabela:** R116ITA

| Origem | Destino |
|--------|---------|
| CodIta | CodIta |

