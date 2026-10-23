# R044BWC

## Descrição

Informações Bolso Wiipo - Colaborador

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatCmp | Date | Não | Competência |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| NomFun | String(040) | Sim | Nome do Colaborador |
| VlrTot | Number(014,2) | Sim | Valor Total Bolsos |
| DatRec | Date | Sim | Data agendada para recarga |
| HorRec | Number(005,0) | Sim | Hora agendada para recarga |
| IdeRec | String(100) | Sim | Identificação da recarga |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatCmp

---

## Índices

### R044BWCIndice1

**Tipo:** Não unico

Campos:
- DatCmp
- NumCpf

---

## Relacionamentos

Nenhum relacionamento cadastrado.
