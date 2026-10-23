# R053CSC

## Descrição

RAIS - Contribuições Sindicais do Colaborador

---

## Resumo

- Campos: 12
- Chave Primária: 10 campo(s)
- Índices: 1
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EmpArq | Number(004,0) | Não | Código da Empresa no Arquivo |
| AnoBas | Number(004,0) | Não | Ano Base da Rais |
| FilArq | Number(006,0) | Não | Código da Filial no Arquivo |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| DatAdm | Date | Não | Data de Admissão |
| CodVin | Number(002,0) | Não | Tipo de Vínculo |
| CodSin | Number(004,0) | Não | Código do Sindicato |
| TipCsi | Number(001,0) | Não | Tipo Contribuição |
| ValCon | Number(011,2) | Sim | Valor Contribuição |
| OriMov | String(001) | Sim | Origem do Registro |

---

## Chave Primária

- EmpArq
- AnoBas
- FilArq
- NumEmp
- TipCol
- NumCad
- DatAdm
- CodVin
- CodSin
- TipCsi

---

## Índices

### R053CSCIndice2

**Tipo:** Não unico

Campos:
- AnoBas
- NumEmp
- TipCol
- NumCad
- OriMov

---

## Relacionamentos

### IR_R053CSC_002

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| EmpArq | NumEmp |
| FilArq | CodFil |

### IR_R053CSC_003

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R053CSC_007

**Tabela:** R022VIN

| Origem | Destino |
|--------|---------|
| CodVin | CodVin |

### IR_R053CSC_008

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

