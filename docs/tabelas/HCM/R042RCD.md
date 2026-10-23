# R042RCD

## Descrição

Rescisão - Digitação Movto

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
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatPag | Date | Não | Data de Pagamento |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodRat | Number(009,0) | Não | Código do Rateio |
| RefEve | Number(011,2) | Sim | Referência do Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatPag
- TabEve
- CodEve
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042RCD_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R042RCD_005

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

