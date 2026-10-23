# R346MCN

## Descrição

eSocial JR - Processo Trabalhista - Mudança de categoria/natureza

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| DatAlt | Date | Não | Data a partir da qual foi reconhecida a nova categoria e/ou a nova natureza da atividade |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| NatAti | Number(001,0) | Sim | Código da natureza da atividade |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
