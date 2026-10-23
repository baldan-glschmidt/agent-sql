# R197DCC

## Descrição

Cenário - Def. Contas p/ Centro Custo

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código do C.Custo Contábil |
| CodCen | Number(004,0) | Sim | Código do cenário |
| FilCtb | Number(006,0) | Sim | Filial Contábil |
| OutEmp | Number(004,0) | Sim | Código da Outra Empresa |
| OutCcu | String(018) | Sim | Código Outro C. Custo |
| TipCta | String(001) | Sim | Tipos de Contas (P,O) |
| CcuTxt | String(010) | Sim | Código Texto C.Custo p/ Exportação |

---

## Chave Primária

- NumEmp
- CodCcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
