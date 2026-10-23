# R126AGP

## Descrição

Agenda do Recrutador - Participantes

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa do Recrutador |
| TipCol | Number(001,0) | Não | Tipo de Colabolador para Recrutador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador Recrutador |
| DatAge | Date | Não | Data do Agendamento |
| HorAge | Number(005,0) | Não | Hora do Agendamento |
| SeqPar | Number(002,0) | Não | Sequência de Participantes |
| NumCan | Number(007,0) | Sim | Cadastro do Candidato Agendado |
| EmpAge | Number(004,0) | Sim | Código da Empresa |
| TipAge | Number(001,0) | Sim | Tipo do Colabolador Agendado |
| CadAge | Number(009,0) | Sim | Cadastro do Colaborador Agendado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAge
- HorAge
- SeqPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126AGP_004

**Tabela:** R126AGE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatAge | DatAge |
| HorAge | HorAge |

