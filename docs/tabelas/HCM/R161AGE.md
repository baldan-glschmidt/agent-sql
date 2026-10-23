# R161AGE

## Descrição

Bs - Agenda de Atendimentos

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAtn | Number(003,0) | Não | Código da Atendente |
| DatAge | Date | Não | Data do Agendamento |
| HorAge | Number(005,0) | Não | Hora do Agendamento. |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Empregado |
| ObsAge | String(500) | Sim | Observação |

---

## Chave Primária

- CodAtn
- DatAge
- HorAge

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R161AGE_000

**Tabela:** R161ATN

| Origem | Destino |
|--------|---------|
| CodAtn | CodAtn |

