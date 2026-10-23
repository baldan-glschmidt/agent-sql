# R353INF

## Descrição

eSocial - perAnt - Informações Complementares

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
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
| DatLau | Date | Sim | Data da moléstia grave atribuída pelo laudo |
| NumRec | String(040) | Sim | Número do recibo do S-1210 original cujas informações complem. serão alteradas |
| TemDif | Number(001,0) | Sim | Possui diferença no S-1210 já enviado na competência |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
