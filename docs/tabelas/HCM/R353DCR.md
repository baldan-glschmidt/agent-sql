# R353DCR

## Descrição

eSocial - perAnt - Dedução do rendimento tributável relativa a dependentes

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| CodRec | Number(006,0) | Não | Código de receita do IRRF sobre rendimentos do trabalho |
| TipRen | Number(002,0) | Não | Tipo de rendimento |
| CpfDep | Number(011,0) | Não | Número de inscrição no CPF |
| VlrDed | Number(014,2) | Sim | Valor da dedução da base de cálculo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- CodRec
- TipRen
- CpfDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
