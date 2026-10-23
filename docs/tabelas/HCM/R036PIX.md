# R036PIX

## Descrição

Pix - (Pensão Judicial)

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
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodDep | Number(002,0) | Não | Código do Dependente |
| DatAlt | Date | Não | Data de Alteração |
| SeqCon | Number(002,0) | Não | Sequência |
| PerCon | Number(005,2) | Sim | Percentual Conta |
| TpcPix | Number(002,0) | Sim | Tipo de Chave Pix - Pagamento Instantâneo |
| ChvPix | String(100) | Sim | Chave Pix - Pagamento Instantâneo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep
- DatAlt
- SeqCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
