# R234HOR

## Descrição

Evento - Horários do Evento

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| DatIni | Date | Não | Data Inicial do Horário |
| HorIni | Number(005,0) | Não | Hora Inicial do Horário |
| DatFim | Date | Sim | Data Final do Horário |
| HorFim | Number(005,0) | Sim | Hora Final do Horário |
| DesAtv | String(200) | Sim | Descrição da atividade desenvolvida neste horário |
| CodSla | Number(004,0) | Sim | Código da sala onde o evento será realizado |
| DesLoc | String(060) | Sim | Descrição do local do evento |
| CodDis | Number(003,0) | Sim | Disposição da sala para evento |
| RecHor | Number(004,0) | Sim | Recorrência do Horário |
| RecAlt | String(001) | Sim | Gerada por Recorrência e Alterada |
| IdeCom | String(020) | Sim | Identificador do Compromisso |

---

## Chave Primária

- CodEvn
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234HOR_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

