# R104BCA

## Descrição

JR - Base Calendário - Cenário

---

## Resumo

- Campos: 12
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
| CmpCal | Date | Não | Competência de referência do calendário |
| CodClr | Number(003,0) | Sim | Código do calendário de repouso |
| DiaUti | Number(002,0) | Sim | Quantidade de dias úteis |
| DiaDSR | Number(002,0) | Sim | Quantidade de dias DSR |
| PerDia | Number(007,4) | Sim | Percentual entre dias trabalhados e dias de DSR |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen
- EmpAut
- TipCol
- NumCad
- CmpCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104BCA_003

**Tabela:** R104PDC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |

