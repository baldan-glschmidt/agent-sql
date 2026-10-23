# R346DPT

## Descrição

eSocial JR - Processo Trabalhista - Dependentes

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
| CpfDep | Number(011,0) | Não | Número do CPF do dependente |
| TipDep | Number(002,0) | Sim | Tipo de dependente no eSocial |
| DesDep | String(030) | Sim | Descrição da dependência quando informado tipo 99 - Agregado/Outros |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- CpfDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
