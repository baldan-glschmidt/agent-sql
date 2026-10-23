# R104BCH

## Descrição

JR - Base Carga Horária - Cenário

---

## Resumo

- Campos: 11
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| DatCen | Date | Não | Data do cenário |
| SeqCen | Number(002,0) | Não | Sequência do cenário |
| EmpAut | Number(004,0) | Não | Empresa do autor |
| TipCol | Number(001,0) | Não | Tipo do colaborador autor |
| NumCad | Number(009,0) | Não | Código do colaborador autor |
| CmpCar | Date | Não | Competência de referência da carga horária |
| HorSem | Number(010,0) | Sim | Quantidade de horas semanais |
| HorMes | Number(010,0) | Sim | Quantidade de horas mensais |
| NotMes | Number(010,0) | Sim | Quantidade de horas noturnas mensais |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen
- EmpAut
- TipCol
- NumCad
- CmpCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104BCH_003

**Tabela:** R104PDC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |

