# R044DIA

## Descrição

Lançamentos - Dias Avulso

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| QtdDia | Number(002,0) | Sim | Quantidade de dias trabalhados |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal
- CodFil
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044DIA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

