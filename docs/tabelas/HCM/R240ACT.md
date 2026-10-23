# R240ACT

## Descrição

Analytics SeniorX - Acidentes de trabalho

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAct | Date | Não | Data Acidente de Trabalho |
| HorAct | Number(005,0) | Não | Hora Acidente de Trabalho |
| DatCat | Date | Não | Data de registro da  CAT |
| TipCat | Number(001,0) | Não | Tipo CAT |
| DatAfa | Date | Sim | Data de Início do Afastamento |
| TerAfa | Date | Sim | Data de Término Afastamento |
| TipAci | Number(001,0) | Sim | Código do tipo de acidente de trabalho |
| CodUsu | Number(009,0) | Sim | Usuário que realizou a última geração |
| DthAlt | Number(014,6) | Sim | Data/Hora em que foi realizada a última geração |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAct
- HorAct
- DatCat
- TipCat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
