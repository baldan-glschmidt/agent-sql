# E075PCO

## Descrição

Cadastros - Produtos - Índice de Produtividade e Consumo Médio

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto |
| DatBas | Date | Não | Data base inicial de validade dos índices |
| ProHec | Number(011,2) | Sim | Valor do índice de produtividade (por hectare) |
| UniPro | String(003) | Sim | Unidade de medida de produção da produtividade |
| ConHec | Number(011,2) | Sim | Valor do índice de consumo (por hectare) |
| UniCon | String(003) | Sim | Unidade de medida de consumo médio |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- DatBas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
