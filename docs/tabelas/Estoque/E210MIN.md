# E210MIN

## Descrição

Estoques - Quantidades Mínimas para Reposição

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto em estoque |
| CodDer | String(007) | Não | Código da derivação do produto em estoque |
| CodDep | String(010) | Não | Código do depósito |
| QtdMin | Number(014,5) | Sim | Quantidade  mínima em estoque para análise de reposição |
| QtdAcu | Number(014,5) | Sim | Quantidade já acumulada para análise de reposição |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
