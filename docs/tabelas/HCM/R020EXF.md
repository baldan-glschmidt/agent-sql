# R020EXF

## Descrição

Rateio MO C.Custo - Exceções - Contas Financeiras

---

## Resumo

- Campos: 9
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

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
| CodRat | Number(009,0) | Não | Código do Rateio |
| ConFin | Number(007,0) | Não | Conta Financeira |
| PerFin | Number(005,2) | Sim | % Conta Financeira |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpRef
- TabEve
- CodEve
- CodRat
- ConFin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R020EXF_005

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

### IR_R020EXF_006

**Tabela:** R020EXC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpRef | CmpRef |
| TabEve | TabEve |
| CodEve | CodEve |
| CodRat | CodRat |

