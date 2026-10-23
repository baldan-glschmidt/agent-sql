# R350PDE

## Descrição

S-2299 - eSocial - Informações do dependente do Plano de Saúde

---

## Resumo

- Campos: 15
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqDes | Number(009,0) | Não | Sequência |
| SeqRec | Number(009,0) | Não | Sequência |
| SeqDlt | Number(009,0) | Não | Sequência |
| SeqSau | Number(009,0) | Não | Sequência |
| SeqPde | Number(009,0) | Não | Sequência |
| TipDep | Number(002,0) | Sim | Tipo de Dependente eSocial |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| NomDep | String(070) | Sim | Nome do Dependente |
| DatNas | Date | Sim | Data Nascto Dependente |
| ValDep | Number(014,2) | Sim | Valor pago ao plano de saúde do dependente |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqDes
- SeqRec
- SeqDlt
- SeqSau
- SeqPde

---

## Índices

### R350PDEIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
