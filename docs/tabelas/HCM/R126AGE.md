# R126AGE

## Descrição

Agenda do Recrutador

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
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
| CodEta | Number(003,0) | Sim | Código da Etapa |
| SitAge | String(001) | Sim | Situção da Etapa Agendada |
| AnoAge | String(500) | Sim | Anotações do Agendamento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAge
- HorAge

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126AGE_005

**Tabela:** R114ETA

| Origem | Destino |
|--------|---------|
| CodEta | CodEta |

