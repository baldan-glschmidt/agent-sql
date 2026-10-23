# R011LAN

## Descrição

Lançamentos do Banco de Horas

---

## Resumo

- Campos: 15
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

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
| PerRef | Date | Sim | Competência de Vencimento do Lançamento. |
| CmpLan | Date | Sim | Competência de Geração do Lançamento |

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

### R011LANIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- PerRef

---

## Relacionamentos

### IR_R011LAN_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R011LAN_003

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBhr | CodBHr |

