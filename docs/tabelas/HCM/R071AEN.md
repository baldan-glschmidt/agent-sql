# R071AEN

## Descrição

Autorização de Entrada - Colaboradores

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Titular |
| DatEnt | Date | Não | Data de Início da Autorização de Entrada |
| HorEnt | Number(005,0) | Não | Hora de Início da Autorização de Entrada |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| CodPrm | Number(005,0) | Sim | Código da Permissão da Autorização de Entrada |
| DatVal | Date | Sim | Data de Validade da Autorização |
| HorVal | Number(005,0) | Sim | Hora de Validade da Autorização |
| DatSai | Date | Sim | Data da Saída do Colaborador |
| HorSai | Number(005,0) | Sim | Hora da Saída do Colaborador |
| ObsAEn | String(080) | Sim | Observação da Autorização de Entrada |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatEnt
- HorEnt

---

## Índices

### R071AENIndice2

**Tipo:** Não unico

Campos:
- NumCra
- DatEnt
- HorEnt

---

## Relacionamentos

### IR_R071AEN_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R071AEN_006

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

