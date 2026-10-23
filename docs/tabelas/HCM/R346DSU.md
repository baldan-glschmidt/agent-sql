# R346DSU

## Descrição

eSocial JR - Informações de Tributos - Detalhamento das deduções com exigibilidade suspensa

---

## Resumo

- Campos: 13
- Chave Primária: 11 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CmpPag | Date | Não | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença |
| CodRec | Number(006,0) | Não | Código de Receita - CR relativo a Imposto de Renda Retido na Fonte |
| NumPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CodSus | Number(014,0) | Não | Código Suspensão |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| IndTde | Number(001,0) | Não | Indicativo do tipo de dedução |
| CodDep | Number(002,0) | Não | Código do Dependente |
| CpfDep | Number(011,0) | Não | Número do CPF do Dependente |
| VlrDsu | Number(015,2) | Sim | Valor da dedução da base de cálculo do imposto de renda com exigibilidade suspensa |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- CmpPag
- CodRec
- NumPro
- CodSus
- IndApu
- IndTde
- CpfDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
