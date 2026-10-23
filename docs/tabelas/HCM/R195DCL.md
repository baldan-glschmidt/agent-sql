# R195DCL

## Descrição

Cenário - Def. Contas p/ Local

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodCen | Number(004,0) | Sim | Código do cenário |
| FilCtb | Number(006,0) | Sim | Filial Contábil |
| OutEmp | Number(004,0) | Sim | Código da Outra Empresa |
| OutTab | Number(004,0) | Sim | Tabela de Organograma |
| OutLoc | Number(009,0) | Sim | Código Outro Local Org. |
| TipCta | String(001) | Sim | Tipos de Contas |
| LocTxt | String(010) | Sim | Local Exp.Arq.Texto |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
