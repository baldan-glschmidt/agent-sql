# R151COL

## Descrição

Vínculo de Colaboradores e Legislação

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro empregado |
| CodLeg | Number(003,0) | Não | Código da legislação alfandegada |
| CodRec | Number(003,0) | Não | Código do recinto alfandegado |
| DatInc | Date | Sim | Data integração BDCC |
| DatIni | Date | Sim | Data de início da vigência |
| HorIni | Number(005,0) | Sim | Hora início da vigência |
| DatFim | Date | Sim | Data fim da vigência |
| HorFim | Number(005,0) | Sim | Hora fim da vigência |
| Status | Number(001,0) | Sim | Status do vínculo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodLeg
- CodRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
