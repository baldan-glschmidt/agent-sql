# R020EXC

## Descrição

Rateio MO C.Custo - Exceções

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CmpRef | Date | Não | Competência do Rateio |
| TabEve | Number(003,0) | Não | Código Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do evento |
| CodRat | Number(009,0) | Não | Código do rateio |
| PerRat | Number(005,2) | Sim | % Rateio |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpRef
- TabEve
- CodEve
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R020EXC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R020EXC_005

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

### IR_R020EXC_006

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

