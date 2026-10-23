# R042PRM

## Descrição

Rescisão - Digitação Prog.

---

## Resumo

- Campos: 10
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
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodRat | Number(009,0) | Não | Código do Rateio |
| RefEve | Number(011,2) | Sim | Referência do Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |
| StaPrg | String(001) | Sim | Indica se a programação está ou não efetivada |

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

### IR_R042PRM_005

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

