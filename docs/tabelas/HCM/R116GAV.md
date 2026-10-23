# R116GAV

## Descrição

Grupos de Avaliação

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodGav | Number(003,0) | Não | Código do Grupo de Avaliação |
| DesGav | String(100) | Sim | Descrição Grupo Avaliação |

---

## Chave Primária

- EstCar
- CodGav

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R116GAV_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

