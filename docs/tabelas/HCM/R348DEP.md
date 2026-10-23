# R348DEP

## Descrição

eSocial - Conferência IRRF - Identificação dependentes

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
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
| CpfDep | Number(011,0) | Não | Número de inscrição no CPF |
| DatNas | Date | Sim | Data de Nascimento |
| NomDep | String(070) | Sim | Nome do Dependente |
| DepIRF | String(001) | Sim | Dependente do trabalhador para fins de dedução de seu rendimento tributável pelo Imposto de Renda |
| DepPju | String(001) | Sim | Dependente de Pensão Judicial |
| DepPsa | String(001) | Sim | Dependente de Plano de Saúde |
| DepFam | String(001) | Sim | Dependente de Salário Família |
| TipDep | Number(002,0) | Sim | Tipo de Dependente |
| DesDep | String(100) | Sim | Descrição da Dependência |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- CpfDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
