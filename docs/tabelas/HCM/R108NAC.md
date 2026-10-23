# R108NAC

## Descrição

Registro de Notificação Compulsória - Acidentes

---

## Resumo

- Campos: 11
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAct | Date | Não | Data Acidente de Trabalho |
| HorAct | Number(005,0) | Não | Hora Acidente de Trabalho |
| DatCat | Date | Não | Data de registro da CAT |
| TipCat | Number(001,0) | Não | Tipo CAT |
| IndAgr | Number(001,0) | Sim | Indicação de Agravo |
| DesAgr | String(1000) | Sim | Descrição detalhada da Doença ou Agravo |
| NotEnv | String(001) | Sim | Indica se a notificação compulsória foi enviada |
| DatEnv | Date | Sim | Data em que a notificação compulsória foi enviada |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAct
- HorAct
- DatCat
- TipCat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
