# R064RAT

## Descrição

Troca de Rateio

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data Inicial da Troca de Rateio |
| HorIni | Number(005,0) | Não | Hora Inicial da Programação de Rateio |
| DatFim | Date | Sim | Data Final da Troca de Rateio |
| HorFim | Number(005,0) | Sim | Hora Final da Programação de Rateio |
| CodRat | Number(009,0) | Sim | Código do Rateio da Troca |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R064RAT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R064RAT_007

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

