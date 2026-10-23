# R171APR

## Descrição

Professores - Rateios Atividades

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
| SeqApf | Number(005,0) | Não | Sequência da Atividade |
| CodRat | Number(009,0) | Não | Código do Rateio |
| PerRat | Number(005,2) | Sim | Percentual Rateio |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- SeqApf
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R171APR_004

**Tabela:** R171APF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatIni | DatIni |
| SeqApf | SeqApf |

### IR_R171APR_005

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

