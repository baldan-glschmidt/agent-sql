# R118GRQ

## Descrição

Grupos de Questionário

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodGrq | Number(003,0) | Não | Código do Grupo do Questionário |
| DesGrq | String(020) | Sim | Descrição Grupo Questionário |
| OriPre | String(2000) | Sim | Orientações de preenchimento do questionário. |

---

## Chave Primária

- EstCar
- CodGrq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R118GRQ_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

