# R110AGD

## Descrição

Agendamento - Marcações de Horas

---

## Resumo

- Campos: 31
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAte | Number(006,0) | Não | Código do Atendente |
| DatMar | Date | Não | Data Marcada |
| HorMar | Number(005,0) | Não | Hora Marcada |
| SeqAgd | Number(002,0) | Não | Sequência do agendamento |
| HorTer | Number(005,0) | Sim | Hora de término |
| NumEmp | Number(004,0) | Sim | Número da Empresa |
| CodFic | Number(009,0) | Sim | Código Ficha Médica |
| AreAte | Number(004,0) | Sim | Código da Área |
| CodOco | Number(006,0) | Sim | Código Ocorrência |
| CodAgd | Number(003,0) | Sim | Motivo do agendamento |
| ObsAgd | String(2000) | Sim | Observação sobre o agendamento |
| CodUsu | Number(010,0) | Sim | Código do usuário que agendou |
| UsuCan | Number(010,0) | Sim | Código do usuário que cancelou o agendamento |
| IndAgd | Number(001,0) | Sim | Situação do Agendamento |
| DatEnc | Date | Sim | Data Encaminhamento |
| HorEnc | Number(005,0) | Sim | Hora do Encaminhamento |
| SeqEnc | Number(003,0) | Sim | Sequência do Encaminhamento |
| NumGer | Number(009,0) | Sim | Nr. identificação da geração de solicitação |
| DatAte | Date | Sim | Data do Atendimento |
| HorAte | Number(005,0) | Sim | Hora do Atendimento |
| CodMoc | Number(003,0) | Sim | Código do motivo de cancelamento |
| CodPos | Number(007,0) | Sim | Código do posto  de atendimento |
| NumTel | String(020) | Sim | Número do Telefone |
| NumAte | Number(009,0) | Sim | Número do Atestado |
| HorChe | Number(005,0) | Sim | Hora de chegada |
| HorSai | Number(005,0) | Sim | Hora de saída |
| AteAss | String(001) | Sim | Define se o atendimento é assistencial/ocupacional |
| NumRam | String(015) | Sim | Número do Ramal |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |
| FusHor | Number(002,0) | Sim | Fuso Horário |

---

## Chave Primária

- CodAte
- DatMar
- HorMar
- SeqAgd

---

## Índices

### R110AGDIndice2

**Tipo:** Não unico

Campos:
- CodAte
- DatMar
- HorMar
- IndAgd

### R110AGDIndice3

**Tipo:** Não unico

Campos:
- NumEmp
- CodFic
- DatMar
- HorMar

---

## Relacionamentos

### IR_R110AGD_000

**Tabela:** R108TAT

| Origem | Destino |
|--------|---------|
| CodAte | CodAte |

### IR_R110AGD_009

**Tabela:** R110MAG

| Origem | Destino |
|--------|---------|
| CodAgd | CodAgd |

