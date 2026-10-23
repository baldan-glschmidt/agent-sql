# R234RHO

## Descrição

Evento - Horários Recorrentes

---

## Resumo

- Campos: 27
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| RecHor | Number(004,0) | Não | Recorrência do Horário |
| HorIni | Number(005,0) | Sim | Hora Inicial do horário |
| HorFim | Number(005,0) | Sim | Hora Final do horário |
| CodSla | Number(004,0) | Sim | Código da Sala de Realização do Curso |
| DesLoc | String(030) | Sim | Descrição do Local do Treinamento |
| CodDis | Number(003,0) | Sim | Disposição da sala para evento |
| PadRec | Number(001,0) | Sim | Padrão para Recorrência |
| PadDia | Number(001,0) | Sim | Padrão para recorrência diária |
| QtdDia | Number(004,0) | Sim | Quantidade de dias para recorrencia |
| QtdSem | Number(004,0) | Sim | Quantidade de semanas para recorrência |
| DiaDom | String(001) | Sim | Domingo para recorrência |
| DiaSeg | String(001) | Sim | Segunda para recorrência |
| DiaTer | String(001) | Sim | Terça para recorrência |
| DiaQua | String(001) | Sim | Quarta para recorrência |
| DiaQui | String(001) | Sim | Quinta para recorrência |
| DiaSex | String(001) | Sim | Sexta para recorrência |
| DiaSab | String(001) | Sim | Sábado para recorrência |
| PadMen | Number(001,0) | Sim | Padrão mensal para recorrência |
| DiaMes | Number(002,0) | Sim | Dia do mês para recorrência |
| OrdMes | Number(001,0) | Sim | Ordem do dia no mês para recorrência |
| TipMes | Number(002,0) | Sim | Tipo do dia no mês para recorrência |
| QtdMes | Number(004,0) | Sim | Quantidade de meses para recorrência |
| IniRec | Date | Sim | Data de início da recorrência |
| PadTer | Number(001,0) | Sim | Padrão para término da recorrência |
| QtdTer | Number(004,0) | Sim | Quantidade ocorrências para término da recorrência |
| DatTer | Date | Sim | Data término recorrência |

---

## Chave Primária

- CodEvn
- RecHor

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234RHO_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

