# E011DEF

## Descrição

Tabelas - Defeitos de Fabricação (Não Conformidade)

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodDft | String(004) | Não | Código do defeito de fabricação do produto (não conformidade) |
| DesDft | String(030) | Não | Descrição do Defeito de fabricação (não conformidade) |
| AbrDft | String(010) | Sim | Abreviatura do Defeito de fabricação (não conformidade) |
| CodOri | String(003) | Sim | Código de origem do produto p/ o defeito |
| SitDft | String(001) | Sim | Situação do defeito |
| USU_DefCau | String(001) | Sim | Defeito ou Causa |

---

## Chave Primária

- CodEmp
- CodDft

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
