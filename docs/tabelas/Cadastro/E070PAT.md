# E070PAT

## Descrição

Cadastros - Filiais - Parâmetros Patrimônio

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodTns | String(005) | Sim | Transação de produtos para geração da nota fiscal de saída |
| CodSnf | String(003) | Sim | Código da série da nota fiscal gerada por transferência no patrimônio |
| IndNtc | String(001) | Não | Indica se gera nota fiscal em transferências entre centro de custos |
| IndNtl | String(001) | Não | Indica se gera nota fiscal em transferências entre locais reais |
| IndNtp | String(001) | Não | Indica se gera nota fiscal em transferências entre portadores de bens |
| UniMed | String(003) | Sim | Código da unidade de medida padrão para geração de notas fiscais |
| IndEcc | String(001) | Sim | Indicativo se exige centro de custos no cadastro de bens |
| IndAqn | String(001) | Sim | Indica se permite alterar a quantidade ao gerar bens via N.F.E. |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
