# R108HOR

## Descrição

Atendentes - Horário de Atendimento

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAte | Number(006,0) | Não | Código Atendente |
| DatIni | Date | Não | Data Inicial para um período de atendimento |
| DiaSem | Number(001,0) | Não | Dia da Semana |
| HorIni | Number(005,0) | Não | Hora inicial para atendimento |
| HorFim | Number(005,0) | Sim | Hora de término para atendimento |
| AreAte | Number(004,0) | Sim | Área Médica(0-Representa todas as áreas) |
| DurAte | Number(003,0) | Sim | Duração do atendimento em Minutos |

---

## Chave Primária

- CodAte
- DatIni
- HorIni
- DiaSem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R108HOR_000

**Tabela:** R108TAT

| Origem | Destino |
|--------|---------|
| CodAte | CodAte |

