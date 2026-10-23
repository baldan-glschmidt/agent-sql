# R005OCO

## Descrição

Esquecimentos/Horas Extras

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatOco | Date | Não | Data Ocorrência |
| HorOco | Number(005,0) | Não | Hora Ocorrência |
| HorTer | Number(005,0) | Sim | Hora Término |
| DesMot | String(100) | Sim | Motivo Ocorrência |
| DesObs | String(249) | Sim | Observação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatOco
- HorOco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
