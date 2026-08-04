# E075EQI

## Descrição

Cadastros - Produtos - Equivalentes

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto base |
| CodDer | String(007) | Não | Código da derivação base |
| ProEqi | String(014) | Não | Código do produto equivalente |
| DerEqi | String(007) | Não | Código da derivação do produto equivalente |
| ConPr1 | Number(012,6) | Sim | Índice de Concentração do produto base em relação ao produto equivalente |
| ConPr2 | Number(012,6) | Sim | Índice de Concentração do produto equivalente em relação ao produto titular |
| USU_indven | String(001) | Sim | Usa Vendas |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- ProEqi
- DerEqi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
