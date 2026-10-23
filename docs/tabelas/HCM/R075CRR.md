# R075CRR

## Descrição

Carreira

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
| CodCrr | Number(003,0) | Não | Código da Carreira |
| DesCrr | String(025) | Sim | Descrição da Carreira |

---

## Chave Primária

- EstCar
- CodCrr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R075CRR_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

