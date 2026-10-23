# R240ICC

## Descrição

Analytics - Absenteísmo - Horas por colaborador/competência

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CmpRef | Date | Não | Competência de Referência |
| HorMes | Number(010,0) | Sim | Horas de trabalho no mês |
| CodUsu | Number(009,0) | Sim | Usuário que realizou a última geração |
| DthAlt | Number(014,6) | Sim | Data/Hora em que foi realizada a última geração |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
