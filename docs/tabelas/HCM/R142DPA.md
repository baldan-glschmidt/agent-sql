# R142DPA

## Descrição

Diagnósticos Treinamento - Participantes

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDia | Number(009,0) | Não | Codigo Diagnostico |
| NumEmp | Number(004,0) | Não | Código da Empresa do Participante |
| TipCol | Number(001,0) | Não | Tipo Participante |
| NumCad | Number(009,0) | Não | Cadastro do Participante |
| CodCua | Number(009,0) | Não | Código do Curso de  Aperfeiçoamento |
| CmpCua | Date | Não | Competência Curso |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CodPar | Number(003,0) | Sim | Código Parecer |
| SeqTre | Number(002,0) | Sim | Sequência da Reserva |

---

## Chave Primária

- CodDia
- NumEmp
- TipCol
- NumCad
- CodCua
- CmpCua
- CodOem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R142DPA_000

**Tabela:** R142DIA

| Origem | Destino |
|--------|---------|
| CodDia | CodDia |

### IR_R142DPA_003

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R142DPA_004

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R142DPA_006

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

### IR_R142DPA_007

**Tabela:** R106PAR

| Origem | Destino |
|--------|---------|
| CodPar | CodPar |

