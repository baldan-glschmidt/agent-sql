# R038HEH

## Descrição

Histórico Horário eSocial

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAlt | Date | Não | Data da Alteração da Escala |
| HorSem | Number(010,0) | Sim | Horas Semanais |
| TipJor | Number(002,0) | Sim | Tipo de Jornada |
| HorNot | String(001) | Sim | Jornada semanal possui horário noturno (no todo ou em parte). |
| DesHor | String(999) | Sim | Descrição do tipo de jornada |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
