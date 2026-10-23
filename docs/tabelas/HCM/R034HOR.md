# R034HOR

## Descrição

Horário Intermitente

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCon | Number(015,0) | Não | Código da Convocação |
| DatHor | Date | Não | Data do Horário |
| CodHor | Number(004,0) | Não | Código do Horário Base |
| HorDiu | Number(005,0) | Sim | Horas DSR Diurna |
| HorNot | Number(005,0) | Sim | Horas DSR Noturna |
| IndVa1 | Number(001,0) | Sim | Indicativo Intermitente 1 |
| IndVa2 | Number(001,0) | Sim | Indicativo Intermitente 2 |
| CodAux | Number(005,0) | Sim | Código de Cálculo |
| CalPto | Number(005,0) | Sim | Código de Cálculo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCon
- DatHor

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
