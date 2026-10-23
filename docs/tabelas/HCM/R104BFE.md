# R104BFE

## Descrição

JR - Base Período Aquisitivo - Cenário

---

## Resumo

- Campos: 14
- Chave Primária: 9 campo(s)
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
| IniPer | Date | Não | Data início do período |
| SeqPer | Number(002,0) | Não | Sequência do período aquisitivo |
| FimPer | Date | Sim | Data fim do período |
| MesPfe | Number(002,0) | Sim | Meses do Período Aquisitivo de Férias |
| DiaDir | Number(005,2) | Sim | Dias de direito |
| CmpGoz | Date | Sim | Competência de gozo |
| DiaGoz | Number(005,2) | Sim | Dias de gozo das férias |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen
- EmpAut
- TipCol
- NumCad
- IniPer
- SeqPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104BFE_003

**Tabela:** R104PDC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |

