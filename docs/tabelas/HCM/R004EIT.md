# R004EIT

## Descrição

Tabela de Horário eSocial - Intervalo

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| IdeInt | Number(009,0) | Não | Identificador do horário eSocial |
| CmpHor | Date | Não | Competência de alteração |
| SeqHor | Number(003,0) | Não | Sequência |
| TipInt | Number(001,0) | Sim | Tipo de Intervalo da Jornada |
| DurInt | Number(004,0) | Sim | Tempo de duração do intervalo, em minutos |
| IniInt | Number(004,0) | Sim | Hora de início do intervalo |
| FimInt | Number(004,0) | Sim | Hora de termino do intervalo |
| HorEso | String(030) | Sim | Código atribuído pelo empresa para o Horário Contratual |

---

## Chave Primária

- NumEmp
- IdeInt
- CmpHor
- SeqHor

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
