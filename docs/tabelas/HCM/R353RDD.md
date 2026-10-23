# R353RDD

## Descrição

eSocial - perAnt - Detalhamento reembolso dependente do plano saúde empresarial

---

## Resumo

- Campos: 12
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
| SeqRps | Number(009,0) | Não | Sequência |
| CpfDep | Number(011,0) | Não | Número de inscrição no CPF do dependente |
| SeqRdd | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição do prestador de serviços |
| NumIns | Number(014,0) | Sim | Número de inscrição do prestador de serviços de assistência médica |
| CfjIns | String(014) | Sim | Número de inscrição do prestador de serviços de assistência médica |
| VlReAt | Number(014,2) | Sim | Valor do reembolso relativo ao período indicado em perApur |
| VlReAn | Number(014,2) | Sim | Valor do reembolso relativo a anos anteriores |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqRps
- CpfDep
- SeqRdd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
