# R011PRR

## Descrição

Prorrogação de Lançamentos do Banco de Horas

---

## Resumo

- Campos: 8
- Chave Primária: 8 campo(s)
- Índices: 0
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
| DatPrr | Date | Não | Data de Prorrogação do Banco de Horas |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodBhr
- DatLan
- CodSit
- OriLan
- DatPrr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R011PRR_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R011PRR_003

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBhr | CodBHr |

