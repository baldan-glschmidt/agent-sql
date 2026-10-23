# R104BPA

## Descrição

JR - Base Paradigma - Cenário

---

## Resumo

- Campos: 13
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
| DatIni | Date | Não | Data início da comparação como paradigma |
| DatFim | Date | Sim | Data de término da comparação como paradigma |
| EmpPar | Number(004,0) | Sim | Empresa do Paradigma |
| TipPar | Number(001,0) | Sim | Tipo do colaborador paradigma |
| CadPar | Number(009,0) | Sim | Código do colaborador paradigma |
| NomPar | String(040) | Sim | Nome Paradigma |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen
- EmpAut
- TipCol
- NumCad
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104BPA_003

**Tabela:** R104PDC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |

