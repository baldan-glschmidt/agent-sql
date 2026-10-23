# R353RPS

## Descrição

eSocial - perAnt - Reembolsos desp. médicas/odontológicas no período de apuração

---

## Resumo

- Campos: 9
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
| SeqRps | Number(009,0) | Não | Sequência |
| IndOri | Number(001,0) | Sim | Indicativo da origem do reembolso |
| CnpjOp | Number(014,0) | Sim | CNPJ da operadora do plano de saúde |
| CfjIns | String(014) | Sim | CNPJ da operadora de plano privado coletivo empresarial de assistência à saúde |
| RegANS | Number(006,0) | Sim | Registro na Agência Nacional de Saúde |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqRps

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
