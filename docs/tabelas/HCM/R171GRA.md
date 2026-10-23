# R171GRA

## Descrição

Professores - Grade Diária - Atividade

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodApf | Number(006,0) | Não | Atividade |
| DatIni | Date | Não | Data |
| SeqApf | Number(006,0) | Não | Sequência Atividade |
| CodRat | Number(009,0) | Sim | Rateio |
| HorDia | Number(010,0) | Sim | Quantidade Horas Diárias |
| HorNot | Number(010,0) | Sim | Quantidade Horas Noturnas |
| StaGra | Number(002,0) | Sim | Status |
| DesGra | String(100) | Sim | Descrição |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodApf
- DatIni
- SeqApf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
