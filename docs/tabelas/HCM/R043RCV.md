# R043RCV

## Descrição

Rescisão Sim.- Eventos Rescisão

---

## Resumo

- Campos: 11
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatPag | Date | Não | Data de Pagamento |
| TclRcs | Number(002,0) | Não | Tipo do Evento |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| RefEve | Number(011,2) | Sim | Referência do Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |
| CodRub | Number(009,0) | Sim | Código da rubrica |
| FatRub | Number(005,2) | Sim | Fator, Percentual Entre Outros da Rubrica. |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatPag
- TclRcs
- TabEve
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R043RCV_006

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

