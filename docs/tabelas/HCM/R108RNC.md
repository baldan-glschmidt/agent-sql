# R108RNC

## Descrição

Registro de Notificação Compulsória - Atendimentos

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
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| DatAte | Date | Não | Data do Atendimento |
| HorAte | Number(005,0) | Não | Hora do Atendimento |
| IndAgr | Number(001,0) | Sim | Indicação de Agravo |
| DesAgr | String(1000) | Sim | Descrição detalhada da Doença ou Agravo |
| NotEnv | String(001) | Sim | Indica se a notificação compulsória foi enviada |
| DatEnv | Date | Sim | Data em que a notificação compulsória foi enviada |

---

## Chave Primária

- NumEmp
- CodFic
- DatAte
- HorAte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
