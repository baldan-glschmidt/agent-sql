# R032PEN

## Descrição

Pagtos Terceiro - Pensão Judicial

---

## Resumo

- Campos: 14
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPte | Date | Não | Competência |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| SeqPte | Number(003,0) | Não | Sequência |
| SeqPen | Number(003,0) | Não | Sequência da Pensão Judicial |
| CodDep | Number(002,0) | Sim | Código do dependente |
| CpfDep | Number(011,0) | Sim | Número de CPF do dependente |
| DatNas | Date | Sim | Data Nascto Dependente |
| VlrPag | Number(014,2) | Sim | Valor da pensão do dependente |
| NomDep | String(060) | Sim | Nome do Dependente |
| TipDep | Number(002,0) | Sim | Tipo do dependente |
| DesDep | String(100) | Sim | Descrição da dependência |

---

## Chave Primária

- NumEmp
- CodFil
- CmpPte
- TipCol
- NumCad
- SeqPte
- SeqPen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
