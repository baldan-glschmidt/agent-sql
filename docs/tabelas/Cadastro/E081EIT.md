# E081EIT

## Descrição

Tabelas - Exclusões de Itens de Produto

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço |
| DatIni | Date | Não | Data validade inicial da tabela de preço |
| CodPro | String(014) | Não | Código do produto da tabela de preço |
| CodDer | String(007) | Não | Código da derivação da tabela de preço |
| QtdMax | Number(011,2) | Não | Faixa máxima para quantidade de venda válida para o preço |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni
- CodPro
- CodDer
- QtdMax

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
