# R042RCV_IMP

## Descrição

Eventos Rescisão - Importação Eventos Sistema Legado

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

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
| CodEve | String(030) | Não | Código do Evento |
| RefEve | Number(011,2) | Sim | Referência do Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |
| CodRub | Number(009,0) | Sim | Código da rubrica |
| FatRub | Number(005,2) | Sim | Fator, Percentual Entre Outros da Rubrica. |
| InfGer | String(100) | Sim | Informações Gerais |

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

Nenhum relacionamento cadastrado.
