# R348CIR

## Descrição

eSocial - Conferência IRRF - Dados Colaborador

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CodFil | Number(006,0) | Não | Código da Filial |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| CatEso | Number(004,0) | Sim | Categoria eSocial do trabalhador |
| NomTra | String(080) | Sim | Nome do trabalhador |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CodFil
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
