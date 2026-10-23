# R004ESO

## Descrição

Horários - eSocial

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| IdeInt | Number(009,0) | Não | Identificador do horário eSocial |
| CmpHor | Date | Não | Competência de alteração |
| HorEnt | Number(004,0) | Sim | Hora de entrada |
| HorSai | Number(004,0) | Sim | Hora de saída |
| DurJor | Number(004,0) | Sim | Tempo de duração da jornada, em minutos |
| PerFex | String(001) | Sim | Permitir flexibilidade de horário |
| CodHor | Number(004,0) | Sim | Código do Horário |
| IniNot | Number(004,0) | Sim | Início do horário noturno |
| FimNot | Number(004,0) | Sim | Fim do horário noturno |
| HorNot | String(001) | Sim | Jornada semanal possui horário noturno (no todo ou em parte). |
| CodEsc | Number(009,0) | Sim | Código da Escala |
| HorEso | String(030) | Sim | Código atribuído pelo empresa para o Horário Contratual |

---

## Chave Primária

- NumEmp
- IdeInt
- CmpHor

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
