# R151CTG

## Descrição

Credenciamento de Colaboradores em Contingência

---

## Resumo

- Campos: 14
- Chave Primária: 6 campo(s)
- Índices: 4
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipCra | Number(001,0) | Não | Tipo de Crachá |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colabolador |
| NumCad | Number(009,0) | Não | Cadastro do Titular |
| DatIni | Date | Não | Data de início do credenciamento |
| HorIni | Number(005,0) | Não | Hora de início do credenciamento |
| NumCra | Number(012,0) | Não | Número do Crachá |
| CodPrm | Number(005,0) | Não | Código da permissão de acesso |
| DatFim | Date | Sim | Data final do credenciamento |
| HorFim | Number(005,0) | Sim | Hora final do credenciamento |
| CPFRes | String(020) | Sim | CPF do reponsável pelo registro da ocorrência |
| CodUsu | Number(010,0) | Sim | Código do usuário que cadastrou o credenciamento |
| DatCad | Date | Sim | Data do Cadastro do Credenciamento de Colaborador em Contingência |
| HorCad | Number(005,0) | Sim | Hora do Cadastro do Credenciamento de Colaborador em Contingência |

---

## Chave Primária

- TipCra
- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

---

## Índices

### R151CTGIndice2

**Tipo:** Não unico

Campos:
- NumCra
- DatIni
- HorIni

### R151CTGIndice3

**Tipo:** Não unico

Campos:
- NumCad

### R151CTGIndice4

**Tipo:** Não unico

Campos:
- TipCra
- TipCol
- NumEmp
- NumCad
- DatIni
- HorIni

### R151CTGIndice5

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

---

## Relacionamentos

### IR_R151CTG_003

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

