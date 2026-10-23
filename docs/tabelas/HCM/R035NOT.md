# R035NOT

## Descrição

PPP - Anotações

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatNot | Date | Não | Data Anotação Registro |
| SeqNot | Number(002,0) | Não | Sequência |
| NotFic | String(2500) | Sim | Descrição da Anotação da Ficha |
| SitRPP | Number(001,0) | Sim | Situação do Registro |
| IgnReg | String(001) | Sim | Define se o registro será ignorado na emissão do PPP |
| IndCon | String(001) | Sim | Apresenta se o registro está em conflito com outro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatNot
- SeqNot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
