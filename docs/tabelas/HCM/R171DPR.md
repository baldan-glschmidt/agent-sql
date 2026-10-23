# R171DPR

## Descrição

Professores - Rateios Disciplinas

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatIni | Date | Não | Data de Início da Atividade |
| SeqDpf | Number(005,0) | Não | Sequência da Disciplina |
| CodRat | Number(009,0) | Não | Código do Rateio |
| PerRat | Number(005,2) | Sim | Percentual Rateio |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- SeqDpf
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R171DPR_004

**Tabela:** R171DPF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatIni | DatIni |
| SeqDpf | SeqDpf |

### IR_R171DPR_005

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

