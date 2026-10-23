# R038HAD

## Descrição

Histórico Adicionais

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| DatAlt | Date | Não | Data de Início da Insalubridade do Colaborador |
| DatTer | Date | Sim | Data Término da Insalubridade do Colaborador |
| PerIns | Number(005,2) | Sim | % Insalubridade |
| PerPer | Number(005,2) | Sim | % Periculosidade |
| FatTpo | Number(004,2) | Sim | Fator Tempo Serviço |
| ApoEsp | Number(002,0) | Sim | Número de Anos p/ Aposentadoria Especial |
| StaHis | Number(001,0) | Sim | Status do Histórico |
| CmpTer | Date | Sim | Competência Término do Adicional |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

### R038HADIndice2

**Tipo:** Não unico

Campos:
- StaHis
- DatAlt

### R038HADIndice3

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- DatTer
- DatAlt

### R038HADIndice4

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- DatAlt
- DatTer

---

## Relacionamentos

### IR_R038HAD_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

