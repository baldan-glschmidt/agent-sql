# R016IDL

## Descrição

Itens Descrição do Local

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
| TabOrg | Number(004,0) | Não | Código da Tabela do Organograma do Local |
| IteDes | Number(002,0) | Não | Código do Item de Descrição do Local |
| NomIte | String(050) | Sim | Nome do Item de Descrição |

---

## Chave Primária

- TabOrg
- IteDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016IDL_000

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

