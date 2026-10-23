# R353DNC

## Descrição

eSocial - perAnt - Dependentes não enviados S-2200/S-2205/S-2300/S-2400/S-2405

---

## Resumo

- Campos: 10
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
| DatNas | Date | Sim | Data de nascimento |
| NomDep | String(070) | Sim | Nome do dependente |
| DepIRF | String(001) | Sim | Dependente para dedução de seu rendimento tributável pelo IRRF |
| TipDep | Number(002,0) | Sim | Tipo de dependente |
| DesDep | String(100) | Sim | Descrição da dependência |

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
