# R171ARF

## Descrição

Professores - Rateios Atividades - Contas Financeiras

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
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
| ConFin | Number(007,0) | Não | Conta Financeira |
| PerFin | Number(005,2) | Sim | % Conta Financeira |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- SeqApf
- CodRat
- ConFin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R171ARF_004

**Tabela:** R171APF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatIni | DatIni |
| SeqApf | SeqApf |

### IR_R171ARF_005

**Tabela:** R171APR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatIni | DatIni |
| SeqApf | SeqApf |
| CodRat | CodRat |

