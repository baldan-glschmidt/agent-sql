# R348RTI

## Descrição

eSocial - Conferência IRRF - Tipos Rendimentos, deduções, isenções e retenções

---

## Resumo

- Campos: 14
- Chave Primária: 11 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| DatPag | Date | Não | Data de pagamento |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipVal | Number(004,0) | Não | Tipo de valor relativo ao IRRF |
| TipOri | Number(002,0) | Não | Tipo origem pagamento |
| RenRRA | String(001) | Não | Rendimentos referente RRA |
| ValRen | Number(014,2) | Sim | Valor do rendimento tributável, dedução, isenção e retenção de tributos |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| CodCal | String(100) | Sim | Códigos de cálculo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- DatPag
- CodFil
- CodRat
- TipCol
- NumCad
- TipVal
- TipOri
- RenRRA

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
