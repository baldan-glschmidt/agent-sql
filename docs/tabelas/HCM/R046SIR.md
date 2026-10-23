# R046SIR

## Descrição

Ficha Financeira c/ Rateio Simulada

---

## Resumo

- Campos: 9
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
| CodCal | Number(005,0) | Não | Código do Cálculo |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodRat | Number(009,0) | Não | Código do Rateio |
| RefEve | Number(011,2) | Sim | Referência Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal
- TabEve
- CodEve
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R046SIR_005

**Tabela:** R046SIM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCal | CodCal |
| TabEve | TabEve |
| CodEve | CodEve |

### IR_R046SIR_006

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

