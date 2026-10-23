# R011LAN_IMP

## Descrição

Lançamentos do Banco de Horas - Importação Eventos Sistema Legado

---

## Resumo

- Campos: 14
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodBhr | Number(005,0) | Não | Banco de Horas |
| DatLan | Date | Não | Data do Lançamento |
| CodSit | Number(003,0) | Não | Situação do Lançamento |
| OriLan | String(001) | Não | Origem Lançamento |
| SinLan | String(001) | Sim | Sinal do Lançamento |
| QtdHor | Number(010,0) | Sim | Quantidade de Horas do Lançamento |
| QtdPag | Number(010,0) | Sim | Quantidade de Horas Pagas |
| HorCmp | Number(010,0) | Sim | Quantidade de Horas a compensar do Lançamento |
| DatCmp | Date | Sim | Data Limite para a Compensação |
| PrrLan | String(001) | Sim | Lançamento prorrogado |
| Obs | String(050) | Sim | Observação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodBhr
- DatLan
- CodSit
- OriLan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
